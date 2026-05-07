# ---------- 1 ----------

rows_range = range(1, 6)
rows = list(rows_range)
print(rows_range)
print(rows)

# ---------- 2 ----------

rows[2] = "Ремонт"
print(rows)

# ---------- 3 ----------

if 5 in rows:
	print('Ряд 5 доступен')

# ---------- 4 ----------

priority_rows=rows[:3]
print(priority_rows)