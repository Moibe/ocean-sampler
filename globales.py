import gradio as gr

version = "3.1.4"
env = "prod" #Importante porque define de donde se leerán los créditos y los datos de los usuarios!
aplicacion = "sampler" #Se usa para que la api de sulku explore data y novelty de ese usuario.

seleccion_api = "eligeAOB" #eligeGratisOCosto , eligeAOB o eligeGratisOCosto
max_size = 20
#Quota o Costo
api_zero = ("Moibe/image-blend", "quota")
api_cost = ("Moibe/image-blend", "costo")
#A o B
api_a = ("Moibe/sampler", "gratis") #Para music-sampler en particular aquí la diferencia será el formato: mp3
api_b = ("Moibe/music-separation", "gratis") #wav
#Gratis o Costo
api_gratis = ("Moibe/image-blend", "gratis")
api_costo = ("Moibe/image-blend", "costo")
process_cost = 0

seto = "sampler"
work = "picswap"
app_path = "/sampler"
server_port=7811
tema = gr.themes.Default()
flag = "auto"