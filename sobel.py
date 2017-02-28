from PIL import Image, ImageFilter

mol = Image.open("mol.png")
mol = mol.filter(ImageFilter.FIND_EDGES)
mol.show()