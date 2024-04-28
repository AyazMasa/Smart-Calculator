class SmartCalculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Error: Division by zero!"
        return num1 / num2

class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class OperationFactory:
    def create_operation(self, operation):
        if operation == '+':
            return AddOperation()
        elif operation == '-':
            return SubtractOperation()
        elif operation == '*':
            return MultiplyOperation()
        elif operation == '/':
            return DivideOperation()

class AddOperation:
    def operate(self, num1, num2):
        return num1 + num2

class SubtractOperation:
    def operate(self, num1, num2):
        return num1 - num2

class MultiplyOperation:
    def operate(self, num1, num2):
        return num1 * num2

class DivideOperation:
    def operate(self, num1, num2):
        if num2 == 0:
            return "Error: Division by zero!"
        return num1 / num2

def save_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

calculator = SmartCalculator()
result = calculator.add(7, 9)
print(result)

operation_factory = OperationFactory()
operation = operation_factory.create_operation('+')
result = operation.operate(20, 2)
print(result)

save_to_file('result.txt', '10')
data = read_from_file('result.txt')
print(data)