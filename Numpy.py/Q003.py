import numpy as np

temperaturas = np.array([33, 31, 25, 15, 26, 19, 25])

"""for i in temperaturas:

    if i<25: False
    elif i>25: True
    else: print("Normal")"""

temperaturasTrue = temperaturas > 25
print(temperaturasTrue)

so_altas = temperaturas[temperaturasTrue]
print(so_altas)