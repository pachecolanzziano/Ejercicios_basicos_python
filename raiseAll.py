class MiExcepcion(Exception):
    def __init__(self, mensaje, informacion):
        self.mensaje = mensaje
        self.informacion = informacion
    
try:
    raise MiExcepcion("Mi Mensaje", "Mi Informacion")
except MiExcepcion as e:
    print(e.mensaje)
    print(e.informacion)