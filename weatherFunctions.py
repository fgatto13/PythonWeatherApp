from datetime import datetime

class WeatherFunctions():
    @staticmethod
    def get_weather_emoji(weather_id) -> tuple[str, str] | None:
        day = WeatherFunctions.is_daytime()
        match weather_id:
            # Thunderstorm
            case 200 | 230:  # thunderstorm w/ light rain
                return "⛈️", "Thunderstorm"
            case 201 | 231:  # thunderstorm w/ rain
                return "🌩️", "Thunderstorm"
            case 202 | 232:  # thunderstorm w/ heavy rain
                return "🌪️", "Thunderstorm"
            case 210 | 211:  # light/moderate thunderstorm
                return "🌩", "Thunderstorm"
            case 212 | 221:  # heavy or ragged thunderstorm
                return "🌩🔥", "Thunderstorm"

            # Drizzle
            case 300 | 310:
                return "🌦️", "Drizzle"
            case 301 | 311 | 321:
                return "🌧", "Drizzle"
            case 302 | 312:
                return "🌧️💧", "Drizzle"
            case 313 | 314:
                return "💦", "Drizzle"

            # Rain
            case 500:
                return "🌦", "Rain"
            case 501:
                return "🌧", "Rain"
            case 502 | 503:
                return "🌧️💦", "Rain"
            case 504:
                return "🌊", "Rain"
            case 511:
                return "🌧️❄️", "Rain"
            case 520:
                return "🌦", "Rain"
            case 521:
                return "🌧", "Rain"
            case 522 | 531:
                return "🌧️💦", "Rain"

            # Snow
            case 600:
                return "🌨️", "Snow"
            case 601:
                return "❄️", "Snow"
            case 602:
                return "❄️❄️", "Snow"
            case 611 | 612:
                return "🌨️💧", "Snow"
            case 613:
                return "🌨️💦", "Snow"
            case 615 | 616:
                return "🌧️❄️", "Snow"
            case 620:
                return "🌨️", "Snow"
            case 621:
                return "🌨️❄️", "Snow"
            case 622:
                return "❄️❄️💦", "Snow"

            # Atmosphere
            case 701:
                return "🌫️", "Atmosphere"
            case 711:
                return "💨", "Atmosphere"
            case 721:
                return "🌁", "Atmosphere"
            case 731 | 751 | 761:
                return "🏜️", "Atmosphere"
            case 741:
                return "🌫️", "Atmosphere"
            case 762:
                return "🌋", "Atmosphere"
            case 771:
                return "💨🌊", "Atmosphere"
            case 781:
                return "🌪️", "Atmosphere"

            # Clear (day/night)
            case 800:
                return ("☀️" if day else "🌙"), "Clear"

            # Clouds (day/night)
            case 801:
                return ("🌤️" if day else "🌤️🌙"), "Clouds"
            case 802:
                return ("⛅" if day else "☁️🌙"), "Clouds"
            case 803:
                return ("🌥️" if day else "☁️🌙"), "Clouds"
            case 804:
                return "☁️", "Clouds"

            case _:
                return None, None

    @staticmethod
    def is_daytime():
        hour = datetime.now().hour
        return 6 <= hour < 18  # daytime between 6:00 and 17:59