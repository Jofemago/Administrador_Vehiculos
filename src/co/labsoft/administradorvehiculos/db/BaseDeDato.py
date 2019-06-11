
import sqlite3

class BaseDeDatos:

    conn = sqlite3.connect('AdmVeh.db')
    c = conn.cursor()


    def closeCursor(self):
        """Este metodo cierra el cursor con el cual se hacen las conexiones"""
        self.c.close()

    def closeConexion(self):
        """Este metodo cierra la conexion con la base de datos..."""
        self.conn.close()


    def Cerrar(self):
        """cierra la base de datos"""
        self.closeCursor()
        self.closeConexion()


if __name__ == '__main__':
    main()
