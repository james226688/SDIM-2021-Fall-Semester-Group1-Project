import RobotArmMotion0
import time

while(True):
    RobotArmMotion0.Reset0()
    time.sleep(3)
    RobotArmMotion0.Test2()
    time.sleep(3)
    RobotArmMotion0.CatchAndRelease(1)
    time.sleep(3)
    RobotArmMotion0.Release()
    time.sleep(3)
    RobotArmMotion0.CatchAndRelease(0)
    time.sleep(3)
    RobotArmMotion0.Reset1()
    time.sleep(3)


# RobotArmMotion0.Reset0()
# time.sleep(3)
#RobotArmMotion0.Random(15,15)
#time.sleep(3)
# time.sleep(3)
# RobotArmMotion0.Test2()
# RobotArmMotion0.Random(18,20)
# time.sleep(3)
# RobotArmMotion0.CatchAndRelease(1)
# time.sleep(3)
# RobotArmMotion0.Release()
# time.sleep(3)
# RobotArmMotion0.CatchAndRelease(0)
# time.sleep(3)
# RobotArmMotion0.Reset1()
# time.sleep(2)
# RobotArmMotion0.CatchAndRelease(1)
# time.sleep(2)
#RobotArmMotion0.AngleMotion(1,105,270)

# RobotArmMotion0.Reset0()
# time.sleep(3)
# RobotArmMotion0.Test1()
# time.sleep(3)
# RobotArmMotion0.AngleMotion(6,140,270)
# time.sleep(3)
# RobotArmMotion0.AngleMotion(5,120,180)
# time.sleep(3)
# RobotArmMotion0.CatchAndRelease(1)
# time.sleep(1)
# RobotArmMotion0.CatchAndRelease(0)
# time.sleep(1)
# RobotArmMotion0.CatchAndRelease(1)
# time.sleep(1)
# RobotArmMotion0.CatchAndRelease(0)
# time.sleep(1)
# RobotArmMotion0.CatchAndRelease(1)
# time.sleep(1)
# RobotArmMotion0.CatchAndRelease(0)
# time.sleep(3)
# RobotArmMotion0.Reset1()