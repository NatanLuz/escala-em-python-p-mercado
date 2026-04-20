[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)]()
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)]()
[![OpenPyXL](https://img.shields.io/badge/OpenPyXL-000000?style=flat&logo=python&logoColor=white)]()
[![Licença MIT](https://img.shields.io/badge/Licen%C3%A7a-MIT-green.svg)](https://opensource.org/licenses/MIT)

# Gerador de Escala de Trabalho Automatizado

## Descrição curta

Aplicação em Python para geração automática de escalas semanais com saída em Excel, orientada por regras de negócio de operação varejista (folga fixa semanal e ciclo de domingos 2x1), executada por CLI e com comportamento determinístico para garantir previsibilidade e reprodutibilidade do resultado.

## Problema resolvido

A montagem manual de escala em redes de supermercados costuma gerar retrabalho, inconsistências entre semanas e baixo controle sobre regras recorrentes de jornada. Esse projeto resolve esse cenário ao transformar um processo operacional sensível em uma rotina automatizada, auditável e repetível.

## Solução proposta

O sistema recebe parâmetros pela linha de comando, calcula a escala com base em datas de início e número de semanas, aplica regras calendáricas fixas e exporta o resultado em formato `.xlsx`. A abordagem elimina decisões manuais na geração: mesmas entradas produzem a mesma escala.

## Funcionalidades

- Geração automática de escala semanal por período configurável.
- Configuração de folga fixa por dia da semana.
- Aplicação automática da regra de domingos no ciclo 2x1.
- Execução por CLI com parâmetros explícitos.
- Exportação direta para planilha Excel (`escala.xlsx`).

## Regras de negócio

1. **Folga fixa semanal**: um dia da semana definido pelo usuário é sempre marcado como folga.
2. **Domingos em ciclo 2x1**: o sistema marca dois domingos consecutivos como trabalho e o terceiro como folga, reiniciando o ciclo na sequência.
3. **Prioridade de regras por data**: para cada data do período, a classificação final (`Trabalho` ou `Folga`) é calculada conforme o calendário da semana e o estado do ciclo dominical.
4. **Cálculo orientado por datas**: a escala é construída por iteração de datas reais (não por posições fixas), o que mantém a consistência em qualquer mês/ano.
5. **Determinismo da geração**: dado o mesmo conjunto de parâmetros (`nome`, `inicio`, `semanas`, `folga`), a saída é invariável e reprodutível.

## Exemplo de uso via CLI

```bash
python "./Projeto_EscalaDeTrabalhov1/main.py" --nome "João" --inicio 2026-01-01 --semanas 4 --folga segunda
```

Parâmetros:

- `--nome`: identificação usada na escala.
- `--inicio`: data inicial no formato `AAAA-MM-DD`.
- `--semanas`: quantidade de semanas a gerar.
- `--folga`: dia fixo da folga semanal.

## Exemplo de saída

| Data       | Dia da Semana | Status   |
| ---------- | ------------- | -------- |
| 2026-01-04 | Domingo       | Trabalho |
| 2026-01-05 | Segunda       | Folga    |
| 2026-01-11 | Domingo       | Trabalho |
| 2026-01-18 | Domingo       | Folga    |

A tabela evidencia duas regras aplicadas em conjunto: folga fixa na segunda-feira e ciclo de domingos 2x1, com alternância previsível e verificável no calendário.

## Stack tecnológica

- **Python**: implementação da lógica de domínio, parsing de argumentos da CLI e cálculo de datas.
- **Pandas**: modelagem tabular da escala, organização dos registros e preparação do dataset para exportação.
- **OpenPyXL**: escrita do arquivo `.xlsx` com compatibilidade nativa com Excel em ambiente corporativo.

## Estrutura do projeto

```text
.
├── Projeto_EscalaDeTrabalhov1/
│   └── main.py
└── escala.xlsx
```

- `Projeto_EscalaDeTrabalhov1/main.py`: ponto de entrada da aplicação e motor de geração da escala.
- `escala.xlsx`: artefato de saída gerado após a execução.

## Instalação e execução

### 1. Clonar o repositório

```bash
git clone https://github.com/archivesysl/escala-em-python-p-mercado.git
cd escala-em-python-p-mercado
```

### 2. Instalar dependências

```bash
pip install pandas openpyxl
```

### 3. Executar a geração da escala

```bash
python "./Projeto_EscalaDeTrabalhov1/main.py" --nome "João" --inicio 2026-01-01 --semanas 4 --folga segunda
```

Execução com parâmetros padrão:

```bash
python "./Projeto_EscalaDeTrabalhov1/main.py"
```

## Diferenciais técnicos

- **Modelagem determinística de regras**: elimina variação manual e facilita auditoria de resultado.
- **Lógica calendárica explícita**: tratamento direto de datas e dias da semana, incluindo regra cíclica para domingos.
- **Operação por CLI**: execução simples em terminal, adequada para uso por liderança operacional sem interface dedicada.
- **Pipeline de saída corporativa**: dados estruturados com Pandas e exportação `.xlsx` via OpenPyXL, prontos para compartilhamento interno.
- **Baixa complexidade operacional**: solução enxuta, com poucas dependências e foco em regra de negócio.

## Possíveis melhorias

- Suporte a múltiplos colaboradores no mesmo ciclo de geração.
- Validação avançada de conflitos de escala e cobertura mínima por dia.
- Geração de múltiplas abas no Excel (por colaborador ou setor).
- Parametrização de feriados e exceções de calendário.

## Autor

**Natan Da Luz**  

Desenvolvedor Backend

Contato: [natandaluz01@gmail.com](mailto:natandaluz01@gmail.com)
