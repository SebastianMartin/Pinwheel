from PIL import Image
import numpy as np
from random import randint
	

w, h = 16, 16
data = np.zeros((h, w, 3), dtype=np.uint8)
for i in range(h):
	for j in range(w):
		data[i,j] = [i*16+j,i*16+j,i*16+j]#[randint(0, 255),randint(0, 255),randint(0, 255)]
img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()


dataTemp = data.copy()
#print(dataTemp)
temp = dataTemp[0,0].copy()
for i in range(h):
	for j in range(w):
		dataTemp[i,j] = dataTemp[j,i]


img2 = Image.fromarray(dataTemp, 'RGB')
img2.save('my2.png')
img2.show()
x = 2
#for x in range(k,h):
for i in range(0,w,x):
	for j in range(0,h,x):
		temp = dataTemp[i][j:j+x-1].copy()
		dataTemp[i]
		print(temp)
	#x*2





for i in range(0,w,2):
	for j in range(0,h,2):
		temp = dataTemp[i,j].copy()


		dataTemp[i,j] = dataTemp[i+1,j]
		dataTemp[i+1,j] = dataTemp[i+1,j+1]
		dataTemp[i+1,j+1] = dataTemp[i,j+1]
		dataTemp[i,j+1] = temp
img2 = Image.fromarray(dataTemp, 'RGB')
img2.save('my2.png')
img2.show()
