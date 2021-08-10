import pyshorteners as short
link=input("Ingrese el link")
Acortador=short.Shortener().tinyurl.short(link)

print("Tu link es el siguiente --->", Acortador)