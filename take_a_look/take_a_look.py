import math

null_handvalues = op('null_handvalues')
null_facevalues = op('null_facevalues')
cache = op('cache1')

indexA = null_handvalues['h1:index_finger_tip:x']
indexB = null_handvalues['h2:index_finger_tip:x']


def average(a,b):
    return abs(a + b) / 2


handLPointsA = []

handLPointsA.append([null_handvalues['h1:index_finger_tip:x'], null_handvalues['h1:index_finger_tip:y'], 0.0])
handLPointsA.append([null_handvalues['h1:index_finger_dip:x'], null_handvalues['h1:index_finger_dip:y'], 0.0])
handLPointsA.append([null_handvalues['h1:index_finger_pip:x'], null_handvalues['h1:index_finger_pip:y'], 0.0])

handLPointsA.append([average(null_handvalues['h1:index_finger_mcp:x'],null_handvalues['h1:middle_finger_mcp:x']), average(null_handvalues['h1:index_finger_mcp:y'],null_handvalues['h1:middle_finger_mcp:y']), 0.0])

handLPointsA.append([average(null_handvalues['h1:index_finger_mcp:x'],null_handvalues['h1:middle_finger_mcp:x']), average(null_handvalues['h1:index_finger_mcp:y'],null_handvalues['h1:middle_finger_mcp:y']), 0.0])

handLPointsA.append([average(null_handvalues['h1:index_finger_mcp:x'],null_handvalues['h1:thumb_cmc:x']), average(null_handvalues['h1:index_finger_mcp:y'],null_handvalues['h1:thumb_cmc:y']), 0.0])
handLPointsA.append([null_handvalues['h1:thumb_mcp:x'], null_handvalues['h1:thumb_mcp:y'], 0.0])
handLPointsA.append([null_handvalues['h1:thumb_ip:x'], null_handvalues['h1:thumb_ip:y'], 0.0])
handLPointsA.append([null_handvalues['h1:thumb_tip:x'], null_handvalues['h1:thumb_tip:y'], 0.0])


handLPointsB = []

handLPointsB.append([average(null_handvalues['h1:index_finger_mcp:x'],null_handvalues['h1:middle_finger_mcp:x']), average(null_handvalues['h1:index_finger_mcp:y'],null_handvalues['h1:middle_finger_mcp:y']), 0.0])

handLPointsB.append([null_handvalues['h1:middle_finger_pip:x'], null_handvalues['h1:middle_finger_pip:y'], 0.0])
handLPointsB.append([null_handvalues['h1:middle_finger_dip:x'], null_handvalues['h1:middle_finger_dip:y'], 0.0])
handLPointsB.append([null_handvalues['h1:middle_finger_tip:x'], null_handvalues['h1:middle_finger_tip:y'], 0.0])


handLPointsC = []

handLPointsC.append([average(null_handvalues['h1:index_finger_mcp:x'],null_handvalues['h1:thumb_cmc:x']), average(null_handvalues['h1:index_finger_mcp:y'],null_handvalues['h1:thumb_cmc:y']), 0.0])
handLPointsC.append([null_handvalues['h1:ring_finger_mcp:x'], null_handvalues['h1:ring_finger_mcp:y'], 0.0])
handLPointsC.append([null_handvalues['h1:ring_finger_pip:x'], null_handvalues['h1:ring_finger_pip:y'], 0.0])
handLPointsC.append([null_handvalues['h1:ring_finger_tip:x'], null_handvalues['h1:ring_finger_tip:y'], 0.0])

handLPointsD = []

handLPointsD.append([average(null_handvalues['h1:index_finger_mcp:x'],null_handvalues['h1:thumb_cmc:x']), average(null_handvalues['h1:index_finger_mcp:y'],null_handvalues['h1:thumb_cmc:y']), 0.0])
handLPointsD.append([null_handvalues['h1:pinky_mcp:x'], null_handvalues['h1:pinky_mcp:y'], 0.0])
handLPointsD.append([null_handvalues['h1:pinky_pip:x'], null_handvalues['h1:pinky_pip:y'], 0.0])
handLPointsD.append([null_handvalues['h1:pinky_tip:x'], null_handvalues['h1:pinky_tip:y'], 0.0])


handRPointsA = []

handRPointsA.append([null_handvalues['h2:index_finger_tip:x'], null_handvalues['h2:index_finger_tip:y'], 0.0])
handRPointsA.append([null_handvalues['h2:index_finger_dip:x'], null_handvalues['h2:index_finger_dip:y'], 0.0])
handRPointsA.append([null_handvalues['h2:index_finger_pip:x'], null_handvalues['h2:index_finger_pip:y'], 0.0])

handRPointsA.append([average(null_handvalues['h2:index_finger_mcp:x'],null_handvalues['h2:middle_finger_mcp:x']), average(null_handvalues['h2:index_finger_mcp:y'],null_handvalues['h2:middle_finger_mcp:y']), 0.0])

handRPointsA.append([average(null_handvalues['h2:index_finger_mcp:x'],null_handvalues['h2:middle_finger_mcp:x']), average(null_handvalues['h2:index_finger_mcp:y'],null_handvalues['h2:middle_finger_mcp:y']), 0.0])

handRPointsA.append([average(null_handvalues['h2:index_finger_mcp:x'],null_handvalues['h2:thumb_cmc:x']), average(null_handvalues['h2:index_finger_mcp:y'],null_handvalues['h2:thumb_cmc:y']), 0.0])
handRPointsA.append([null_handvalues['h2:thumb_mcp:x'], null_handvalues['h2:thumb_mcp:y'], 0.0])
handRPointsA.append([null_handvalues['h2:thumb_ip:x'], null_handvalues['h2:thumb_ip:y'], 0.0])
handRPointsA.append([null_handvalues['h2:thumb_tip:x'], null_handvalues['h2:thumb_tip:y'], 0.0])

handRPointsB = []

handRPointsB.append([average(null_handvalues['h2:index_finger_mcp:x'],null_handvalues['h2:middle_finger_mcp:x']), average(null_handvalues['h2:index_finger_mcp:y'],null_handvalues['h2:middle_finger_mcp:y']), 0.0])

handRPointsB.append([null_handvalues['h2:middle_finger_pip:x'], null_handvalues['h2:middle_finger_pip:y'], 0.0])
handRPointsB.append([null_handvalues['h2:middle_finger_dip:x'], null_handvalues['h2:middle_finger_dip:y'], 0.0])
handRPointsB.append([null_handvalues['h2:middle_finger_tip:x'], null_handvalues['h2:middle_finger_tip:y'], 0.0])

handRPointsC = []

handRPointsC.append([average(null_handvalues['h2:index_finger_mcp:x'],null_handvalues['h2:thumb_cmc:x']), average(null_handvalues['h2:index_finger_mcp:y'],null_handvalues['h2:thumb_cmc:y']), 0.0])
handRPointsC.append([null_handvalues['h2:ring_finger_mcp:x'], null_handvalues['h2:ring_finger_mcp:y'], 0.0])
handRPointsC.append([null_handvalues['h2:ring_finger_pip:x'], null_handvalues['h2:ring_finger_pip:y'], 0.0])
handRPointsC.append([null_handvalues['h2:ring_finger_tip:x'], null_handvalues['h2:ring_finger_tip:y'], 0.0])

handRPointsD = []

handRPointsD.append([average(null_handvalues['h2:index_finger_mcp:x'],null_handvalues['h2:thumb_cmc:x']), average(null_handvalues['h2:index_finger_mcp:y'],null_handvalues['h2:thumb_cmc:y']), 0.0])
handRPointsD.append([null_handvalues['h2:pinky_mcp:x'], null_handvalues['h2:pinky_mcp:y'], 0.0])
handRPointsD.append([null_handvalues['h2:pinky_pip:x'], null_handvalues['h2:pinky_pip:y'], 0.0])
handRPointsD.append([null_handvalues['h2:pinky_tip:x'], null_handvalues['h2:pinky_tip:y'], 0.0])


faceRotation = 0

eyeL = tdu.Vector([null_facevalues['p1:left_eye:x'],null_facevalues['p1:left_eye:y'], 0.0])
eyeR = tdu.Vector([null_facevalues['p1:right_eye:x'],null_facevalues['p1:right_eye:y'], 0.0])


def cook(scriptOp):

    scriptOp.clear()

    getFaceRotation(eyeL,eyeR)

    if indexA != 0:
        drawGlasses(scriptOp)
        
    return


def drawGlasses(scriptOp):

    if indexA != 0:
        closedL = abs(handLPointsA[0][0] - handLPointsA[8][0]) + abs(handLPointsA[0][1] - handLPointsA[8][1])
        closedR = abs(handRPointsA[0][0] - handRPointsA[8][0]) + abs(handRPointsA[0][1] - handRPointsA[8][1])
        if closedL < 0.08:
            drawPolyClosed(scriptOp,handLPointsA)
        else:
            drawPolyOpen(scriptOp,handLPointsA)
        drawPolyOpen(scriptOp,handLPointsB)
        drawPolyOpen(scriptOp,handLPointsC)
        drawPolyOpen(scriptOp,handLPointsD)

        if closedR < 0.08:
            drawPolyClosed(scriptOp,handRPointsA)
        else:
            drawPolyOpen(scriptOp,handRPointsA)

        drawPolyOpen(scriptOp,handRPointsB)
        drawPolyOpen(scriptOp,handRPointsC)
        drawPolyOpen(scriptOp,handRPointsD)

    return

def drawPolyOpen(scriptOp,handPoints):

    myPolyA = scriptOp.appendPoly(len(handPoints), closed=False, addPoints=True)

    for i, eachPoint in enumerate(myPolyA):
        hPoint = handPoints[i]
        #eachPoint.point.P = ((hPoint[0]-0.5), (hPoint[1]-0.5)*0.55, hPoint[2])
        eachPoint.point.P = ((hPoint[0]*1280), hPoint[1]*720, hPoint[2])

    return

def drawPolyClosed(scriptOp,handPoints):

    myPolyA = scriptOp.appendPoly(len(handPoints), closed=True, addPoints=True)

    for i, eachPoint in enumerate(myPolyA):
        hPoint = handPoints[i]
        eachPoint.point.P = ((hPoint[0]*1280), hPoint[1]*720, hPoint[2])

    return

def getFaceRotation(eyeL,eyeR):
    global faceRotation

    faceDir = tdu.Vector(eyeR) - tdu.Vector(eyeL)
    faceDir.normalize()

    '''
    # Reference vector pointing to the right (along X axis)
    from_vec = tdu.Vector([1, 0, 0])

    angle_rad = faceDir.angle(from_vec)

    faceRotation = math.floor(angle_rad)
    '''

    # Calculate signed angle using atan2
    angle = math.atan2(faceDir.y, faceDir.x)  # Returns signed angle in radians
    angle_deg = math.degrees(angle)

    faceRotation = angle_deg

    op('const_faceRotation').par.value0 = faceRotation

    return

