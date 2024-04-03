DEBUG = False


def calculate_jumps(x):
    jumps = 1
    y = 1

    while y < x:
        jumps += 1
        y += jumps
        print(f"{jumps=}, {y=}") if DEBUG else None

    jumps += 1 if y - x == 1 else 0

    return jumps


def validate_input_t():
    t_flag = True
    while t_flag:
        t = int(input("Ingrese el número de pruebas: " if DEBUG else ""))

        if t < 0 or t > 1000:
            print(
                "error: Punto destino no puede ser menor que cero. "
            ) if DEBUG else None
        else:
            t_flag = False
    return t


def validate_input_x():
    x_flag = True
    while x_flag:
        x = int(input("Punto destino: " if DEBUG else ""))

        if x < 0 or x > 106:
            print(
                "error: Punto destino no puede ser menor que cero ni mayor a 106. "
            ) if DEBUG else None
        else:
            x_flag = False
    return x


def main():
    t = validate_input_t()

    for _ in range(t):
        x = validate_input_x()

        jumps = calculate_jumps(x)

        print("saltos necesarios: ", jumps) if DEBUG else print(jumps)


if __name__ == "__main__":
    main()
