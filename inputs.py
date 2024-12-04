import sets
import time

def inputs_selector(set):    

    # Obtener la configuración según el valor de 'set'
    config = sets.configuraciones.get(set)

    # Si la configuración existe, usarla
    if config:
        if len(config) == 2:
            input1 = config["input1"]
            result = config["result"]
            return input1, result
        elif len(config) == 3:
            input1 = config["input1"]
            result_voice = config["result_voice"]
            result_audio = config["result_audio"]
            
            return input1, result_voice, result_audio
    else:
        print("Set no válido")