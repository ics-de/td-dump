null_handvalues = op('null_handvalues')

indexTip = null_handvalues['h1:index_finger_tip:y']
indexBase = null_handvalues['h1:index_finger_mcp:y']
middleTip = null_handvalues['h1:middle_finger_tip:y']
middleBase = null_handvalues['h1:middle_finger_mcp:y']

def onSetupParameters(scriptOp):
    scriptOp.appendChan('peace')
    return

def onCook(scriptOp):

    if indexTip != 0 and middleTip != 0:
        checkPeace(scriptOp)
    else:
        #op('level_cache').par.opacity = 0

        scriptOp.clear()
        scriptOp.appendChan('peace')
        scriptOp['peace'][0] = 0
    return

def checkPeace(scriptOp):
    scriptOp.clear()
    raw_diff = (indexTip+middleTip)-(indexBase+middleBase)
    diff = tdu.remap(raw_diff,0.1,0.4,-0.2,1)
    diff = max(0, min(diff, 1))
    print(raw_diff)

    scriptOp.clear()
    scriptOp.appendChan('peace')
    scriptOp['peace'][0] = diff
    #vanish(diff)

    return

def vanish(diff):
    op('level_cache').par.opacity = diff

    return