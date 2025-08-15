import sys
from PyQt5.QtWidgets import QApplication
from weatherApp import WeatherApp

def main():
    app = QApplication(sys.argv)
    weatherApp = WeatherApp()
    weatherApp.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()