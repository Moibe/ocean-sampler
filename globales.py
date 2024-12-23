import gradio as gr

api_zero = "Moibe/sampler"
api_cost = "Moibe/music-separation" #wav
same_api = True
process_cost = 0

version = "1.0.3"
env = "prod" #Importante porque define de donde se leerán los créditos y los datos de los usuarios!

aplicacion = "sampler" #Se usa para que la api de sulku explore data y novelty de ese usuario.

seto = "sampler"
work = "picswap"
app_path = "/sampler"
server_port=7811
tema = gr.themes.Default()
flag = "auto"