import ast 
import globales
import sulkuPypi
import tools

def authenticate(username, password):      
    cadena_usuarios = sulkuPypi.getData(globales.aplicacion)  
    lista_usuarios = ast.literal_eval(cadena_usuarios)    
    for u, p in lista_usuarios:
        #Si el usuario y la contraseña son correctas...
        if username == u and password == p:
            tools.initAPI()                                           
            return True    
    return False