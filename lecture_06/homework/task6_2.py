# ---------- 1 ----------

prices = [100, -50, 300, 40, 800]

# ---------- 2 ----------

prices.remove(-50)
print(prices)

# ---------- 3 ----------

prices.append(150)
print(prices)

# ---------- 4 ----------

prices.sort()
print(prices)

# ---------- 5 ----------

tax_prices = [price * 1.2 for price in prices if price >= 100.0]
print(tax_prices)

# ---------- 6 ----------

result = f"\n\tБазовый прайс (очищенный): {prices}\n\tЦены с НДС (>100): {tax_prices}\n\tОбщая выручка: {sum(tax_prices)}\n\tМинимум: {min(tax_prices)}\n\tМаксимум: {max(tax_prices)}"
print(result)
