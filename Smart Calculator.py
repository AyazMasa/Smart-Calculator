import os
import json

class Operation:
    def operate(self, num1, num2):
        pass

class AddOperation(Operation):
    def operate(self, num1, num2):
        return num1 + num2

class SubtractOperation(Operation):
    def operate(self, num1, num2):
        return num1 - num2

class MultiplyOperation(Operation):
    def operate(self, num1, num2):
        return num1 * num2

class DivideOperation(Operation):
    def operate(self, num1, num2):
        if num2 == 0:
            return "Error: Division by zero!"
        return num1 / num2

class SmartCalculator:
    def __init__(self):
        self.operations = {
            '+': AddOperation(),
            '-': SubtractOperation(),
            '*': MultiplyOperation(),
            '/': DivideOperation()
        }

    def calculate(self, operation, num1, num2):
        if operation in self.operations:
            return self.operations[operation].operate(num1, num2)
        else:
            return "Error: Unsupported operation"

class FileManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(FileManager, cls).__new__(cls)
        return cls._instance

    def save_to_file(self, filename, data):
        with open(filename, 'w') as file:
            json.dump(data, file)

    def read_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return json.load(file)
        else:
            return None

def main():
    calculator = SmartCalculator()
    file_manager = FileManager()

    num1 = float(input("Enter the first number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    result = calculator.calculate(operation, num1, num2)
    print("Result:", result)

    filename = 'calculator_result.json'
    file_manager.save_to_file(filename, {'num1': num1, 'operation': operation, 'num2': num2, 'result': result})
    print("Data saved to file.")

    data = file_manager.read_from_file(filename)
    print("Data read from file:", data)

if __name__ == "__main__":
    main()
