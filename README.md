# Documentação do Script de Automação

## Descrição Geral
Este script automatiza o processo de criação de geradores solares para a Neosolar. Ele realiza as seguintes etapas:
1. Carrega os dados dos produtos disponíveis em estoque.
2. Configura os geradores de acordo com as instruções de compatibilidade de potência.
3. Gera um arquivo CSV com os detalhes dos geradores configurados.
4. Gera um arquivo PDF com a mensagem de e-mail para o time de marketing.

## Passo a Passo

### Carregamento dos Dados
Os dados dos produtos foram carregados em um DataFrame do pandas a partir de uma lista de dicionários.

### Configuração dos Geradores
Os geradores foram configurados seguindo as regras do Anexo B. Cada gerador foi composto por:
- Um ou mais painéis solares da mesma marca e potência.
- Um inversor de corrente com potência igual à dos painéis solares.
- Um controlador de carga com potência igual à dos painéis solares.

### Geração do Arquivo CSV
O arquivo CSV foi gerado com os detalhes dos geradores configurados, incluindo ID do gerador, potência do gerador, IDs dos produtos componentes, nomes dos produtos e quantidade de cada item.

### Geração do Arquivo PDF
O arquivo PDF foi gerado com a mensagem de e-mail para o time de marketing, informando o número de geradores configurados na semana e anexando a tabela de geradores.

## Instruções de Uso
Para executar o script, certifique-se de ter as bibliotecas pandas e fpdf instaladas. Em seguida, execute o script em um ambiente Python. Os arquivos `geradores_configurados.csv` e `email_marketing.pdf` serão gerados no diretório atual.
