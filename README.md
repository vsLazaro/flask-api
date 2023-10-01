# FLASK API

Para conseguir rodar a aplicação basta seguir o passo a passo abaixo

#### 1 - Instalando o ambiente conda

- No caminho `/api/enviroment.yml` encontra-se o arquivo para importação do ambiente conda 
- Basta acessar o aplicativo anaconda e ir em **Environments**, logo após na aba importar e selecionar o arquivo indicado acima.
- Após isso basta você estar no ambiente conda que foi criado para rodar a api

#### 2 - Subindo o docker

- Estando na raiz do projeto e tendo docker instalado basta rodar `docker compose up -d` para subir o banco de dados.

#### 3 - Inserindo dados no banco

- Com o docker up você deve digitar no terminal `docker ps`, isso irá listar seus containers, assim você pode visualizar o id do container nomeado **mysql-coleta**
- Copie o id desse container
- No terminal na raiz do projeto rode o comando `docker exec -i ID_CONTAINER mysql -uroot -pexample  < crashes.sql`
- Após finalizar essa etapa o banco estará completo

#### 4 - Subindo a aplicação:
- Para subir a aplicação basta ir no diretorio `api/` e executar o comando `flask run`, isso irá executar a api provavelmente na porta 5000
- Também foi disponibilizado a collection do postman para consumir a API, você pode importar ela, ela esta na raiz do projeto com nome collection_api.json
