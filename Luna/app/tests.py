import requests

# Definir os dados a serem enviados no corpo da requisição
data = {
    'name': 'John Doe',
    'email': 'johndoe@example.com',
    'age': '25-01-2001',
    'sex': 'Male'
}

# Realizar a requisição POST para o endpoint desejado
response = requests.post(
    'http://127.0.0.1:8000/create-internal-user/', json=data)

# Verificar a resposta da requisição
if response.status_code == 200:
    print('Requisição POST bem-sucedida!')
    print(response.json())
else:
    print('Falha na requisição POST!')
    print(response.text)
