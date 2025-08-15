import requests

class DataFetcher():
    @staticmethod
    def get_data(api_key, city_name):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        try:
            response = requests.get(url, timeout=10)
            data = response.json()
            if data["cod"] == 200:
                return data
            else:
                raise requests.exceptions.HTTPError
        except requests.exceptions.HTTPError as e:
            match response.status_code:
                case 400:
                    return f"Error {response.status_code}\nBad Request\n Check your input"
                case 401:
                    return f"Error {response.status_code}\nUnauthorized\n Check your input"
                case 403:
                    return f"Error {response.status_code}\nForbidden\n Check your input"
                case 404:
                    return f"Error {response.status_code}\nNot Found"
                case 500:
                    return f"Error {response.status_code}\nInternal Server Error"
                case 502:
                    return f"Error {response.status_code}\nBad Gateway"
                case 503:
                    return f"Error {response.status_code}\nService Unavailable"
                case 504:
                    return f"Error {response.status_code}\nGateway Timeout"
                case _:
                    return f"HTTP error occured:\n {e}"
        except requests.exceptions.ConnectionError:
            return "Connection Error\n Check \ninternet connection"
        except requests.exceptions.Timeout:
            return "Timeout Error\n The request \ntook too long"
        except requests.exceptions.TooManyRedirects:
            return "Too many redirects\n Check the URL"
        except requests.exceptions.RequestException as e:
            return f"Error: {e}"