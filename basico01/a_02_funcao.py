# def = definição de função

def somar(num1,num2):
    """soma entre dois números inteiros"""
    somar=int(num1)+int(num2)
    print(somar)

def subtrair(num1,num2):
    """"subtração entre dois números inteiros"""
    subtrair=int(num1)-int(num2)
    print(subtrair)
    
def cores():
    pass

def main():
    num1=input("digite um número:")
    num2=input("digite outro número:")
    somar(num1,num2)
    subtrair(num1,num2)

if __name__ == "__main__":
    main()