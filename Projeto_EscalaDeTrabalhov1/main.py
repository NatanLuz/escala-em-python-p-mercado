import argparse
from datetime import datetime, timedelta
import pandas as pd


def gerar_escala(nome_funcionario: str, data_inicial: str, semanas: int, folga_fixa: str = "segunda"):
    dias_semana = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
    folga_fixa = folga_fixa.lower()
    if folga_fixa not in dias_semana:
        raise ValueError(f"Dia de folga inválido: {folga_fixa}. Use um de: {', '.join(dias_semana)}")

    escala = []
    data_atual = datetime.strptime(data_inicial, "%Y-%m-%d")

    for semana in range(semanas):
        for dia in dias_semana:
            status = "Trabalho"
            if dia == folga_fixa:
                status = "Folga"
            elif dia == "domingo":
                # Regra 2x1: a cada 3º domingo do ciclo, é folga
                if (semana + 1) % 3 == 0:
                    status = "Folga"

            escala.append({
                "Data": data_atual.strftime("%Y-%m-%d"),
                "Dia": dia,
                "Status": status,
                "Funcionário": nome_funcionario,
            })
            data_atual += timedelta(days=1)

    return escala


def salvar_escala_excel(escala, arquivo_excel: str):
    df = pd.DataFrame(escala)
    df.to_excel(arquivo_excel, index=False, engine="openpyxl")
    print(f"Escala salva em {arquivo_excel}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Gerador de escala de trabalho com exportação para Excel (regra domingo 2x1 e folga fixa)."
    )
    parser.add_argument("--nome", "-n", default="João", help="Nome do funcionário")
    parser.add_argument(
        "--inicio", "-i", default="2024-10-01", help="Data inicial no formato AAAA-MM-DD"
    )
    parser.add_argument("--semanas", "-s", type=int, default=4, help="Quantidade de semanas")
    parser.add_argument(
        "--folga", "-f", default="segunda", help="Dia de folga fixa (segunda, terça, quarta, quinta, sexta, sábado, domingo)"
    )
    # Saída padronizada: arquivo sempre será 'escala.xlsx'
    return parser.parse_args()


def main():
    args = parse_args()

    # Validação simples de data
    try:
        datetime.strptime(args.inicio, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida para --inicio. Use o formato AAAA-MM-DD, por exemplo 2024-10-01.")

    # Validação adicional: semanas devem ser > 0
    if args.semanas <= 0:
        raise ValueError("O parâmetro --semanas deve ser um inteiro maior que 0.")

    # Validação: data de início não pode ser no passado
    hoje = datetime.today().date()
    inicio_date = datetime.strptime(args.inicio, "%Y-%m-%d").date()
    if inicio_date < hoje:
        raise ValueError("A data em --inicio não pode ser no passado.")

    escala = gerar_escala(
        nome_funcionario=args.nome,
        data_inicial=args.inicio,
        semanas=args.semanas,
        folga_fixa=args.folga,
    )
    salvar_escala_excel(escala, "escala.xlsx")


if __name__ == "__main__":
    main()
