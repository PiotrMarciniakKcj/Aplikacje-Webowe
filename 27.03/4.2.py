with open('wynik4_2.txt', "w") as wynik:
    with open("slowa.txt") as file:
        for line in file:
            w = line.count("w")
            a = (line.count("a")/2).__floor__()
            k = line.count("k")
            c = line.count("c")
            j = line.count("j")
            e = line.count("e")
            letters = [w,a,k,c,j,e]
            wynik.write(str(min(letters)) + " ")

