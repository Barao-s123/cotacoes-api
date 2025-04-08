import requests
from rich.console import Console
from rich.table import Table
import matplotlib.pyplot as plt

# Inicializa o console do Rich
console = Console()

# Moedas a consultar
moedas = ["USD-BRL", "EUR-BRL", "BTC-BRL"]
cotacoes = {}

console.print("🔍 [bold cyan]Consultando cotações...[/bold cyan]\n")

# Monta a tabela colorida
tabela = Table(title="Cotações de Moedas", show_header=True, header_style="bold magenta")
tabela.add_column("Moeda")
tabela.add_column("Valor em R$")

# Consulta a API e preenche a tabela
for moeda in moedas:
    url = f"https://economia.awesomeapi.com.br/last/{moeda}"
    resposta = requests.get(url)
    dados = resposta.json()
    
    codigo = moeda.replace("-", "")
    valor = float(dados[codigo]["bid"])
    nome = dados[codigo]["name"]

    cotacoes[nome] = valor
    tabela.add_row(nome, f"R$ {valor:.2f}")

# Exibe no terminal com estilo
console.print(tabela)

# Salva em .txt
with open("cotacoes.txt", "w", encoding="utf-8") as arquivo:
    for nome, valor in cotacoes.items():
        arquivo.write(f"{nome}: R$ {valor:.2f}\n")

# Gera gráfico
nomes = list(cotacoes.keys())
valores = list(cotacoes.values())

plt.figure(figsize=(8, 4))
plt.bar(nomes, valores, color=["green", "blue", "orange"])
plt.title("Cotações em Reais")
plt.ylabel("Valor em R$")
plt.tight_layout()
plt.savefig("grafico_cotacoes.png")
plt.show()

console.print("\n✅ [green]Consulta finalizada! Dados salvos em 'cotacoes.txt' e gráfico gerado.[/green]")
