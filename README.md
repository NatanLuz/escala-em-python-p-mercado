# Gerador de Escala de Trabalho em Python

Este projeto é um gerador de escala de trabalho automatizado para um funcionário, desenvolvido em Python. Ele cria uma tabela semanal em formato Excel, onde é possível definir a quantidade de semanas, o dia fixo de folga, e implementar uma regra de trabalho no domingo (2 domingos de trabalho e 1 de folga).

## Funcionalidades

- Geração de uma escala de trabalho para múltiplas semanas.
- Folga fixa em um dia específico da semana.
- Regra 2x1 para domingos (2 domingos de trabalho e 1 domingo de folga).
- Exportação da escala gerada para um arquivo Excel.

## Como funciona

O script gera uma escala de trabalho com base nos parâmetros fornecidos:

1. **Nome do funcionário**: O nome do funcionário a quem a escala será aplicada.
2. **Data inicial**: A data inicial a partir da qual a escala começará a ser gerada.
3. **Número de semanas**: Quantidade de semanas que a escala irá cobrir.
4. **Dia fixo de folga**: (Opcional) O dia da semana em que o funcionário terá folga fixa. Por padrão, o dia de folga é segunda-feira.
5. **Regra 2x1 para domingos**: Implementa uma lógica onde o funcionário trabalha dois domingos seguidos e folga no terceiro domingo.

## Como usar

1. **Instalar dependências**:

   Certifique-se de ter o Python instalado e, em seguida, instale as dependências necessárias utilizando o comando:

   ```bash
   pip install pandas openpyxl



Esse README explica como o código funciona, suas funcionalidades, e como executar o script, além de incluir instruções para instalar as dependências. Basta salvar esse conteúdo em um arquivo chamado `README.md` no mesmo diretório do seu projeto.
