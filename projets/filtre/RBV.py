from PIL import Image
image = Image.open("photo1.jpg")
taille = image.size
print(taille)
formatImage = image.format
print(formatImage)
print(image.mode)
data = list(image.getdata())
print(len(data))
print(data[0:10])
print("fin")
rouge = [i[0] for i in data]
print("rouge",rouge[0:10])
vert = [i[1] for i in data]
print("vert",vert[0:10])
bleu = [i[2] for i in data]
print("bleu",bleu[0:10])