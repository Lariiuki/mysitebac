# Importando bibliotecas necessárias
import numpy as np

print("< Montante final >")
# Definição dos investimentos
investimentos = [
    {"nome": "Opção 1", "taxa": 1.2805 * 10.65 / 100 + 0.042, "vencimento": "10/04/2027"},
    {"nome": "Opção 2", "taxa": 1.214 * 10.65 / 100 + 0.0335, "vencimento": "10/04/2026"},
    {"nome": "Opção 3", "taxa": 1.1988 * 10.65 / 100 + 0.03, "vencimento": "15/10/2026"},
    {"nome": "Opção 4", "taxa": 16.50 / 100, "vencimento": "15/10/2025"},
    {"nome": "Opção 5", "taxa": 14.70 / 100, "vencimento": "10/07/2025"},
    {"nome": "Opção 6", "taxa": 13.65 / 100, "vencimento": "05/04/2027"},
    {"nome": "Opção 7", "taxa": 13.10 / 100, "vencimento": "05/10/2026"},
    {"nome": "Opção 8", "taxa": 12.23 / 100, "vencimento": "05/10/2026"},
]

# Função para calcular o montante final com aportes mensais
def calcular_montante(aporte_mensal, taxa_anual, meses):
    taxa_mensal = (1 + taxa_anual) ** (1/12) - 1  # Convertendo taxa anual para mensal
    montante = 0
    for t in range(meses):
        montante = (montante + aporte_mensal) * (1 + taxa_mensal)
    return montante

# Definição dos períodos de investimento (em meses)
prazo_meses = {
    "Opção 1": (2027 - 2025) * 12 + 3,  # Até abril de 2027
    "Opção 2": (2026 - 2025) * 12 + 3,  # Até abril de 2026
    "Opção 3": (2026 - 2025) * 12 + 9,  # Até outubro de 2026
    "Opção 4": (2025 - 2025) * 12 + 9,  # Até outubro de 2025
    "Opção 5": (2025 - 2025) * 12 + 6,  # Até julho de 2025
    "Opção 6": (2027 - 2025) * 12 + 3,  # Até abril de 2027
    "Opção 7": (2026 - 2025) * 12 + 9,  # Até outubro de 2026
    "Opção 8": (2026 - 2025) * 12 + 9,  # Até outubro de 2026
}

# Cálculo dos montantes finais para cada opção
aporte_mensal = 200
resultados = []

for inv in investimentos:
    meses = prazo_meses[inv["nome"]]
    montante_final = calcular_montante(aporte_mensal, inv["taxa"], meses)
    resultados.append({"nome": inv["nome"], "montante_final": montante_final})

# Ordenando por maior montante final
resultados.sort(key=lambda x: x["montante_final"], reverse=True)

# Exibindo resultados
for r in resultados:
    print(f"{r['nome']}: R$ {r['montante_final']:.2f}")

print("< Porncetagem de rentabilidade >")
# Resultados fornecidos pelo usuário
resultados_usuario = {
    "Opção 1": 6576.86,
    "Opção 6": 6291.03,
    "Opção 3": 4816.80,
    "Opção 7": 4710.80,
    "Opção 8": 4676.47,
    "Opção 2": 3322.23,
    "Opção 4": 1919.30,
    "Opção 5": 1249.21,
}

# Definição dos períodos de investimento (em meses)
prazo_meses = {
    "Opção 1": (2027 - 2025) * 12 + 3,  # Até abril de 2027
    "Opção 2": (2026 - 2025) * 12 + 3,  # Até abril de 2026
    "Opção 3": (2026 - 2025) * 12 + 9,  # Até outubro de 2026
    "Opção 4": (2025 - 2025) * 12 + 9,  # Até outubro de 2025
    "Opção 5": (2025 - 2025) * 12 + 6,  # Até julho de 2025
    "Opção 6": (2027 - 2025) * 12 + 3,  # Até abril de 2027
    "Opção 7": (2026 - 2025) * 12 + 9,  # Até outubro de 2026
    "Opção 8": (2026 - 2025) * 12 + 9,  # Até outubro de 2026
}

# Cálculo do total investido para cada opção
investimentos_totais = {op: prazo_meses[op] * 100 for op in resultados_usuario}

# Cálculo da rentabilidade percentual
rentabilidades = {
    op: ((resultados_usuario[op] / investimentos_totais[op]) - 1) * 100 for op in resultados_usuario
}

# Ordenando pela maior rentabilidade
rentabilidades_ordenadas = sorted(rentabilidades.items(), key=lambda x: x[1], reverse=True)

# Exibindo os resultados
for op, rentabilidade in rentabilidades_ordenadas:
    print(f"{op}: {rentabilidade:.2f}%")
