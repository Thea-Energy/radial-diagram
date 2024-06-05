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
layers = [line.rstrip().split(',') for line in f]
# print(layers)

segmentHeight = 60
xStart = 400
yStart = 350
scale = 10
xList = []
widthList = []
segList = []

pw = 10
px1 = xStart-pw*scale
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
    x2 = xval + width * scale
    y2 = yStart + segmentHeight * scale

    mid = (x2+x1)/2

    canvas.create_rectangle(x1, y1, x2, y2, fill=color)
   
    if width < 5:
        ticLen = 50
        xtic = mid+ticLen*math.sin(45)
        ytic = y1-ticLen*math.sin(45)
        canvas.create_line(mid, y1, xtic, ytic)
        canvas.create_text(mid, y1, text=label, fill="Black", font="Consolas 16", anchor="sw", angle=45)
    else:
        canvas.create_text(mid, (y1+y2)/2, text=label, font="Consolas 22", angle=90)

# def addSegment(name, width, color="snow"):
def addSegment(seg):
    name = seg[0]
    width = int(seg[1])
    color = seg[2]

    xVal = xList[-1] + widthList[-1] * scale
    segList.append([name, width, xVal, color])
    xList.append(xVal)
    widthList.append(width)


for layer in layers:
    addSegment(layer)

for val in range(len(segList)):
    print(segList[val])
    rectangle(val)


## Ruler
rLength = 1000
rStep = 10
rMax = int(rLength/rStep)
rEnd = rLength + xStart
ticY1 = 990
ticLen = 10
ticY2 = ticY1 - ticLen
canvas.create_line(xStart, ticY1, rEnd, ticY1)

for val in range(0, rMax, rStep):
    x = xStart + val * rStep
    canvas.create_line(x, ticY1, x, ticY2)
    canvas.create_text(x, ticY2+30, text=rStep*val/scale, font="Consolas 12")



root.mainloop()