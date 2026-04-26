[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)]()
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)]()
[![OpenPyXL](https://img.shields.io/badge/OpenPyXL-000000?style=flat&logo=python&logoColor=white)]()

# 📊 Gerador de Escala de Trabalho

Aplicação em Python para geração automática de escalas de trabalho semanais, com exportação para Excel (`.xlsx`).

Projeto desenvolvido com foco em automação de processos reais utilizados em ambiente de supermercado.

---

## 🚀 Visão Geral

Este sistema permite gerar escalas de trabalho de forma simples e automatizada, seguindo regras comuns do mercado:

- ✔ Folga semanal fixa (configurável)
- ✔ Regra de domingo 2x1 (trabalha dois domingos e folga no terceiro)
- ✔ Geração automática de períodos
- ✔ Exportação para Excel pronta para uso

---

## 🖼️ Prévia do Projeto

<p align="center">
  <img src="escaladetrabalho.PNG" alt="Gerador de Escala" width="700"/>
</p>

---

## 📁 Estrutura do Projeto

```text
Projeto_EscalaDeTrabalhov1/
│
├── main.py                 # Script principal
├── escaladetrabalho.PNG    # Imagem de preview
├── README.md               # Documentação
├── requirements.txt        # Dependências
└── escala.xlsx             # Arquivo gerado (após execução)
```

---

## ⚙️ Pré-requisitos

- Python 3.9 ou superior
- pip instalado

### Bibliotecas utilizadas

- pandas
- openpyxl

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/archivesysl/escala-em-python-p-mercado.git
cd escala-em-python-p-mercado
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Ou manualmente:

```bash
pip install pandas openpyxl
```

---

## ▶️ Como Executar

Execução com parâmetros personalizados:

```bash
python "./Projeto_EscalaDeTrabalhov1/main.py" \
--nome "João" \
--inicio 2026-01-01 \
--semanas 4 \
--folga segunda
```

Execução padrão:

```bash
python "./Projeto_EscalaDeTrabalhov1/main.py"
```

---

## 📄 Saída

Após a execução, será gerado automaticamente:

```text
escala.xlsx
```

Arquivo pronto para:

- Compartilhamento
- Impressão
- Uso operacional

---

## 🧠 Como Funciona

O sistema gera uma sequência de datas e aplica regras:

- 📅 Folga fixa: define um dia da semana como folga recorrente
- 🔁 Regra 2x1 domingos:
  - Trabalha 2 domingos consecutivos
  - Folga no 3º domingo
- 📤 Exportação:
  - Utiliza openpyxl para gerar o Excel

---

## ⚡ Personalização Rápida

Você pode ajustar facilmente:

| Parâmetro | Descrição | Exemplo |
| --- | --- | --- |
| `--nome` | Nome do funcionário | `João` |
| `--inicio` | Data inicial | `2026-01-01` |
| `--semanas` | Quantidade de semanas | `4` |
| `--folga` | Dia de folga fixa | `segunda` |

---

## 🛠️ Solução de Problemas

Erro: ModuleNotFoundError

```bash
pip install -r requirements.txt
```

Python não reconhecido:

```bash
py -3
```

Ou adicione ao PATH.

Erro de permissão no Windows:

- Execute PowerShell como administrador

---

## 🧩 Tecnologias

- Python
- Pandas
- OpenPyXL

---

## 📌 Melhorias Futuras

- Interface gráfica (GUI)
- Exportação para PDF
- API para integração com sistemas
- Dashboard web

---

## 👨‍💻 Autor

Natan Da Luz
Desenvolvedor Backend

📧 natandaluz01@gmail.com

---

## 📄 Licença

Este projeto é de uso livre para fins de estudo e melhoria.
