def main():
    loop_for()

def loop_for():
    países=["Brasil","Argentina","Portugal","China","Tunísia"]
    locais=["América do Sul", "América do Sul", "Europa", "Ásia", "África"]
    capitais=["Brasília", "Buenos Aires", "Lisboa", "Pequim", "Túnis"]
    print(países)
    print(locais)
    print(capitais)
    for país, local, capital in zip(países, locais, capitais):
        print(país, local, capital)
        if país=="Brasil":
            print(f"O nome deste país é {país}. A localização é {local}. A capital é {capital}.")
        elif país=="Tunísia":
            print("Tunísia venceu a França")

        if país=="Argentina":
            print(f"O nome deste país é {país}. A localização é {local}. A capital é {capital}.")
        elif país=="Tunísia":
            print("Tunísia venceu a França")

if __name__ == "__main__":
    main()