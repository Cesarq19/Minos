import os
import machine
import uos
import uerrno

class SD:
    def __init__(self, sd_pin):
        self.sd_pin = sd_pin

    def mount(self):
        try:
            sd = machine.SDCard(self.sd_pin, machine.SDCard.SD1)
            uos.mount(sd, "/sd")
        except OSError as e:
            print("Error al montar la tarjeta SD:", e)

    def umount(self):
        try:
            uos.umount("/sd")
        except OSError as e:
            print("Error al desmontar la tarjeta SD:", e)

    def list_files(self, path="/sd"):
        try:
            files = uos.listdir(path)
            print("Archivos en", path)
            for file in files:
                print("- ", file)
        except OSError as e:
            if e.args[0] == uerrno.ENOENT:
                print("No se encontró el directorio", path)
            else:
                print("Error al listar los archivos en", path, ":", e)

    def create_file(self, filename, data, path="/sd"):
        try:
            with open(path + "/" + filename, "w") as f:
                f.write(data)
            print("Archivo", filename, "creado en", path)
        except OSError as e:
            print("Error al crear el archivo", filename, "en", path, ":", e)

    def read_file(self, filename, path="/sd"):
        try:
            with open(path + "/" + filename, "r") as f:
                data = f.read()
            print("Contenido del archivo", filename, "en", path, ":")
            print(data)
            return data
        except OSError as e:
            print("Error al leer el archivo", filename, "en", path, ":", e)

    def delete_file(self, filename, path="/sd"):
        try:
            uos.remove(path + "/" + filename)
            print("Archivo", filename, "eliminado de", path)
        except OSError as e:
            print("Error al eliminar el archivo", filename, "de", path, ":", e)

    def append_to_file(self, filename, data, path="/sd"):
        try:
            with open(path + "/" + filename, "a") as f:
                f.write(data)
            print("Texto añadido al final del archivo", filename, "en", path)
        except OSError as e:
            print("Error al añadir texto al final del archivo", filename, "en", path, ":", e)
