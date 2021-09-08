def tulosta_tyhja_ruudukko():
    print(" | | ")
    print("-+-+-")
    print(" | | ")
    print("-+-+-")
    print(" | | ")

def tulosta_ruudukko(pelitilanne):
    print("{}|{}|{}".format(pelitilanne[0][0], pelitilanne[0][1], pelitilanne[0][2]))
    print("-+-+-")
    print("{}|{}|{}".format(pelitilanne[1][0], pelitilanne[1][1], pelitilanne[1][2]))
    print("-+-+-")
    print("{}|{}|{}".format(pelitilanne[2][0], pelitilanne[2][1], pelitilanne[2][2]))


if __name__ == "__main__":
    tulosta_tyhja_ruudukko()
    print()

    pelitilanne = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]
    tulosta_ruudukko(pelitilanne)
    print()

    pelitilanne = [
        ["X", " ", "O"],
        [" ", "X", " "],
        [" ", " ", "O"],
    ]
    tulosta_ruudukko(pelitilanne)