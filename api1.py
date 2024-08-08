import requests

'''r = requests.get("https://github.com/timelife/.json") 
print(r.status_code)
print(r.text)'''


'''r = requests.post("http://httpbin.org/pos")
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")'''


'''Passando parâmetros em URLs
Você geralmente quer mandar algum tipo de dado na query string da URL.
Se você estivesse construindo a URL manualmente, este dado seria dado como pares chave/valor na URL após um ponto
de interrogação, por exemplo httpbin.org/get?key=val. Requests permite que você forneça estes argumentos
como um dicionário, usando o argumento params. Por exemplo, se você quisesse passar key1=vaue1 e key2=value2
para httpbin.org/get, você usaria o seguinte código:


payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/ge", params=payload)
print(r.url)
'''


'''r = requests.get("http://httpbin.org/get")

if r.status_code == 200:
    print('Requisição bem-sucedida')
else:
    print(f'Erro na requisição, status code{r.status_code}')'''

'''def get_simples(url):
    r = requests.get(url)
    return r

def get_params(url, params):
    pass

def get_post(url, data):
    pass

url_get = "http://localhost:5000/olamundo"
url_post = "http://localhost:5000/cadastra/usuario"

response = get_simples(url_get)
print(response.text)
print(response.json())'''



'''r = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(r.json())'''

'''post_data = {
    'userId': 3,
    'title': 'Novo Título',
    'body': 'Corpo do novo post',
}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=post_data)
print(response.json())

post_data = {
    'userId': 1,
    'title': 'Novo Título',
    'body': 'Corpo do novo post',
}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=post_data)
print(response.json())'''
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)