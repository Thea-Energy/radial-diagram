# RadialBuild.py 
import tkinter as tk
from tkinter import Canvas
import math

root = tk.Tk()
root.title("Radial Build")
root.geometry("1860x1100")
# root.attributes('-fullscreen', True)

bgColor = "gray82"

canvas = tk.Canvas(root, width=1920, height=1100, bg=bgColor)
canvas.place(x=0, y=0)
canvas.create_text(10, 10, text="EOS Radial Build", font = "Consolas 36", anchor="nw")
canvas.create_text(10, 55, text="as of 5/27/2024", font = "Consolas 20", anchor="nw")

f = open("Radial_Layers.txt", 'r')
layers = [line.strip().split(',') for line in f]
print(layers)

segmentHeight = 60
xStart = 100
yStart = 300

xscale = 7.5
yscale = 11
xList = []
widthList = []
segList = []

pw = 10
px1 = xStart-pw*xscale
segList.append(["Plasma",pw, px1, "PaleGreen1"])
xList.append(px1)
widthList.append(pw)

def rectangle(index):
    name = segList[index][0]
    width = segList[index][1]
    xval = segList[index][2]
    color = segList[index][3]
    if len(color) < 1:
        color = "red"
    
    label = "{} ({} cm)".format(name, width)
    x1 = xval
    y1 = yStart
    x2 = xval + width * xscale
    y2 = yStart + segmentHeight * yscale
    
    mid = (x2+x1)/2
    labelAngle = 60

    canvas.create_rectangle(x1, y1, x2, y2, fill=color)
   
    if width < 5:
        ticLen = 50
        xtic = mid+ticLen*math.cos(math.radians(labelAngle))
        ytic = y1-ticLen*math.sin(math.radians(labelAngle))
        canvas.create_line(mid, y1, xtic, ytic)
        canvas.create_text(mid, y1, text=label, fill="Black", font="Consolas 12", anchor="sw", angle=labelAngle)
    else:
        canvas.create_text(mid, (y1+y2)/2, text=label, font="Consolas 22", angle=90)

def addSegment(seg):
    name = seg[0]
    width = float(seg[1])
    color = seg[2]

    xVal = xList[-1] + widthList[-1] * xscale
    segList.append([name, width, xVal, color])
    xList.append(xVal)
    widthList.append(width)


for layer in layers:
    addSegment(layer)

for val in range(len(segList)):
    print(segList[val])
    rectangle(val)


## Ruler
rLength = 220
rStep = 10

ticY1 = 1000
ticLen = 10
ticY2 = ticY1 - ticLen
ticY3 = ticY1 - ticLen/2
canvas.create_line(xStart, ticY1, rLength*xscale + xStart, ticY1)

for val in range(0, rLength+rStep, rStep):
    print(val)
    x = xStart + val * xscale
    canvas.create_line(x, ticY1, x, ticY2)
    canvas.create_text(x, ticY2+30, text=val, font="Consolas 12")

    if val < rLength:
        for j in range(1, rStep):
            x2 = x + j*xscale
            canvas.create_line(x2, ticY1, x2, ticY3 )


root.mainloop()