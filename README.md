# Inverse Kinematics using Neural Networks

This project is aimed to calculate the inverse kinematics of a 3-DoF robotic manipulator using neural networks

## Dependencies

- Cyberobotics, Webots
- Python==3.7
- Numpy
- Tensorflow

## Approach

We have designed a deep neural network for prediciting the joint rotations of the manipulator given the position of the end effector. For training the neural networks the data was generated with the help of WeBots simulator, position of the end effector was recorded and was saved in X_train.csv file, while the joint rotations were recorded in Y_train.csv. Then the data is passed through a deep linear regressor model to train it. 

### Dataset generation

In this postion of end effector is recorded(using supervisor node in WeBots) for every randomly selected theta1, theta2, theta3 in range -3.14 to +3.14 radians, theta1, theta2, theta3 were recorded in Y_train.csv and position of end effector was recorded in X_train.csv. In this collision is set off, to avoid errors as data points are taken randomly.

![Hnet com-image](https://user-images.githubusercontent.com/64823050/130271518-dd71215f-9cd3-417b-af3c-406509dc62dd.gif)


### Neural Network Architecture



## Results




## References
