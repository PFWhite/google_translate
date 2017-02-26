import numpy as np


# sigmoid function
def sigmoid(x):
    output = 1 / (1 + np.exp(-x))
    return output

# derivative of sigmoid function
def sigmoid_output_derivative(output):
    return output * (1 - output)

# sample dataset
# input
X = np.array([[0, 1],
              [0, 1],
              [1, 0],
              [1, 0]])
# output
y = np.array([[0, 0, 1, 1]]).T

# learning rates
alphas = [0.001,0.01,0.1,1,10,100,1000]

# set seed
np.random.seed(1)

# generates initial weights as random numbers between [-1, 1)
w_0 = 2 * np.random.random((2, 1)) - 1

# run loop with various values of alpha to find which learning rate converges the most quickly
for alpha in alphas:
    print("\nTraining With Alpha = " + str(alpha))

    # perform gradient descent
    for iter in range(10000):

        # output_0 is really our initial starting input
        output_0 = X
        output_1 = sigmoid(np.dot(output_0, w_0))

        # (-1) * (target - output)
        output_1_error = output_1 - y

        # check to see if error is getting better
        if (iter % 1000) == 0:
            print("Error after " + str(iter) + " iterations:" + str(np.mean(np.abs(output_1_error))))

        # multiply error by slope of sigmoid function (ie its derivative) at the values in layer 1
        output_1_delta = output_1_error * sigmoid_output_derivative(output_1)

        # dot product of initial starting input and result of previous line
        w_0_delta = alpha * np.dot(output_0.T, output_1_delta)

        # update weights (ie change weight by the negative of the slope)
        w_0 = w_0 - w_0_delta

    print("Output After Training is Complete:")
    print(output_1)

# note: it looks like larger values of alpha actually converge faster here, but very large values (ie alpha>10) seem to produce output of all zeros

