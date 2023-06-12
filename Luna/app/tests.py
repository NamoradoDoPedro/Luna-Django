import requests
data = {
    'name': 'Teste request',
    'email': 'johndoe@example.com',
    'age': '2001-05-05',
    'sex': 'Outro'
}

# response = requests.get('http://127.0.0.1:8000/users/')
response = requests.post('http://127.0.0.1:8000/users/', json=data)

if response.ok:
    print('Requisição bem-sucedida!')
    print(response.json())
else:
    print('Falha na requisição!')
    print(response.text)
