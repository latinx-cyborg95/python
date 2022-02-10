# importamos la libreria csv llamandola c
# import csv as c
import csv
import random
from PIL import Image
import glob
import p5

nombre_archivo = 'bomba.csv'

with open(nombre_archivo, 'r') as csv_file:
  # objecto csv
  data_lina = csv.reader(csv_file, delimiter=";")
  # for en data_lina (objeto csv) para obtener las filas
  for fila in data_lina:
    # imprimimos las filas
    #print(fila)
    for data in fila:
      pass
      #print(data)
      
ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "." ]

nombre_imagenes = []

def resize(image, new_width = 100):
    width, height = image.size
    new_height = new_width * height / width
    new_height = round(new_height)
    return image.resize((new_width, new_height))

def to_greyscale(image):
    return image.convert("L")

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "";
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//25];
    return ascii_str

def creador_de_ascii(nombre, llave):
  image = Image.open(nombre)
  image = resize(image);
  #convert image to greyscale image
  greyscale_image = to_greyscale(image)
  # convert greyscale image to ascii characters
  ascii_str = pixel_to_ascii(greyscale_image)
  img_width = greyscale_image.width
  ascii_str_len = len(ascii_str)
  ascii_img=""
  #Split the string based on width  of the image
  for i in range(0, ascii_str_len, img_width):
      ascii_img += ascii_str[i:i+img_width] + "\n"
  #save the string to a file
  with open("ascii_gif/"+str(llave)+".txt", "w") as f:
      f.write(ascii_img);
  #print(randchar from data)
#K=key
for llave, imagen in enumerate(glob.glob("gif/*.jpg")):
  nombre_imagenes.append(imagen)
  creador_de_ascii(imagen, llave)