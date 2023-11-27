height = float(input("Height: "))
weight = int(input("Weight: "))

if height>3:
    raise ValueError("Human height shpuld not be over 3meters")

bmi = weight/height**2
print(bmi)
