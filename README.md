# Exemplo de uma API simples construido com Python-Flask

# Dados iniciais do projeto
- Autor: Francisco Gomes
- Version: 1.0
- Data de deploy: 01/07/2024

## Inicializando o código

![image](https://github.com/ArretadoLabs/API-example-Python/assets/165390931/a24ceaa0-7ed4-484a-ad7a-09515c93b5c8)

## Criando uma lista de dicionário com dados de exemplo
![image](https://github.com/ArretadoLabs/API-example-Python/assets/165390931/3dfeeab7-88eb-4a21-9469-7fe07b2438b0)


# Criando os Endpoints
## Retornando todos os dados
![image](https://github.com/ArretadoLabs/API-example-Python/assets/165390931/0a801730-de64-44f2-b2a5-db21417353b4)

> - @app.route("/books", methods=["GET"])
>> Explicando sobre o endpoint, primeiramente criando a rota usando a anotação "@app.route"
>> E especificando a rota com o nome /books e que recebe como segundo parâmetro que é o método para forçar apenas o método especificado, que nesse caso é aceito apenas GET

# Retornando os dados do livro baseado no "ID"
![image](https://github.com/ArretadoLabs/API-example-Python/assets/165390931/5b84da60-16d0-4866-9965-faed4d884771)

# Realizando uma operação de atualização com o parâmetro "PUT"
![image](https://github.com/ArretadoLabs/API-example-Python/assets/165390931/3b5f44ff-c065-41f1-8da0-b39eea85b0f6)

# Inserindo um novo livro, com a operação POST
![image](https://github.com/ArretadoLabs/API-example-Python/assets/165390931/40e57948-3044-4d88-8e37-d70f63db5a6c)

# Executando a aplicação com as especificações de porta
![image](https://github.com/ArretadoLabs/API-example-Python/assets/165390931/3faef8c0-4852-4380-a85a-11ed5a9201bd)

