from flask import Flask, Response
import json
import math

app = Flask(__name__)


def is_prime(n):
# Tarkistaa, onko luku alkuluku
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    try:
        luku = int(luku)
        onko_alkuluku = is_prime(luku)

        tilakoodi = 200
        vastaus = {
            "Number": luku,
            "isPrime": onko_alkuluku
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen syöte, anna kokonaisluku"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")


@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
