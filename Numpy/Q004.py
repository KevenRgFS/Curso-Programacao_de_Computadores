import numpy as kk

array1 = kk.array([10, 20, 30, 40, 50])

media = kk.mean(array1)

desvioP = kk.std(array1)

print(f"Sua média é {media}\nE seu desvio padrão: {desvioP:.2f}")


