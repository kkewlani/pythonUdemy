temperatures_c = [10, -20, -289, 100]

def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make any sense."
    else:
        f = c * 9/5 + 32
        return f

with open("temps.txt", 'w') as f_temp_file:
    for t in temperatures_c:
        f = c_to_f(t)
        print(f)
        if isinstance(f, str):
            continue
        f_temp_file.write(str(f) + "\n")