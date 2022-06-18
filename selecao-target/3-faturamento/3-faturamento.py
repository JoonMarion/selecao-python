import json

f = open('dados.json')
datas = json.load(f)

min_value = float('inf')
max_value = float('-inf')
avg_list = []
avg = 0.0
count_days = 0

for data in datas:
    if data["valor"] < min_value:
        min_value = data["valor"]
    if data["valor"] > max_value:
        max_value = data["valor"]
    if data["valor"] > 0:
        avg_list.append(data["valor"])
        avg = sum(avg_list) / len(avg_list)
    if data["valor"] > avg:
        count_days = count_days + 1

print(f'O menor valor faturado no mês foi R${min_value:.2f}')
print(f'O maior valor faturado no mês foi R${max_value:.2f}')
print(f'Número de dias em que o faturamento foi maior que a média: {count_days}')
f.close()