from controller import Supervisor
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
import numpy as np
from keras import backend as K
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
supervisor = Supervisor()
timestep = 64
arms = []
pos = []
target = supervisor.getFromDef('TARGET')
print(target.getId())
armsNames = ['1','2','3','4','5','6']
posnames = ['1 sensor', '2 sensor' , '3 sensor', '4 sensor', '5 sensor', '6 sensor']
for i in range(6) :
    arms.append(supervisor.getDevice(armsNames[i]))
    arms[i].setPosition(float('inf'))
for i in range(6) :
    pos.append(supervisor.getDevice(posnames[i]))
    pos[i].enable(timestep)
end_effector = supervisor.getFromDef('GRIPPER')
j = 0
def base_model():
     model = Sequential()
     model.add(Dense(32, input_dim=3, activation='relu'))
     model.add(Dense(64, activation='relu'))
     model.add(Dense(128, activation='relu'))
     model.add(Dense(32, activation='relu'))
     model.add(Dense(6, activation='linear'))
     model.compile(loss='mean_absolute_error', optimizer = 'adam')
     return model
while supervisor.step(timestep) != -1:
    if j == 0 :
        X_train = np.genfromtxt('X_train.csv',delimiter=',')
        Y_train = np.genfromtxt('Y_train.csv',delimiter=',')
        X_train = X_train.T
        Y_train = Y_train.T
        print("Training")
        clf = KerasRegressor(build_fn=base_model, epochs=10000, batch_size=200,verbose=2)
        clf.fit(X_train,Y_train)
        res = clf.predict(X_train)
        score = mean_absolute_error(Y_train, res)
        print(score) 
        j = j + 1
    else :
        result = clf.predict(np.array([[target.getPosition()[0]],[target.getPosition()[1]],[target.getPosition()[2]]]).T)
        print(float(result[0]))
        print(float(result[1]))
        print(float(result[2]))
        print(float(result[3]))
        print(float(result[4]))
        print(float(result[5]))
        arms[0].setPosition(float(result[0]))
        arms[1].setPosition(float(result[1]))
        arms[2].setPosition(float(result[2]))
        arms[3].setPosition(float(result[3]))
        arms[4].setPosition(float(result[4]))
        arms[5].setPosition(float(result[5]))
        print(end_effector.getPosition(),'supervisor')
    pass
