import gradio as gr
import tools

#MAIN
version = "0.0.0"
env = "dev"
aplicacion = "sampler-dev"
api = "Moibe/sampler"
#api = "abidlabs/music-separation"
#api = "https://abidlabs-music-separation.hf.space/--replicas/f5un4/"
seto = "sampler"
work = "picswap"
app_path = "/sampler-dev"
server_port=7810
#tema = tools.theme_selector()
tema = gr.themes.Default()
flag = "auto"