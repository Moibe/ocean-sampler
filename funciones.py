import bridges
import globales
import sulkuPypi
import sulkuFront
import gradio as gr
import gradio_client
import time
import tools

btn_buy = gr.Button("Get Credits", visible=False, size='lg')

#PERFORM es la app INTERNA que llamará a la app externa.
def perform(input1, request: gr.Request):

    tokens = sulkuPypi.getTokens(sulkuPypi.encripta(request.username).decode("utf-8"), globales.env)
    
    #1: Reglas sobre autorización si se tiene el crédito suficiente.
    autorizacion = sulkuPypi.authorize(tokens, globales.work)
    if autorizacion is True:
        try: 
            resultado_voz, resultado_audio = mass(input1)
            
        except Exception as e:            
            info_window, resultado, html_credits = sulkuFront.aError(request.username, tokens, excepcion = tools.titulizaExcepDeAPI(e))
            return resultado_voz, resultado_audio, info_window, html_credits, btn_buy
    else:
        info_window, resultado, html_credits = sulkuFront.noCredit(request.username)
        return resultado_voz, resultado_audio, info_window, html_credits, btn_buy


    #Primero revisa si es imagen!: 
    if "vocals.wav" in resultado_voz:
        #Si es imagen, debitarás.
        print("Entré a vocals.wav")
        html_credits, info_window = sulkuFront.presentacionFinal(request.username, "debita")
        return resultado_voz, resultado_audio, info_window, html_credits, btn_buy
    else: 
        #Si no es imagen es un texto que nos dice algo.
        info_window, resultado, html_credits = sulkuFront.aError(request.username, tokens, excepcion = tools.titulizaExcepDeAPI(resultado))
        return resultado, info_window, html_credits, btn_buy      
    
    

#MASS es la que ejecuta la aplicación EXTERNA
def mass(input1):
    
    client = gradio_client.Client(globales.api, hf_token=bridges.hug)
    audioSource = gradio_client.handle_file(input1)    
    
    resultado = client.predict(audioSource, api_name="/predict")
    resultado_voz, resultado_audio = tools.desTuplaResultado(resultado)

    return resultado_voz, resultado_audio