import LayoutScript
from LayoutScript import *


l=project.newLayout(); # open new instance of layout class
dr=l.drawing # pointer to the main drawing

# offset of labels from cell center
mm4_offsetx = -2600000
mm4_offsety =  3020000
mm8_offsetx = -4800000
mm8_offsety =  5020000

# 8mm cell spacings
mm8_xspacing = 10300.
mm8_yspacing = 10300.
# 4mm cell spacings
mm4_xspacing = 6300.
mm4_yspacing = 6300.

icol_offset_4mm = 12.
irow_offset_4mm = 7.
icol_offset_8mm = 7.
irow_offset_8mm = 7.

# EPIR logo offset 
Elogox_8mm =  4500000
Elogoy_8mm = -4700000

Elogox_4mm =  2600000
Elogoy_4mm = -2800000

NMetal=12


SetUp=setup()  # work around as static string variables are not handled correctly
hdir = "/Users/ronlipton/Dropbox/Consult/EPIR Design/"
l.open(hdir+"EPIR.GDS") # load design

sourceFile = open(hdir+'/EPIR_Cells.txt', 'w')

cl=l.drawing.firstCell # pointer to current cell
c=cl.thisCell
#
clab = l.drawing.addCell()
clab.thisCell.cellName = "labels"
labcell = clab.thisCell
clogo=l.drawing.findCell("EPIR_Logo")

el=c.firstElement
while (el!=None):  #loop over all cells
 if (el.thisElement!=None):
   if (el.thisElement.isCellref()):
     cname=el.thisElement.depend().cellName
#         print("Cell :"+ cname)
#        result+="reference_to_"+cname
     pa=el.thisElement.getPoints()
     ang = el.thisElement.getTrans().getAngle()
#         print("Angle: " + str(ang))
#          sy.setNum(el->thisElement->getTrans().getScale(),3);
     for i in range (0,pa.size()): # output all coordinates
        xn=pa.point(i).x()
        yn=pa.point(i).y()
        x = xn/1000
        y = yn/1000
#        print(cname + " , "+str(x)+" , "+str(y)+" ", file = sourceFile)
        if (y>0):
          col = (x + mm4_xspacing/2)/mm4_xspacing + icol_offset_4mm 
          icol = int(col + .5)
          row = (y + mm4_yspacing/2)/mm4_yspacing+ irow_offset_4mm
          irow = int(row +.5 )
          lname = cname+  "(R" + str(irow) + "C" + str (icol) + ")"
          par = point(xn+mm4_offsetx, yn+mm4_offsety)
          e=labcell.addText(NMetal,par,lname)
          e.setWidth(200000)
          p=point(xn + Elogox_4mm, yn + Elogoy_4mm)
          labcell.addCellref(clogo,p)
          
        else:   
          col = (x + mm8_xspacing/2)/mm8_xspacing + icol_offset_8mm 
          icol = int(col + .5 )
          row = (y + mm8_yspacing/2)/mm8_yspacing+ irow_offset_8mm 
          irow = int(row + .5 )
          lname = cname+  "(R" + str(irow) + "C" + str (icol) + ")"
          par = point(xn+mm8_offsetx, yn+mm8_offsety)
          e=labcell.addText(NMetal,par,lname)
          e.setWidth(200000)
          p=point(xn + Elogox_8mm, yn + Elogoy_8mm)
          labcell.addCellref(clogo,p)
          
        print(lname + " R" + str(row) + " C" + str(col), file = sourceFile)


 el=el.nextElement

import os
sourceFile.close()

l.drawing.saveFile(hdir+"EPIR_Nov17.GDS")

print ("Python script completed" )