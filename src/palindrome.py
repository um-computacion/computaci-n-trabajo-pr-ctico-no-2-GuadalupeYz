def is_palindrome(texto):
    caracteres_validos = "abcdefghijklmnopqrstuvwxyz0123456789"
    texto_limpio = ""
    for c in texto.lower():
        if c in caracteres_validos:
            texto_limpio += c
    return texto_limpio == texto_limpio[::-1]

entrada = input("Ingrese una palabra o frase: ")
if is_palindrome(entrada):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

