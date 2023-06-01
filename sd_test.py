import os
from machine import Pin, SoftSPI
from sdcard import SDCard
# Pin assignment: 
# 	MISO -> GPIO 13
#	MOSI -> GPIO 12
#	SCK  -> GPIO 14
#	CS   -> GPIO 27
spisd = SoftSPI(-1,
                miso=Pin(13),#!!!!!!!!cambiar a los pines que usaremos estos son los de la sp32 normal!!!!!!!!!!!1
                mosi=Pin(12),
                sck=Pin(14))
sd = SDCard(spisd, Pin(27))

print('Root directory:{}'.format(os.listdir()))
vfs = os.VfsFat(sd)
os.mount(vfs, '/sd')
print('Root directory:{}'.format(os.listdir()))
os.chdir('sd')#aqui indico que estoy dentro de la tarjeta sd y todos los archivos que cree se crearan en la sd, los archivis se manejan normalmente como es en python.
print('SD Card contains:{}'.format(os.listdir()))
