def validar_contraseña(contraseña):
    estado = 0
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_especial = False
    longitud = len(contraseña)

    # Verificamos la longitud mínima
    if longitud < 8:
        return "Contraseña inválida: menos de 8 caracteres."

    # Recorremos cada carácter de la contraseña
    for char in contraseña:
        if char.isupper():
            tiene_mayuscula = True
        if char.islower():
            tiene_minuscula = True
        if char.isdigit():
            tiene_numero = True
        if char in "!@#$%^&*()_+=-":
            tiene_especial = True

        # Transiciones de estados
        if estado == 0:  # Esperando el primer carácter
            if char.isalnum() or char in "!@#$%^&*()_+=-":
                estado = 1
        elif estado == 1:  # Contando caracteres hasta al menos 8
            if longitud >= 8:
                estado = 2
        elif estado == 2:
            if tiene_mayuscula:
                estado = 3
            if tiene_numero:
                estado = 4
            if tiene_especial:
                estado = 5
        elif estado == 3:
            if tiene_numero:
                estado = 4
            if tiene_especial:
                estado = 5
        elif estado == 4:
            if tiene_mayuscula:
                estado = 3
            if tiene_especial:
                estado = 5
        elif estado == 5:
            if tiene_mayuscula:
                estado = 3
            if tiene_numero:
                estado = 4

    # Regla adicional: debe tener al menos una letra minúscula
    if not tiene_minuscula:
        return "Contraseña inválida: debe contener al menos una letra minúscula."

    # Verificamos si la contraseña cumple todas las reglas
    if estado in [3,4,5] and tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial:
        return "Contraseña válida"
    else:
        return "Contraseña inválida"

def main():
    contraseña = input("Ingrese la contraseña a validar: ")
    resultado = validar_contraseña(contraseña)
    print(resultado)

if __name__ == "__main__":
    main()

