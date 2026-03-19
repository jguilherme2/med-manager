import json

ARQUIVO = "data.json"

def carregar():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return []

def salvar(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)

def adicionar(nome, horario):
    dados = carregar()
    dados.append({
        "nome": nome,
        "horario": horario,
        "tomado": False
    })
    salvar(dados)

def listar():
    return carregar()