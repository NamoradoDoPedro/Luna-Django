import requests

data = {
    'name': 'John Doe',
    'email': 'johndoe@example.com',
    'age': '25-01-2001',
    'sex': 'Male'
}

response = requests.post(
    'http://127.0.0.1:8000/api/post-users', json=data)

if response.status_code == 200:
    print('Requisição POST bem-sucedida!')
    print(response.json())
else:
    print('Falha na requisição POST!')
    print(response.text)
