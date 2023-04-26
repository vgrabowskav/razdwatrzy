print("Czy chcesz się wybrać ze mną na wycieczkę po Berlinie? tak/nie")
odp1 = input()
if odp1 == "tak":
    print("Świetnie, bardzo się cieszę!\nNaszą wycieczkę rozpoczniemy od dworca Hbf. Ale uwaga!\nWłaśnie dostałeś/aś informację, że twój pociąg powrotny został odwołany. Czy chcesz wsiąść do pewnego pociągu powrotnego za 20min czy może zaryzykujemy? ")
    print("Wybierz numer:\n1 - wsiadam do pociągu\n2 - ryzykuję")
    odp2 = input()
    if odp2 == "2":
        print("Uf fantastyczie! Proszę wybrać pozycję za pomocą numeru.\n1 - Brama Brandenburska\n2 - Reischtag\n3 - Kroll Opera House")
        print("To co? Idziemy?")
        odp3 = input()
        if odp3 == "1":
            print("Witam. witam!\nJesteśmy pod Bramą Brandenburską!\nTo co może pocztówkę kupimy sobie z tym widoczkiem? Albo pójdziemy poszukać misiów? A może Plac Poczdamski?\nNo dobra lepiej nie mieszajmy. Wybierz opcję:\n1 - Przechadzka ulicą Pod Lipami i zakup pocztówki\n2 - Szukanie Berlińskich misiów\n3 - Plac Poczdamski")
            odp4 = input()
            if odp4 == "1":
                print("Cudowny wybór! Idąc prosto tą ulicą trafisz na grzane wino. Smacznego!")
            elif odp4 == "2":
                print("Świetny wybór!\nIdąc ulicą Pod Lipami za bramą Brandenburską natrafisz na co najmniej 3 misie, z którymi możesz zrobić sobie zdjęcie!\nCzy będziesz ich szukał dalej? tak/nie")
                odp5 = input()
                if odp5 == "tak":
                    print("Cudownie. Słyszałam, że blisko Alexanderplatz natrafisz na kolejnego!")
                else:
                    print("Zdjęcia z misiami zrobione i tak! Teraz możesz zwiedzić sobie na spokojnie Wyspę Muzeów czy iść coś zjeść.")
            elif odp4 == "3":
                print("Po trasie minąłeś Pomnik Zamordowanych Żydów! Mam nadzieję, że zerknąłeś.")
        elif odp3 == "2":
            print("No i proszę! Jesteśmy pod jednym z najbardziej rozpoznawalnych budynków, z których słynie Berlin. No, ale niestety jest rozkopane i nie da się zbliżyć:(\nMoże dajmy sobie jeszcze jedną szansę. Co ty na to?")
        elif odp3 == "3":
            print("Życzę przyjemnej wycieczki po parku!")
    else:
        print("No cóż. Życzę miłej podróży!")
else:
    print("No cóż. Może innym razem.")