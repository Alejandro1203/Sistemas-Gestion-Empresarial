tienda1 = {"manzanas": 10, "naranjas": 15, "plátanos": 5}
tienda2 = {"manzanas": 8, "naranjas": 20, "uvas": 13}
tienda_fusion = {}

tienda_fusion.update(tienda1)

for key in tienda2:
    if key in tienda_fusion:
        tienda_fusion[key] = tienda_fusion[key] + tienda2[key]
    else:
        tienda_fusion[key] = tienda2[key]

print(tienda_fusion)