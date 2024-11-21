import ast 
import bridges
import globales
import sulkuPypi
import gradio_client

def authenticate(username, password):    
    
    cadena_usuarios = sulkuPypi.getData(globales.aplicacion)  
    lista_usuarios = ast.literal_eval(cadena_usuarios)
    
    for u, p in lista_usuarios:
        #Si el usuario y la contraseña son correctas...
        if username == u and password == p:
            
            # try: #No usar si siempre estará prendida.
            #     client = gradio_client.Client(globales.api, hf_token=bridges.hug)
            #     terminal = "AI engine ready."
            #     client = None
            # except Exception as e:
            #     print("No api, encendiendo: ", e)    
 
            print(f"{username} logged.")                                                
            return True
    
    return False