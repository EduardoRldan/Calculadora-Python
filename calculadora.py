def add(x,y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def divide(x, y):
    if y == 0:
        return "Error ! La división entre 0"
        return x / y

def main():
    print("Selecciona la Operación")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    choice = input("Escoge la Opción(1/2/3/4):")

    num1 = float(input("Escoge el Primer Número"))
    num2 = float(input("Escoge el Segundo Número"))

    if choice == '1':
        print("Resultado: ", add(num1, num2))

    elif choice == '2':
        print("Resultado:", subtract(num1, num2))
    
    elif choice == '3':
        print("Resultado:", multiply(num1, num2))

    elif choice == '4':
        print("Resultado:", divide(num1, num2))

    else:
        print ("Digito Invalido")

if __name__ == "__main__":
    main()
