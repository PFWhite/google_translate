import numpy as np

# test data
X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
y = np.array([[0,1,1,0]]).T

# alpha = learning rate
# hidden_dim = dimension of hidden output
alpha,hidden_dim = (0.5,4)

# generates initial weights as random numbers between [-1, 1)
# weights for first layer
w_0 = 2*np.random.random((3,hidden_dim)) - 1
# weights for second layer
w_1 = 2*np.random.random((hidden_dim,1)) - 1

print(w_0)
print(w_1)

for j in range(10000):
    # pass the "net" (ie the dot product of the X values and the weights) through the sigmoid function
    output_1 = 1/(1+np.exp(-(np.dot(X,w_0))))

    # input of layer 2 is output of layer 1
    output_2 = 1/(1+np.exp(-(np.dot(output_1,w_1))))

    # change in weights
    w_1_delta = (output_2 - y)*(output_2*(1-output_2))
    w_0_delta = w_1_delta.dot(w_1.T) * (output_1 * (1-output_1))

    # update weights
    w_1 = w_1 - (alpha * output_1.T.dot(w_1_delta))
    w_0 = w_0 - (alpha * X.T.dot(w_0_delta))


print(w_0)
print(w_1)
