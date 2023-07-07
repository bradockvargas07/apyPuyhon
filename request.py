import requests
link = 'https://eadstudium.com.br/api/todosCursos'
requisicao = requests.get(link)

print(requisicao)
print(requisicao.json())
