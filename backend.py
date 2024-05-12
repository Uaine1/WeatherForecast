import requests

API_KEY = "01477f0cba26f5c858c3700ad6e49055"


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
        data = response.json()
        filtered_data = data.get("list", [])  # Use .get() method to handle missing 'list' key

        if forecast_days:
            nr_values = 8 * forecast_days
            filtered_data = filtered_data[:nr_values]
        return filtered_data
    
    except requests.exceptions.RequestException as error:
        print(f"Error fetching data: {error}")
        return None

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))