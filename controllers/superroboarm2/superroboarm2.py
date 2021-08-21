from controller import Supervisor
import random
import numpy as np
supervisor = Supervisor()
timestep = 64
arms = []
pos = []
armsNames = ['Joint_1','Joint_2','Joint_3']
posnames = ['Joint_1_sensor','Joint_2_sensor','Joint_3_sensor']
for i in range(3) :
    arms.append(supervisor.getDevice(armsNames[i]))
    arms[i].setPosition(float('inf'))
    arms[i].setVelocity(5)
for i in range(3) :
    pos.append(supervisor.getDevice(posnames[i]))
    pos[i].enable(timestep)
#target = supervisor.getFromDef("TARGET")
end_effector = supervisor.getFromDef('GRIPPER')
while supervisor.step(timestep) != -1:
    arms[0].setPosition(-0.70)
    arms[1].setPosition(-1.4)
    arms[2].setPosition(1.79)
    print(end_effector.getPosition())
    #print(target.getPosition())
    #print(target.getId())