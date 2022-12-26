from aa import data
import random

Devam = True

while Devam:
    seçim1 = random.choice(data)
    seçim2 = random.choice(data)
    if seçim2 == seçim1:
        seçim2 = random.choice(data)


    seçim1_takipçi = int(seçim1["follower_count"])

    seçim1_isim = seçim1["name"]
    seçim1_açıklama = seçim1["description"]
    seçim1_ülke = seçim1["country"]

    print(f" B == {seçim1_isim} is {seçim1_açıklama} from {seçim1_ülke} ")

    seçim2_takipçi = int(seçim2["follower_count"])

    seçim2_isim = seçim2["name"]
    seçim2_açıklama = seçim2["description"]
    seçim2_ülke = seçim2["country"]

    print(f" A == {seçim2_isim} is {seçim2_açıklama} from {seçim2_ülke}")

    answer = input("Büyük mu Küçük mü B - K: ").lower()

    if answer == "b":
        if seçim1_takipçi > seçim2_takipçi:
            print("dogru seçim: ")
        else:
            print("yanlış seçim ")
            Devam = False
    elif answer == "a":
        if seçim2_takipçi > seçim1_takipçi:
            print("dogru seçim: ")
        else:
            print("yanlış seçim ")
            Devam = False
    else:
        print("yanlış deger girdiniz ")
        Devam = False