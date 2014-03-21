ebeam_ASCII_comands
===================

Programs to produce ASCII commands to be read by ebeam

What's here now
----------------

This repositry contains a module file *(ASCIIwriter.py)* and an example file using said module 
*(ringsASCIIfilewriter.py)* and a example output file *(17814ringsdosetest.txt)*.
The ASCIIwriter.py module contains the following commands:-

**circledraw**(dose, xposofcenterofcirle, yposofcenterofcircle, theradiushalfwaybetweeninnerRandouterR, trackwidth (change this if you want rings), layernumber(optional), numberofvertecies(also optional))

**polydraw**(dose, layer, xpoints, ypoints)

**elipsedraw**(dose, xposofcenterofcirle, yposofcenterofcircle, majorradius, minorradius, rotationtrackwidth (change this if you want rings), layer(optional), numberofverticies(also optional))

**textdraw**(dose, trackwidth, xpositionofcenter, ypositionofcenter, textheight, textangle, ualign, valign, textiteld, layer(optional))

**circlewrite**(dose, xposofcenterofcirle, yposofcenterofcircle, theradiushalfwaybetweeninnerRandouterR, fileID, trackwidth (change this if you want rings), layernumber(optional), numberofvertecies(also optional))

**polywrite**(dose, layer, fileID, xpoints, ypoints)

**elipsewrite**(dose, xposofcenterofcirle, yposofcenterofcircle, majorradius, minorradius rotation, fileID, trackwidth (change this if you want rings) layer(optional), numberofverticies(also optional))

**textwrite**(dose, textwidth, xpositionofcenter, ypositionofcenter, textheight, textangle, ualign, valign, textiteld, fileID, layer(optional))

Future developments
--------------------

There will also be functions that draw the results so you can check that you've done the right thing on the fly.
