
import ASCIIwriter as AS
import os
filename = '19314ringsdosetest.txt'



if os.path.isfile(filename):
    print 'WARNING: Overwriting previous file'
    open(filename, 'w').close()#emptys the file and warns the user that it's
    #doing so
    
f=open(filename, 'w')

ringdiams = (0.5, 1, 2, 5, 10, 15, 20)#Outer diameters of the rings
tracks = (1, 0.8, 0.6, 0.4, 0.2, 0.1, 0.05)#Thicknesses of the ring tracks
poses = (130, 160, 190, 220, 250, 280, 310)#Positions of ring centers (raw)
lopyoff = (0, 210) #The offset due to the fact we have 2 sets of rings in each
#object set
doses = range(10,210,10)#list of the doses we want
dxoff = range(0, 3750 , 750) #list of  the x offsets in order to put each set of 
#objects with different doses at different postions
dyoff = range(0, 3750 , 750)#list of  the x offsets in order to put each set of 
#objects with different doses at different postions

#Loop for putting the ringsw down, puts down 2 sets of rings one higher
#than the other in y
count = 0
for y1 in range(4):#moves up a step in y draws all the squares in x and moves on
    for x1 in range(5):#runs along x increasing the dose each time
        dose = doses[count]#sets the dose for this object
        count += 1#sets a counter so that you can know which object set your
        #working on
        print dose
        for n1 in range(2):
            for x in range(len(tracks)):
                for y in range(len(ringdiams)):
                    outrad = ringdiams[y] / 2
                    track = tracks[x]
                    crad = outrad - (track / 2)
                    xpos = poses[x] + dxoff[x1]
                    ypos = poses[y] + lopyoff[n1] + dyoff[y1]
                    if track*2 < outrad:
                        lines = AS.circledraw(dose, xpos, ypos, crad, track)
                        for item in lines:
                            f.write("%s\n" % item)#writes the loop to the file


        sqxoff = (0, 0, 0, 370, 370, 370)
        sqyoff = (0, 305, 610, 0, 305, 610)
        layer = 2
        for sq1 in range(6):
            xs = [0, 0, 100, 100, 0]
            ys = [0, 100, 100, 0, 0]

            for i in range(len(xs)):
                xs[i] = xs[i] + sqxoff[sq1] + dxoff[x1]#set the x offset on each
                #corner on the square
                ys[i] = ys[i] + sqyoff[sq1] + dyoff[y1]#set the y offset on each
                #corner on the square
            lines = AS.polydraw(dose, layer, xs, ys)
            for item in lines:
                f.write("%s\n" % item)#writes the square to the file
    

f.close()

