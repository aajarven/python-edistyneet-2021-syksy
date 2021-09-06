def visaile(kysymykset):
    pisteet = 0

    for kysymys in kysymykset:
        print(kysymys["kysymys"])
        vastaus = input()
        if vastaus == kysymys["vastaus"]:
            print("oikein meni!")
            pisteet += 1
        else:
            print("väärin meni =(")
        print()

    print("Sait {}/{} pistettä".format(pisteet, len(kysymykset)))

if __name__ == "__main__":
    kysymykset = [
        {"kysymys": "Mikä on maailman painavin eläin?",
         "vastaus": "sinivalas"},
        {"kysymys": "Mikä on Suomen korkein tunturi?",
         "vastaus": "Halti"},
        {"kysymys": "Mikä on viikon kolmas päivä?",
         "vastaus": "keskiviikko"},
        {"kysymys": "Montako jalkaa on hämähäkillä (vastaa numerolla, esim 3)",
         "vastaus": "8"},
    ]

    visaile(kysymykset)