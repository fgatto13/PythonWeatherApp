# a5cce5fb01f2c0b348360574110a5096
# for ui
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
# for alignment
from PyQt5.QtCore import Qt, QSize

from weatherFunctions import WeatherFunctions
from dataFetcher import DataFetcher

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        # UI elements
        self.cityLabel = QLabel("Enter city name: ", self)
        self.cityInput = QLineEdit(self)
        self.getWeatherButton = QPushButton("Get Weather", self)
        self.temperatureLabel = QLabel(self)
        self.weatherEmojiLabel = QLabel(self)
        self.descriptionLabel = QLabel(self)
        # initialize the UI
        self.initUI()

    def initUI(self):
        # define the window title
        self.setWindowTitle("Weather App")
        self.setFixedSize(400, 600)
        # create a new vertical layout
        layout = QVBoxLayout()

        # add all the widgets to it
        layout.addWidget(self.cityLabel)
        layout.addWidget(self.cityInput)
        layout.addWidget(self.getWeatherButton)
        layout.addWidget(self.temperatureLabel)
        layout.addWidget(self.weatherEmojiLabel)
        layout.addWidget(self.descriptionLabel)

        # set the layout of the window
        self.setLayout(layout)

        # set all the items to be aligned at the center of the window
        self.cityLabel.setAlignment(Qt.AlignCenter)
        self.cityInput.setAlignment(Qt.AlignCenter)
        self.temperatureLabel.setAlignment(Qt.AlignCenter)
        self.weatherEmojiLabel.setAlignment(Qt.AlignCenter)
        self.descriptionLabel.setAlignment(Qt.AlignCenter)

        # define unique IDs for each item
        self.cityLabel.setObjectName('cityLabel')
        self.cityInput.setObjectName('cityInput')
        self.getWeatherButton.setObjectName('getWeatherButton')
        self.temperatureLabel.setObjectName('temperatureLabel')
        self.weatherEmojiLabel.setObjectName('weatherEmojiLabel')
        self.descriptionLabel.setObjectName('descriptionLabel')
        self.setObjectName('mainWindow')

        # set the style for our window
        self.load_stylesheet("styles.qss")

        # and the cursor for the buttons
        for child in self.findChildren(QPushButton):
            child.setCursor(Qt.PointingHandCursor)

        # finally, let's link the clicked button to the get data method
        self.getWeatherButton.clicked.connect(self.get_data)

    def load_stylesheet(self, path: str):
        with open(path, "r") as f:
            self.setStyleSheet(f.read())

    def get_data(self):
        api_key = "YOUR_API_KEY"
        city = self.cityInput.text()

        result = DataFetcher.get_data(api_key, city)

        if isinstance(result, dict) and result.get("cod") == 200:
            self.display_weather(result, city)
        else:
            # result is an error message string produced by DataFetcher
            self.display_error(str(result))

    def display_error(self, message):
        self.temperatureLabel.setStyleSheet("color: red; font-size: 30px")
        self.temperatureLabel.setText(f"{message}")
        self.weatherEmojiLabel.clear()
        self.descriptionLabel.clear()

    def display_weather(self, data, city):
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        # temperature_f = (temperature_k * 9/5) - 459.67

        weather_id = data["weather"][0]["id"]
        emoji = WeatherFunctions.get_weather_emoji(weather_id)
        description = data["weather"][0]["description"]

        # resets the temperature label that is also used for error messages
        self.temperatureLabel.setStyleSheet("")
        self.temperatureLabel.setText(f"{temperature_c:.0f}℃")

        self.setProperty("weather", emoji[1])
        self.weatherEmojiLabel.setText(emoji[0])

        # re-apply for immediate effect
        self.setProperty("time", "day" if WeatherFunctions.is_daytime() else "night")
        self.style().unpolish(self)
        self.style().polish(self)
        self.update()
        # force the styling on QLabels
        for lab in self.findChildren(QLabel):
            lab.style().unpolish(lab)
            lab.style().polish(lab)
            lab.update()
        self.descriptionLabel.setText(f"{description}")