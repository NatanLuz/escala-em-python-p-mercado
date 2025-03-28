## Gerador de Escala de Trabalho em Python

Este projeto é um gerador automatizado de escala de trabalho para funcionários, desenvolvido em Python. O sistema permite a criação de escalas semanais em formato Excel, com a opção de configurar o dia fixo de folga e aplicar uma regra de trabalho para os domingos (2 domingos de trabalho e 1 domingo de folga).

##  Funcionalidades

- **Geração de Escala de Trabalho**: Cria a escala para múltiplas semanas com base nos parâmetros fornecidos.
- **Folga Fixa**: Define um dia fixo da semana para a folga (por padrão, segunda-feira).
- **Regra 2x1 para Domingos**: Implementa a regra onde o funcionário trabalha dois domingos seguidos e folga no terceiro.
- **Exportação para Excel**: A escala gerada é exportada para um arquivo Excel, facilitando a visualização e controle.
  
##  Como funciona

O script gera uma escala de trabalho com base nos seguintes parâmetros:

1. **Nome do Funcionário**: Define o nome do funcionário para quem a escala será gerada.
2. **Data Inicial**: Define a data inicial a partir da qual a escala começará.
3. **Número de Semanas**: Especifica quantas semanas a escala vai cobrir.
4. **Dia Fixo de Folga**: (Opcional) Define o dia fixo da semana em que o funcionário terá folga. O valor padrão é segunda-feira.
5. **Regra 2x1 para Domingos**: A regra aplica-se aos domingos, onde o funcionário trabalhará dois domingos seguidos e terá folga no terceiro domingo.

##  Pré-requisitos

Certifique-se de que você tenha o Python instalado no seu sistema, bem como as seguintes bibliotecas:

- **pandas**: Para manipulação de dados e exportação para Excel.
- **openpyxl**: Para salvar o arquivo Excel com os dados da escala.

Para instalar as dependências, utilize o seguinte comando:

```bash
pip install pandas openpyxl

Como usar:

Clone o repositório abaixo

git clone https://github.com/archivesysl/escala-em-python-p-mercado.git

Navegue até o diretório do projeto:

cd escala-em-python-p-mercado

Abra o script gerador_escala.py no seu editor de código preferido e edite os parâmetros conforme necessário:

nome_funcionario = "João"  # Nome do funcionário
data_inicial = "2024-10-01"  # Data inicial para gerar a escala
semanas = 4  # Quantidade de semanas para gerar a escala

Execute o script:

python gerador_escala.py

Isso irá gerar a escala e salvar o arquivo escala_trabalho.xlsx no mesmo diretório.

 Exportação para Excel
A escala de trabalho será salva em um arquivo Excel chamado escala_trabalho.xlsx. O arquivo terá as seguintes colunas:

Data: A data específica de cada dia de trabalho.
Dia: O dia da semana correspondente (segunda, terça, etc.).
Status: Indica se o dia é de Trabalho ou Folga.
Funcionário: Nome do funcionário para quem a escala foi gerada.

Personalização
Você pode personalizar a geração da escala alterando os seguintes parâmetros no código:

Nome do Funcionário: Altere o nome para o funcionário desejado.

Data Inicial: Defina a data inicial para o início da escala.

Número de Semanas: Especifique o número de semanas que você deseja para a escala.

Dia Fixo de Folga: Caso queira alterar o dia fixo de folga, basta definir outro dia da semana (por padrão, é segunda-feira).

Regra 2x1 para Domingos: Essa regra já está implementada, onde o funcionário trabalha dois domingos seguidos e folga no terceiro.

Tecnologias Usadas
Este projeto foi desenvolvido utilizando as seguintes tecnologias:
Python 3
Pandas (para manipulação de dados e exportação para Excel)
Openpyxl (para gerar e salvar o arquivo Excel)

Autor
Natan Da Luz - Desenvolvedor - @archivesysl

💭 FAQ - Perguntas Frequentes
1. Como posso personalizar o dia fixo de folga?
Você pode alterar a variável folga_fixa para o dia da semana que preferir. O valor padrão é segunda.

2. Como funciona a regra 2x1 para os domingos?
A cada três semanas, o funcionário trabalha dois domingos seguidos e folga no terceiro domingo.

3. Como faço para gerar uma escala para mais de uma pessoa?
Para gerar escalas para outros funcionários, basta chamar a função gerar_escala novamente com o nome de outro funcionário e os parâmetros desejados.

Contato para mais info: natandaluz01@gmail.com
