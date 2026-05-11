import math
import random
from Matrix import Matrix
def sigmoid(x):
    return 1/(1+math.exp(-x))
def der_sigmoid(y):
    return y*(1-y)
class NeuralNetwork:
    def __init__(self,input_nodes,hidden_nodes,output_nodes):
        self.input_nodes= input_nodes
        self.hidden_nodes= hidden_nodes
        self.output_nodes= output_nodes
        self.weights_input_hidden= Matrix(self.hidden_nodes,self.input_nodes)
        self.weights_hidden_output= Matrix(self.output_nodes,self.hidden_nodes)
        self.weights_input_hidden.random()
        self.weights_hidden_output.random()
        self.bias_hidden= Matrix(self.hidden_nodes,1)
        self.bias_output= Matrix(self.output_nodes,1)
        self.bias_hidden.random()
        self.bias_output.random()
        self.learning_rate=0.1
        
    #Generating the hidden outputs    
    def feedforward(self,input_array):
        inputs=Matrix.fromarray(input_array)
        hidden=Matrix.multiply_matrices(self.weights_input_hidden,inputs)
        hidden.add(self.bias_hidden)
        hidden.map(sigmoid)
        output=Matrix.multiply_matrices(self.weights_hidden_output,hidden)
        output.add(self.bias_output)
        output.map(sigmoid)
        return output.toArray()
    
    def train(self,input_array,target_array):
        inputs=Matrix.fromarray(input_array)
        hidden=Matrix.multiply_matrices(self.weights_input_hidden,inputs)
        hidden.add(self.bias_hidden)
        hidden.map(sigmoid)
        outputs=Matrix.multiply_matrices(self.weights_hidden_output,hidden)
        outputs.add(self.bias_output)
        outputs.map(sigmoid)
        #Convert array to matrix ibject
        targets=Matrix.fromarray(target_array)
        #calculate the error
        #Error= Targets - outputs
        output_error=Matrix.subtract(targets,outputs)
        #Calculate Gradient
        gradients=Matrix.map_static(outputs,der_sigmoid)
        gradients.multiply(output_error)
        gradients.multiply(self.learning_rate)
        #Claculate Deltas
        hidden_t=Matrix.transpose(hidden)
        self.weights_hidden_output_delta=Matrix.multiply_matrices(gradients,hidden_t)
        #Adjust the weights by Deltas
        self.weights_hidden_output.add(self.weights_hidden_output_delta)
        #Adjust the buas by it's deltas(which is just the gradient)
        self.bias_output.add(gradients)

        
        outputs.print()
        output_error.print()
        
        #Calculate the hidden errors

        self.weights_hidden_output_transpose= Matrix.transpose(self.weights_hidden_output)
        hidden_error=Matrix.multiply_matrices(self.weights_hidden_output_transpose,output_error)
        #Calculate Hidden Gradeients
        hidden_gradients=Matrix.map_static(hidden,der_sigmoid)
        hidden_gradients.multiply(hidden_error)
        hidden_gradients.multiply(self.learning_rate)
        
        #Calculate input to hidden deltas
        inputs_t=Matrix.transpose(inputs)
        self.weights_input_hidden_delta=Matrix.multiply_matrices(hidden_gradients, inputs_t)
        self.weights_input_hidden.add(self.weights_input_hidden_delta)
        #Adjust the buas by it's deltas(which is just the gradient)
        self.bias_hidden.add(hidden_gradients)

        print("Hidden error")
        hidden_error.print()
         

training_data=[{'input':[0,0],'targets':[0]},
               {'input':[0,1],'targets':[1]},
               {'input':[1,0],'targets':[1]},
               {'input':[1,1],'targets':[0]}]

def setup():
    nn=NeuralNetwork(2,2,1)
    for i in range(50000):
        data= random.choice(training_data)
        nn.train(data['input'],data['targets'])
    print("0,0",nn.feedforward([0,0]))
    print("0,1",nn.feedforward([0,1]))
    print("1,0",nn.feedforward([1,0]))
    print("1,1",nn.feedforward([1,1]))
setup()