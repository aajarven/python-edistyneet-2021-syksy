import random


def kysy_lasku():
    luku1 = random.randint(1, 9999)
    luku2 = random.randint(1, 9999)

    print("Mitä on {}+{}?".format(luku1, luku2))
    vastaus = int(input())

    if vastaus == luku1 + luku2:
        print("Oikein meni!")
        return True
    else:
        print("Väärin meni! Oikea vastaus on {}".format(luku1 + luku2))
        return False


if __name__ == "__main__":
    peli_kaynnissa = True
    pisteet = -1

    while peli_kaynnissa:
        peli_kaynnissa = kysy_lasku()
        pisteet += 1

    print("\nSait {} pistettä".format(pisteet))
