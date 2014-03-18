#Writing ASCII in python
import os


def circledraw(dose, track, xpos, ypos, basecircle, layer = 2, vertex = 64):
    lines=[]
    lines.append('C ' + repr(dose) + ' ' + repr(layer) + ' ' + repr(track) + '')
    lines.append('' + repr(xpos) + ' ' + repr(ypos) + '')
    lines.append('' + repr(basecircle) + '')
    lines.append('' + repr(vertex) + '')
    lines.append('#')
    return lines
#This is the function for drawing the rings,it takes in the dose, then the
#width of the track, then the x position of the center of the ring, then the
#y position of the ring, then the radius of the basic circle and then, if you
#want, you can input the layer and the vertex numbers which are set to 2 and 64
#respectivly by default


def polydraw(dose, layer, *x):
    if x[0][0] == x[0][len(x[0])-1] and len(x[0]) == len(x[1]):

        line1 = '1 ' + repr(dose) + ' ' + repr(layer) + ''
        lines = [line1]

        for i in range(len(x[0])):
            coords = '' + repr(x[0][i]) + ' ' + repr(x[1][i]) + ''
            lines.append(coords)

        finalline = '#'
        lines.append(finalline)
        #Adds the hash to end the defenition of the object
    else:
        lines = []
        lines.append('Error constructing polygon, check the co-ordinates are correct')
        lines.append('' + repr(x) + '')
        lines.append('' + repr(x[0][len(x[0]) -  1]) + ' ' + repr(x[1][len(x[0]) - 1]) + '')
        lines.append('' + repr(len(x[0])) + ' ' + repr(len(x[1])) + '')
        #append.lines(line2)
        #append.lines(line3)
        #returns an error if the starting and ending co-ords don't match
        #or if there are a different number of x co-ords to y co-ords
    
    return lines
#This is the function for drawing polygons. It takes in a dose, the layer
#number and then the x, y positions. It is important to note that it takes
#all the x positions and then all the y positions. This could very easely be
#a source of errors

def ellipsedraw(dose, trackwidth, xpos, ypos, rad1, rad2, rotation, layer = 2, vertex = 64):
    lines = []
    lines.append('E ' + repr(dose) + ' ' + repr(layer) + ' ' + repr(trackwidth) + '')
    lines.append('' + repr(xpos) + ' ' + repr(ypos) + '')
    lines.append('' + repr(rad1) + ' ' + repr(rad2) + '')
    lines.append('' + repr(vertex) + '')
    lines.append('' + repr(rotation) + '')
    lines.append('#')
    return lines
    
#This section draws elipses. It requires the dose, the width of the track, the x and y
#positions of the center of the ring, the two radi of the majopr and minor axes and
#the rotation of the ring. If you want you can change the layer the ring is on and
#the number of vertecies making it up which are automatically set to 2 and 64
#respectily if you can't be arsed


def textdraw(dose, width, xpos, ypos, height, angle, ualign, valign, text, layer = 2):
    lines = []
    lines.append('T ' + repr(dose) + ' ' + repr(width) + '')
    lines.append('' + repr(xpos) + ' ' + repr(ypos) + '')
    lines.append('' + repr(height) + ' ' + repr(angle) + '')
    lines.append('' + repr(ualign) + ' ' +repr(valign) + '')
    lines.append('' + repr(text) + '')
    lines.append('#')
    return lines
#This section writes text

def circlewrite(dose, track, xpos, ypos, basecircle, f, layer = 2, vertex = 64):
    lines=[]
    lines.append('C ' + repr(dose) + ' ' + repr(layer) + ' ' + repr(track) + '')
    lines.append('' + repr(xpos) + ' ' + repr(ypos) + '')
    lines.append('' + repr(basecircle) + '')
    lines.append('' + repr(vertex) + '')
    lines.append('#')
    for item in lines:
        f.write("%s\n" % item)
#This is the function for drawing the rings,it takes in the dose, then the
#width of the track, then the x position of the center of the ring, then the
#y position of the ring, then the radius of the basic circle and then, if you
#want, you can input the layer and the vertex numbers which are set to 2 and 64
#respectivly by default


def polywrite(dose, layer, f, *x):
    if x[0][0] == x[0][len(x[0])-1] and len(x[0]) == len(x[1]):

        line1 = '1 ' + repr(dose) + ' ' + repr(layer) + ''
        lines = [line1]

        for i in range(len(x[0])):
            coords = '' + repr(x[0][i]) + ' ' + repr(x[1][i]) + ''
            lines.append(coords)

        finalline = '#'
        lines.append(finalline)
        #Adds the hash to end the defenition of the object
    else:
        lines = []
        lines.append('Error constructing polygon, check the co-ordinates are correct')
        lines.append('' + repr(x) + '')
        lines.append('' + repr(x[0][len(x[0]) -  1]) + ' ' + repr(x[1][len(x[0]) - 1]) + '')
        lines.append('' + repr(len(x[0])) + ' ' + repr(len(x[1])) + '')
        #append.lines(line2)
        #append.lines(line3)
        #returns an error if the starting and ending co-ords don't match
        #or if there are a different number of x co-ords to y co-ords
    
    for item in lines:
        f.write("%s\n" % item)
#This is the function for drawing polygons. It takes in a dose, the layer
#number and then the x, y positions. It is important to note that it takes
#all the x positions and then all the y positions. This could very easely be
#a source of errors

def ellipsewrite(dose, trackwidth, xpos, ypos, rad1, rad2, rotation, f, layer = 2, vertex = 64):
    lines = []
    lines.append('E ' + repr(dose) + ' ' + repr(layer) + ' ' + repr(trackwidth) + '')
    lines.append('' + repr(xpos) + ' ' + repr(ypos) + '')
    lines.append('' + repr(rad1) + ' ' + repr(rad2) + '')
    lines.append('' + repr(vertex) + '')
    lines.append('' + repr(rotation) + '')
    lines.append('#')
    for item in lines:
        f.write("%s\n" % item)
    
#This section draws elipses. It requires the dose, the width of the track, the x and y
#positions of the center of the ring, the two radi of the majopr and minor axes and
#the rotation of the ring. If you want you can change the layer the ring is on and
#the number of vertecies making it up which are automatically set to 2 and 64
#respectily if you can't be arsed


def textwrite(dose, width, xpos, ypos, height, angle, ualign, valign, text, f, layer = 2):
    lines = []
    lines.append('T ' + repr(dose) + ' ' + repr(width) + '')
    lines.append('' + repr(xpos) + ' ' + repr(ypos) + '')
    lines.append('' + repr(height) + ' ' + repr(angle) + '')
    lines.append('' + repr(ualign) + ' ' +repr(valign) + '')
    lines.append('' + repr(text) + '')
    lines.append('#')
    for item in lines:
        f.write("%s\n" % item)
#This section writes text


