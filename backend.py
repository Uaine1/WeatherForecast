import requests

API_KEY = "01477f0cba26f5c858c3700ad6e49055"


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    reponse = requests.get(url)
    data = reponse.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]        
    return filtered_data 


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))