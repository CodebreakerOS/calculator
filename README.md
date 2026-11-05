# Calculator

A Python 3 calculator used from the Terminal, built step by step in SCCM4910.

## What it will do
Add, subtract, multiply and divide two numbers; display the result.

## How to run it
Use the run script: ./run.sh

Enter the first number, operator (+ - * /), then a second number.
The program prints Result: followed by the answer.

## How to test
1. Make sure you are in the test environment. If not, please run: "source /opt/python-venv/sccm-4910/bin/activate"
2. Run unit tests with: "./check.sh" - Should pass all 5
3. Check exit status is zero: "echo $?"

## Sample test
First number: 6
Operator (+ - * /): *
Second number: 7
Result: 42.0

## How to exit
To exit out of the calculator, press CTRL+C
