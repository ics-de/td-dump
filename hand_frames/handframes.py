null_handvalues = op('null_handvalues')
opCache = op('cache_photo')

indexA = null_handvalues['h1:index_finger_tip:x']
indexB = null_handvalues['h2:index_finger_tip:x']

bottom = (null_handvalues['h1:index_finger_tip:y'] - 0.5) * 0.55
top = (null_handvalues['h2:index_finger_tip:y'] - 0.5) * 0.55
left = null_handvalues['h1:thumb_ip:x'] - 0.5
right = null_handvalues['h2:thumb_ip:x'] - 0.5

thumbX = null_handvalues['h1:thumb_tip:x']
thumbY = null_handvalues['h1:thumb_tip:y']

def onCook(scriptOp):
    scriptOp.clear()

    if indexA != 0 and indexB != 0:
        #print('test')
        drawFrame(scriptOp)

    return

def drawFrame(scriptOp):
    inputGeo = scriptOp.inputs[0]

    
    p0 = scriptOp.appendPoint()
    p0.P = tdu.Position(left, bottom, 0)

    p1 = scriptOp.appendPoint()
    p1.P = tdu.Position(right, bottom, 0)

    p2 = scriptOp.appendPoint()
    p2.P = tdu.Position(right, top, 0)

    p3 = scriptOp.appendPoint()
    p3.P = tdu.Position(left, top, 0)

    poly = scriptOp.appendPoly(4, closed=True, addPoints=True)
    poly[0].point = p0
    poly[1].point = p1
    poly[2].point = p2
    poly[3].point = p3

    #print(indexA - thumbX)
    if abs(indexA - thumbX) < 0.02:
        opCache.par.active = False

    return