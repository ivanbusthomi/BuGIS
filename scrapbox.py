# from test.py -----------------------------------------------------------------------------
from qgis.core import *

def createPointsAt(distance, lineGeom):                 # STATUS OK
    currentdistance = distance
    # Get a point along the line at the current distance
    pointAtLine = geom.interpolate(currentdistance)
    # Increase the distance
    currentdistance = currentdistance + distance
    return pointAtLine

def pointsAlongLine(distance):
    # Create a new memory layer and add a distance attribute
    vl = poi
    pr = vl.dataProvider()
    # Loop though all the selected features
    for feature in line.selectedFeatures():
        geom = feature.geometry()
        features = createPointsAt(distance, geom)
        pr.addFeatures(features)
        vl.updateExtents()

# ------------------------------------------------------------------------------------------------------
lay = iface.mapCanvas().layers()
pLayerA=lay[0]
pLayerB=lay[1]
#from PyQt4.QtCore import QVariant
#----- polygon
cFeat = QgsFeature()
cFeat.setGeometry(c)
buffLayer = QgsVectorLayer("Polygon","Buffer Result", "memory")
prBuff = buffLayer.dataProvider()
prBuff.addFeatures()
QgsMapLayerRegistry.instance().addMapLayer(buffLayer)

#----- point
cFeat = QgsFeature()
cFeat.setGeometry(c)
buffLayer = QgsVectorLayer("Point","Buffer Result", "memory")
prBuff = buffLayer.dataProvider()
prBuff.addFeatures()
QgsMapLayerRegistry.instance().addMapLayer(buffLayer)

#----- line
lineLayer = QgsVectorLayer("LineString","Line Result", "memory")

lFeat = QgsFeature()
lFeat.setGeometry(ppLine)
lineBuff = lineLayer.dataProvider()
lineBuff.addFeatures([lFeat])

QgsMapLayerRegistry.instance().addMapLayer(lineLayer)

def thirdIteration(self,pLayerA,pLayerB,ppLine):               #check
    #container for third point
    threePoints = []
    # find minimum distance of intersection


    for b in pLayerB.getFeatures():
        for d in range (0,21):
            distance = d*1000
            buff = pointAgeom.buffer(distance,20)
            if buff.intersects(b.geometry()):
                break
        break
    # find which point intersect at minimum given distance
    inter = [] # container for intersect feature
    for b in pLayerB.getFeatures():
        buff = pointAgeom.buffer(distance,20)
        if buff.intersects(b.geometry()):
            inter.append(b)
    # find closest point
    if len(inter) = 1:
        thirdPoint.append(inter[0])
    elif len(inter)>1:
        nearestPoint =

def nearestPoint(point, points):                    #check this
    import math

    for i in points:
        iAsPoint = i.geometry().asPoint()
        currentDistance = 99999999999999999
        distance = math.sqrt(point.sqrDist(iAsPoint))
        if distance < currentDistance:
            currentDistance = distance
            nearestPoint = iAsPoint



def perpendicularLine(pointA,pointB):                      # STATUS : working      OUTPUT : QgsGeometry
    # this function is to find a line that is perpendicular to line AB at its midpoint
    import math
    x1 = pointA.x()
    y1 = pointA.y()
    x2 = pointB.x()
    y2 = pointB.y()
    #-------------------------------------
    middleCoord = midPoint(pointA,pointB)
    middlePoint = QgsPoint(middleCoord[0],middleCoord[1])
    xm = middlePoint.x()
    ym = middlePoint.y()
    #-------------------------------------
    # get max extent value from both point layer
    extA = pLayerA.extent()     #global variable
    extB = pLayerB.extent()     #global variable
    if extA.xMaximum() > extB.xMaximum():
        xmax = extA.xMaximum()
    else:
        xmax = extB.xMaximum()
    if extA.yMaximum() > extB.yMaximum():
        ymax = extA.yMaximum()
    else:
        ymax = extB.yMaximum()
    # in order to shorten the equation
    P = x2 - x1
    Q = y2 - y1
    R = xm - x1
    S = ym - y1
    # line gradien, for determining max distance of perpendicular line
    gradien1 = Q / P
    gradien2 = -1/gradien1
    #-------------------------------------
    u = R / P
    u_ = S / Q                                                      # optional value, only for checking
    d2 = pointA.sqrDist(pointB)                                     # d is the distance. d2 is square of d
    #-------------------------------------
    # here comes the equation
    # y3*Q = (-P)*x3 + P*x1 + Q*y1 + u*d2
    # x3*P = (-Q)*y3 + P*x1 + Q*y1 + u*d2
    #-------------------------------------
    # we want the perpendicular line goes until the maximum value of pointA and B, just to make sure it works
    # in any shape of topography,,,,,,,,,, or maybe minimum value of pointA and B. need more consideration later.
    if math.pow(gradien2,2) > 1:
        y3 = ymax
        x3 = ((-Q)*y3 + P*x1 + Q*y1 + u*d2) / P
    else:
        x3 = xmax
        y3 = ((-P)*x3 + P*x1 + Q*y1 + u*d2) / Q
    #-------------------------------------
    ppdPoint = QgsPoint(x3,y3)
    pointList = []
    pointList.append(middlePoint)
    pointList.append(ppdPoint)
    #-------------------------------------
    p3Line = QgsGeometry.fromPolyline(pointList)
    return p3Line                                               # type QgsGeometry




def createPointsAt(distance, ppLine):
    length = ppLine.length()
    currentdistance = distance
    feats = []
    while currentdistance < length:
        # Get a point along the line at the current distance
        point = ppLine.interpolate(currentdistance)
        # Create a new QgsFeature and assign it the new geometry
        feats.append(point)
        # Increase the distance
        currentdistance = currentdistance + distance
    return feats

def pointsAlongLine(distance):
    # Create a new memory layer and add a distance attribute
    pA = pLayerA.selectedFeatures()
    pB = pLayerB.selectedFeatures()
    pointA = pA[0].geometry().asPoint()
    pointB = pB[0].geometry().asPoint()
    res = []
    ppLine = perpendicularLine(pointA,pointB)
    features = createPointsAt(distance, ppLine)
    res.append
    return features