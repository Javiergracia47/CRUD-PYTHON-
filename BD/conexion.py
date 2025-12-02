import mysql.connector # conecto python con mysql
from mysql.connector import Error # capturo los erorres de muysql

class DatabaseConexion():  
    def __init__(self):
        try: 
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='', 
                database='universidad'
            )
        except Error as ex:
            print("Error al intentar la conexion: {0}".format(ex)) # 
  

# metodos de mi clase DatabaseConexion 
    def ListarCursos(self): # esto no me trae muy ordenados mis cursos. en lista de tuplas y la funcion mostrar cursos los formatea para mostrarlos enumerados
        print("listar cursos")
        if self.conexion.is_connected(): # verifico si la conexion esta activa antes de hacer una consulta 
            print("Conexión exitosa a la base de datos!")
            try:
                cursor = self.conexion.cursor() # puntero que permite ejecutar las consultas
                cursor.execute("SELECT * FROM curso ORDER BY nombre ASC")
                resultados = cursor.fetchall() # con fetchall traigo los registros y los guardo en la variable resultados
                return resultados # devuelve los resultados para mostrarlos fuera del metodo
            except Error as ex:
                   print(f"Error al intentar la conexion: {ex}")

   
    def registrarCurso(self,nuevo_curso): #| metodo para registrar un curso en la base de datos, el parametro curso es una tupla (un array de datos pero no son todos de un mismo tipo)con los datos del curso
        if self.conexion.is_connected():
            try:
                codigo, nombre, creditos = nuevo_curso # aca hago una destructuracion de la tupla curso para obtener los datos individuales, que es una tupla?
                cursor=self.conexion.cursor() # llamo al puntero que permite ejecutar las consultas
                cursor.execute(f"INSERT INTO curso (codigo,nombre,creditos) VALUES ('{codigo}','{nombre}',{creditos})")
                self.conexion.commit()
                print("✓ Curso registrado")
            except Error as ex:
              print(f"Error al intentar la conexion: {ex}")
    

    def eliminarCurso(self, codigoEliminar) :# metodo para eliminar un curso en la base de datos, el parametro codigoEliminar es el codigo del curso que quiero eliminar
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor() # llamo al puntero que permite ejecutar las consultas
                cursor.execute(f"DELETE FROM curso WHERE codigo = '{codigoEliminar}'") # ejecuto la consulta para eliminar el curso con el codigo recibido como parametro
                self.conexion.commit()
                print("✓ Curso eliminado")
            except Error as ex:
              print(f"Error al intentar la conexion: {ex}")
              

    def actualizarCurso(self, curso_actualizar):
     if self.conexion.is_connected():
        try:
            codigo, nombre, creditos = curso_actualizar
            cursor = self.conexion.cursor()
            
            sql = "UPDATE curso SET nombre = %s, creditos = %s WHERE codigo = %s"
            cursor.execute(sql, (nombre, creditos, codigo))
            
            self.conexion.commit()
            print("✓ Curso actualizado")
        except Error as ex:
            print(f"Error al intentar la conexion: {ex}")

     

# Al final del archivo
if __name__ == "__main__":
    dao = DatabaseConexion()
    if dao.conexion.is_connected(): # verifico si la conexion esta activa antes de hacer una consulta
     print("Conexión exitosa a la base de datos!")
    


# estas son las formas de destructurar en python
# Lista
""" """ """ valores = [1, 2, 3]
a, b, c = valores
print(a, b, c)  # Salida: 1 2 3

# Tupla
coordenadas = (10, 20)
x, y = coordenadas
print(x, y)  # Salida: 10 20
 """"""  """ """ """
