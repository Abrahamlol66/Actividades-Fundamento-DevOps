def Menu():
    print("--------------------")
    print("1. Edad")
    print("2. Sexo")
    print("3. Nombre")
    print("4. Estatura")
    print("5. Todas las anteriores")
    print("6. Salir")
    print("--------------------")

def Opciones():
    #Edad
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad < 0:
                print("La edad no puede ser negativa.")
            else:
                break
        except:
            print("Debe ingresar un número válido.")
    #Sexo
    while True:
        sexo = input("Ingrese su sexo (M/F): ").upper()
        if sexo in ["M", "F"]:
            break
        else:
            print("El sexo debe ser M o F.")
    #Nombre
    while True:
        nombre = input("Ingrese su nombre: ")
        if nombre.isalpha():
            break
        else:
            print("El nombre debe contener solo letras.")
    #Estatura
    while True:
        try:
            estatura = float(input("Ingrese su estatura en metros: "))
            if estatura <= 0 or estatura > 2.5:
                print("La estatura debe estar entre 0 y 2.5 metros.")
            else:
                break
        except:
            print("Debe ingresar un número válido.")

    print("\nDatos guardados correctamente")
    print("Edad:", edad)
    print("Sexo:", sexo)
    print("Nombre:", nombre)
    print("Estatura:", estatura)
    
    return edad, sexo, nombre, estatura


edad, sexo, nombre, estatura = Opciones()
while True:
    Menu()
    opcion = input("Seleccione una opción (1-6) o 'salir' para terminar: ")
    if opcion == "1":
        print("Tu edad es: ", edad)
    elif opcion == "2":
        print("Tu genero es: ", sexo)
    elif opcion == "3":
        print("Tu nombre es: ", nombre)
    elif opcion == "4":
        print("Tu estatura es: ", estatura)
    elif opcion == "5":
        print("Todos los datos son: ", ("edad: " + str(edad), "sexo: " + sexo, "nombre: " + nombre, "estatura: " + str(estatura)))
    elif opcion.lower() == "6":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción entre 1 y 6 o 'salir'.")