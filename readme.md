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
5. ADVANCED DATA HANDLING WITH PANDAS <br/>
6. DESIGN PATTERNS FOR SCALABLE ARCHITECTURE <br/>
7. CONFIGURATION VIA ENVIRONMENT VARIABLES <br/>


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




