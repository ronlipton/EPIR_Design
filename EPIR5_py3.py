# -*- coding: utf-8 -*-
# EPIR4 - Add n+ layer 
from pprint import pprint
def grdraw(c, xgr, ygr, wlow, whigh, layer, radius):
#
#  Draw guard rings at radius
#
#       c - cell name
#       xgr - array o x coord of GR arc centers
#       ygr - array o y coord of GR arc centers
#		radius - radius of reference arc
#		wlow - low offset from reference
#		whigh - high offset from reference
#
  angle = 0
  for ind in range(len(xgr)):
    horiz = bool(True)
    x = xgr[ind]
    y = ygr[ind]
#    print(str(angle), str(layer), str(radius))
    c.addPolygonArc(point(x, y), int(radius-wlow), int(radius+whigh), angle, angle+90, layer)
    angle = angle+90
    horiz = not horiz
 #
 #      connect arcs
 #
  pa = pointArray()
  x=xgr[0]
  y=ygr[0]
  pa.attach(x,y+radius-wlow)
  pa.attach(x,y+radius+whigh)
  xn = xgr[1]
  yn = ygr[1]
  pa.attach(xn, yn+radius+whigh)
  pa.attach(xn, yn+radius-wlow)
  c.addBox(pointArray(pa),layer)

  pa = pointArray()
  x=xgr[1]
  y=ygr[1]
  pa.attach(x-radius+wlow,y)
  pa.attach(x-radius-whigh,y)
  xn = xgr[2]
  yn = ygr[2]
  pa.attach(xn-radius-whigh, yn)
  pa.attach(xn-radius+wlow, yn)
  c.addBox(pointArray(pa),layer)

  pa = pointArray()
  x=xgr[2]
  y=ygr[2]
  pa.attach(x,y-radius+wlow)
  pa.attach(x,y-radius-whigh)
  xn = xgr[3]
  yn = ygr[3]
  pa.attach(xn, yn-radius-whigh)
  pa.attach(xn, yn-radius+wlow)
  c.addBox(pointArray(pa),layer)

  pa = pointArray()
  x=xgr[3]
  y=ygr[3]
  pa.attach(x+radius-wlow,y)
  pa.attach(x+radius+whigh,y)
  xn = xgr[0]
  yn = ygr[0]
  pa.attach(xn+radius+whigh, yn)
  pa.attach(xn+radius-wlow, yn)
  c.addBox(pointArray(pa),layer)

def ecdraw(c, xgr, ygr, wlow, whigh, layer, radius):
#
#  Draw edge contacts for x y location tests
#
  angle = 0
  whigh = wlow
  for ind in range(len(xgr)):
    horiz = bool(True)
    x = xgr[ind]
    y = ygr[ind]
#    print(str(angle), str(layer), str(radius))
#    c.addPolygonArc(point(x, y), int(radius-wlow), int(radius+whigh), angle, angle+90, layer)
    angle = angle+90
    horiz = not horiz
 #
 #      connect arcs
 #
    pa = pointArray()
    x=xgr[0]
    y=ygr[0]
    pa.attach(x,y+radius-wlow)
    pa.attach(x,y+radius+whigh)
    xn = xgr[1]
    yn = ygr[1]
    pa.attach(xn, yn+radius+whigh)
    pa.attach(xn, yn+radius-wlow)
    c.addBox(pointArray(pa),layer)
    c.addCircle(layer, point(x, y+radius), point(x-wlow,y+radius), 0)
    c.addCircle(layer, point(xn, yn+radius), point(xn-wlow,yn+radius), 0)
    

    pa = pointArray()
    x=xgr[1]
    y=ygr[1]
    pa.attach(x-radius+wlow,y)
    pa.attach(x-radius-whigh,y)
    xn = xgr[2]
    yn = ygr[2]
    pa.attach(xn-radius-whigh, yn)
    pa.attach(xn-radius+wlow, yn)
    c.addBox(pointArray(pa),layer)

    pa = pointArray()
    x=xgr[2]
    y=ygr[2]
    pa.attach(x,y-radius+wlow)
    pa.attach(x,y-radius-whigh)
    xn = xgr[3]
    yn = ygr[3]
    pa.attach(xn, yn-radius-whigh)
    pa.attach(xn, yn-radius+wlow)
    c.addBox(pointArray(pa),layer)

    pa = pointArray()
    x=xgr[3]
    y=ygr[3]-50
    pa.attach(x+radius-wlow,y)
    pa.attach(x+radius+whigh,y)
    xn = xgr[0]
    yn = ygr[0]
    pa.attach(xn+radius+whigh, yn)
    pa.attach(xn+radius-wlow, yn)
    c.addBox(pointArray(pa),layer)
   


 
def grarray(c, nr, xg, yg, lyr, low, high, rad):
#
#   Draw guard ring array of nr guard rings
#
  for ind in range(nr):
    grdraw(c, xg, yg, low[ind], high[ind], lyr, rad[ind])

def drcorner(xarr, yarr, npts, layer):
#
#   draw 4 corners
#   points assumed as upper right
#
  dr.clearPoints()
  dr.activeLayer = layer
  for ind in range(npts):
    dr.point(xarr[ind], yarr[ind])
  dr.polygon()
# Upper left
  dr.clearPoints()
  dr.activeLayer = layer
  for ind in range(npts):
    dr.point(-xarr[ind], yarr[ind])
  dr.polygon()
# lower left
  dr.clearPoints()
  dr.activeLayer = layer
  for ind in range(npts):
    dr.point(-xarr[ind], -yarr[ind])
  dr.polygon()
# lower right
  dr.clearPoints()
  dr.activeLayer = layer
  for ind in range(npts):
    dr.point(xarr[ind], -yarr[ind])
  dr.polygon()

def DrawGuard(c, activeLength, LImp, LCon, LMet, LOxide, LJTE, ngr):
#
#  Draw an assembly of guard rings
# X and Y center of guard ring assembly
  arccgr = activeLength//2+120000
  halfLength = activeLength//2
  arccx = arccgr
  arccy = arccgr
# passivation opening parameters
  dlong=400000
  dshort=100000
# extent of implants
  implo = [5000]*ngr
  imphi = [5000]*ngr
# extent of contacts
  conlo = [3000]*ngr
  conhi = [3000]*ngr
# JTE
  jtelo = [8000]*ngr
  jtehi = [8000]*ngr
# metal overhang
  metallo = [11000, 11000, 11000, 11000, 34000]
  metalhi = [15000, 15000, 15000, 18000, 63000]
# ring radii from xy center
  ringrad = [84000, 115000, 147000, 178000, 244000]
  xguard = [arccx, -arccx, -arccx, arccx]
  yguard = [arccy, arccy, -arccy, -arccy]
#  layout.drawing.activeLayer=4
# draw implants
  layer = LImp
  grarray(c, nrings, xguard, yguard, layer, implo, imphi, ringrad)
# draw jte
  layer = LJTE
  grarray(c, nrings, xguard, yguard, layer, jtelo, jtehi, ringrad)
# draw contacts
  layer = LCon
  grarray(c, nrings, xguard, yguard, layer, conlo, conhi, ringrad)
# draw metal
  layer= LMet
  grarray(c, nrings, xguard, yguard, layer, metallo, metalhi, ringrad)
# Draw inner guard - outer section
  ogrc = 28000
  grdraw(c, xguard, yguard, ogrc, ogrc-10000, LImp, ogrc)
  grdraw(c, xguard, yguard, 3000, 3000, LCon, ogrc)
  grdraw(c, xguard, yguard, ogrc, ogrc+10000, LMet, ogrc)
  grdraw(c, xguard, yguard, ogrc+5000, ogrc-5000, LJTE, ogrc)
# inner section
  darc = (arccx-halfLength)//2
  arccx = activeLength//2
  arccy = activeLength//2
  xguard = [arccx, -arccx, -arccx, arccx]
  yguard = [arccy, arccy, -arccy, -arccy]
  grdraw(c, xguard, yguard, darc-75000, darc, LImp, darc)
  grdraw(c, xguard, yguard, darc-70000, darc+5000, LJTE, darc)
  grdraw(c, xguard, yguard, darc-60000, darc, LMet, darc)
  grdraw(c, xguard, yguard, darc-85000, darc+15000, LOxide, darc)
# fill in arc
  xcorns = [arccgr, arccgr, arccx]
  ycorns = [arccgr, arccy, arccgr]
  drcorner(xcorns, ycorns, 3, LImp)
  drcorner(xcorns, ycorns, 3, LMet)
  drcorner(xcorns, ycorns, 3, LJTE)
#  Edge ring warning - hard wire n type
#  grdraw(c, xguard, yguard, 50000, 200000, Ledg, 800000) 
#  grdraw(c, xguard, yguard, 5000, 5000, LCon, 800000)
#  grdraw(c, xguard, yguard, 55000, 200000, LMet, 800000)
#  grdraw(c, xguard, yguard, 100000,100000, LOxide, 920000)
  
def InnerGuard(c, activeLength, LImp, LCon, LMet, LOxide, Ledg):
# Draw inner guard - outer section
  arccgr = activeLength//2+120000
  halfLength = activeLength//2
  arccx = arccgr
  arccy = arccgr
  xguard = [arccx, -arccx, -arccx, arccx]
  yguard = [arccy, arccy, -arccy, -arccy]
  ogrc = 28000
  grdraw(c, xguard, yguard, ogrc, ogrc, LImp, ogrc)
  grdraw(c, xguard, yguard, 3000, 3000, LCon, ogrc)
  grdraw(c, xguard, yguard, ogrc, ogrc+10000, LMet, ogrc)
# inner section
  darc = (arccx-halfLength)//2
  arccx = activeLength//2
  arccy = activeLength//2
  xguard = [arccx, -arccx, -arccx, arccx]
  yguard = [arccy, arccy, -arccy, -arccy]
  grdraw(c, xguard, yguard, darc-70000, darc, LImp, darc)
  grdraw(c, xguard, yguard, darc-60000, darc, LMet, darc)
  grdraw(c, xguard, yguard, darc-80000, darc+20000, LOxide, darc)
# fill in arc
  xcorns = [arccgr, arccgr, arccx]
  ycorns = [arccgr, arccy, arccgr]
  drcorner(xcorns, ycorns, 3, LImp)
  drcorner(xcorns, ycorns, 3, LMet)

def EdgeRing(c, activeLength, LImp, LCon, LMet, LOxide, Ledg):
# Draw inner guard - outer section
  arccgr = activeLength//2+120000
  halfLength = activeLength//2
  arccx = activeLength//2
  arccy = activeLength//2
  darc = (arccx-halfLength)//2
  xguard = [arccx, -arccx, -arccx, arccx]
  yguard = [arccy, arccy, -arccy, -arccy]
# fill in arc
  xcorns = [arccgr, arccgr, arccx]
  ycorns = [arccgr, arccy, arccgr]
#  Edge ring warning 
  grdraw(c, xguard, yguard, 50000, 200000, Ledg, 800000) 
  grdraw(c, xguard, yguard, 5000, 5000, LCon, 800000)
  grdraw(c, xguard, yguard, 60000, 220000, LMet, 800000)
  grdraw(c, xguard, yguard, 45000, 190000, LOxide, 800000)

def TEdgeRing(c, activeLength, LImp, LCon, LMet, LOxide, Ledg):
# Draw inner guard - outer section
  arccgr = activeLength//2+120000
  halfLength = activeLength//2
  arccx = activeLength//2
  arccy = activeLength//2
  darc = (arccx-halfLength)//2
  xguard = [arccx, -arccx, -arccx, arccx]
  yguard = [arccy, arccy, -arccy, -arccy]
# fill in arc
  xcorns = [arccgr, arccgr, arccx]
  ycorns = [arccgr, arccy, arccgr]
#  Edge ring warning 
  grdraw(c, xguard, yguard, 225000, 360000, Ledg, 400000) 
  grdraw(c, xguard, yguard, 5000, 5000, LCon, 400000)
  grdraw(c, xguard, yguard, 340000, 420000, LMet, 400000)
#  grdraw(c, xguard, yguard, 45000, 190000, LOxide, 400000)

def makeStrip(cl, activeLength, sgap, siwidth, scwidth, moffs, LP, LM, LC):
#
#   make a Strip cell
#
  slength = activeLength-2*sgap-2*siwidth+120000
  mlength = slength - moffs
  if activeLength < 2000000:
    clength = 160000
  else:
    clength = mlength//2
# add implant
  cl.addBox(-siwidth//2, -slength//2, siwidth, slength, LP)
  cl.addCircle(LP, point(0, -slength//2), point(-siwidth//2, -slength//2), 0)
  cl.addCircle(LP, point(0, slength//2), point(-siwidth//2, slength//2), 0)
# add metal
  cl.addBox(-smwidth//2, -mlength//2, smwidth, mlength, LM)
  cl.addCircle(LM, point(0, -mlength//2), point(-smwidth//2, -mlength//2), 0)
  cl.addCircle(LM, point(0, mlength//2), point(-smwidth//2, mlength//2), 0)
# add contact
  cl.addBox(-scwidth//2, -clength//2, scwidth, clength, LC)
  cl.addCircle(LC, point(0,-clength//2), point(-scwidth//2, -clength//2), 0)
  cl.addCircle(LC, point(0, clength//2), point(-scwidth//2,  clength//2), 0)

def makeACStrip(cl, activeLength, sgap, mwidth, LM):
#
#	sgap - half gap to active length
#	mwidth - metal width
#	LM - metal layer
#		see about pad locations ...
#
  slength = activeLength-2*sgap+120000
  mlength = slength
# add metal
  cl.addBox(-smwidth//2, -mlength//2, mwidth, mlength, LM)
  cl.addCircle(LM, point(0, -mlength//2), point(-mwidth//2, -mlength//2), 0)
  cl.addCircle(LM, point(0, mlength//2), point(-smwidth//2, mlength//2), 0)

#
def makeAssy(cel, celllist):
#
#  make an assembly of multiple cells, all at 0,0
#
  for ind in range(len(celllist)):
    cnew=l.drawing.findCell(clist[ind])
    p=point(0,0)
#    print(cnew, " - ", clist[ind])
    cel.addCellref(cnew,p)

def bpArray(celtgt, bpcell, xur, yur):
#
#  make an 2x2 array of corner bond pad of bpcell
#
	p = point(xur, yur)
	e = celtgt.addCellref(bpcell, p)
	p = point(xur, -yur)
	e = celtgt.addCellref(bpcell, p)
	p = point(-xur, -yur)
	e = celtgt.addCellref(bpcell, p)
	p = point(-xur, yur)
	e = celtgt.addCellref(bpcell, p)

def padArray(homecell, padcell, npad, xstart, xpitch, ypos, smwidth):
  xpad = xstart
  for ind in range(npad):
    p = point (xpad, ypos)
    e = homecell.addCellref(padcell, p)
#    print(p,"-",)
#    pa = pointArray()
#    pa.attach(xpad-smwidth, 0)
#    pa.attach(xpad+smwidth, 0)
#    pa.attach(xpad+smwidth, ypos)
#    pa.attach(xpad-smwidth, ypos)
#    pa.attach(xpad-smwidth, 0)
#    e = homecell.addBox(pa, 6)
    xpad = xpad + xpitch

import LayoutScript
from LayoutScript import *

l=project.newLayout(); # open new instance of layout class
dr=l.drawing 
# pointer to the main drawing
setup.gdsTextToPolygon = True
setup.gdsTextToPolygonDefaultWidth = 200000
setup.defaultTextWidth = 200000
# Layer definitions


#LMetal = 6
#LContact = 5
#LPImplant = 4
NPGain = 3
LNImplant = 8
LOxide = 7
NJTE = 2
NNImplant = 11
NNPlus = 10
NMetal = 12
NContact = 13
NOxide =14
NTrench=15
NPStop=16
# Number of guard rings
nrings = 5
# Device "active lenght"
length = [4000000, 8000000]

SetUp=setup()  # work around as static string variables are not handled correctly
c=l.drawing.currentCell

# Small Bond Pad -top
cpadl=l.drawing.addCell()
cpadl.thisCell.cellName="Bond_Pad_small"
cp = cpadl.thisCell
spadWidth = 300000
spadLength = 70000
oxinset = 5000
e = cp.addRoundedBox((-spadLength+oxinset)//2, (-spadWidth+oxinset)//2, spadLength-oxinset, spadWidth-oxinset, 5000, NOxide)
e = cp.addRoundedBox(-spadLength//2, -spadWidth//2, spadLength, spadWidth, 5000, NMetal)

# Small Bond Pad bottom
cpadl=l.drawing.addCell()
cpadl.thisCell.cellName="Bond_Pad_small_bot"
cp = cpadl.thisCell
oxinset = 5000
e = cp.addRoundedBox((-spadLength+oxinset)//2, (-spadWidth+oxinset)//2, spadLength-oxinset, spadWidth-oxinset, 5000, NOxide)
e = cp.addRoundedBox(-spadLength//2, -spadWidth//2, spadLength, spadWidth, 5000, NMetal)


# Short Bond Pad
cpadl=l.drawing.addCell()
cpadl.thisCell.cellName="Bond_Pad_short"
cp = cpadl.thisCell
spadWidth = 200000
spadLength = 70000
oxinset = 5000
e = cp.addRoundedBox((-spadLength+oxinset)//2, (-spadWidth+oxinset)//2, spadLength-oxinset, spadWidth-oxinset, 5000, NOxide)
e = cp.addRoundedBox(-spadLength//2, -spadWidth//2, spadLength, spadWidth, 5000, NMetal)

Letters = []
CNames = "abcdefghijklmn"
for j in range(13):
	num = l.drawing.addCell()
	cname = "c_" + CNames[j]
	num.thisCell.cellName=cname
##	e = l.drawing.setCell(cname)
	cCell = num.thisCell
	e = cCell.addText(NMetal,point(0,0),CNames[j])
	e.setWidth(200000)
	l.drawing.textSelect()
	l.drawing.toPolygon()
	Letters.append(cCell)

ntype = 3

GR_N = ["4mm_GR_N","8mm_GR_N"]
GR_NJTEcl = []
# GR cell loop
for i in range(len(length)):
	activeLength = length[i]
	halfLength = activeLength//2
	cbJ=l.drawing.addCell()
	cbJ.thisCell.cellName=GR_N[i]
##	e = l.drawing.setCell(GR_NJTEn[i])
	cbJs=cbJ.thisCell
	DrawGuard(cbJs, activeLength, NNPlus, NContact, NMetal, NOxide, 0, nrings)
	GR_NJTEcl.append(cbJs)

# n side Pad and gain cells
Pad_nSide = ["4mm_n_pad","8mm_n_pad"]
#Gain_NJTE = ["1mm_gain_NJTE","4mm_gain_NJTE","8mm_gain_NJTE"]
#Gain_Celln = ["1mm_gain","4mm_gain","8mm_gain"]
Pad_nCells = []
gainround = 100000  # radius of reference arc for GR edges
gainsurr = 50000
moff = 80000
JTEsurr = 10000

#
#  Trenches
#
TRCell = ["TR_4mm_i0","TR_8mm_i0"]
TRInset = ["0", "2", "4"]
TRi = [0, -2000, -4000]
for i in range(len(length)):
	for j in range(len(TRInset)):
		activeLength = length[i]
		ctr = l.drawing.addCell()
		ctr.thisCell.cellName = TRCell[i]+TRInset[j]
		ctrench = ctr.thisCell
		wbox = (activeLength+gainsurr)//2
		xpm = wbox-gainround		
		xm = [xpm, -xpm, -xpm, xpm]
		ym = [xpm, xpm, -xpm, -xpm]
		grdraw(ctrench, xm, ym, TRi[j], 100000, NTrench, gainround)

#  Bias ring
BRName = ["4mm_Bias", "8mm_Bias"]
#	contact half-width
cwidth = 6000   # width of contact
for i in range(len(length)):
	activeLength = length[i]
	cbr = l.drawing.addCell()
	cbr.thisCell.cellName = BRName[i]
	cbias = cbr.thisCell
	wbox = (activeLength+gainsurr)//2
	xpm = wbox-gainround		
	xm = [xpm, -xpm, -xpm, xpm]
	ym = [xpm, xpm, -xpm, -xpm]
	grdraw(cbias, xm, ym, 0, 100000, NNPlus, 0)
	xmi = xpm-11000
	ymi = xpm-34000
	xm = [xmi, -xmi, -xmi, xmi]
	ym = [ymi, ymi, -ymi, -ymi]	
	grdraw(cbias, xm, ym, 0, 23000, NNPlus, 11000)
#		metal
	grdraw(cbias, xm, ym, 50000, 50000, NMetal, 50000)
#		contacts
	xcon = wbox-gainsurr
	conl = activeLength//2
	# add contact
	cbias.addBox(xcon, -conl//2, cwidth, conl, NContact)
	cbias.addCircle(NContact, point(xcon+cwidth//2,-conl//2), point(xcon, -conl//2), 0)
	cbias.addCircle(NContact, point(xcon+cwidth//2,conl//2), point(xcon, conl//2), 0)
	# add contact
	xcon = -xcon
	cbias.addBox(xcon, -conl//2, cwidth, conl, NContact)
	cbias.addCircle(NContact, point(xcon+cwidth//2,-conl//2), point(xcon, -conl//2), 0)
	cbias.addCircle(NContact, point(xcon+cwidth//2,conl//2), point(xcon, conl//2), 0)
	
# bond pads
	bpcell = l.drawing.findCell("Bond_Pad_small_bot")
	xbp = activeLength//2 + spadLength//2 - 70000
	ybp = activeLength//2 - spadWidth//2 - 100000
	bpArray(cbias, bpcell, xbp, ybp)
	
# Pad cell loop

# DC Pad cell
for i in range(len(length)):
	activeLength = length[i]
	wbox = (activeLength+gainsurr)//2
	cpd = l.drawing.addCell()
	cpd.thisCell.cellName = Pad_nSide[i]
	cpad = cpd.thisCell
	e = cpad.addRoundedBox(-(activeLength+gainsurr)//2, -(activeLength+gainsurr)//2, \
	activeLength+gainsurr, activeLength+gainsurr, gainround, NNImplant)
	#  edge region
	xpm = wbox - moff
	xm = [xpm, -xpm, -xpm, xpm]
	ym = [xpm, xpm, -xpm, -xpm]
	grdraw(cpad, xm, ym, 3000, 3000, NContact, moff-17000)
# ** 
	grdraw(cpad, xm, ym, 5000, 5000, NNPlus, moff-17000)
	grdraw(cpad, xm, ym, 0, 70000, NMetal, 0)
#	draw trench
#	xpm = wbox-gainround
#	xm = [xpm, -xpm, -xpm, xpm]
#	ym = [xpm, xpm, -xpm, -xpm]
#	grdraw(cpad, xm, ym, 0, 100000, NTrench, gainround)
	# bond pads
	bpcell = l.drawing.findCell("Bond_Pad_small_bot")
	xbp = activeLength//2 + spadLength//2 - 70000
	ybp = activeLength//2 - spadWidth//2 - 100000
	bpArray(cpad, bpcell, xbp, ybp)
	
#
#	edge contact cell
#
eccell = ["4mm_ec","8mm_ec"]
eccellr = ["4mm_ecr","8mm_ecr"]
ecmetal = 100000
eccont = 10000
ecnpls = 30000
ecinset = 100000
for i in range(len(length)):
	activelength = length[i]
	mlength = activelength-4*ecmetal
	ecpd = l.drawing.addCell()
	ecpd.thisCell.cellName = eccell[i]
	cec = ecpd.thisCell
	cec.addBox(-ecmetal//2, -mlength//2, ecmetal, mlength, NMetal)
	cec.addCircle(NMetal, point(0, -mlength//2), point(-ecmetal//2, -mlength//2), 0)
	cec.addCircle(NMetal, point(0,  mlength//2), point(-ecmetal//2,  mlength//2), 0)
# ** **
	cec.addBox(-eccont//2, -mlength//2, eccont, mlength, NContact)
	cec.addCircle(NContact, point(0, -mlength//2), point(-eccont//2, -mlength//2), 0)
	cec.addCircle(NContact, point(0,  mlength//2), point(-eccont//2,  mlength//2), 0)
	
	cec.addBox(-ecnpls//2, -mlength//2, ecnpls, mlength, NNPlus)
	cec.addCircle(NNPlus, point(0, -mlength//2), point(-ecnpls//2, -mlength//2), 0)
	cec.addCircle(NNPlus, point(0,  mlength//2), point(-ecnpls//2,  mlength//2), 0)
	
	p = point (50000, 0)
	e = cec.addCellref(cp, p)
	
	ecpdr = l.drawing.addCell()
	ecpdr.thisCell.cellName = eccellr[i]
	cecr = ecpdr.thisCell
	p = point (0, 0)
	e = cecr.addCellref(cec ,p)
	e = cecr.selectCellref(eccell[i])
	e = cecr.rotateSelect(180.,p)
	
	
# XY Pad cell
Pad_xy = ["4mm_xy_pad","8mm_xy_pad"]
#Gain_NJTE = ["1mm_gain_NJTE","4mm_gain_NJTE","8mm_gain_NJTE"]
#Gain_Celln = ["1mm_gain","4mm_gain","8mm_gain"]
Pad_nCells = []
for i in range(len(length)):
	activeLength = length[i]
	wbox = (activeLength+gainsurr)//2
	epd = l.drawing.addCell()
	epd.thisCell.cellName = Pad_xy[i]
	cpad = epd.thisCell
	e = cpad.addRoundedBox(-(activeLength+gainsurr)//2, -(activeLength+gainsurr)//2, \
	activeLength+gainsurr, activeLength+gainsurr, gainround, NNImplant)
	#  edge region
	xpm = wbox - moff
	edgeoff = activeLength//2-ecinset
	cnew = dr.findCell(eccell[i])
	p = point(-edgeoff, 0)
	e = cpad.addCellref(cnew ,p)
	p = point(edgeoff, 0)
	cnewr = dr.findCell(eccellr[i])
	e = cpad.addCellref(cnewr ,p)
		
	e = cpad.selectCellref(eccell[i])
	e = cpad.selectCellref(eccellr[i])
	p = point(0, 0)
	e = cpad.copySelect(p)
	e = cpad.rotateSelect(90.,p)
## add top, bottom	
#	draw trench
#	xpm = wbox-gainround
#	xm = [xpm, -xpm, -xpm, xpm]
#	ym = [xpm, xpm, -xpm, -xpm]
#	grdraw(cpad, xm, ym, 0, 100000, NTrench, gainround)
	# bond pads
#	bpcell = l.drawing.findCell("Bond_Pad_small_bot")
#	xbp = activeLength//2 + spadLength//2 - 70000
#	ybp = activeLength//2 - spadWidth//2 - 100000
#	bpArray(cpad, bpcell, xbp, ybp)

#
#	make AC strips
#
ACStripn = ["4mm_80m_acstrip","8mm_80m_acstrip"]
sgap = 160000
#	use 80n micron width for now
smwidth = 80000
for i in range(len(length)):
#  AC Strip Cell
	# full width strip
	cac=l.drawing.addCell()
	cac.thisCell.cellName=ACStripn[i]
	mo = 0
	activeLength = length[i]-sgap
	makeACStrip(cac.thisCell, activeLength, sgap, smwidth,  NMetal)

#  make DC strip
#  def makeStrip(cl, activeLength, sgap, siwidth, scwidth, moffs, LP, LM, LC):
SPitch = [100000,200000]
DCStripn = ["4mm_DCstrip","8mm_DCstrip"]
siwidth = 50000
scwidth = 6000
moffs = 10000
for i in range(len(length)):
#  DC Strip Cell
	# full width strip
	cdc=l.drawing.addCell()
	cdc.thisCell.cellName=DCStripn[i]
	cd = cdc.thisCell
	activeLength = (length[i]-sgap)
	makeStrip(cd, activeLength, sgap, siwidth, scwidth, moffs, NNPlus, NMetal, NContact)

#
#	add p-stop to strip
rad = 25000
inset = 6000
pswidth=3000
PSLenn = ["4mm","8mm"]
PSPitchn = ["_100PS", "_200PS"]
for i in range(len(length)):
	pslen = (length[i]-sgap)//2-120000
	DCCell = DCStripn[i]
	for j in range(len(SPitch)):
		celln = PSLenn[i]+PSPitchn[j]
		psx = SPitch[j]//2-rad
		xps = [psx, -psx,-psx, psx]
		yps = [pslen, pslen, -pslen, -pslen]
		c=l.drawing.addCell()
		c.thisCell.cellName=celln
		cc = c.thisCell
		grdraw(cc, xps, yps, pswidth, pswidth, NPStop, rad)
		p=point(0,0)
		cnew=l.drawing.findCell(DCCell)
		cc.addCellref(cnew,p)


#	Make DCstrip arrays
#
DCAName = ["DCArr100_", "DCArr200_"]
# PSPitchn = ["_100PS", "_200PS"] PSLenn = ["4mm","8mm"]
for i in range(len(length)):
	for j in range(len(SPitch)):
		PSCell = PSLenn[i]+PSPitchn[j]
		celln = DCAName[j]+PSCell
		activeLength = length[i]
		c=l.drawing.addCell()
		c.thisCell.cellName=celln
		cc = c.thisCell
		spitch = SPitch[j]		
		sgap = 25000  # ???
#		nstrip = (activeLength - 2*sgap + 120000)/spitch
		nstrip = (activeLength - 2*sgap)/spitch
#		print(spitch)
		ns = int(nstrip)-2
		p = point(0, 0)
		xoff = int(-(spitch*(ns-1)//2))
#		print(PSCell)
		cnew=l.drawing.findCell(PSCell)
		e = cc.addCellrefArray(cnew, point(xoff, 0), point(xoff+spitch, 0), ns, 1)
#  bond pads
		endoffset = 600000
		midoffset = 330000
		endpt = (activeLength - 2*(sgap) + 120000)//2
		padArray(cc, cp, int(nstrip//2), xoff, spitch*2, endpt-midoffset, smwidth//2)
		padArray(cc, cp, int(nstrip//2)-1, xoff+spitch, spitch*2, endpt-endoffset, smwidth//2)
		padArray(cc, cp, int(nstrip//2), xoff, spitch*2, -(endpt-midoffset), smwidth//2)
		padArray(cc, cp, int(nstrip//2)-1, xoff+spitch, spitch*2, -(endpt-endoffset), smwidth//2)

#	Make ACstrip arrays
#
ACAName = ["ACArr100_", "ACArr200_"]
ACPName = ["4mm","8mm"]
ACSPitch = [100000,200000]
for i in range(len(length)):
	for j in range(len(ACSPitch)):
		celln = ACAName[j]+ACPName[i]
		activeLength = length[i]
		c=l.drawing.addCell()
		c.thisCell.cellName=celln
		cc = c.thisCell
		spitch = ACSPitch[j]		
		sgap = 25000  # ???
#		nstrip = (activeLength - 2*sgap + 120000)/spitch
		nstrip = (activeLength - 2*sgap)/spitch
#		print(spitch)
		ns = int(nstrip)-2
		p = point(0, 0)
		xoff = int(-(spitch*(ns-1)//2))
		cnew=l.drawing.findCell(ACStripn[i])
		e = cc.addCellrefArray(cnew, point(xoff, 0), point(xoff+spitch, 0), ns, 1)
#  pads
		endoffset = 600000
		midoffset = 330000
		endpt = (activeLength - 2*(sgap) + 120000)//2
		padArray(cc, cp, int(nstrip//2), xoff, spitch*2, endpt-midoffset, smwidth//2)
		padArray(cc, cp, int(nstrip//2)-1, xoff+spitch, spitch*2, endpt-endoffset, smwidth//2)
		padArray(cc, cp, int(nstrip//2), xoff, spitch*2, -(endpt-midoffset), smwidth//2)
		padArray(cc, cp, int(nstrip//2)-1, xoff+spitch, spitch*2, -(endpt-endoffset), smwidth//2)

#  DC Strip Arrays
DCAName = ["DCArr100_", "DCArr200_"]
DCPName = ["4mm","8mm"]
for i in range(len(length)):
	for j in range(len(SPitch)):
		celln = DCAName[j]+DCPName[i]
		activeLength = length[i]
		c=l.drawing.addCell()
		c.thisCell.cellName=celln
		cc = c.thisCell
		spitch = SPitch[j]		
		sgap = 25000  # ???
		
#		nstrip = (activeLength - 2*sgap + 120000)/spitch
		nstrip = (activeLength - 2*sgap)/spitch
#		print(spitch)
		ns = int(nstrip)-2
		p = point(0, 0)
		xoff = int(-(spitch*(ns-1)//2))
		cnew=l.drawing.findCell(DCStripn[i])
		e = cc.addCellrefArray(cnew, point(xoff, 0), point(xoff+spitch, 0), ns, 1)
#  pads
		endoffset = 600000
		midoffset = 330000
		endpt = (activeLength - 2*(sgap) + 120000)//2
		padArray(cc, cp, int(nstrip//2), xoff, spitch*2, endpt-midoffset, smwidth//2)
		padArray(cc, cp, int(nstrip//2)-1, xoff+spitch, spitch*2, endpt-endoffset, smwidth//2)
		padArray(cc, cp, int(nstrip//2), xoff, spitch*2, -(endpt-midoffset), smwidth//2)
		padArray(cc, cp, int(nstrip//2)-1, xoff+spitch, spitch*2, -(endpt-endoffset), smwidth//2)

# cutlines
CVert = [3150000, 5150000]
CHor = [3154500, 5150500]
CutLn = ["4mm_cutl","8mm_cutl"]
halfwid = 50000
for i in range(len(length)):
	ccl = l.drawing.addCell()
	ccl.thisCell.cellName= CutLn[i]
	cutline = ccl.thisCell
	lcx = -CVert[i]-halfwid
	lcy = -CHor[i]-halfwid
	e = cutline.addBox(lcx, lcy, 2*halfwid, 2*CHor[i]+2*halfwid, NContact)
	e = cutline.addBox(lcx, lcy, 2*halfwid, 2*CHor[i]+2*halfwid, NOxide)
	e = cutline.addBox(lcx, lcy, 2*CVert[i]+2*halfwid, 2*halfwid, NContact)
	e = cutline.addBox(lcx, lcy, 2*CVert[i]+2*halfwid, 2*halfwid, NOxide)
	lcx = CVert[i]-halfwid
	e = cutline.addBox(lcx, lcy, 2*halfwid, 2*CHor[i]+2*halfwid, NContact)
	e = cutline.addBox(lcx, lcy, 2*halfwid, 2*CHor[i]+2*halfwid, NOxide)
	lcx = -CVert[i]-halfwid
	lcy = CHor[i]-halfwid
	e = cutline.addBox(lcx, lcy, 2*CVert[i]+2*halfwid, 2*halfwid, NContact)
	e = cutline.addBox(lcx, lcy, 2*CVert[i]+2*halfwid, 2*halfwid, NOxide)

#
#		Make assemblies
#
#  list of cell names
CellList = []
# Assemble pad cells
#
#	TRCell = ["TR_4mm_i0","TR_8mm_i0"]
#	TRInset = ["0", "2", "4"]
#	Pad_nSide = ["4mm_n_pad","8mm_n_pad"]
#	CutLn = ["4mm_cutl","8mm_cutl"]
#print(Pad_nSide)
for i in range(len(length)):
	c = l.drawing.addCell()
	cname = "Assy_" + Pad_nSide[i]
	c.thisCell.cellName = cname
	tname = TRCell[i] + TRInset[0]
	Assy_pad = c.thisCell
	clist = [Pad_nSide[i],tname,CutLn[i]]
	makeAssy(Assy_pad, clist)
	CellList.append(cname)

#  xy Pads
#	Pad_xy = ["4mm_xy_pad","8mm_xy_pad"]
for i in range(len(length)):
	c = l.drawing.addCell()
	cname = "Assy_" + Pad_xy[i]
	c.thisCell.cellName = cname
	Assy_xypad = c.thisCell
	tname = TRCell[i] + TRInset[0]
	clist = [Pad_xy[i],tname, CutLn[i]]
	makeAssy(Assy_xypad, clist)
	CellList.append(cname)

# Strip cells
for i in range(len(length)):
	for j in range(len(ACSPitch)):
		c = l.drawing.addCell()
		cname =  "Assy_" + ACAName[j] + ACPName[i]
		c.thisCell.cellName = cname
		ACname = ACAName[j] + ACPName[i]
		tname = TRCell[i] + TRInset[0]
		Assy_pad = c.thisCell
		clist = [Pad_nSide[i], ACname, tname, CutLn[i]]
#		print(clist)
		makeAssy(Assy_pad, clist)
		CellList.append(cname)

#		DC Strips
#
# Strip cells
for i in range(len(length)):
	for j in range(len(SPitch)):
		PSCell = PSLenn[i]+PSPitchn[j]
		celln = DCAName[j]+PSCell
		c = l.drawing.addCell()
		cname = "Assy_" + celln
		c.thisCell.cellName = cname
		tname = TRCell[i] + TRInset[0]
		Assy_pad = c.thisCell
		clist = [celln, BRName[i], tname, CutLn[i]]
#		print(clist)
		makeAssy(Assy_pad, clist)
		CellList.append(cname)
		
print(CellList)
l.drawing.saveFile("/Users/ronlipton/Dropbox/Programming/EPIR_V5.gds")
print("Python script completed")
exit()

# Assemble 8mm pad cell
c = l.drawing.addCell()
c.thisCell.cellName = "8mm_pad_Assy"
# e = l.drawing.setCell("8mm_pad_Assy")
Asy_pad_8mm = c.thisCell
#clist = ["8mm_GR_bot","8mm_GR_top","8mm_gain","8mm_pad","8mm_n_pad"]
clist = ["8mm_GR_bot","8mm_GR_top","8mm_gain","8mm_pad","8mm_cutl"]
makeAssy(Asy_pad_8mm, clist)
# Assemble 8mm pad cell - nogain
c = l.drawing.addCell()
c.thisCell.cellName = "8mm_pad_Assy_ng"
Asy_pad_8mm_ng = c.thisCell
clist = ["8mm_GR_bot","8mm_GR_top","8mm_pad","8mm_bot_pad","8mm_cutl"]
makeAssy(Asy_pad_8mm_ng, clist)
#  Assembly DC strips


l.drawing.saveFile("/Users/ronlipton/Dropbox/Programming/EPIR_V5_Test.gds")
print("Python script completed")

 
