# {{ cookiecutter.project_name }} [![build](https://github.com/{{ cookiecutter.repository_owner }}/{{ cookiecutter.repository_name }}/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/{{ cookiecutter.repository_owner }}/{{ cookiecutter.repository_name }}/actions/workflows/main.yml)

{{ cookiecutter.project_short_description }}

## Como rodar

Se for a primeira vez:
```bash
make setup_install
```

Depois, apenas:
```bash
make up
```

### Opcional

Criar ambiente virtual:
```bash
make setup_venv
```

Rodar seed do banco:
```bash
make seed
```

## Arquitetura

- `apps`: aqui devem estar todas as django apps locais que devem ser criadas ao longo do desenvolvimento do projeto.{%- if cookiecutter.user_app|lower == 'y' %} No projeto base esta pasta conterá apenas a app `user`.{%- endif %} Para criar uma nova app, deve-se usar o comando *make startapp* na raiz do projeto para criá-la no lugar correto e seguindo o template do projeto base.
- `conf`: módulo que contém arquivos de configuração do projeto.
    - `app_template`: template usado para criação de novas apps. Geralmente, não deve ser alterado.
    - `asgi.py`: arquivo asgi padrão do Django para deploy.
    - `settings`: pasta com os arquivos settings do django. É modularizado de forma a possuir um arquivo de settings para cada ambiente: local, production, etc.
    - `urls.py`: arquivo de urls do projeto. É preferível incluir apenas as urls das outras apps, deixando a configuração específica de cada módulo em seu próprio arquivo urls.py.
    - `wsgi.py`: arquivo wsgi padrão do Django para deploy.
- `requirements`: contém as dependências do projeto, separadas por ambiente (local, production, etc.).
- `scripts`: contém shell scripts úteis para o projeto.
- `env.example`: arquivo env de exemplo para iniciar o projeto. Deve ser copiado para um arquivo `.env` (não versionado).
- `docker-compose.yml` e `Dockerfile`: arquivos de configuração Docker.
- `Makefile`: contém comandos úteis, como por exemplo entrar num container ou criar uma app.

## Testes unitários

Utilizamos a biblioteca **pytest** para rodar testes unitários. Seu arquivo de configuração é *pytest.ini*.

- Para rodas os testes, usar o comando `make test`.

Como por padrão os testes reutilizam o banco de dados gerado, caso tenha novas migrações é necessário re-criar o banco.

- Para re-criar o banco, usar o comando `make test_create_db`.

## Comandos úteis

### Criar uma app

`make startapp [app_name]`

### Entrar em um container

`make enter [service_name]`

### Abrir o django shell

`make shell`
