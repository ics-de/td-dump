null_handvalues = op('null_handvalues')

# handPointsA = op('null_handvalues')[2,3,4]
indexA = null_handvalues['h1:index_finger_tip:x']
indexB = null_handvalues['h2:index_finger_tip:x']

'''
handPointsA = []
handPointsA.append([null_handvalues['h1:index_finger_tip:x'], null_handvalues['h1:index_finger_tip:y'], 0.0])
handPointsA.append([null_handvalues['h1:index_finger_dip:x'], null_handvalues['h1:index_finger_dip:y'], 0.0])
handPointsA.append([null_handvalues['h1:index_finger_pip:x'], null_handvalues['h1:index_finger_pip:y'], 0.0])
handPointsA.append([null_handvalues['h1:index_finger_mcp:x'], null_handvalues['h1:index_finger_mcp:y'], 0.0])
handPointsA.append([null_handvalues['h1:middle_finger_pip:x'], null_handvalues['h1:middle_finger_pip:y'], 0.0])
handPointsA.append([null_handvalues['h1:middle_finger_dip:x'], null_handvalues['h1:middle_finger_dip:y'], 0.0])
handPointsA.append([null_handvalues['h1:middle_finger_tip:x'], null_handvalues['h1:middle_finger_tip:y'], 0.0])

handPointsA.append([null_handvalues['h2:middle_finger_tip:x'], null_handvalues['h2:middle_finger_tip:y'], 0.0])
handPointsA.append([null_handvalues['h2:middle_finger_dip:x'], null_handvalues['h2:middle_finger_dip:y'], 0.0])
handPointsA.append([null_handvalues['h2:middle_finger_pip:x'], null_handvalues['h2:middle_finger_pip:y'], 0.0])
handPointsA.append([null_handvalues['h2:index_finger_mcp:x'], null_handvalues['h2:index_finger_mcp:y'], 0.0])
handPointsA.append([null_handvalues['h2:index_finger_pip:x'], null_handvalues['h2:index_finger_pip:y'], 0.0])
handPointsA.append([null_handvalues['h2:index_finger_dip:x'], null_handvalues['h2:index_finger_dip:y'], 0.0])
handPointsA.append([null_handvalues['h2:index_finger_tip:x'], null_handvalues['h2:index_finger_tip:y'], 0.0])
'''

def average(a,b):
    return (a + b) / 2

heartEndsY = -0.05
heartSidesX = 0.025


handPointsB = []
handPointsB.append([null_handvalues['h1:index_finger_tip:x'], null_handvalues['h1:index_finger_tip:y'], 0.0])
handPointsB.append([null_handvalues['h1:index_finger_dip:x'], null_handvalues['h1:index_finger_dip:y'], 0.0])
handPointsB.append([null_handvalues['h1:index_finger_pip:x'], null_handvalues['h1:index_finger_pip:y'], 0.0])
handPointsB.append([null_handvalues['h1:index_finger_mcp:x'], null_handvalues['h1:index_finger_mcp:y'], 0.0])

handPointsB.append([average(null_handvalues['h1:index_finger_mcp:x'],null_handvalues['h1:thumb_mcp:x'])-heartSidesX, average(null_handvalues['h1:index_finger_mcp:y'],null_handvalues['h1:thumb_mcp:y']), 0.0])

handPointsB.append([null_handvalues['h1:thumb_mcp:x'], null_handvalues['h1:thumb_mcp:y'], 0.0])
handPointsB.append([null_handvalues['h1:thumb_ip:x'], null_handvalues['h1:thumb_ip:y'], 0.0])
handPointsB.append([null_handvalues['h1:thumb_tip:x'], null_handvalues['h1:thumb_tip:y'], 0.0])

handPointsB.append([average(null_handvalues['h1:thumb_tip:x'],null_handvalues['h2:thumb_tip:x']), average(null_handvalues['h1:thumb_tip:y'],null_handvalues['h2:thumb_tip:y'])+heartEndsY, 0.0])

handPointsB.append([null_handvalues['h2:thumb_tip:x'], null_handvalues['h2:thumb_tip:y'], 0.0])
handPointsB.append([null_handvalues['h2:thumb_ip:x'], null_handvalues['h2:thumb_ip:y'], 0.0])
handPointsB.append([null_handvalues['h2:thumb_mcp:x'], null_handvalues['h2:thumb_mcp:y'], 0.0])

handPointsB.append([average(null_handvalues['h2:index_finger_mcp:x'],null_handvalues['h2:thumb_mcp:x'])+heartSidesX, average(null_handvalues['h2:index_finger_mcp:y'],null_handvalues['h2:thumb_mcp:y']), 0.0])

handPointsB.append([null_handvalues['h2:index_finger_mcp:x'], null_handvalues['h2:index_finger_mcp:y'], 0.0])
handPointsB.append([null_handvalues['h2:index_finger_pip:x'], null_handvalues['h2:index_finger_pip:y'], 0.0])
handPointsB.append([null_handvalues['h2:index_finger_dip:x'], null_handvalues['h2:index_finger_dip:y'], 0.0])
handPointsB.append([null_handvalues['h2:index_finger_tip:x'], null_handvalues['h2:index_finger_tip:y'], 0.0])

handPointsB.append([average(null_handvalues['h1:index_finger_tip:x'],null_handvalues['h2:index_finger_tip:x']), average(null_handvalues['h1:index_finger_tip:y'],null_handvalues['h2:index_finger_tip:y'])+heartEndsY, 0.0])

shapePoints = len(handPointsB)

def cook(scriptOp):

    scriptOp.clear()

    proximity = abs(indexA - indexB)

    if proximity > 0 and proximity < 0.05:
        # print(proximity)
        drawHeart(scriptOp)
        # drawCircle(scriptOp)

    return


def drawHeart(scriptOp):

    myPoly = scriptOp.appendPoly(shapePoints, closed=True, addPoints=True)
    
    for i, eachPoint in enumerate(myPoly):
        hPoint = handPointsB[i]
        eachPoint.point.P = ((hPoint[0]-0.5), (hPoint[1]-0.5)*0.55, hPoint[2])
        # print(eachPoint.point.P)

    return








'''
def drawCircle(scriptOp):
    
    inputGeo = scriptOp.inputs[0]
    
    for i, pt in range(inputGeo.points):
        if i < len(handPointsA):
            pt.P = handPointsA[i]
    return


    #values = op('null1')[0].vals  # Use the first channel from CHOP
    values = handPointsA
    # numPoints = len(inputGeo.points)

    # Store new points
    newPoints = []

    for i, pt in enumerate(inputGeo.points):
        # pos = pt.P
        newPos = handPointsA[i]

        newPt = scriptOp.appendPoint()
        newPt.P = newPos
        newPoints.append(newPt)

    # Rebuild the primitive (polygon)
    for prim in inputGeo.prims:
        verts = prim.vertices
        newPrim = scriptOp.appendPoly(len(verts), closed=prim.closed)
        for i, vert in enumerate(verts):
            newPrim[i].point = newPoints[vert.point.index]
'''
