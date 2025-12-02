def MostrarCursos(cursos):   # ← RECIBE los datos como parametro cursos = [('C001', 'Matemáticas', 5), ('C002', 'Física', 4)] forma no ordenada
    
    print("----- Lista de Cursos -----")
    contador = 1
    for item in cursos:  # Recorre cada tupla
        # Primera vuelta: item = ('C001', 'Matemáticas', 5) etc..
        print(f"{contador}. Codigo: {item[0]} | Nombre: {item[1]} | ({item[2]} Creditos:)")
        # aca Imprimo: 1. Codigo: C001 | Nombre: Matemáticas | (5 Creditos:)
        contador = contador + 1
        # Segunda vuelta: item = ('C002', 'Física etc..


def pedirDatosRegistro():
    codigoCorrecto = False
    while(not codigoCorrecto):
        codigo = input("Ingrese código: ")
        if len(codigo) == 6:
            codigoCorrecto = True
        else:
            print("Código incorrecto: Debe tener 6 dígitos.")

    nombre = input("Ingrese nombre: ")

    creditosCorrecto = False
    while(not creditosCorrecto):
        creditos = input("Ingrese créditos: ")
        if creditos.isnumeric():
            if (int(creditos) > 0):
                creditosCorrecto = True
                creditos = int(creditos)
            else:
                print("Los créditos deben ser mayor a 0.")
        else:
            print("Créditos incorrectos: Debe ser un número únicamente.")

    nuevo_curso = (codigo, nombre, creditos)
    return nuevo_curso # retorno la tupla con los datos del curso

def pedirDatosActualizacion(cursos):
    MostrarCursos(cursos) # llamo a mi funcuion para mostrar los cursos disponibles pero ordeados. la variable cursos podria tener otro nombre e igual funcionaria igual porque es un parametro eso significa que recibe un valor al momento de ser llamada
    existeCodigo = False
    codigoEditar = input("Ingrese el código del curso a editar: ")
    for cur in cursos:
        if cur[0] == codigoEditar: # si el codigo del curso (cur[0]) es igual al codigo que el usuario ingreso
            existeCodigo = True # cambio la variable existeCodigo a true
            break # salgo del ciclo porque ya encontre el codigo

    if existeCodigo: # si l vrible existeCodigo es true, es decir, si el codigo existe en la lista de cursos comienzo a pedir los nuevos datos
        nombre = input("Ingrese nombre a modificar: ")

        creditosCorrecto = False
        while(not creditosCorrecto): # mientras la variable creditosCorrecto sea false
            creditos = input("Ingrese créditos a modificar: ") # pido los creditos a modificar
            if creditos.isnumeric(): # si los creditos son numericos
                if (int(creditos) > 0): # y si los creditos son mayores a 0
                    creditosCorrecto = True # cambio la variable creditosCorrecto a true para salir del ciclo
                    creditos = int(creditos) # convierto los creditos a entero
                else:
                    print("Los créditos deben ser mayor a 0.")
            else:
                print("Créditos incorrectos: Debe ser un número únicamente.")

        curso = (codigoEditar, nombre, creditos)
    else:
        curso = None

    return curso


def pedirDatosEliminacion(cursos):
    MostrarCursos(cursos)
    existeCodigo = False
    codigoEliminar = input("Ingrese el código del curso a eliminar: ")
    for cur in cursos:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break

    if not existeCodigo:
        codigoEliminar = ""

    return codigoEliminar