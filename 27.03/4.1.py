f = open("slowa.txt", "r")
with open("wynik4_1.txt", "w") as f2:
    with open("slowa.txt", "r") as file:
        for line in file:
            if(line.count("w") == line.count("k")):
                print(line)
                f2.write(line)
