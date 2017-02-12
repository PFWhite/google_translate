class Perceptron(object):

    def __init__(self, weights, inputs, threshold, learning_rate=0.1):
        self.weights = weights
        self.inputs = inputs
        self.threshold = threshold

    def test(self, input_vector):
        sum = 0
        for index, item in enumerate(input_vector):
            sum += (self.weights[index] * input_vector[index])
        self.last_result = 1 if sum > self.threshold else return -1
        return self.last_result

    def update_weights(self, difference_vec):
        for index, difference in enumerate(difference_vec):
            self.weights[index] += difference * self.learning_rate

    

