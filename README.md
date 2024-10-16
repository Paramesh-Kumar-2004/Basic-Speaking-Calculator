Speaking Calculator
  This project is a voice-interactive calculator created in Python using the pyttsx3 library for text-to-speech functionality. It allows users to input two numbers and select an arithmetic operator. The calculator not only performs the calculations but also speaks the input and results.

Features:
  1.Interactive voice prompts and responses.
  2.Supports basic arithmetic operations: addition, subtraction, multiplication, division, modulus, and integer division.
  3.Text-to-speech support for enhanced user interaction.




Explanation of the Speaking Calculator Code:

This Python script creates a voice-interactive calculator using the pyttsx3 library, which allows the program to speak the input and output.

  1.pyttsx3 Initialization:
    i) The script initializes the text-to-speech engine pyttsx3 with the "sapi5" voice engine, which is commonly available on Windows.
    ii) The engine.setProperty("voices", voice[0]) sets the voice to the first available one.

  2.say Function:
    The say() function is defined to handle speech synthesis. It takes a string as input, speaks it, and waits until the speech finishes with engine.runAndWait().

  3.Introduction and Number Inputs:
    i) The program starts by announcing itself as a "speaking calculator."
  ii) It prompts the user to enter the first and second numbers, using say() to speak these prompts. After the user inputs each number, it reads the input back aloud.

  4.Operator Input:
    i)  A list of valid operators (+, -, /, *, %, //) is shown.
    ii) The user is asked to select an operator, and this selection is also read aloud by the program.

  5.Performing Operations:
    i) Using conditional if-elif statements, the program performs the operation corresponding to the operator input.
  ii) Each mathematical operation (addition, subtraction, multiplication, division, modulus, and integer division) is calculated and printed, followed by the result being spoken using say().

  6.Error Handling:
    i) If the user enters an invalid operator, the program prints and speaks an error message: "You Entered Invalid Operators. Please Try Again."


How to Use:
  1.Clone the repository to your local machine.
  2.Ensure Python and the required libraries are installed (pyttsx3).
  3.Run the script:
      python speaking_calculator.py
  4.Follow the spoken instructions and enter your numbers and operator.


  Prerequisites:
    1.Python 3.x
    2.pyttsx3 library (Install with pip install pyttsx3)

  Future Enhancements:
    1.Add more mathematical operations.
    2.Improve voice interaction with more detailed instructions and error handling.
