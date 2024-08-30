# COVID-19 Data Analyzer

## Overview
The COVID-19 Data Analyzer is a graphical user interface (GUI) application designed to provide users with various tools for analyzing and visualizing COVID-19 datasets. Users can easily present summary statistics, clean data, and generate plots from individual columns of a processed and cleaned COVID-19 dataset. The application offers an intuitive interface for data manipulation and visualization.

## Getting Started

### Prerequisites
To use the COVID-19 Data Analyzer, you'll need to set up your environment with the following dependencies. We recommend using PyCharm for this project:

1. **PyQt5**: For building the GUI.
    ```bash
    pip install PyQt5
    ```
2. **PyQt5 Tools**: Provides additional tools for PyQt5.
    ```bash
    pip install pyqt5-tools
    ```
3. **Matplotlib**: For plotting charts.
    ```bash
    pip install matplotlib
    ```
4. **NumPy**: Provides support for numerical operations.
    ```bash
    pip install numpy
    ```
5. **Pandas**: Used for data manipulation and analysis.
    ```bash
    pip install pandas
    ```

### Project Files
After setting up the environment, open the project folder in PyCharm. The folder contains the following files:

- **main.py**: The main script to run the application.
- **app_framework.py**: Contains the core functionality of the app.
- **cleaning.py**: Handles data cleaning tasks for the `cleaned_covid19_data.csv` file.
- **data_analyzer_gui2.ui**: The design file for the GUI.
- **cleaned_covid19_data.csv**: The pre-processed and cleaned dataset.
- **COVID-19_Cases_World.csv**: The original raw dataset.
- **mplwidget.py**: Custom widget for integrating Matplotlib plots.
- **requirements.txt**: Contains a list of Python packages and the Python version used for this project.
- **user_guide.txt**: Detailed instructions and guidance on using the application.

## User Interface

### Main Features
- **Open**: Loads the cleaned dataset into the application.
- **Column Selection**: Dropdown menu to select columns for analysis.
- **Chart Display Area**: The area where generated charts will be displayed.
- **Rename Column**: Renames the selected column based on user input.
- **Check Empty Value**: Identifies empty values within the dataset.
- **Drop Null Rows**: Removes rows containing null values.
- **Mean**: Calculates the mean of the selected column.
- **Median**: Computes the median of the selected column.
- **Min**: Returns the minimum value in the selected column.
- **Max**: Returns the maximum value in the selected column.
- **Data Shape**: Displays the number of rows and columns in the dataset.
- **Columns**: Lists all columns in the dataset.
- **Drop Column**: Deletes the selected column from the dataset.
- **Standard Deviation**: Calculates the standard deviation of the selected column.
- **Histogram**: Plots a histogram for the selected column.
- **Pie Chart**: Plots a pie chart for the selected column.
- **Check Punctuations**: Checks for punctuation marks in the dataset.
- **Clear Output**: Clears the output display area.
- **Drop Duplicate Rows**: Removes duplicate rows from the dataset.
- **Check Duplicates**: Identifies duplicate rows in the dataset.
- **User Input**: Text input area for entering custom commands or values.
- **User Output**: Displays the results or messages to the user.

## Usage

### Running the Application
For the best experience, run the application in full-screen mode:

1. **Load the Dataset**: Run `main.py` to start the application. Use the "Open" button to load the dataset. The filename and a confirmation message will appear in the output area.
2. **Column Operations**: Select a column from the dropdown menu and perform any desired operations using the available buttons. If the dataset is not loaded, an error message will be displayed.
3. **Renaming Columns**: Enter a new name (up to 15 characters) in the input field above the "Rename Column" button, then click the button to rename the selected column.
4. **Generating Charts**: To plot a histogram or pie chart, select a column and click the respective button.

This application offers a robust toolset for analyzing and visualizing COVID-19 data, making it easier to derive insights and perform essential data operations.
