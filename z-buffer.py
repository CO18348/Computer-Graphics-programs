#imports
from PIL import Image,ImageColor,ImageDraw
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

#draw image
im = Image.new(mode = "RGB" , size=(400,300))
draw = ImageDraw.Draw(im)

# draw.line((x1,y1,x2,y2) , fill = 128)

d=[[float("-inf") for i in range(300)] for j in range(400)]
c=[[(213, 191, 255) for i in range(300)] for j in range(400)]

# cofficients of plane
A=[5,10]
B=[-150,10]
C=[10,-10]
D=[-5,5]

# Z buffer 
for plane in range(2):
    for y in range(300):
        z=(-B[plane]*y-D[plane])/C[plane] 
     
        for x in range(400):
            if(z>d[x][y]): 
                d[x][y]=z
                c[x][y]=(255*(plane),0,255*(1-plane))
            z=z-(A[plane]/C[plane]) 
 
for y in range(300):
    for x in range(400):
        im.putpixel((x,y) ,c[x][y])
figure(figsize=(16,16)) 
imgplot = plt.imshow(im)
plt.show()
