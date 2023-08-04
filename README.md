# Django Base Capyba Day 2023 [![build](https://github.com/rodrigo-capyba/django-base-capybaday/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/rodrigo-capyba/django-base-capybaday/actions/workflows/main.yml)

O objetivo deste projeto é fornecer uma base de código Django que servirá como passo inicial para novos projetos de backend em que se opte pela tecnologia Python/Django. Os princípios que devem guiar o projeto são:

1. Fornecer o máximo possível de bibliotecas e funcionalidades básicas de toda aplicação web backend. 
2. Fazer o mínimo possível de suposições sobre a aplicação, mantendo-se sempre generalista.
3. Encorajar um modelo de arquitetura e estilo de código que seja adaptável, extensível e siga as boas práticas de padrões de projeto.
4. Preparar uma mecânica de geração de código que possibilite ao desenvolvedor instanciar o Django Base e escolher as funcionalidades que ele deseja para iniciar um novo projeto.

## Como começar um projeto

1. Instalar o **cookiecutter**, seguir as instruções de instalação na [documentação](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html):

2. Gerar o projeto a partir do template Django Base (adicionar `--checkout nome-da-branch` para usar branch específica):
```bash
cookiecutter git@github.com:rodrigo-capyba/django-base-capybaday.git
```

3. Configurar as variáveis pedidas pelo cookiecutter conforme desejado para o projeto (*project_name*, *project_slug*, etc.). Cada variável está descrita abaixo:

- **project_name**: Nome do projeto. Aparecerá, por exemplo, no README e na documentação.
- **project_slug**: Nome "programático" do projeto. Será o nome da pasta raiz, por exemplo.
- **project_short_description**: Descrição sucinta do projeto. Aparecerá, por exemplo, no README e na documentação.
- **repository_owner**: Nome de usuário criador do repositório em que o projeto será versionado.
- **repository_name**: Nome do repositório em que o projeto será versionado.
- **user_app**: Responder 'y' se deseja adicionar a app de usuário customizada do Django.

## Como desenvolver

Por ser este um projeto Cookiecutter, o desenvolvimento é um pouco diferente do usual, já que o código-fonte do projeto na verdade é um template de código-fonte. Normalmente, o desenvolvimento segue da seguinte forma:

1. Clonar o código-fonte do projeto (se ainda não o fez).
2. Na pasta do projeto clonado, gerar o código base localmente com o comando `cookiecutter .`
    1. A escolha das configurações deve ser feita de acordo com o que se deseja desenvolver.
3. Realizar as mudanças no projeto gerado (dentro da pasta _project-name_, se gerado com as configurações padrão).
4. Quando finalizar as mudanças desejadas, refleti-las no projeto template e submetê-las para revisão*.
    1. Antes de submeter as mudanças é importante testar o que foi feito, repetindo o passo 2 e rodando os testes no projeto gerado. 

Caso a mudança a ser feita seja muito pequena, o passo 3 pode ser pulado e o código pode ser modificado direto no template. Fica a critério do desenvolvedor decidir se é mais cômodo programar direto no template, mas precisando gerar sempre um novo projeto para testar o que foi feito; ou programar no projeto gerado, funcional e testável, mas que não será submetido, precisando portanto refletir as mudanças no template para serem submetidas.

## Como testar

Utilizamos a biblioteca **pytest** para rodar testes unitários. Seu arquivo de configuração é *pytest.ini*.

Para rodas os testes, é necessário ter o [pytest-cookies](https://pytest-cookies.readthedocs.io/en/latest/) instalado: `pip install requirements.txt` e depois simplesmente rodar `pytest`.

Os testes do projeto consistem em simular a geração do projeto usando cookiecutter e testar o que foi criado.

**OBS:** O projeto gerado tem a sua própria suíte de testes. Esses testes não são rodados dentro do teste do *template cookiecutter*.

## Deploy

Uma branch de *deploy* será mantida neste repositório para representar a versão gerada do template, com todas as opções default do cookiecutter. O intuito é testarmos a build, cobertura de código e deploy de um projeto genérico gerado a partir do base em sua configuração padrão.

Para atualizar a branch *deploy* com versão mais recente do template:

```bash
git checkout deploy
cd ..
cookiecutter -f git@github.com:rodrigo-capyba/django-base-capybaday.git --no-input
cd django-base-capybaday
```

Dessa forma, se poderá ver no git o que foi modificado na nova versão do template e assim fazer um commit em *deploy* com as mudanças.
