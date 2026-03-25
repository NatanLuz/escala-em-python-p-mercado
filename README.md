[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)]()
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)]()
[![OpenPyXL](https://img.shields.io/badge/OpenPyXL-000000?style=flat&logo=python&logoColor=white)]()

## Leia abaixo sobre o Projeto 👇🏻

Este projeto é um gerador de escala de trabalho SIMPLES, porém automático em Python, com exportação para Excel. Ele cria escalas semanais configuráveis, incluindo:

- Folga semanal fixa (padrão: segunda-feira)
- Regra de domingo 2x1 (trabalha dois domingos e folga no terceiro)
- Exportação para `.xlsx` com layout simples e compartilhável

Prévia:
![Gerador de Escala](https://i.imgur.com/LrlI6FJ.png)

## Estrutura do Projeto

- Script principal: veja [Projeto_EscalaDeTrabalhov1/main.py](Projeto_EscalaDeTrabalhov1/main.py)
- Saída esperada: `escala.xlsx` gerado na raiz do projeto

## Pré-requisitos para rodar na máquina

- Python 3.9+ (Windows, macOS ou Linux)
- Bibliotecas Python:
  - `pandas`
  - `openpyxl`

Instale as dependências (Windows/PowerShell):

```powershell
pip install -r requirements.txt
```

Caso não queira usar `requirements.txt`, instale diretamente:

```powershell
pip install pandas openpyxl
```

## Como Executar (Windows)

1. Clone o repositório:

```powershell
git clone https://github.com/archivesysl/escala-em-python-p-mercado.git
cd escala-em-python-p-mercado
```

2. Opcional: crie um ambiente virtual e instale dependências:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

3. Executar via CLI (recomendado):

```powershell
python ".\Projeto_EscalaDeTrabalhov1\main.py" --nome "João" --inicio 2026-01-01 --semanas 4 --folga segunda
```

Se preferir usar valores padrão, basta:

```powershell
python ".\Projeto_EscalaDeTrabalhov1\main.py"
```

4. Execute e verifique o resultado:

```powershell
python ".\Projeto_EscalaDeTrabalhov1\main.py"
```

5. Verifique o arquivo `escala.xlsx` gerado na pasta do projeto.

## Como Funciona

O script cria uma lista com todos os dias, marcando `Trabalho` ou `Folga` conforme regras:

- `folga_fixa`: o dia da semana escolhido fica como `Folga` toda semana
- Domingos seguem 2x1: no 3º domingo de cada ciclo, marca `Folga`
- Exportação: os dados são salvos em `escala.xlsx` usando `openpyxl`

## Personalização Rápida

- Alterar nome: mude `nome_funcionario`
- Alterar início: mude `data_inicial` (formato `AAAA-MM-DD`)
- Duração: ajuste `semanas`
- Dia de folga: mude `folga_fixa` para `"terça"`, `"quarta"`, etc.

## Solução de Problemas

- Erro `ModuleNotFoundError`: instale dependências com `pip install -r requirements.txt`
- `python` não é reconhecido: use `py -3` ou instale Python no PATH
- Permissão ao ativar `.venv`: execute o PowerShell como administrador ou ajuste a política de execução

## Tecnologias

- Python, Pandas, OpenPyXL

## Autor

Natan Da Luz – Developer
Contato: natandaluz01@gmail.com

Projeto desenvolvido como trabalho freelance para automação de processos em uma rede de supermercado.
