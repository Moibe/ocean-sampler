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

    if "vocals" in resultado_voz:
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

    api, tipo_api = tools.eligeAPI(globales.seleccion_api)
    
    client = gradio_client.Client(api, hf_token=bridges.hug)
    audioSource = gradio_client.handle_file(input1)   

    try:    
        resultado = client.predict(audioSource, api_name="/predict")
    
     #(Si llega aquí, debes debitar de la quota, incluso si detecto no-face o algo.)
        if tipo_api == "quota":
            print("Como el tipo api fue gratis, si debitaremos la quota.")
            sulkuPypi.updateQuota(globales.process_cost)
        #No debitas la cuota si no era gratis, solo aplica para Zero.  
  
        resultado_voz, resultado_audio = tools.desTuplaResultado(resultado)
        return resultado_voz, resultado_audio
    
    except Exception as e:
            mensaje = tools.titulizaExcepDeAPI(e)        
            return mensaje