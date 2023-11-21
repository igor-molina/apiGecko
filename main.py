import requests

url = 'https://api.coingecko.com/api/v3/'


def get_coin_list_id():
    r = requests.get(url+"coins/list")
    list_coins = r.json()
    id_list = [coin['id'] for coin in list_coins[:2]]
    return ",".join(id_list)


def supported_vs_currencies():
    r = requests.get(url+"simple/supported_vs_currencies")
    svc_list = r.json()
    svc_list = svc_list[:2]
    return ",".join(svc_list)


def get_coin_markets(svc, id_list):
    payload = {"vs_currency": svc, "ids": id_list}
    r = requests.get(url + "coins/markets", params=payload)

    try:
        r.raise_for_status()  # Verificar se houve algum erro na requisição
        data = r.json()
        print(data)
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Ocorreu um erro durante a requisição:", err)


svc_string = supported_vs_currencies()
coins_id_list = get_coin_list_id()
get_coin_markets(svc_string, coins_id_list)
