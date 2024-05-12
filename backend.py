import requests

API_KEY = "01477f0cba26f5c858c3700ad6e49055"


def get_data(place, forecase_day, type):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    reponse = requests.get(url)
    data = reponse.json()

    return data 


if __name__ == "__main__":
    print(get_data())