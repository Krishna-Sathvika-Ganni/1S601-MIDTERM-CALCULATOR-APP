# HELLO PROFESSOR!! THIS IS MY MIDTERM PROJECT!!

## ADVANCED PYTHON CALCULATOR FOR SOFTWARE ENGINEERING GRADUATE COURSE.

## **PROJECT OVERVIEW**

THE DESIGN OF THIS PROJECT IS IMPLEMENTED USING: 

1. [COMMAND - LINE INTERFACE ( REPL )](#1-command-line-interface--repl-) <br/>
    - [Execution of Arithmetic operations](#-execution-of-arithmetic-operations-performs-add-subtract-multiply-and-divide-operations) <br/>
        - [Addition](#1-addition) <br/>
        - [Subtraction](#2-subtraction) <br/>
        - [Multiplication](#3-multiplication) <br/>
        - [Division](#4-division) <br/>
    - [History Management](#-history-management-saves-loads-clears-and-deletes-the-operations-performed)
        - [Save History](#1-save-history)
        - [Load History](#2-load-history)
        - [Clear History](#3-clear-history)
        - [Delete History](#4-delete-history)
    - [Plugin System](#-plugin-system-the-functionalities-are-dynamically-loaded-through-plugins)
2. [PLUGIN SYSTEM](#2-plugin-system) <br/>
    - [Menu Command](#-menu-command)
3. [CALCULATION HISTORY MANAGEMENT WITH PANDAS](#3-calculation-history-management-with-pandas) <br/>
4. [PROFESSIONAL LOGGING PRACTICES](#4-professional-logging-practices) <br/>
5. [ADVANCED DATA HANDLING WITH PANDAS](#5-advanced-data-handling-with-pandas) <br/>
6. [DESIGN PATTERNS FOR SCALABLE ARCHITECTURE](#6-design-patterns-for-scalable-architecture) <br/>
7. [CONFIGURATION VIA ENVIRONMENT VARIABLES](#7-configuration-via-environment-variables) <br/>
    - [ENVIRONMENT](#1-environment)
    - [LOG_LEVEL](#2-log_level)
    - [HISTORY_FILE](#3-history_file) <br/>
8. [EXCEPTION HANDLING STRATEGIES](#8-exception-handling-strategies) <br/>
    - [LBYL](#1-lbyl)
    - [EAFP](#2-eafp)
9. [INSTALLATION REQUIREMENTS]



## **1. COMMAND-LINE INTERFACE ( REPL )**

~ The **Read-Eval-Print Loop (REPL)** is used for direct interaction with the calculator in real-time. REPL is used for: 

#### ~ Execution of Arithmetic operations: Performs add, subtract, multiply and divide operations.

- [Addition](#1-addition) <br/>
- [Subtraction](#2-subtraction) <br/>
- [Multiplication](#3-multiplication) <br/>
- [Division](#4-division) <br/>


##### 1. **Addition:** 
- Sum of Two numbers is performed. 
- Errors are handled using try & except block if arises. 
- The program is designed to take two arguments and raises a error if more than two are given. 
- The user is asked for input, if arguments are not given.

[Click to view Code](./app/plugins/addcommand.py)

Video:  

https://github.com/user-attachments/assets/31b50d6f-e655-4c11-82dd-917fd73601ad





##### 2. **Subtraction:** 
- Difference of Two numbers is performed. 
- Errors are handled using try & except block if arises. 
- The program is designed to take two arguments and raises a error if more than two are given. 
- The user is asked for input, if arguments are not given.

[Click to view Code](./app/plugins/subtractcommand.py)

Video:

https://github.com/user-attachments/assets/7ef00c91-a9cf-425b-ab3f-2f6ccd7d2e4e


##### 3. **Multiplication:** 
- Product of Two numbers is performed. 
- Errors are handled using try & except block if arises. 
- The program is designed to take two arguments and raises a error if more than two are given. 
- The user is asked for input, if arguments are not given.

[Click to view Code](./app/plugins/multiplycommand.py)

Video: 

https://github.com/user-attachments/assets/64be29b5-f0a3-4a6a-b773-1077c05bf247


##### 4. **Division:** 
- Quotient of Two numbers is performed. 
- Errors are handled using try & except block if arises. 
- The program is designed to take two arguments and raises a error if more than two are given. 
- The user is asked for input, if arguments are not given.

[Click to view Code](./app/plugins/dividecommand.py)

Video: 

https://github.com/user-attachments/assets/d46c54f8-8171-441f-8e04-46143ccccc6c


#### ~ History Management: Saves, loads, clears and deletes the operations performed.

- [Save History](#1-save-history)
- [Load History](#2-load-history)
- [Clear History](#3-clear-history)
- [Delete History](#4-delete-history)

##### 1. **Save History:**
-  This stores the history of operations performed.
-  The History is saved to a CSV file.
-  If there is no history to save, it displays "No history to save" when executed Savehistory.

[Click to view code](./app/plugins/savehistorycommand.py)

Video:

https://github.com/user-attachments/assets/e1c55528-510b-441d-a39e-0724145a3f2b

[Click to view the saved history file](./data/calculation_history.csv)

##### 2. **Load History:**
-  This loads the history of operations performed.
-  The saved history file is displayed when executed loadhistory.
-  When there is no history saved, it displays "no History found".

[Click to view code](./app/plugins/loadhistorycommand.py)

Video:

https://github.com/user-attachments/assets/57690175-aaf2-432a-859e-577575e162c7


##### 3. **Clear History:**
-  This clears only in-memory history of operations performed.
-  If there is no in-memory, it displays "No history found to clear" when executed clearhistory. 

[Click to view code](./app/plugins/clearhistorycommand.py)

Video:

https://github.com/user-attachments/assets/bba3b243-4913-4b8c-83c6-fff7346e5e67


##### 4. **Delete History:**
-  This delete the history of operations performed.
-  If there is no saved history, it displays "No history found to delete" when executed deletehistory.

[Click to view code](./app/plugins/historycommand.py)

Video:

https://github.com/user-attachments/assets/a4675570-2d6e-44d9-a61a-4a27103b3f64


#### ~ Plugin System: The functionalities are dynamically loaded through plugins.

- The plugin folder contains the commands folders to execute the operations.

[Click to view code](./app/plugins/__init__.py)


## **2. PLUGIN SYSTEM**

- Implemented plugins architecture to extend the capabilities of the functionalities without making changes to the core application.
- The commands are loaded and integrated dynamically with plugins without modifying the application code.

#### ~ Menu Command:

- The Menu command lists all the available plugin commands.
- When "menu" is given as input, it displays all the available registered commands.
- If there are no commands registered, when given menu it displays "No commands available"

[Click to view code](./app/plugins/menucommand.py)

Video:

https://github.com/user-attachments/assets/c6cb2c72-c9ba-412d-8518-4fdfafba3827



## **3. CALCULATION HISTORY MANAGEMENT WITH PANDAS**

- The calculation history is managed using Pandas efficiently.

``` 
    import pandas as pd

    data=pd.DataFrame([
            {"x":calc.x, "y":calc.y, "operation":calc.operation.__name__, "result":calc.perform()} 
            for calc in history
        ])
    file_exists = os.path.exists(cls.HISTORY_FILE)
    data.to_csv(cls.HISTORY_FILE, mode='a', header=not file_exists, index=False) 
```

[Click to view code](./app/History/Managing_History.py)

- Using pandas, we can perform the following through REPL:
    - [Save the History](#1-save-history)
    - [Load the History](#2-load-history)
    - [Clear the History](#3-clear-history)
    - [Delete the History](#4-delete-history)

 Video:

https://github.com/user-attachments/assets/a51f2732-b01c-4c30-b4b5-62d99bcaa071


## **4. PROFESSIONAL LOGGING PRACTICES**

- A comprehensive logging system is implemented to record detailed application operations, data manipulations, errors and informational messages.
- The severity of messages is differentiated as INFO, WARNING, ERROR.
    - INFO: Logs general events
    - WARNING: Logs potential issues
    - ERROR: Logs errors and exceptions.
``` 
   logging.info("Enter two numbers:")
   logging.error("Invalid inputs")
   logging.WARNING("Cannot be divided by zero")
``` 
- Created a Configuration file for the logging system.
- Created dynamic logging configuration through environment variables for levels and output destinations.

Video:

https://github.com/user-attachments/assets/70f84547-735b-4a8e-8057-ac67d0c854ba


## **5. ADVANCED DATA HANDLING WITH PANDAS**

- The History is stored and retrieved from the CSV file which helps in efficient management of data.

```
# Saving the history to csv file:

    data=pd.DataFrame([
            {"x":calc.x, "y":calc.y, "operation":calc.operation.__name__, "result":calc.perform()} 
            for calc in history
        ])

    file_exists = os.path.exists(cls.HISTORY_FILE)

    data.to_csv(cls.HISTORY_FILE, mode='a', header=not file_exists, index=False) 

```

```
# Retrieving history from csv file:

     df = pd.read_csv(cls.HISTORY_FILE)

```

[Click to view the History Management file](./app/History/Managing_History.py)


## **6. DESIGN PATTERNS FOR SCALABLE ARCHITECTURE**

- For the maintable, scalable, reusable and neat structure of the code design patterns are implemented.
- The Design patterns used in this Calculator Program are 
    - [Command Pattern](#1-command-pattern)
    - [Facade Pattern](#2-facade-pattern)
    - [Factory Method Pattern](#3factory-method-pattern)
    - [Singleton Pattern](#4-singleton-pattern)
    - [Strategy Pattern](#5-strategy-pattern)

#### **1. Command Pattern:**

- The data required to execute an action is encapsulated in an object for better organization.

**- Formal Definition:** Command is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request. This transformation lets you pass requests as a method arguments, delay or queue a request’s execution, and support undoable operations.

Source: https://refactoring.guru/design-patterns/command

[Click to view code](./app/commands/__init__.py)



#### **2. Facade Pattern:**

- Facade pattern provides a simplified interface for history management using pandas.

**- Formal Definition:** Facade is a structural design pattern that provides a simplified interface to a library, a framework, or any other complex set of classes.

Source: https://refactoring.guru/design-patterns/facade

[Click to view code](./app/History/Facade_History.py)


#### **3.Factory Method Pattern:**

- Factory method allows us to create a centralized command.

**- Formal Definition:**  Factory Method is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

Source: https://refactoring.guru/design-patterns/factory-method

[Click to view code](./app/Factory/Command_Factory.py)


#### **4. Singleton Pattern:**

- Ensures that only one instance of logging or history management exists.

**- Formal Definition:**  Singleton is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.

Source: https://refactoring.guru/design-patterns/singleton

[Click to view code](./app/__init__.py)


#### **5. Strategy Pattern:**

- The data is encapsulated inside a object into different strategies.

**- Formal Definition:** Strategy is a behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.

Source: https://refactoring.guru/design-patterns/strategy



~ Factory and Singleton design patterns are Creational patterns. <br/>
~ Facade design pattern is a Structural pattern. <br/>
~ Command and Strategy design patterns are behavioral patterns. 


## **7. CONFIGURATION VIA ENVIRONMENT VARIABLES**

- To manage the settings dynamically, environment variables are used.
- This makes the application more adaptable, flexible and scalable.
    - [ENVIRONMENT](#1-environment)
    - [LOG_LEVEL](#2-log_level)
    - [HISTORY_FILE](#3-history_file)


#### **1. ENVIRONMENT:**

- Mode of execution of application is determined.(whether it's DEVELOPMENT OR PRODUCTION OR TESTING)

#### **2. LOG_LEVEL:**

- The logging levels ( INFO, ERROR, WARNING) are set and controlled using environment variables.

#### **3. HISTORY_FILE:**

- The file where calculation history is stored is specified.

```

load_dotenv()

```

[Click to view Code](./app/__init__.py)


## **8. EXCEPTION HANDLING STRATEGIES**

- Exception Handling is used to try and catch errors.
    - [LBYL](#1-lbyl)
    - [EAFP](#2-eafp)

- Exception handling blocks are used to handle errors efficiently.

#### **1. LBYL:**

- Look Before You Leap ( LBYL ) checks the condition before execution.

```
def divide(x: Decimal,y: Decimal) -> Decimal:
    if y == Decimal('0'):
        raise ValueError("Cannot be divided by Zero")
    return x / y
```

[Click to view code](./app/operation/operations.py)


#### **2. EAFP:**

- Easier to Ask for Forgiveness than Permission ( EAFP ) executes and ctches errors.

```

try:
    result = Calculator.divide(x, y)
except InvalidOperation:
    logger.error("Invalid arguments given")
except Exception as e:
    logger.error("Unexpected error")
    print(f"{e}")

```

[Click to view code](./app/plugins/dividecommand.py)


## **9. INSTALLATION REQUIREMENTS**

- The Following are installed dependencies to ensure code quality, testing and functionality:
    - [pytest](#1-pytest)
    - [pylint](#2-pylint)
    - [coverage](#3-coverage)
    - [Virtual environment](#4-virtual-environment)
    - [Faker](#5-faker)
    - [Pandas](#6-pandas)
    - [Requirements text file](#7-requirements-text-file)

#### **1. pytest:** 

- A Strong python testing framework is the pytest.
- It ensures that all features and functions operate as intended by automating the testing process.

```
    pip install pytest

```

#### **2. pylint:** 

- Pylint checks whether the code adheres to PEP 8 compliance.

```
    pip install pylint-pytest

```

#### **3. coverage:**

- 'pytest-cov' shows which codes are tested and generates a code coverage report.

```
    pip install pytest-cov

```

#### **4. Virtual Environment:**

- Dependencies are isolated by a virtual environment (venv), which avoids conflicts between several projects.

```

    # Installing virtual environment
    pip3 install virtualenv

    # Creating a Virtual environment
    python3 -m virtualenv vir_env

    # Activating the virtual environment
    source vir_env/bin/activate

    # De-activating the virtual environment
    deactivate

```


#### **5. Faker:**

- The faker generates fake data that is realistic.

```

    pip install faker

```

## **6. Pandas:**

- To store and manage calculation history in .csv file, pandas is installed.

```

    pip install pandas

```

#### **7. Requirements text file:**

- The installed dependencies and their versions are stored in the requirements text file.

```

    pip freeze > requirements.txt

```

[Click to view the requirements text file](./requirements.txt)





