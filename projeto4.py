vendas_semanais = [1, 10, 15, 20]
total=0
for venda in vendas_semanais:
    total= total + venda
print(f"você atingiu {total}, de vendas esse mês")
if total>=200:
    print("parabens meta batida")

elif total >=100:
    print("boas vendas, mas, podemos melhorar")

else:
    print("pessimas vendas, precisamos de uma formla para vendas,nova.")