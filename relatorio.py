import csv

total = 0

with open("vendas.csv", "r") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        total += float(linha["valor"])

print("=== RELATÓRIO DE VENDAS ===")
print("Total vendido: R$", total)
