[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)]()
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)]()
[![OpenPyXL](https://img.shields.io/badge/OpenPyXL-000000?style=flat&logo=python&logoColor=white)]()
[![Licença MIT](https://img.shields.io/badge/Licen%C3%A7a-MIT-green.svg)](https://opensource.org/licenses/MIT)

# Gerador de Escala de Trabalho Automatizado

Automação de escalas semanais com regras de negócio reais e exportação para Excel.

## Sobre o Projeto 📌

Este projeto foi desenvolvido para resolver um problema recorrente em operações de varejo: a montagem manual de escalas semanais, que consome tempo e aumenta a chance de erros operacionais.

A solução automatiza a geração de escalas de trabalho com base em regras reais utilizadas em supermercados, garantindo previsibilidade, padronização, eficiência, confiabilidade e escalabilidade. O resultado é uma rotina mais eficiente para liderança e RH, com saída pronta para compartilhamento em Excel.

## Funcionalidades ⚙️

- Geração automática de escala semanal
- Definição de folga fixa por dia da semana (ex.: segunda-feira)
- Regra de domingos no formato 2x1 (trabalha dois, folga no terceiro)
- Configuração por linha de comando (CLI)
- Exportação automática para arquivo `.xlsx`

## Prévia 🖼️

Imagem ilustrativa da escala gerada:

![Previa do Gerador de Escala](https://i.imgur.com/LrlI6FJ.png)

## Regras de Negócio 🧠

As regras implementadas refletem cenários reais de operação:

1. Um dia fixo da semana é sempre marcado como folga.
2. Os domingos seguem um ciclo 2x1:
   - 1º domingo: trabalho
   - 2º domingo: trabalho
   - 3º domingo: folga
3. A escala é construída por manipulação de datas, permitindo geração contínua por semanas.
4. A lógica de geração é determinística: para a mesma entrada de parâmetros, a saída da escala permanece consistente.

## Tecnologias 💻

- **Python:** linguagem principal para implementar as regras de negócio, validação de parâmetros da CLI e manipulação de datas para montagem da escala.
- **Pandas:** organização dos dados em formato tabular, facilitando o processamento da escala e a preparação da estrutura final de saída.
- **OpenPyXL:** engine utilizada para gravar a planilha `.xlsx`, garantindo compatibilidade com o ambiente corporativo (Excel).

## Estrutura do Projeto 🗂️

- `Projeto_EscalaDeTrabalhov1/main.py`: script principal de geração da escala
- `escala.xlsx`: arquivo de saída gerado automaticamente

## Como Executar ▶️

### 1) Clonar o repositório

```bash
git clone https://github.com/archivesysl/escala-em-python-p-mercado.git
cd escala-em-python-p-mercado
```

### 2) Instalar dependências

```bash
pip install pandas openpyxl
```

### 3) Executar o script principal

Exemplo completo com parâmetros opcionais:

```bash
python "./Projeto_EscalaDeTrabalhov1/main.py" --nome "João" --inicio 2026-01-01 --semanas 4 --folga segunda
```

Parâmetros disponíveis:

- `--nome`
- `--inicio` (formato `AAAA-MM-DD`)
- `--semanas`
- `--folga`

Também é possível executar com valores padrão:

```bash
python "./Projeto_EscalaDeTrabalhov1/main.py"
```

## Saída Gerada 📄

Após a execução, o arquivo `escala.xlsx` é criado automaticamente na raiz do projeto.

Trecho ilustrativo da planilha gerada:

| Data       | Dia da Semana | Status   |
| ---------- | ------------- | -------- |
| 2026-01-04 | Domingo       | Trabalho |
| 2026-01-05 | Segunda       | Folga    |
| 2026-01-11 | Domingo       | Trabalho |
| 2026-01-18 | Domingo       | Folga    |

## Contexto Profissional 🏢

Projeto desenvolvido como solução prática freelance para automação de escala em uma rede de supermercados. O objetivo foi transformar uma atividade manual e suscetível a inconsistências em um processo reprodutível, auditável e de fácil operação e manutenção.

## Autor 👤

**Natan Da Luz**  
Contato: [natandaluz01@gmail.com](mailto:natandaluz01@gmail.com)
