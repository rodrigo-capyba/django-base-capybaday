## Arquitetura

- `apps`: aqui devem estar todas as django apps locais que devem ser criadas ao longo do desenvolvimento do projeto. No projeto base esta pasta conterá apenas a app `user`. Para criar uma nova app, deve-se usar o comando *make startapp* na raiz do projeto para criá-la no lugar correto e seguindo o template do projeto base.
- `conf`: módulo que contém arquivos de configuração do projeto.
    - `app_template`: template usado para criação de novas apps. Geralmente, não deve ser alterado.
    - `asgi.py`: arquivo asgi padrão do Django para deploy.
    - `settings`: pasta com os arquivos settings do django. É modularizado de forma a possuir um arquivo de settings para cada ambiente: local, production, etc.
    - `urls.py`: arquivo de urls do projeto. É preferível incluir apenas as urls das outras apps, deixando a configuração específica de cada módulo em seu próprio arquivo urls.py.
    - `wsgi.py`: arquivo wsgi padrão do Django para deploy.
- `requirements`: contém as dependências do projeto, separadas por ambiente (local, production, etc.).
