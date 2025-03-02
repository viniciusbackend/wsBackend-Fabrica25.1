criar venv e atvar
instalar django, rest_framework e criar no settings do projeto
criar projeto 
criar app dentro do diretório do projeto e criar uma url dentro do app
adicionar uma url default no projeto
criar models e fazer o makemigrations e migrate, criar um superuser e adicionar um model novo sendo admin
criar um serializers para transforma os dados em jsonApi feito pelo desafio da fábrica de sofware, consumindo api do omdb com crud, está api usar protocolo rest, é possivel criar, deletar, alterar e vizualizar usuários e filmes e também criar, deletar, alterar e vizualizar lista de filmes para cada usuário

### Exemplos

Endpoint: http://127.0.0.1:8000/api/filmes/
Descrição: lista todos os filmes criados
Método: GET
Parametros:
Retorno Status: 200 OK

Endpoint: http://127.0.0.1:8000/api/filmes/
Descrição: cria e adiciona o filme na listagem
Método: POST
Parametros: {"titulo": "Avatar"} <---- nome do filme tem que estar igual ao omdb respeitando as letras maiúsculas e minúsculas
Retorno Status: 201 CREATED

Endpoint: http://127.0.0.1:8000/api/filmes/Avatar
Descrição: delete o filme atráves do nome
Método: DELETE
Parametros: {"titulo": "Avatar"} <---- nome do filme tem que estar igual ao omdb respeitando as letras maiúsculas e minúsculas
Retorno Status: 200 OK

Endpoint: http://127.0.0.1:8000/api/usuario/
Descrição:criar usuario
Método: POST
Parametros: {
    "filmes": [],
    "nome": "davi",
    "email": "davi@gmail.com",
    "data_nascimento": "2025-03-02"
}


