def obter_previsao_tempo(cidade):
    # Dados fictícios para simular a previsão do tempo
    previsoes = {
        "São Paulo": {"temperatura": 25, "descricao": "céu limpo"},
        "Rio de Janeiro": {"temperatura": 30, "descricao": "ensolarado"},
        "Curitiba": {"temperatura": 18, "descricao": "nublado"},
    }

    if cidade in previsoes:
        dados = previsoes[cidade]
        print(f"Previsão do tempo para {cidade}:")
        print(f"Temperatura: {dados['temperatura']}°C")
        print(f"Descrição: {dados['descricao']}")
    else:
        print(f"Desculpe, não temos dados para a cidade '{cidade}'.")

if __name__ == "__main__":
    cidade = input("Digite o nome da cidade: ")
    obter_previsao_tempo(cidade)
    


