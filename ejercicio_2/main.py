def calculate_points(results, scoring_system):
    points = [0] * (max(results) + 1)
    for i, result in enumerate(results):
        if i < len(scoring_system):
            points[result] += scoring_system[i]
    return points


def determine_champion(points):
    max_points = max(points)
    champions = [i for i, p in enumerate(points) if p == max_points]
    return champions


def main():
    while True:
        try:
            G, P = map(int, input().split())
        except ValueError:
            print("{e}: Tipo de dato incorrecto, deben ser numeros enteros")
            continue

        if (G < 0 or G > 100) or (P < 0 or P > 100):
            print("Error: valor mayor que 100 o menor a 0 ")
            continue
        if G == 0 and P == 0:
            break

        results = []
        for _ in range(G):
            race_results = list(map(int, input().split()))
            results.append(race_results)

        S = int(input())
        for _ in range(S):
            scoring_system = list(map(int, input().split()))[1:]
            points = [0] * (P + 1)

            for race_results in results:
                race_points = calculate_points(race_results, scoring_system)
                for i in range(1, P + 1):
                    points[i] += race_points[i]

            champions = determine_champion(points)
            print(" ".join(map(str, champions)))


if __name__ == "__main__":
    main()
