rates = {'Sberbank':55.8,'VTB24':53.91}
value_min = min(rates.values(), key=lambda unit:unit.real)
keys = list(rates.keys())
index = list(rates.values()).index(value_min)
name_min = keys[index]
print(name_min, " -> ", value_min)
