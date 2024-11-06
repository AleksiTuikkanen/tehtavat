import requests


api_key = "ccc3368ddc259981a0c75688d550ad84"

city_name = input("Enter city name: ")
# Määritellään API-pyynnön URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_key}"

print(url)
try:
    # Lähetetään GET-pyyntö
    vastaus = requests.get(url)

    # Tarkistetaan, onnistuiko pyyntö
    if vastaus.status_code == 200:
        # Muutetaan JSON-vastaus sanakirjaksi
        data = vastaus.json()

        # Tulostetaan lämpötila, joka löytyy "value"-avaimesta
        print(f"Lämpötila on {data['main']['temp']}\u00B0C")
    else:
        print("hakeminen epäonnistui:", vastaus.status_code)

except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa:", e)
