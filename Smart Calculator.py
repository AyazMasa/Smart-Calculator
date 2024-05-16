import unittest
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

class TestSmartCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = SmartCalculator()

    def test_addition(self):
        result = self.calculator.calculate('+', 5, 3)
        self.assertEqual(result, 8)

    def test_subtraction(self):
        result = self.calculator.calculate('-', 5, 3)
        self.assertEqual(result, 2)

    def test_multiplication(self):
        result = self.calculator.calculate('*', 5, 3)
        self.assertEqual(result, 15)

    def test_division(self):
        result = self.calculator.calculate('/', 10, 2)
        self.assertEqual(result, 5)

    def test_division_by_zero(self):
        result = self.calculator.calculate('/', 10, 0)
        self.assertEqual(result, "Error: Division by zero!")

if __name__ == "__main__":
    unittest.main()
