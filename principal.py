from BD.conexion import DatabaseConexion
import funciones


def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("==================== MENÚ PRINCIPAL ====================")
            print("1.- Listar cursos")
            print("2.- Registrar curso")
            print("3.- Actualizar curso")
            print("4.- Eliminar curso")
            print("5.- Salir")
            print("========================================================")
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 5:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 5:
                continuar = False
                print("¡Gracias por usar este sistema!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

#_-------------------------------------------------------------------
def ejecutarOpcion(opcion):
    dao = DatabaseConexion()

    if opcion == 1:
        try:
            cursos = dao.ListarCursos() # obtengo la lista de cursos desde la base de datos, pero no ordenados
            if len(cursos) > 0:
                funciones.listarCursos(cursos) # le envio la lista de cursos a la funcion listarCursos para que los muestre de forma ordenada
            else:
                print("No se encontraron cursos...")
        except Exception as e:
            print(f"Ocurrió un error...{e}")
#--------------------------------------------------------------------

    elif opcion == 2:
        nuevo_curso = funciones.pedirDatosRegistro() # pido los datos del nuevo curso y los recibo en una tupla, entonces en esta funcion recibo una tupla
        try:
            dao.registrarCurso(nuevo_curso)
        except Exception as e:
            print(f"Ocurrió un error...{e}")

#-------------------------------------------------------
    elif opcion == 3:
        try:
            cursos = dao.ListarCursos()
            if len(cursos) > 0:
                curso = funciones.pedirDatosActualizacion(cursos) # aqui recibo la tupla con los datos del curso a actualizar osea  codigo, nombre, creditos
                if curso: # si la variable curso tiene datos (no es None)
                    dao.actualizarCurso(curso) # si cursos tiene datos llamo al metodo actualizarCurso y le paso la tupla con los datos del curso a actualizar de mi base de datos
                else:
                    print("Código de curso a actualizar no encontrado...\n")
            else:
                print("No se encontraron cursos...")
        except Exception as e:
            print(f"Ocurrió un error...{e}")
#---------------------------------------------------------

    elif opcion == 4:
        try:
            cursos = dao.ListarCursos()
            if len(cursos) > 0:
                codigoEliminar = funciones.pedirDatosEliminacion(cursos)
                if not(codigoEliminar == ""):
                    dao.eliminarCurso(codigoEliminar)
                else:
                    print("Código de curso no encontrado...\n")
            else:
                print("No se encontraron cursos...")
        except:
            print("Ocurrió un error...")
    else:
        print("Opción no válida...")


menuPrincipal()