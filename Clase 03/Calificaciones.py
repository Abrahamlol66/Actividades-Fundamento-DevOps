while True:
    entrada = input("¿Cuántas materias deseas ingresar?: ").strip()
    if entrada.isdigit():
        materias = int(entrada)
        if materias >= 0:
            break
        else:
            print("La cantidad debe ser mayor o igual a 0.")
    else:
        print("Por favor, ingresa solo números enteros.")

if materias == 0:
    print("No hay materias que mostrar. El programa finaliza.")
    exit()

nombres = []
calificaciones = []

for i in range(1, materias + 1):
    nombre = input(f"Nombre de la materia #{i}: ").strip()
    while not nombre.isalpha():
        print("El nombre de la materia debe contener solo letras (sin números ni espacios).")
        nombre = input(f"Reingresa el nombre de la materia #{i}: ").strip()

    def leer_calificacion(periodo):
        while True:
            valor = float(input(f"Calificación periodo {periodo} (0-100): "))
            if 0 <= valor <= 100:
                return valor
            print("Calificación inválida. Debe estar entre 0 y 100.")

    p1 = leer_calificacion(1)
    p2 = leer_calificacion(2)
    p3 = leer_calificacion(3)

    nombres.append(nombre)
    calificaciones.append([p1, p2, p3])

pregunta = input("¿Qué materia deseas ver? Ingresa nombre o número: ").strip()
indice = None

if pregunta.isdigit():
    pos = int(pregunta) - 1
    if 0 <= pos < len(nombres):
        indice = pos
    else:
        print("Número de materia inválido.")
else:
    for idx, nom in enumerate(nombres):
        if nom.lower() == pregunta.lower():
            indice = idx
            break

if indice is None:
    print("Materia no encontrada.")
else:
    cal = calificaciones[indice]
    promedio = (cal[0] + cal[1] + cal[2]) / 3
    print(f"\nMateria: {nombres[indice]}")
    print(f"Calificaciones: {cal[0]}, {cal[1]}, {cal[2]}")
    print(f"Promedio: {promedio:.2f}")
    if promedio >= 60:
        print("Estado: Aprobado")
    elif promedio <= 59:
        print("Estado: Reprobado")