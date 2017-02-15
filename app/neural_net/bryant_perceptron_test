import csv

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
        if sum > 0:
            self.last_classification = 1
        else:
            if sum < 0:
                self.last_classification = -1
            else:
                self.last_classification = 0
#        return self.last_classification

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


#Sorry for how painful loading the data in is; I generated everything in R, and R likes to work with csv files

#data upload
testdata = open('testdata.csv')
csv_test = csv.reader(testdata)
i = []
x = []
y = []
z = []
t = []
for row in csv_test :
    i.append(row[1])
    x.append(row[2])
    y.append(row[3])
    z.append(row[4])
    t.append(row[5])

i.remove('K0')
x.remove('K1')
y.remove('K2')
z.remove('K3')
t.remove('Y')

#had to turn things into floats because it yelled at me about syntax issues
for k in range(len(i)) :
    i[k] = float(i[k])
for k in range(len(x)) :
    x[k] = float(x[k])
for k in range(len(y)) :
    y[k] = float(y[k])
for k in range(len(z)) :
    z[k] = float(z[k])
for k in range(len(t)) :
    t[k] = float(t[k])

#setting initial values for perceptron
w = [0,0,0,0]
a = 1
e = .0001

p1 = Perceptron(w, a, e)
X = [i,x,y,z,t]

#running Perceptron update 20 times, saving the outputs of the last time
for j in range(19) :
    for k in range(len(i)) :
        up = [X[0][k], X[1][k], X[2][k], X[3][k]]
        p1.classify(up)
        p1.update_weights(X[4][k])

O = []
for k in range(len(i)) :
    up = [X[0][k], X[1][k], X[2][k], X[3][k]]
    p1.classify(up)
    p1.update_weights(X[4][k])
    O.append(p1.last_classification)

#figuring out where it went wrong
D = []
for k in range(len(O)) :
    D.append(t[k] - float(O[k]))
