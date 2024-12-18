import requests

# Määritellään API-pyynnön URL
url = "https://api.chucknorris.io/jokes/random"

try:
    # Lähetetään GET-pyyntö
    vastaus = requests.get(url)

    # Tarkistetaan, onnistuiko pyyntö
    if vastaus.status_code == 200:
        # Muutetaan JSON-vastaus sanakirjaksi
        data = vastaus.json()

        # Tulostetaan vitsi, joka löytyy "value"-avaimesta
        print(data["value"])
    else:
        print("Vitsin hakeminen epäonnistui:", vastaus.status_code)

except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa:", e)


