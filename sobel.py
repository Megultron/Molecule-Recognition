from PIL import Image, ImageFilter

mol = Image.open("mol.png")
#convert to grayscale (8-bit)
mol = mol.convert('L')
#experimentally defined magic number
threshold = 90
mol = mol.point((lambda x: 0 if x<threshold else 255), '1')
mol.save("modified.png")
mol.show()