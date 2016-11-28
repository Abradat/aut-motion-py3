from API import herkulex
from API.herkulex import servo

#herkulex.connect("")
motors = []
for mCnt in range(1, 19):
    motors.append(servo(mCnt))


