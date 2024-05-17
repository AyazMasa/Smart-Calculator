# Smart Calculator
## Created by Ayaz Masa
 ## 1. Introduction

The Smart Calculator application is a Python program designed to perform basic arithmetic operations using object-oriented programming principles.

### What is Smart Calculator?

Smart Calculator is a command-line tool that allows users to perform addition, subtraction, multiplication, and division operations on numbers.

### How to Run the Program?

To run the program, follow these steps:
1. Ensure you have Python installed on your system.
2. Clone the repository to your local machine.
3. Navigate to the project directory in the command line.
4. Run the `Smart_Calculator.py` file using Python.

### How to Use the Program?

Once the program is running, follow these steps to perform calculations:
1. Enter the operation you want to perform (`+`, `-`, `*`, `/`).
2. Enter the first number.
3. Enter the second number.
4. The program will display the result of the operation.
## 2. Analysis

### Body/Analysis

The Smart Calculator program implements various classes and methods to support arithmetic operations. Here's a breakdown of its implementation:

- **Operation:** Abstract base class defining the `operate` method.
- **AddOperation, SubtractOperation, MultiplyOperation, DivideOperation:** Concrete subclasses implementing the `operate` method for addition, subtraction, multiplication, and division, respectively.
- **SmartCalculator:** Class managing the calculation process by mapping operation symbols to their respective operation objects.
- **FileManager:** Singleton class providing file I/O operations for saving and reading data.
- **TestSmartCalculator:** Unit test class verifying the correctness of arithmetic operations.
### Implementation of OOP principles

1. **Polymorphism**

   Polymorphism allows objects of different classes to be treated as objects of a common superclass.

   **Implementation:** Method overriding is used in subclasses of the `Operation` class (`AddOperation`, `SubtractOperation`, `MultiplyOperation`, `DivideOperation`). Each subclass implements the `operate` method differently to perform specific arithmetic operations.

```python
   class
        Operation:
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
```

2. **Abstraction**

   Abstraction involves hiding the complex implementation details and only exposing necessary features of an object.

   **Implementation:** The use of classes (`Operation`, `AddOperation`, `SubtractOperation`, `MultiplyOperation`, `DivideOperation`) encapsulates the behavior for performing arithmetic operations, hiding the implementation details from the user.

```python
   class Operation:
    def operate(self, num1, num2):
        pass
```
3. **Inheritance**

   Inheritance allows a class to inherit properties and behavior from another class.

   **Implementation:** Subclasses (`AddOperation`, `SubtractOperation`, `MultiplyOperation`, `DivideOperation`) inherit from the `Operation` class. They inherit the `operate` method and override it to implement specific behavior for each operation.

```python
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

class TestSmartCalculator(unittest.TestCase):

```

4. **Encapsulation**

   Encapsulation involves bundling the data and methods that operate on the data into a single unit (class).

   **Implementation:** Classes such as `Operation`, `AddOperation`, `SubtractOperation`, `MultiplyOperation`, `DivideOperation` encapsulate the behavior for performing arithmetic operations. Methods like `operate` and `calculate` encapsulate the logic for performing calculations.

```python
class Operation:

class SmartCalculator:
    def __init__(self):
        self.operations = {
            '+': AddOperation(),
            '-': SubtractOperation(),
            '*': MultiplyOperation(),
            '/': DivideOperation()
        }
    
class FileManager:
    _instance = None
```
### Utilized design patterns

1. **Singleton Pattern**:

The Singleton Pattern is suitable for the FileManager class to ensure that only one instance of the class is created throughout the program's lifecycle. Here's why it's the most suitable choice:

- Guaranteed Single Instance: The Singleton Pattern guarantees that there is only one instance of the FileManager class in the entire application. This ensures that resources, such as file handles and memory, are efficiently managed.

- Global Access Point: By providing a single globally accessible instance, the Singleton Pattern facilitates easy access to the FileManager functionality from any part of the codebase. This promotes code reusability and simplifies resource management.

- Lazy Initialization: The Singleton Pattern supports lazy initialization, meaning that the instance is created only when it is first requested. This helps improve performance and resource utilization by delaying the creation of the object until it is actually needed.
   - The `FileManager` class implements the Singleton pattern to ensure that only one instance of the class is created throughout the program's lifecycle. This is achieved by using a class variable `_instance` to hold the single instance and ensuring that the constructor (`__new__` method) only creates a new instance if `_instance` is `None`.
```python

class FileManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(FileManager, cls).__new__(cls)
        return cls._instance
```
2. **Factory Method Pattern (Implicit):**

The Factory Method Pattern is suitable for the SmartCalculator class because it encapsulates the object creation logic for different operation objects (AddOperation, SubtractOperation, etc.) based on the provided operation symbol. Here's why it's the most suitable choice:

- Encapsulation of Creation Logic: The Factory Method Pattern encapsulates the logic for creating objects, which allows the SmartCalculator class to abstract away the details of object creation. This promotes cleaner code and separation of concerns.

- Flexibility and Extensibility: By using the Factory Method Pattern, the SmartCalculator class can easily accommodate new types of operations without modifying its core implementation. Adding a new operation simply requires adding a new entry to the operations dictionary with the corresponding operation symbol and operation object.

- Reduced Coupling: The Factory Method Pattern reduces coupling between the SmartCalculator class and the concrete operation classes (AddOperation, SubtractOperation, etc.). The SmartCalculator class only depends on the common interface provided by the Operation superclass, rather than directly instantiating concrete operation objects.

  - The `SmartCalculator` class utilizes a factory method pattern implicitly when instantiating different operation objects (`AddOperation`, `SubtractOperation`, etc.) based on the provided operation symbol. It encapsulates the object creation logic and allows for the creation of operation objects without exposing the instantiation logic.

```python
class SmartCalculator:
    def __init__(self):
        self.operations = {
            '+': AddOperation(),
            '-': SubtractOperation(),
            '*': MultiplyOperation(),
            '/': DivideOperation()
        }
```
### Unit Testing Overview

The unit testing in the provided code ensures that the `SmartCalculator` class functions correctly by testing each arithmetic operation method (`operate`) of its various subclasses (`AddOperation`, `SubtractOperation`, `MultiplyOperation`, `DivideOperation`). Additionally, it includes tests for error handling, specifically division by zero.

1. **Test Cases:**
   - **test_addition:** Tests the addition operation (+).
   - **test_subtraction:** Tests the subtraction operation (-).
   - **test_multiplication:** Tests the multiplication operation (*).
   - **test_division:** Tests the division operation (/).
   - **test_division_by_zero:** Tests division by zero error handling.

2. **Test Setup:**
   - The `setUp` method in the `TestSmartCalculator` class initializes an instance of the `SmartCalculator` class before each test case execution, ensuring a clean test environment.

3. **Assertions:**
   - Each test case uses assertions (specifically `self.assertEqual`) to verify that the calculated result matches the expected result.

4. **Running the Tests:**
   - The tests can be run by executing the script with the `--test` argument. This triggers the execution of the unit tests using the `unittest` framework.

**Usage:**

To run the unit tests, execute the script with the `--test` argument:

```python
python "Smart Calculator.py_2.py" --test
```

**Example Output:**

```python
.....
Ran 5 tests in 0.001s
OK
```
This indicates that all five tests passed successfully.

## Converting to Executable

To convert the Python script into a standalone executable (.exe) file, follow these steps:

### 1. Install PyInstaller

If PyInstaller is not already installed, install it via pip:

     python smart_calculator.py

2. Navigate to Project Directory
Open a terminal or command prompt and navigate to the directory containing your Python script (smart_calculator.py).

3. Run PyInstaller
Execute the following command to generate the executable:
```python
pyinstaller --onefile smart_calculator.py
```
This command tells PyInstaller to create a single executable file (smart_calculator.exe) for your script.

4. Locate the Executable
Once PyInstaller has finished running, it will create a dist directory within your project directory. Inside the dist directory, you'll find your executable file (smart_calculator.exe on Windows).

5. Test the Executable
Run the executable to ensure that it works as expected. You can do this by double-clicking on it or running it from the command line.

    ## How to Run the Executable?

To run the created executable file (`Smart_Calculator.exe`), follow these steps:

1. Navigate to the directory where the executable file is located.
2. Double-click on the `Smart_Calculator.exe` file.
3. The Smart Calculator program will start, and you can use it to perform arithmetic calculations.


## Results and Summary

- The Smart Calculator program successfully performs basic arithmetic operations.
- Challenges were faced during the implementation, especially in converting Python script into an executable (.exe) file.
- The program demonstrates the effective use of object-oriented programming principles for building a calculator application.

## Conclusions

In conclusion, the Smart Calculator application has achieved its goal of providing a simple yet effective tool for performing arithmetic calculations. Future prospects for the program include enhancing its user interface, adding support for more complex mathematical functions, and improving error handling.
