from main import calculate_points, determine_champion
def test():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        index = 0

        with open("output.txt", "w") as output_file:
            while index < len(lines):
                try:
                    G, P = map(int, lines[index].split())
                    index += 1
                except ValueError:
                    output_file.write("{e}: Tipo de dato incorrecto, deben ser numeros enteros\n")
                    continue

                if (G < 0 or G > 100) or (P < 0 or P > 100):
                    output_file.write("Error: valor mayor que 100 o menor a 0\n")
                    continue
                if G == 0 and P == 0:
                    break

                results = []
                for _ in range(G):
                    race_results = list(map(int, lines[index].split()))
                    results.append(race_results)
                    index += 1

                S = int(lines[index])
                index += 1
                for _ in range(S):
                    scoring_system = list(map(int, lines[index].split()))[1:]
                    index += 1
                    points = [0] * (P + 1)

                    for race_results in results:
                        race_points = calculate_points(race_results, scoring_system)
                        for i in range(1, P + 1):
                            points[i] += race_points[i]

                    champions = determine_champion(points)
                    output_file.write(" ".join(map(str, champions)) + "\n")

if __name__ == "__main__":
    test()
