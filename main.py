import pandas as pd
import matplotlib.pyplot as plt

# Carrega o conjunto de dados a partir do arquivo CSV
gas = pd.read_csv("gas_prices.csv")

# Cria a figura do gráfico e define o tamanho
plt.figure(figsize=(10, 6))

# Define o título do gráfico
plt.title("Valor do combustível em US$")

# Cria as linhas do gráfico para cada país
plt.plot(gas["Year"], gas["Australia"], "r.-", label="Australia")
plt.plot(gas["Year"], gas["Italy"], "y.-", label="Italy")
plt.plot(gas["Year"], gas["USA"], "b.-", label="USA")
plt.plot(gas["Year"], gas["Japan"], "g.-", label="Japan")

# Personalização dos eixos
# Mostra os anos no eixo X de dois em dois para melhor visualização
plt.xticks(gas["Year"][::2])

# Define os rótulos dos eixos
plt.xlabel("Years")
plt.ylabel("US$")

# Exibe a legenda e adiciona uma grade leve ao gráfico
plt.legend()
plt.grid(alpha=0.3)

# Salva o gráfico em formato PDF
# IMPORTANTE: savefig deve ser chamado antes do show
plt.savefig("country.pdf")

# Exibe o gráfico na tela
plt.show()
