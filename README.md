# README for Tkinter User Information Application

## Overview

This application is a simple Tkinter-based GUI tool designed to manage user information. Users can input and save details such as name, address, birth date, amount, gender, and nationality. The application also includes functionality to list saved information and clear input fields.

## Features

- **Input Fields**: Users can enter their first name, last name, address, birth date, amount, gender, and nationality.
- **Save Information**: Save the entered data to a text file.
- **Cancel Input**: Clear all input fields.
- **List Saved Data**: Display saved information in a list box.
- **Gender Selection**: Choose between "Masculin" and "Féminin" using radio buttons.
- **Nationality Selection**: Select nationality from a dropdown menu.

## Requirements

To run this application, you need Python installed with the `tkinter` module (which is included with Python standard library). Ensure you have Python 3.x.

### Required Libraries

- `tkinter` (included with Python standard library)

## Installation

1. Ensure Python 3.x is installed on your system.
2. No additional installations are required as `tkinter` is included with Python.

## Usage

1. **Running the Application**:
   - Save the script as `main.py`.
   - Open a terminal or command prompt and navigate to the directory containing `main.py`.
   - Run the script using the command: `python main.py`.

2. **Using the Application**:
   - **Input Fields**: Fill out the fields for First Name, Last Name, Address, Birth Date, Amount, Gender, and Nationality.
   - **Save**: Click the "Sauvegarder" button to save the information. If any required field is empty, a warning message will be displayed.
   - **Cancel**: Click the "Annuler" button to clear all input fields.
   - **List Data**: Click the "Lire les données" button to display all saved entries in the list box.

3. **File Handling**:
   - All user information is saved in `information.txt` in the same directory as the script.

## Code Structure

### Functions

- `sauvegarder()`: Validates and saves user information to a file. Displays warnings if required fields are empty.
- `annuler()`: Clears all input fields and sets the focus to the first input field.
- `lister()`: Reads data from the file and displays it in the list box.
- `button_radio(liste)`: Creates radio buttons for gender selection (not currently used in the main code).

### GUI Elements

- **Labels and Entry Widgets**: For user input of personal information.
- **Radio Buttons**: For gender selection.
- **ComboBox**: For selecting nationality.
- **Buttons**: For saving, cancelling, and listing data.
- **ListBox**: For displaying saved information.
