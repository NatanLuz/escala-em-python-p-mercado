import pandas as pd
from datetime import datetime, timedelta

# Função para gerar a escala semanal
def gerar_escala(nome_funcionario, data_inicial, semanas, folga_fixa='segunda'):
    dias_semana = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
    escala = []
    data_atual = datetime.strptime(data_inicial, "%Y-%m-%d")  # Corrigido de 'data atual' para 'data_atual'

    for semana in range(semanas):  # Corrigido de 'semana' para 'semanas'
        for dia in dias_semana:
            if dia == folga_fixa:
                escala.append({'Data': data_atual.strftime("%Y-%m-%d"), 'Dia': dia, 'Status': 'Folga', 'Funcionário': nome_funcionario})
            elif dia == 'domingo':
                # Adicionando a lógica para domingos: 2x1
                if (semana + 1) % 3 == 0:
                    escala.append({'Data': data_atual.strftime("%Y-%m-%d"), 'Dia': dia, 'Status': 'Folga', 'Funcionário': nome_funcionario})
                else:
                    escala.append({'Data': data_atual.strftime("%Y-%m-%d"), 'Dia': dia, 'Status': 'Trabalho', 'Funcionário': nome_funcionario})
            else:
                escala.append({'Data': data_atual.strftime("%Y-%m-%d"), 'Dia': dia, 'Status': 'Trabalho', 'Funcionário': nome_funcionario})
            data_atual += timedelta(days=1)  # Corrigido a indentação

    return escala  # Não estava retornando a escala

# Função para salvar a escala em Excel
def salvar_escala_excel(escala, arquivo_excel):
    df = pd.DataFrame(escala)
    df.to_excel(arquivo_excel, index=False, engine='openpyxl')
    print(f"Escala salva em {arquivo_excel}")  # Corrigido de 'Arquivo_excel' para 'arquivo_excel'

# Parâmetros do projeto
nome_funcionario = "João"
data_inicial = "2024-10-01"  # Data inicial para gerar a escala
semanas = 4  # Quantidade de semanas para gerar a escala

# Gerar e salvar escala
escala = gerar_escala(nome_funcionario, data_inicial, semanas)  # Corrigido o argumento
salvar_escala_excel(escala, "escala_trabalho.xlsx")
