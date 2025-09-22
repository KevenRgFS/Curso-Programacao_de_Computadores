import numpy as np

array_a = np.arange(1,11)
print(array_a)
print("\n")
array_b = np.array([0.268, 0.48, 0.789, 0.3, 0.564, 0.7, 0.7894, 0.412, 0.98, 0.999])
print(array_b)
print("\n")

array_c = array_a + array_b

print(f"array_a + array_b = {array_c}")