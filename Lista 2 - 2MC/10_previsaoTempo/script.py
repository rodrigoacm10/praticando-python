import requests

def obter_previsao_tempo(api_key, cidade):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        clima = dados['weather'][0]['description']
        temperatura = dados['main']['temp']
        return f"Condição climática: {clima}\nTemperatura: {temperatura}°C"
    else:
        return "Erro ao obter a previsão do tempo. Verifique a cidade e a chave da API."

def main():
    api_key = "31bf0531b8e053959d6aaca91db1c50c"  # Substitua com a sua chave de API da OpenWeatherMap
    cidade = input("Digite o nome da cidade para obter a previsão do tempo: ")

    previsao = obter_previsao_tempo(api_key, cidade)

    print("\nPrevisão do tempo:")
    print(previsao)

 
main()