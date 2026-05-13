import requests


def buscar_medicamento(nome):
    url = f"https://api.fda.gov/drug/label.json?search={nome}&limit=1"

    try:
        resposta = requests.get(url, timeout=5)

        if resposta.status_code == 200:
            return resposta.json()

        return None

    except requests.exceptions.RequestException:
        return None