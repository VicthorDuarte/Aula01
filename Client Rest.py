import requests
from requests.auth import HTTPBasicAuth

params = {
    "filtro": "todos",
    "ordem": "desc"
}

payload = {
    "nome": "João",
    "idade": 30
}


jwt_token = None

def get_com_basic(url, user, password):
    resp = requests.get(url, params=params, auth=HTTPBasicAuth(user, password))
    print("GET (Básico):", resp.status_code, resp.json())

def post_com_basic(url, user, password, payload):
    resp = requests.post(url, json=payload, auth=HTTPBasicAuth(user, password))
    print("POST (Básico):", resp.status_code, resp.json())



def obter_jwt(url, user, password):
    credenciais = {
        "usuario": user,
        "senha": password
    }
    resp = requests.post(url, json=credenciais)

    if resp.status_code == 200:
        jwt_token = resp.json().get("token")
        print("JWT Obtido:", jwt_token)
        return jwt_token
    
    else:
        print("Erro ao obter JWT:", resp.status_code, resp.text)


def get_com_jwt(url, token):
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(url, params=params, headers=headers)
    print("GET (JWT):", resp.status_code, resp.json())


def post_com_jwt(url, token, payload):
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.post(url, json=payload, headers=headers)
    print("POST (JWT):", resp.status_code, resp.json())


if __name__ == "__main__":
    BASE_URL = "http://192.168.31.173:5000"
    ENDPOINT = "/login"
    url = BASE_URL + ENDPOINT
    user = "admin"
    password = "senha123"
    jwt = obter_jwt(url, user, password)


    BASE_URL = "http://192.168.31.204:5000"
    ENDPOINT = "/protegida"
    url = BASE_URL + ENDPOINT
    get_com_jwt(url,jwt)