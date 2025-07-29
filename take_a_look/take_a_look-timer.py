# me - this DAT
# timerOp - the connected Timer CHOP
# cycle - the cycle index
# interrupt - True if the user initiated a premature
#                     False if a result of a normal timeout
# fraction - the time in 0-1 fractional form
#
# segment - an object describing the segment:
#
#    can be automatically cast to its index: e.g.:  segment+3, segment==2, etc      
#    
#  members of segment object:
#      index     numeric order of the segment, from 0
#      owner    Timer CHOP it belongs to
#
#      lengthSeconds, lengthSamples, lengthFrames
#      delaySeconds, delaySamples, delayFrames
#      beginSeconds, beginSamples, beginFrames
#      speed
#      cycle, cycleLimit, maxCycles
#      cycleEndAlertSeconds, cycleEndAlertSamples, cycleEndAlertFrames
#
#      row - one validly named member per column:
#            column headings used to override parameters:
#                          length, delay, speed, cyclelimit, maxcycles, cycleendalert
#            special column headings:
#                          begin (time at which to start, independent of delays/lengths, overrides delay)
#
#    custom - dictionary of all columns that don't map to a built-in feature
#

# onInitialize(): if return value > 0, it will be
# called again after the returned number of frames.
# callCount increments with each attempt, starting at 1

def onInitialize(timerOp, callCount):
	if(op('const_counter')['count'] == 0):
		op('cache_mesh1').par.active = 1
		op('cache_mesh2').par.active = 1
		op('switch_visuals').par.index = 0
		op('delete_mesh2').bypass = 0
	return 0

def onReady(timerOp):
	return
	
def onStart(timerOp):
	return
	
def onTimerPulse(timerOp, segment):
	return

def whileTimerActive(timerOp, segment, cycle, fraction):
	return

def onSegmentEnter(timerOp, segment, interrupt):
	return
	
def onSegmentExit(timerOp, segment, interrupt):
	return

def onCycleStart(timerOp, segment, cycle):
	return

def onCycleEndAlert(timerOp, segment, cycle, alertSegment, alertDone, interrupt):
	return
	
def onCycle(timerOp, segment, cycle):
	return

def onDone(timerOp, segment, interrupt):
	count = op('const_counter')['count']
	match(count):
		case 0:
			op('cache_mesh1').par.active = 0
			op('const_counter').par.value0 = 1
			op('delete_mesh2').bypass = 0

		case 1:
			op('delete_mesh2').bypass = 1
			op('cache_mesh2').par.active = 0
			op('const_counter').par.value0 = 2

	
	op('switch_visuals').par.index = 1

	return

def onSubrangeStart(timerOp):
	return

	