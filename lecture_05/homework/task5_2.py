product = " фермерский ТВОРОГ "
price = 4.567
qty = 3
csv_row = "milk,bread,cheese"
review = "Это лучший ТВОРОГ в городе!"
file_path = r"C:\EcoMarket\data\2025\january\sales.csv"

# ---------- 1 ----------

clean_product = product.strip().lower().title()

# ---------- 2 ----------

total = price * qty
receipt = f"Чек 'EcoMarket' \nТовар: {clean_product} \nКол-во: {qty} \nИтого: {total:.2f} руб."
print(receipt)

# ---------- 3 ----------

csv_row_result = " | ".join(csv_row.split(","))
print(csv_row_result)

# ---------- 4 ----------

if "творог" in review.lower():
    print("Отзыв относится к категории: Dairy")

# ---------- 5 ----------

# r"" делает строку "сырой", чтобы обратный слеш (\) не считался началом спецсимвола
# (как \n или юникод \U), а воспринимался как обычный текст в пути к файлу.
print(file_path)

# ---------- Result ----------

result = f'\n\tЧек "EcoMarket" \n\tТовар: {clean_product} \n\tКол-во: {qty}  \n\tИтого: {total:.2f} руб.\n\t{csv_row_result} \n\tОтзыв относится к категории: Dairy {file_path}'
print(result)
