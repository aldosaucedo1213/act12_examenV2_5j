class proveedor1310:

    def Diccionario_camionero1310(self):
        print("Tabla de camionero: \n")
        Contenido1 =	{
    "dni -> ": "24576",
    "Nombre -> ": "ramon juarez",
    "Direccion -> ": "Calle pistache ",
    "Num. telefono -> ": 6564876232,
    "Correo -> ": "ramon1310@gmail.com",
    "salario -> ": 2312,
    "Horario -> ": "10:30 am / 2:00 pm",
}
        print(Contenido1)
        for A,B in Contenido1.items():
            print(A,B)

    def Diccionario_paquetes1310(self):
        print("Tabla de paquetes: \n")
        Contenido2 =	{
    "codigo de paquete: -> ": 23121,
    "descripcion -> ": "fragil",
    "destinatario -> ": "bernardo",
    "Num. telefono -> ": 656348762,
    "Correo -> ": "benardo@gmail.com",
    "Domicilio -> ": "Calle paseos de alba ",
    "Forma de pago -> ": "Tarjeta",
}
        print(Contenido2)
        for C,D in Contenido2.items():
            print(C,D)

    def Diccionario_camiones1310(self):
        print("Tabla de camiones: \n")
        Contenido3 =	{
    "matricula -> ": 2230889,
    "tipo de camion-> ": "carga",
    "Numero de camion -> ": 65,
    "modelo-> ": "2024",
   
}
        print(Contenido3)
        for E,F in Contenido3.items():
            print(E,F)
   
       
objeto = proveedor1310()
print("")
objeto.Diccionario_camionero1310()
print("")
objeto.Diccionario_paquetes1310()
print("")
objeto.Diccionario_camiones1310()
print("")


