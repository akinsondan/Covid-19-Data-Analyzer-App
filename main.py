from PyQt5 import QtWidgets
import sys

# import app_framework module
import app_framework as af

# run app
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = af.AppWindow()
    window.show()
    sys.exit(app.exec_())