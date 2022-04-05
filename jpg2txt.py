from PIL import Image
from PIL import ImageEnhance
import os

print(''''Диск:', если телефон то '1' ''')
disk = input()
if disk == '1' :
	disk = '/storage/emulated/0/'
print('Путь к файлу:')
image_info = disk + input('')
image = Image.open(image_info)
(w,h) = image.size
print('Сколько символов в строке:')
weight = int(int(input())*2.9)
height= (weight*h)/w
height = int(height)

color_image = Image.open(image_info)
bw = color_image.convert('L')
try:
	bw.save(disk + 'jpg2txt/dd.jpg',quality=100)
except:
	os.mkdir(disk + 'jpg2txt')
	bw.save(disk + 'jpg2txt/dd.jpg',quality=100)
imagn = Image.open(disk + 'jpg2txt/dd.jpg')
enhancer_object = ImageEnhance.Contrast(imagn)
out = enhancer_object.enhance(100.0)
out.save(disk + 'jpg2txt/dd.jpg',quality=100)
image = Image.open(disk + 'jpg2txt/dd.jpg')
timage = image.resize((weight,height), Image.ANTIALIAS)
timage.save(disk + 'jpg2txt/dd.jpg', quality=100)
image = Image.open(disk + 'jpg2txt/dd.jpg')


a = []
ris = []
i = 1
ii = 1
x = 0
y = 0
xx = 0
xy = 0
yx = 0
yy = 0
flx = 0
for ii in range (15000):
	x = 0
	y = 0
	flx += 1
	im_crop = image.crop((xx, xy, yx + 2, yy + 4))
	xx += 3
	yx += 3
	im_crop.save(disk + 'jpg2txt/'+str(flx)+'.jpg')
	imx = Image.open(disk + 'jpg2txt/'+str(flx)+'.jpg')
	for i in range(8):
		p = imx.getpixel((x,y))
		x += 1
		if x == 2:
			x = 0
			y += 1
		if p >= 128:
			a.append('0')
		if p <= 128:
			a.append('1')
	if yx > weight:
		yx = 0
		xx = 0
		xy += 5
		yy += 5
		print('ooooooo')
		x += 1
	if xy > int(height)+1:
		break
	e = a[6]+a[7]+a[4]+a[2]+a[0]+a[5]+a[3]+a[1]
	r = int(e, 2)
	hy = 10240
	if r != 0:
		print(chr(hy+r))
		ris.append(chr(hy+r))
	if r == 0:
		print('⠀')
		ris.append('⠀')
	a = []
	if x != 0:
		ris.append('\n')
print()
i = 1
lop = 0
os.remove(disk + 'jpg2txt/dd.jpg')
f = open(disk + 'jpg2txt/txt.txt', 'w')
try:
	for i in range(15000):
		print(ris[lop], end='')
		f = open(disk + 'jpg2txt/txt.txt', 'a')
		f.write(ris[lop])
		lop += 1
		os.remove(disk + 'jpg2txt/'+str(i+1)+'.jpg')
except:
	print('\n')
	print('Сохранено в ' + disk + 'jpg2txt/txt.txt')