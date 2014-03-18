ebeam_ASCII_comands
===================

Programs to produce ASCII commands to be read by ebeam

What's here now
----------------

This repositry contains a module file *(ASCIIwriter.py)* and an example file using said module 
*(ringsASCIIfilewriter.py)* and a example output file *(17814ringsdosetest.txt)*.
The ASCIIwriter.py module contains the following commands:-

**circledraw**(dose, trackwidth, xposofcenterofcirle, yposofcenterofcircle, theradiushalfwaybetweeninnerRandouterR, layernumber(optional), numberofvertecies(also optional))

**polydraw**(dose, layer, xpoints, ypoints)

**elipsedraw**(dose, trackwidth, xposofcenterofcirle, yposofcenterofcircle, majorradius, minorradius rotation, layer(optional), numberofverticies(also optional))

**textdraw**(dose, trackwidth, xpositionofcenter, ypositionofcenter, textheight, textangle, ualign, valign, textiteld, layer(optional))

**circlewrite**(dose, trackwidth, xposofcenterofcirle, yposofcenterofcircle, theradiushalfwaybetweeninnerRandouterR, fileID, layernumber(optional), numberofvertecies(also optional))

**polywrite**(dose, layer, fileID, xpoints, ypoints)

**elipsewrite**(dose, trackwidth, xposofcenterofcirle, yposofcenterofcircle, majorradius, minorradius rotation, fileID layer(optional), numberofverticies(also optional))

**textwrite**(dose, trackwidth, xpositionofcenter, ypositionofcenter, textheight, textangle, ualign, valign, textiteld, fileID, layer(optional))

Future developments
--------------------

There will also be functions that draw the results so you can check that you've done the right thing on the fly.
