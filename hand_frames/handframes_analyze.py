null_handvalues = op('null_handvalues')
opCache1 = op('cache_photo1')
#opCache2 = op('cache_photo2')
#filledCache = 0

indexAx = null_handvalues['h1:index_finger_tip:x']
indexAy = null_handvalues['h1:index_finger_tip:y']
indexBx = null_handvalues['h2:index_finger_tip:x']

bottom = (null_handvalues['h1:index_finger_tip:y'] - 0.5) * 0.55
top = (null_handvalues['h2:index_finger_tip:y'] - 0.5) * 0.55
left = null_handvalues['h1:thumb_ip:x'] - 0.5
right = null_handvalues['h2:thumb_ip:x'] - 0.5

thumbX = null_handvalues['h1:thumb_tip:x']
thumbY = null_handvalues['h1:thumb_tip:y']

def onCook(scriptOp):
    scriptOp.clear()

    if indexAx != 0 and indexBx != 0:
        #print('test')
        drawFrame(scriptOp)
        op('const_disp').par.value0 = 0.001

    else:
        filledCache = 0
        op('const_disp').par.value0 = 0


    return

def drawFrame(scriptOp):
    filledCache = False

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

    print(abs(indexAx - thumbX))
    if abs(indexAx - thumbX) < 0.025 and abs(indexAy - thumbY) < 0.025:
        #opCache1.par.active = False

        if(op('const_block').par.value0 == 0):
            opCache1.par.prefillpulse.pulse()
            opCache1.par.prefill = 0
            op('const_block').par.value0 = 1
            print('open')
            return
    else:
        #opCache1.par.active = True
        
        opCache1.par.prefill = 1
        op('const_block').par.value0 = 0
        print('closed')
    return