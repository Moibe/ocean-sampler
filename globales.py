import gradio as gr
import tools

#MAIN
version = "2.4.3"
env = "dev"
aplicacion = "astroblend-dev"
api = "Moibe/image-blend"
#api = "Kwai-Kolors/Kolors-Character-With-Flux"
seto = "image-blend"
#seto = "zhi"
work = "picswap"
app_path = "/boilerplate"
server_port=7860
#tema = tools.theme_selector()
tema = gr.themes.Default()
flag = "auto"

sample_userfile = "gAAAAABmEZA4SLBC2YczouOrjIEi9WNCNGOIvyUcqBUnzxNsftXTdy54KaX9x8mAjFkABSI6FJrdZDQKk_5lpJOgJoMChxlniw=="