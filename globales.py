import gradio as gr

version = "0.0.1"
env = "dev"
aplicacion = "sampler" #Se usa para que la api de sulku explore data y novelty de ese usuario.
api = "Moibe/sampler"
#api = "abidlabs/music-separation"
#api = "https://abidlabs-music-separation.hf.space/--replicas/f5un4/"
seto = "sampler"
work = "picswap"
app_path = "/sampler"
server_port=7811
#tema = tools.theme_selector()
tema = gr.themes.Default()
flag = "auto"
