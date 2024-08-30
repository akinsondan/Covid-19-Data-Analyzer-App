from string import punctuation
import numpy as np
import pandas as pd
from PyQt5 import QtWidgets, uic


class AppWindow(QtWidgets.QMainWindow):

    # the initialisation method of the class, the first method to be run in the class
    # self keyword that it can be called from outside the class
    def __init__(self):
        super(AppWindow, self).__init__()

        # load ui file
        uic.loadUi("data_analyzer_gui2.ui", self)

        # Connect the clicked event on user interface to custom method, which will execute when the button is clicked
        self.file_open.clicked.connect(self.load_file)
        self.mean_btn.clicked.connect(self.avg_val)
        self.median_btn.clicked.connect(self.median_val)
        self.min_btn.clicked.connect(self.min_val)
        self.max_btn.clicked.connect(self.max_val)
        self.std_dv_btn.clicked.connect(self.std_dv_val)
        self.columns_btn.clicked.connect(self.df_columns_values)
        self.rename_col_btn.clicked.connect(self.rename_col)
        self.empty_values_btn.clicked.connect(self.check_null_values)
        self.drop_null_btn.clicked.connect(self.drop_null_values)
        self.data_shape_btn.clicked.connect(self.df_shape)
        self.hist_btn.clicked.connect(self.plot_hist)
        self.reset_index_btn.clicked.connect(self.reset_index)
        self.pie_chart_btn.clicked.connect(self.plot_pie)
        self.drop_columns_btn.clicked.connect(self.drop_col)
        self.check_punct_btn.clicked.connect(self.check_punct)
        self.check_dup_btn.clicked.connect(self.check_dup)
        self.drop_dup_btn.clicked.connect(self.drop_dup)
        self.clear_output_btn.clicked.connect(self.clear_output)

    # custom methods

    # load file
    def load_file(self):
        # load file into an attribute/variable
        self.df = pd.read_csv("cleaned_covid19_data.csv")

        # clear user display
        self.user_output.clear()

        #  set text to user output display
        self.user_output.setText('file opened')

        # set file name to user_output
        self.file_path.setText('cleaned_covid_data.csv')

        # send dataframe column as list to comboBox drop down menu
        self.col_list.addItems([i for i in self.df.columns])

    def clear_output(self):
        # clears user_output
        try:
            self.user_output.clear()

        # catch error if file is not opened
        except:
            self.user_output.setText('Please open file')



    # calculate average
    def avg_val(self):
        try:
            # calculate mean with numpy np.median and string formatting and round up
            self.user_output.setText(f'Average value: {round(np.mean(self.df[self.col_list.currentText()]))}')

        # catch error if incompatible column is selected
        except TypeError:
            self.user_output.setText("Can't Perform this operation on this column, please select another column")

        # catch error if file is not opened
        except:
            self.user_output.setText('Please open file and select column')

    # calculate median
    def median_val(self):
        try:
            # calculate mean with numpy np.median, round up and string formatting
            self.user_output.setText(f'Median value: {round(np.median(self.df[self.col_list.currentText()]))}')

        # catch error if incompatible column is selected
        except TypeError:
            self.user_output.setText("Can't Perform this operation on this column, please select another column")

        # catch error if file is not opened
        except BaseException:
            self.user_output.setText('Please open file and select column')

    # calculate minimum value
    def min_val(self):
        try:
            # calculate minimum value with python min function and string formatting
            self.user_output.setText(f'Minimum value: {round(min(self.df[self.col_list.currentText()]))}')
        except TypeError:
            self.user_output.setText("Can't Perform this operation on this column, please select another column")
        except BaseException:
            self.user_output.setText('Please open file and select column')

    # calculate maximum value
    def max_val(self):
        try:
            # calculate maximum value with python max function numpy , round up and string formatting
            self.user_output.setText(f'Maximum value: {round(max(self.df[self.col_list.currentText()]))}')

        # catch error if incompatible column is selected
        except TypeError:
            self.user_output.setText("Can't Perform this operation on this column, please select another column")

        # catch error if file is not opened
        except BaseException:
            self.user_output.setText('Please open file and select column')

    # calculate standard deviation
    def std_dv_val(self):
        # calculate standard deviation with numpy np.std, round up and string formatting
        try:
            self.user_output.setText(f'Standard deviation: {round(np.std(self.df[self.col_list.currentText()]))}')

        # catch error if incompatible column is selected
        except TypeError:
            self.user_output.setText("Can't Perform this operation on this column, please select another column")

        # catch error if file is not opened
        except BaseException:
            self.user_output.setText('Please open file and select column')

    # print columns
    def df_columns_values(self):

        # print dataframe columns to user_output
        try:
            self.user_output.setText(str([i for i in self.df.columns]))

        # catch error if file is not opened
        except BaseException:
            self.user_output.setText('Please open file and select column')

    # rename column
    def rename_col(self):
        try:
            # input is requested if lineEdit is empty
            if self.new_col_name.text() == '':
                self.user_output.setText('Please write new column name')
            else:
                # column updated in dataframe
                self.df.rename({self.col_list.currentText(): self.new_col_name.text()}, axis='columns', inplace=True)

                # old comboBox is cleared
                self.col_list.clear()

                # new columns added to comboBox
                self.col_list.addItems([i for i in self.df.columns])
                self.user_output.setText('Column name changed!')

                # lineEdit is cleared
                self.new_col_name.clear()

        # catch error if file is not opened
        except BaseException:
            self.user_output.setText('Please open file and select column')

    # check null values
    def check_null_values(self):
        try:
            # return number of null values in each column
            self.user_output.setText(f'{self.df.isnull().sum()}')

        # catch error if file is not opened
        except BaseException:
            self.user_output.setText('Please open file and select column')

    # drop null values
    def drop_null_values(self):

        # drop empty rows in dataframe
        try:
            self.df.dropna(inplace=True)

            # print result to user_output
            self.user_output.setText('Rows with empty values dropped')

        # catch error if file is not opened
        except BaseException:
            self.user_output.setText('Please open file and select column')

    # dataframe shape (rows,columns)
    def df_shape(self):
        try:
            # print number of columns and rows to user_output
            self.user_output.setText(str(f'columns: {self.df.shape[0]}, rows: {self.df.shape[1]}'))

        # catch error if file is not opened
        except BaseException:
            self.user_output.setText('Please open file and select column')

    #   plot histogram
    def plot_hist(self):
        try:
            # first clear the plotting area
            # plot for selected column from selected column
            # if not numerical matplotlib plots the most suitable plot
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(self.df[self.col_list.currentText()])
            # plot tiltle
            self.MplWidget.canvas.axes.set_title(f'Data Distribution')

            # command to finally draw chart
            self.MplWidget.canvas.draw()

        # catch error if incompatible column is selected
        except TypeError:
            self.user_output.setText("Can't Perform this operation on this column, please select another column")

        # catch error if file is not opened
        except BaseException:
            self.user_output.setText('Please open file and select column')

    # plot pie chart
    def plot_pie(self):
        try:
            # clear plotting area
            self.MplWidget.canvas.axes.clear()

            # pot pie chart with labels and count of selected column in comboBox
            self.MplWidget.canvas.axes.pie(self.df[self.col_list.currentText()].value_counts(), labels=self.df[self.col_list.currentText()].unique())

            # plot Title
            self.MplWidget.canvas.axes.set_title(f'Data composition')

            # draw plot
            self.MplWidget.canvas.draw()

        # catch error if incompatible column is selected
        except TypeError:
            self.user_output.setText("Can't Perform this operation on this column, please select another column")

        # catch error if file is not opened
        except BaseException:
            self.user_output.setText('Please open file and select column')

    # reset dataframe index
    def reset_index(self):
        try:
            # reset index of dataframe
            self.df.reset_index(inplace=True)

        # catch error if file is not opened
        except BaseException:
            self.user_output.setText('Please open file and select column')

    # drop column from dataframe
    def drop_col(self):
        try:
            # drop column from selected column
            self.df.drop(self.col_list.currentText(), axis=1, inplace=True)

            # clear comboBox
            self.col_list.clear()

            # add new columns to comboBox
            self.col_list.addItems([i for i in self.df.columns])
            
            # print to user_output
            self.user_output.setText('Column dropped')

        # catch error if file is not opened
        except BaseException:
            self.user_output.setText('Please open file and select column')

    # check for number of duplicates rows
    def check_dup(self):

        # number of duplicate rows is printed to user_output
        try:
            self.user_output.setText(f'Number of duplicate row is: {self.df.duplicated().sum()}')

        # catch error if file is not opened
        except BaseException:
            self.user_output.setText('Please open file and select column')

    def check_punct(self):
        try:

            # cells with punctuations is printed to user_output
            self.user_output.setText(f'Number of values with punctuations is : {self.df.isin(list(punctuation)).any().sum()}')

        # catch error if file is not opened
        except BaseException:
            self.user_output.setText('Please open file and select column')

    # drop duplicate row if there is duplicate
    def drop_dup(self):
        try:
            # drop duplicates if there are duplicates and prints to user_output
            if self.df.duplicated().sum() == 0:
                self.user_output.setText(f'There are no duplicate rows')
            else:
                self.df.drop_duplicates(inplace=True)
                self.user_output.setText(f'Duplicates removed')

        # catch error if file is not opened
        except BaseException:
            self.user_output.setText('Please open file and select column')
