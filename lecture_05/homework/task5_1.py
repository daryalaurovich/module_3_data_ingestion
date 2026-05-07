# ---------- 1 ----------

raw_log = "ORDER-2025-01-15|FRT-APPLE-PL|+111 (23) 456-78-90| мИНсК "
raw_log_split = raw_log.split("|")
order_id, product_code, raw_phone, raw_city = raw_log_split

# ---------- 2 ----------

category = product_code[:3]
print(category)
region = product_code[-2:]
print(region)
pos_hyphen = product_code.find("-")
print(f"Позиция первого дефиса в коде товара: {pos_hyphen}")
if product_code.startswith("FRT"):
    print("Код товара начинается с 'FRT'")
else:
    print("Код товара не начинается с 'FRT'")

# ---------- 3 ----------

clean_phone = ""
for raw_phone_elem in raw_phone:
    if raw_phone_elem.isdigit():
        clean_phone += raw_phone_elem
print(clean_phone)
print("Длина номера {}".format(len(clean_phone)))

# ---------- 4 ----------

city = raw_city.strip().lower().title()
print(city)

# ---------- 5 ----------
report = f"Заказ: {order_id} \nКатегория: {category} | Регион: {region} \nТелефон: {clean_phone} \nГород: {city}"
print(report)
