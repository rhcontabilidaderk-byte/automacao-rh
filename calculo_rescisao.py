from datetime import datetime

def calcular_rescisao(salario_base, data_admissao, data_demissao):
    # Converter datas
    admissao = datetime.strptime(data_admissao, "%d/%m/%Y")
    demissao = datetime.strptime(data_demissao, "%d/%m/%Y")

    # Tempo trabalhado em anos e meses
    tempo_total = demissao - admissao
    anos = tempo_total.days // 365
    meses = (tempo_total.days % 365) // 30

    # 1. Aviso Prévio Indenizado
    aviso_previo_dias = 30 + (anos * 3)
    aviso_previo_dias = min(aviso_previo_dias, 90)  # limite 90 dias
    aviso_previo_valor = (salario_base / 30) * aviso_previo_dias

    # 2. Férias proporcionais + 1/3
    ferias_proporcionais = (salario_base / 12) * meses
    ferias_terco = ferias_proporcionais / 3
    ferias_total = ferias_proporcionais + ferias_terco

    # 3. 13º proporcional
    decimo_terceiro = (salario_base / 12) * meses

    # 4. FGTS (8% do salário por mês trabalhado)
    fgts = (salario_base * 0.08) * ((anos * 12) + meses)

    # 5. Multa de 40% sobre o FGTS
    multa_fgts = fgts * 0.40

    # 6. Resumo total
    total_rescisao = aviso_previo_valor + ferias_total + decimo_terceiro + multa_fgts

    return {
        "Aviso Prévio": round(aviso_previo_valor, 2),
        "Férias + 1/3": round(ferias_total, 2),
        "13º Proporcional": round(decimo_terceiro, 2),
        "FGTS Acumulado": round(fgts, 2),
        "Multa 40% FGTS": round(multa_fgts, 2),
        "Total Rescisão": round(total_rescisao, 2)
    }


# Exemplo de uso
if __name__ == "__main__":
    salario = 3000.00
    admissao = "01/02/2022"
    demissao = "16/08/2025"

    resultado = calcular_rescisao(salario, admissao, demissao)

    print("\n===== Rescisão Calculada =====")
    for item, valor in resultado.items():
        print(f"{item}: R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
