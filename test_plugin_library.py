from qgis.core import *
from PyQt4.QtCore import QVariant
import math

def circumCenter(self, pointA, pointB, pointC):
    xA=pointA.x()
    yA=pointA.y()

    xB=pointB.x()
    yB=pointB.y()

    xC=pointC.x()
    yC=pointC.y()

    a2 = xA^2+yA^2
    b2 = xB^2+yB^2
    c2 = xC^2+yC^2

    const = 2*(xA*(yB-yC)+xB*(yC-yA)+xC*(yA-yB))
    xO = (a2*(yB-yC)+b2*(yC-yA)+c2*(yA-yB))/const
    yO = (a2*(xC-xB)+b2*(xA-xC)+c2*(xB-xA))/const
    pointO = QgsPoint(xO,yO)
    return pointO

def lineToPoint(lineLayer,attr):                                       # STATUS : working      OUTPUT : memory layer
    #from PyQt4.QtCore import QVariant
    # function to convert line feature to point feature
    # PS: add function to add Attribute of A and B layer, to differentiate in processing later
    pointLayer = QgsVectorLayer("Point", "Point Result", "memory")
    prPoint = pointLayer.dataProvider()
    # add attribute collumns
    prPoint.addAttributes([QgsField("fid",QVariant.Int),QgsField("ket",QVariant.String)])
    feats = []
    for line in lineLayer.getFeatures():
        #get coordinate list from asPolyline function
        lineGeom = line.geometry()
        listCoord = lineGeom.asPolyline()
        inc = 0
        #convert to point
        for c in listCoord:
            increase = inc
            point = QgsPoint(c[0],c[1])
            geomPoint = QgsGeometry.fromPoint(point)
            #feat = QgsFeature(fields_)
            feat = QgsFeature()
            feat.setGeometry(geomPoint)
            # add atributes
            feat.setAttributes([increase,attr])
            inc = increase + 1
            feats.append(feat)
        prPoint.addFeatures(feats)
        QgsMapLayerRegistry.instance().addMapLayer(pointLayer)                      #add to defined point layer
        return pointLayer


def pointToLine(pointLayer):                                    # STATUS : working      OUTPUT : memory layer
    # function to convert point features to line feature
    canvas = iface.mapCanvas()
    lineLayer = QgsVectorLayer("LineString", "Line Result", "memory")              # line Layer saved in memory
    prLine = lineLayer.dataProvider()
    pointList = []
    for point in pointLayer.getFeatures():
        p = point.geometry().asPoint()
        pointList.append(p)
    feat = QgsFeature()
    lineGeom = QgsGeometry.fromPolyline(pointList)
    feat.setGeometry(lineGeom)
    prLine.addFeatures([feat])
    QgsMapLayerRegistry.instance().addMapLayer(lineLayer)

def midPoint(point1,point2):        # working fine
    #this function returns midpoint from two input point as result.
    x1=point1.x()
    y1=point1.y()
    x2=point2.x()
    y2=point2.y()
    xMid=x1+(x2-x1)/2.0
    yMid=y1+(y2-y1)/2.0
    mid=(xMid,yMid)
    return mid

def pointInLine(line):
    # this function will return nearest poin within a line, and take mouse click position as input.
    # similiar with perpendicular line creation,
    # param 1 type is polyline layer


def perpendicularLine(pointA,pointB,direction):
    # this function is to find a line that is perpendicular to line AB at its midpoint
    # param 1 and 2 type is point
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
        xmin = extA.xMinimum()
    else:
        xmax = extB.xMaximum()
        xmin = extB.xMinimum()
    if extA.yMaximum() > extB.yMaximum():
        ymax = extA.yMaximum()
        ymin = extA.yMinimum()
    else:
        ymax = extB.yMaximum()
        ymin = extB.yMinimum()
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
    if direction == 1:                  # line direction is up
        xlim = xmax
        ylim = ymax
    elif direction == 0:                # line direction is down
        xlim = xmin
        ylim = ymin

    if math.pow(gradien2,2) > 1:
        y3 = ylim
        x3 = ((-Q)*y3 + P*x1 + Q*y1 + u*d2) / P
    else:
        x3 = xlim
        y3 = ((-P)*x3 + P*x1 + Q*y1 + u*d2) / Q
    #-------------------------------------
    ppdPoint = QgsPoint(x3,y3)
    pointList = []
    pointList.append(middlePoint)
    pointList.append(ppdPoint)
    #-------------------------------------
    p3Line = QgsGeometry.fromPolyline(pointList)
    return p3Line                                               # type QgsGeometry

def nearestPoint(point, points):                                # STATUS working
    import math                                                 # param1 = point, param 2=list of features
    currentDistance = 99999999999999999                         # output = nearest feature to param1
    for i in points:
        iAsPoint = i.geometry().asPoint()
        distance = math.sqrt(point.sqrDist(iAsPoint))
        if distance < currentDistance:
            currentDistance = distance
            nearest = i
    return nearest

def distanceFromPoints(point1,point2):
    import math
    return math.sqrt(point1.sqrDist(point2))

def pointAlongLine(intv, line):
    # this function will create geometry point along line at the specified distance
    length = line.length()
    cDistance = intv
    features = []
    while cDistance < length:
        point = line.interpolate(cDistance)
        feat = QgsFeature()
        feat.setGeometry(point)
        features.append(feat)
        #increase
        cDistance = cDistance + intv
    return features

def join(pLayerA,pLayerB):
    # join two points layer
    aC = []
    bC = []
    for a in pLayerA.getFeatures():
        aC.append(a)
    for b in pLayerB.getFeatures():
        bC.append(b)
    mC = aC + bC
    return mC       #return list of feature

def intersected(pointA,pointB,geom,list_of_feat):           #STATUS : working
    list_of_result=[]
    for f in list_of_feat:
        fGeom = f.geometry()
        fPoint = fGeom.asPoint()
        if fGeom.intersects(geom):
            list_of_result.append(f)
    return list_of_result

def nextPoint(start_pointA,start_pointB,itv):                   #STATUS : working
    # iteration with input from point layers and interval with result dictionary of three point list
    pA = start_pointA
    pB = start_pointB
    ppLine = perpendicularLine(pA,pB,0) # perpendicular line at ab's midpoint. third parameter defines directions of the line that will be created
    ppPoints = pointAlongLine(itv,ppLine)
    #-------------------- buffer method
    for p in ppPoints:
        pPoint=p.geometry().asPoint()
        dA = distanceFromPoints(pA,pPoint)
        buff = p.geometry().buffer(dA,15)
        jPoint = join(pLayerA,pLayerB)
        result_ = intersected(pA,pB,buff,jPoint)
        if len(result_)>1:
            r = nearestPoint(pPoint,result_)
            break
        elif len(result_)==1:
            r = result_[0]
            break
        elif len(result_)==0:
            continue
    return p,r  #,result_                   <-------- return result only for checking purpose


    #result = []
    #for p in poly.getFeatures():
    #    pGeom = p.geometry()
    #    for q in poi.getFeatures():
    #        qGeom = q.geometry()
    #        if qGeom.intersects(pGeom):
    #            result.append(q)

    #-------------------- shortest distance method
    #for p in ppPoints:
    #    dA = distanceFromPoints(pA,p)
    #    for j in jPoint:
    #        if distanceFromPoints(j,p)<dA and j.geometry().asPoint()!= pA.geometry().asPoint():
    #            return j
    #            break
    #    else:
    #        continue
    #    break


    #for p in ppPoints:

#for a in aaa:
#    print "OUTER LOOP"
#    print a
#    for b in bbb:
#        print "--inner loop"
#        print b
#        if b<a:
#            print "!!break here"
#            break
#    else:
#        continue
#    break