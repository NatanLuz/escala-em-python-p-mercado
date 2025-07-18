#  Gerador de Escala de Trabalho em Python

Este projeto é um **gerador automatizado de escalas de trabalho** desenvolvido em Python, com exportação para Excel. Ele permite criar escalas semanais personalizadas, com regras como **folga fixa semanal** e **regime 2x1 aos domingos** (trabalha dois, folga um).

---

## Sobre o Projeto

Esta ferramenta foi criada como uma **solução personalizada para uma rede de mercados**, em um trabalho **freelance profissional**. O objetivo foi **automatizar a criação de escalas**, reduzindo o tempo manual e eliminando falhas no processo.

A aplicação do projeto gerou resultados visíveis: **aumento da eficiência operacional**, **organização aprimorada da equipe de RH**, e **processos mais ágeis e confiáveis**.

---

##  Funcionalidades

- **Geração de Escala:** Cria escalas semanais/mensais com base em parâmetros configuráveis.
- **Folga Fixa:** Permite selecionar um dia da semana para folga (segunda-feira por padrão).
- **Regra 2x1 para Domingos:** Trabalha dois domingos consecutivos e folga no terceiro.
- **Exportação para Excel:** Gera arquivo `.xlsx` com layout claro e compartilhável.

---

##  Como Funciona ?

O script gera a escala com base em:

- **nome_funcionario:** Nome do funcionário.
- **data_inicial:** Data de início da escala.
- **semanas:** Número de semanas a cobrir.
- **folga_fixa:** Dia fixo de folga (opcional; padrão = segunda-feira).
- **Regra 2x1 para Domingos:** Aplicada automaticamente.

---

## Pré-requisitos

- Python 3
- Bibliotecas:

```bash
pip install pandas openpyxl

Como Usar
Clone o repositório:

git clone https://github.com/archivesysl/escala-em-python-p-mercado.git
cd escala-em-python-p-mercado
Configure os parâmetros no gerador_escala.py:

python:
nome_funcionario = "João"
data_inicial = "2024-10-01"
semanas = 4
Execute o script:

python gerador_escala.py
Verifique o arquivo escala_trabalho.xlsx gerado no mesmo diretório.

 Personalização
nome_funcionario: Mude o nome conforme necessário.

data_inicial: Defina a data de início.

semanas: Ajuste a duração da escala.

folga_fixa: Escolha outro dia para a folga.

A lógica 2x1 para domingos já está incluída.

Tecnologias Usadas
Python 3
Pandas
Openpyxl

Resultados Alcançados

✅ Automação completa das escalas
✅ Eliminação de erros manuais
✅ Facilidade de uso para times não técnicos
✅ Código modular e pronto para novas adaptações

Autor
Natan Da Luz – Desenvolvedor
Contato: natandaluz01@gmail.com

Projeto realizado como trabalho freelance para automatização de processos em uma rede de mercados.

💭 DÚVIDAS
1. Como alterar o dia fixo de folga?
Basta definir folga_fixa = "terca" (ou outro dia) no código.

2. Como funciona a regra 2x1 para domingos?
A cada três semanas: trabalha dois domingos seguidos e folga no terceiro.

mais alguma dúvida ? só me mandar um email hehe.

3. É possível gerar mais de uma escala?
Sim! Chame a função gerar_escala() mais vezes, ajustando o nome e parâmetros para cada funcionário.
