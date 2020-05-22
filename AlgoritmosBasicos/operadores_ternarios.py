esta_chovendo = True
# Usando True, ele vai mostrar o valor q está mais proximo a variavel
print("Hoje estou com as roupas " + ("secas.", "molhadas.")[esta_chovendo])

# Outra forma é usando IF

print("Hoje estou com as roupas ", ('molhadas' if esta_chovendo else 'secas'))
