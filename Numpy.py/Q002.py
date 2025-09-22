import numpy as np

alexandre = np.array([7.5, 8.1, 6.4, 7.0, 9.8])
pesos = np.arange(1,6)

soma_pesos = np.sum(pesos)
print(soma_pesos)

multi = alexandre * pesos
print(np.sum(multi))

media = np.sum(multi) / soma_pesos

print(f"{np.sum(multi)} / {soma_pesos} = {media:.2f} de média")

#ou, também pode ser:

"""media = np.average(alexandre, weights=pesos)

print(f"{media:.2f}")"""