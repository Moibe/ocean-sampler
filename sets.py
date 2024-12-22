import gradio as gr

# Diccionario para mapear los sets a sus respectivas configuraciones
configuraciones = {
    "image-blend": {
        "input1": gr.Image(label="Source", type="filepath"),
        "input2": gr.Image(label="Destination", type="filepath"),
        "result": gr.Image(label="Result"),
    },
    "video-blend": {
        "input1": gr.Image(label="Source", type="filepath"),
        "input2": gr.Video(label="Destination"),
        "result": gr.Video(label="Result") 
    },
    "sampler": {
        "input1": gr.Audio(label="Source", type="filepath"),
        "result_voice": gr.Audio(label="Voice", type="filepath"),
        "result_audio": gr.Audio(label="Result") 
    },
    "splashmix": {
        "input1": gr.Image(label="Source", type="filepath"),
        "result": gr.Image(label="Destination", type="filepath"),
    },
    "txt2image": {
        "input1": gr.Textbox(),
        "result": gr.Image(label="Source", type="filepath"),
    },
    "txt2video": {
        "input1": gr.Textbox(),
        "result": gr.Video(label="Destination"),
    },
    "zhi": {
        "input1": gr.Image(label="Source", type="filepath"),
        "input2": gr.Textbox(label="Prompt"),
        "result": gr.Image(label="Result"),
    },
}