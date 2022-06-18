sp = 67.83643
rj = 36.67866
mg = 29.22988
es = 27.16548
others = 19.84953

total = sp + rj + mg + es + others

sp_percent = sp / total * 100
rj_percent = rj / total * 100
mg_percent = mg / total * 100
es_percent = es / total * 100
others_percent = others / total * 100

print('Faturamento mensal SP: {:.2f}%'.format(sp_percent))
print('Faturamento mensal RJ: {:.2f}%'.format(rj_percent))
print('Faturamento mensal MG: {:.2f}%'.format(mg_percent))
print('Faturamento mensal ES: {:.2f}%'.format(es_percent))
print('Outros: {:.2f}%'.format(others_percent))