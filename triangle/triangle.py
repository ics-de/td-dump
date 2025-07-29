null_handvalues = op('null_handvalues')
transform_face = op('transform_face')

index1x = null_handvalues['h1:index_finger_tip:x']
index1y = null_handvalues['h1:index_finger_tip:y']
index2x = null_handvalues['h2:index_finger_tip:x']
index2y = null_handvalues['h2:index_finger_tip:y']

thumb1x = (null_handvalues['h1:thumb_mcp:x'] - 0.5) * 1
thumb1y = (null_handvalues['h1:thumb_mcp:y'] - 0.48) * 0.5
thumb2x = (null_handvalues['h2:thumb_mcp:x'] - 0.5) * 1
thumb2y = (null_handvalues['h2:thumb_mcp:y'] - 0.48) * 0.5

distThumb = abs(thumb1x - thumb2x)
distIndex = abs(index1x - index2x)

#zoom['zoom'] = distIndex

def onCook(scriptOp):
    scriptOp.clear()

    if index1x != 0 and index2x != 0:
        #print('test')
        drawTriangle(scriptOp)
    else:
        zoom(1)
        transform_face.par.tx = 0
        transform_face.par.ty = 0
    return

def drawTriangle(scriptOp):
    inputGeo = scriptOp.inputs[0]

    
    p0 = scriptOp.appendPoint()
    p0.P = tdu.Position(thumb1x, thumb1y, 0)

    p1 = scriptOp.appendPoint()
    p1.P = tdu.Position(thumb2x, thumb2y, 0)

    p2 = scriptOp.appendPoint()
    #p2.P = tdu.Position(thumb1x+distThumb/2, distThumb/2, 0)
    #tHeight = lerp(abs((index1y-index2y)/2),thumb2y+distThumb*0.5, distIndex*2)
    triangleMid = thumb1x+distThumb*0.5
    triangleHeight = thumb2y+distThumb*0.666
    p2.P = tdu.Position(triangleMid, triangleHeight, 0)

    poly = scriptOp.appendPoly(3, closed=True, addPoints=True)
    poly[0].point = p0
    poly[1].point = p1
    poly[2].point = p2
    print(distIndex)

    transform_face.par.tx = triangleMid
    transform_face.par.ty = thumb2y+distThumb*0.333
    zoom(lerp(0.95,2.5,distIndex))
    return


def zoom(factor: float):
    op('const_zoom').par.value0 = round(factor,2)
    return

def lerp(a: float, b: float, t: float) -> float:
    return (1 - t) * a + t * b