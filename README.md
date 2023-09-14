# Bot do Discord com Lightbulb

Este é um bot do Discord simples construído usando a biblioteca Lightbulb para Python. O bot possui recursos como saudação, piadas, calculadora e consulta de informações de temperatura.

## Pré-requisitos

Antes de começar a usar este bot, você precisará ter o Python instalado em sua máquina. Além disso, é necessário ter as seguintes dependências Python instaladas:

- `lightbulb` (instalado via `pip install hikari-lightbulb`)

## Configurando o Bot

Siga estas etapas para configurar e modificar o bot:

1. Clone este repositório para sua máquina local usando o comando `git clone`.

2. Crie um arquivo `tokens` na pasta raiz do projeto. Neste arquivo, você deve fornecer as seguintes chaves de acesso:
   - `token_ds.txt`: Token do seu bot Discord. Você pode obter esse token criando um novo aplicativo no [Painel de Desenvolvedor do Discord](https://discord.com/developers/applications) e configurando um bot.
   - `api_weather_key.txt`: Sua chave de acesso à API do OpenWeatherMap para obter informações sobre o clima. Você pode obter uma chave acessando [OpenWeatherMap API](https://openweathermap.org/api) e seguindo as instruções de registro.

3. Preencha o arquivo `ds_channel_id.txt` com o ID do canal padrão onde você deseja que o bot esteja habilitado.

4. Personalize o bot conforme suas necessidades. Você pode adicionar mais comandos, personalizar as mensagens e muito mais. Consulte a documentação do [Lightbulb](https://lightbulb-api.readthedocs.io/en/stable/) para obter informações detalhadas sobre como criar comandos personalizados.

5. Após fazer as modificações necessárias, execute o bot usando `python nome_do_seu_bot.py`, onde `nome_do_seu_bot.py` é o nome do arquivo onde o bot está definido.

## Uso

Depois de executar o bot, ele estará online no servidor Discord especificado. Você pode interagir com o bot usando os comandos definidos. Por exemplo, você pode digitar `/msg_kleber` para receber uma saudação do bot.

## Contribuindo

Sinta-se à vontade para contribuir para este projeto aberto. Você pode adicionar novos recursos, corrigir bugs ou melhorar a documentação.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

---

**Aviso**: Não compartilhe suas chaves de acesso à API publicamente. Certifique-se de proteger as informações em `tokens` e não as inclua em seu repositório público no GitHub. Use variáveis de ambiente ou outros métodos seguros para gerenciar essas chaves em produção.

