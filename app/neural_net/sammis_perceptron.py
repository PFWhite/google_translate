class Perceptron(object):

    def __init__(self, weights, learning_rate, epsilon):
        self.weights = weights
        self.learning_rate = learning_rate
        self.epsilon = epsilon

    def classify(self, inputs):
        #this will do our weights times our input vector
        self.last_input = inputs
        sum = 0
        for index, input in enumerate(inputs):
            sum += self.weights[index] * inputs[index]
        if sum >= 0:
            self.last_classification = 1
        else:
            self.last_classification = -1

        return self.last_classification

    def update_weights(self, correct_classification):
        delta_weight = []
        for index, input in enumerate(self.last_input):
            delta_weight.append(self.learning_rate * (correct_classification - self.last_classification) * input)

        # check if within our tolerance for updating weights
        total_delta = 0
        for index, delta in enumerate(delta_weight):
            total_delta += delta
        if total_delta >= self.epsilon:
            for index, delta in enumerate(delta_weight):
                self.weights[index] += delta



