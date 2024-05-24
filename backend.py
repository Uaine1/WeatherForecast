import requests

API_KEY = "put your weather api key here"


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        filtered_data = data.get("list", []) 

        if forecast_days:
            nr_values = 8 * forecast_days
            filtered_data = filtered_data[:nr_values]
        return filtered_data
    
    except requests.exceptions.RequestException as error:
        print(f"Error fetching data: {error}")
        return None

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))
