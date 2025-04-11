def is_palindrome(texto):
    caracteres_validos = "abcdefghijklmnopqrstuvwxyz0123456789"
    texto_limpio = ""

    for c in texto.lower():
        if c in caracteres_validos:
            texto_limpio += c

    return texto_limpio == texto_limpio[::-1]
  
