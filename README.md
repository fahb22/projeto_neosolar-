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

## Manutenção
Estrutura do Projeto
A estrutura do projeto é organizada em três componentes principais:

Model (Modelo): Gerencia os dados e a lógica de negócios.
View (Visão): Gerencia a apresentação dos dados.
Controller (Controlador): Gerencia a interação entre o modelo e a visão.
Main: Ponto de entrada do script.





Componentes
1. Model (Modelo)
Localização: models/product_model.py

Responsabilidade:

Gerenciar dados dos produtos e a lógica de negócios para criar geradores solares.
Funções Principais:

__init__(): Inicializa a lista de produtos e o DataFrame.
criar_geradores(): Cria e retorna a lista de geradores solares com base nas regras de compatibilidade de potência.
Manutenção:

Adicionar Novos Produtos: Edite a lista de produtos no método __init__.
Alterar Regras de Configuração: Ajuste a lógica no método criar_geradores().

2. View (Visão)
Localização: views/report_view.py

Responsabilidade:

Gerenciar a apresentação dos dados e gerar relatórios em CSV e PDF.
Funções Principais:

gerar_csv(geradores): Gera um arquivo CSV com os detalhes dos geradores.
gerar_pdf(geradores): Gera um arquivo PDF com um relatório dos geradores.
Manutenção:

Modificar Relatórios: Ajuste os métodos gerar_csv() e gerar_pdf() para alterar o formato dos relatórios.


3. Controller (Controlador)
Localização: controllers/generator_controller.py

Responsabilidade:

Gerenciar a interação entre o modelo e a visão, coordenando o processo de criação de geradores e geração de relatórios.
Funções Principais:

__init__(): Inicializa o modelo e a visão.
run(): Cria geradores e gera os arquivos de relatório.
Manutenção:

Adicionar Funcionalidades: Modifique o método run() para incluir novas funcionalidades ou alterar o fluxo existente.


4. Main
Localização: main.py

Responsabilidade:

Ponto de entrada do script. Inicializa o controlador e inicia o processo de execução.
Manutenção:

Alterações no Main: Normalmente não requer alterações, a menos que haja mudanças significativas na estrutura do controlador.

Instruções de Manutenção
Adicionar Novos Produtos
Edite o Modelo:
Adicione novos produtos à lista de produtos em ProductModel.__init__().
Atualize a Lógica de Configuração:
Certifique-se de que a nova configuração está contemplada na lógica do método criar_geradores().
Alterar Regras de Configuração
Modifique a Lógica no Modelo:
Atualize o método criar_geradores() para refletir as novas regras de compatibilidade.
Verifique os Resultados:
Execute o código para garantir que os geradores estão sendo configurados corretamente de acordo com as novas regras.
Modificar Relatórios
Edite a Visão:
Ajuste os métodos gerar_csv() e gerar_pdf() em ReportView para alterar o formato dos relatórios.
Teste os Relatórios:
Execute o script para verificar se os relatórios estão sendo gerados conforme esperado.
Adicionar Novas Funcionalidades
Atualize o Controlador:
Adicione ou ajuste funcionalidades no método run() do GeneratorController.
Garanta a Coerência:
Verifique a integração entre o modelo e a visão para garantir que a nova funcionalidade está funcionando corretamente.

# projeto_neosolar-
