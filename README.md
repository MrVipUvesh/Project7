# Multi-Utility Toolkit

Multi-Utility Toolkit is a menu-driven Python application that brings together several useful operations in one program. It provides tools for working with dates and time, performing mathematical calculations, generating random data, creating unique identifiers, and managing text files.

The project is designed to practice Python programming concepts through a modular structure, with separate modules handling different categories of operations.

## Features

### 1. Date and Time Operations
- Display the current date and time.
- Calculate the difference between two dates.
- Format dates according to a custom format.
- Use a stopwatch.
- Run a countdown timer in seconds.

### 2. Mathematical Operations
- Calculate the factorial of a number.
- Calculate compound interest.
- Perform trigonometric calculations.
- Calculate inverse trigonometric values.
- Find the area of geometric shapes.

The trigonometric operations include sine, cosine, tangent, inverse sine, inverse cosine, and inverse tangent.

### 3. Random Data Generation
- Generate a random number within a specified range.
- Generate a random list.
- Create a random password of a specified length.
- Generate a random OTP.

If the starting value of a random-number range is greater than the ending value, the program swaps the values before generating the number.

### 4. Unique Identifier Generation
- Generate a UUID using a dedicated module.
- Display the generated identifier.

### 5. File Operations
- Create a new text file.
- Write text to a file.
- Read the contents of a file.
- Append additional text to a file.
- Delete a file after confirmation.

The program automatically adds the `.txt` extension to filenames entered through the file operations menu.

### 6. Module Attribute Exploration
- Enter a module name to explore its attributes.
- Use Python's `dir()` function to inspect available attributes.

### 7. Interactive Menu
- Navigate through different categories of operations.
- Return to the main menu from submenus.
- Handle invalid menu selections.
- Exit the application when finished.

## Technologies and Concepts Used

This project demonstrates the practical use of the following Python concepts:

- Functions and methods
- Classes and objects
- Modular programming
- Importing custom modules
- Variables and data types
- User input and output
- Type conversion using `int()` and `float()`
- Conditional statements
- `while` loops
- `match-case` statements
- String formatting with f-strings
- Lists and iteration
- Exception handling, where implemented in the supporting modules
- Date and time manipulation
- Mathematical calculations
- Random data generation
- File handling
- Operating system operations
- UUID generation
- Built-in functions such as `dir()`

## Project Structure

The main program imports five custom modules. A suitable project structure is:

    Multi-Utility-Toolkit/
    ├── main.py
    ├── dt_module.py
    ├── math_module.py
    ├── random_module.py
    ├── uuid_module.py
    ├── file_module.py
    └── README.md

The filenames shown above correspond to the module imports used in the main program. Keep the actual filenames and class or method names consistent with your implementation.

## Requirements

- Python 3.10 or later
- The five supporting Python modules used by the main program
- No additional third-party packages are required by the main program itself, provided the supporting modules use only Python's standard library.

Python 3.10 or later is needed because the application uses the `match-case` statement.

## Installation and Execution

1. Install Python 3.10 or later.
2. Place the main program and all supporting modules in the same project directory.
3. Open a terminal or command prompt in that directory.
4. Run the following command:

       python main.py

   On systems where Python 3 is invoked separately, use:

       python3 main.py

The main menu will appear after the program starts.

## Main Menu

The application presents the following options:

    Welcome to Multi-Utility Toolkit

    Choose an option:
    1. Date and Time Operations
    2. Mathematical Operations
    3. Random Data Generation
    4. Generate Unique Identifiers
    5. File Operations
    6. Explore Module Attributes
    7. Exit

Enter the number corresponding to the operation you want to perform.

## Usage Examples

The following examples illustrate the interaction supported by the main program. Actual output may vary depending on the implementation of the supporting modules and the values entered.

### Date and Time Operations

Select option `1` to open the date and time submenu.

    Date and Time Operations:
    1. Display current date and time
    2. Calculate difference between two dates/times
    3. Formate date into custom format
    4. Stopwatch
    5. Countdown timer
    6. Back to Main Menu

To calculate the difference between two dates, select option `2` and enter dates in the specified format.

    Enter the first date (YYYY-MM-DD): 2026-01-01
    Enter the second date (YYYY-MM-DD): 2026-01-10

The result is displayed by the date and time module.

### Mathematical Operations

Select option `2` from the main menu.

    Mathematical Operations:
    1. Calculate Factorial
    2. Solve Compound Interest
    3. Trigonometric Calculations
    4. Area of Geometric Shapes
    5. Back to Main Menu

For example, to calculate a factorial:

    Enter a number to count factorial: 5
    Factorial of 5 is: 120

For compound interest, the program requests the principal amount, interest rate, and time period.

    Enter principal amount: 10000
    Enter rate of interest (in %): 5
    Enter time (in years): 2

The compound interest result is returned by the mathematical module.

### Random Data Generation

Select option `3` to access the random data tools.

For example, generating a random number:

    Enter starting range: 1
    Enter ending range: 100

    Random Number: 42

The displayed number is illustrative; actual output is random.

The random list and password options allow the user to specify a desired length. The OTP option generates an OTP through the random operations module.

### Generating a Unique Identifier

Select option `4` from the main menu.

    Generated UUID: [generated identifier]

The identifier is generated by the UUID module. The value shown here is a placeholder for the actual output.

### File Operations

Select option `5` to access the file management submenu.

    File Operations:
    1. Create a new file
    2. Write to a file
    3. Read from a file
    4. Append to a file
    5. Delete a file
    6. Back to Main Menu

For example, creating a file:

    Enter file name: notes

The main program passes `notes.txt` to the file handling module.

To write content:

    Enter name to write: notes
    Enter text to add: This is my first text file.

The read option displays the file contents, while the append option adds additional text. The delete option asks for confirmation before requesting file deletion.

### Exploring Module Attributes

Select option `6` from the main menu.

    Explore Module Attributes
    Enter module name to explore: math

The program then calls `dir()` on the entered value and displays the result.

Note that `dir(name)` examines the string stored in `name`; it does not automatically import or inspect a module based on its name. To inspect an actual imported module, the module object must be passed to `dir()`.

## Modular Design

The application separates its operations into dedicated modules rather than placing every operation in the main program.

- `dt_module` handles date and time operations through the `DtOperations` class.
- `math_module` handles mathematical calculations through the `MathOperations` class.
- `random_module` provides random-number, list, password, and OTP generation through the `randomOperations` class.
- `uuid_module` generates unique identifiers through the `UUIDoperation` class.
- `file_module` provides file management through the `FileHandling` class.

This structure makes the main program easier to navigate and allows related functionality to remain grouped together.

## Learning Objectives

The main purpose of this project is to understand how different Python concepts can be combined into one application.

By working on this project, you can gain experience with:

- Designing menu-driven programs
- Dividing a program into multiple modules
- Creating and using classes
- Working with dates and time
- Implementing mathematical operations
- Generating random values and identifiers
- Reading, writing, appending, and deleting files
- Using loops and conditional logic
- Calling methods from imported modules
- Handling user choices and invalid selections

## Conclusion

Multi-Utility Toolkit is a practical Python project that combines several everyday utilities into one command-line application. Its modular design provides an opportunity to practise organizing code into separate files while building a variety of useful features.

The project can also serve as a foundation for future improvements, such as stronger input validation, more detailed error handling, additional mathematical operations, and a graphical user interface.
