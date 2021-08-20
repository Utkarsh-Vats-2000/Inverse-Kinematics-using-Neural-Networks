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
j = 0
X_train = np.zeros((3,5000))
Y_train = np.zeros((3,5000))
i = 0
while supervisor.step(timestep) != -1:
    if j < 5000*20 :
        if j%20 == 0 :
            k = round(random.uniform(-3.139, 3.139), 4)
            l = round(random.uniform(-3.139, 3.139), 4)
            m = round(random.uniform(-3.139, 3.139), 4)
            arms[0].setPosition(k)
            arms[1].setPosition(l)
            arms[2].setPosition(m)
            X_train[:,i] = np.copy(np.array([end_effector.getPosition()[0],end_effector.getPosition()[1],end_effector.getPosition()[2]]))
            Y_train[:,i] = np.copy(np.array([pos[0].getValue(),pos[1].getValue(),pos[2].getValue()]))
            i = i + 1
        j = j + 1
        print(j)
    else :
        np.savetxt('X_train.csv', X_train, delimiter=',')
        np.savetxt('Y_train.csv', Y_train, delimiter=',')
        break
    #print(target.getPosition())
    #print(target.getId())