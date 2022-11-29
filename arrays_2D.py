size = 3
array_x = [[10 for _ in range(size)] for _ in range(size)]
print(f"Array-X Before: {array_x}")
array_x[0][0] = 99
print(f"Array-X After:  {array_x}")


array_y = [[10]*size]*size
print(f"Array-Y Before: {array_y}")
array_y[0][0] = 99
print(f"Array-Y After:  {array_y}")