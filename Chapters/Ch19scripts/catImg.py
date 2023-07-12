import os 
from PIL import Image

os.chdir('/home/harrison/Desktop/gitHubRepos/AutoBorPy/automate_online-materials')
catIm = Image.open('zophie.png')
width, height = catIm.size
print(width, height)
print(catIm.filename, catIm.format)


# This commemnted code will save cat image as a jpg
# in the directory specfed above in the script
#catIm.save('zophie.jpg')
croppedIm = catIm.crop((335, 345, 565, 560))
# croppedIm.save('cropped.png')
crimg = Image.open('cropped.png')