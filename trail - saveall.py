# Adapted to Python 3 from
# http://www.tobias-westmeier.de/astronomy_tutorial_startrails.php
# requires Pillow instead of PIL

import os, numpy, shutil, glob
from PIL import Image

files   = os.listdir(os.getcwd())
images  = [name for name in files if name[-4:] in [".jpg", ".JPG"]]
width, height = Image.open(images[0]).size

total = str(len(images))
prefix = input("Specify a prefix: ")
folder_name = input("Name of subfolder to save results in [empty to skip subfolder]: ")

stack   = numpy.zeros((height, width, 3), numpy.float)
counter = 1

for image in images:
    print ("Processing image " + str(counter) + " of " + total)
    image_new = numpy.array(Image.open(image), dtype = numpy.float)
    stack     = numpy.maximum(stack, image_new)
    stack = numpy.array(numpy.round(stack), dtype = numpy.uint8)
    output = Image.fromarray(stack, mode = "RGB")
    output.save(prefix + str(counter) + ".jpg") #, "JPEG")
    counter  += 1

if len(folder_name) > 0:
   os.mkdir(folder_name)
   for file in glob.glob(prefix + '*'):
      shutil.move(file, folder_name)

