#concatenar uan cadena
text1 = "Fundamentos con"
text2 = "Python"
#text3 = 5
result = text1 + text2
print(result)

#fotmato de cadenas
name = "Erick"
lastName = "Muñoz"
fullName = name + "" + lastName
print(fullName)

#
price = 97
text3 = f"the price is {price:.2f} dollars"
print(text3)

text4 =f"La multiplicacion es {20 +59}"
print(text4)

#metodos con cadenas
#funcion capitalize() pone en mayuscula la 1era letra de una frase
text5 = "python es un lenguaje de alto nivel de programacion"
result1 = text5.capitalize()
print(result1)

#funcion casefold()
#convierte la cadena en minuscula, esta es mas fuerte que lower()
title = "Cien años de soledad"
titleConvert = title.casefold()
print(titleConvert)

#funcion Center
#agrag caracteres ocupando los espacios establecidos
fruit = "banana"
textCenter = fruit.center( 20,  "-" )
print(textCenter)

#funcion count
#devuelve el numero de veces que aparece un valor en la cadena
title1 = "i love apples, apple are my favorite fruit"
result2 = title1.count("apple")
print(result2)

#funcion endswith
#Función que comprueba si la cadena termina con un signo de puntuación (.).
text6 = "Curso, Fundamentos con python."
result3 = text6.endswith(".")
print(result3)

#funcion expandtabs
#La función establece el tamaño de tabulaciones en la cantidad especificada
#de espacios en blanco.
letter = "F\tU\tP"
letterSpaces = letter.expandtabs(2)
print(letterSpaces)

#funcion find()
#Esta función encuentra la primera aparición del valor especificado.
text7 = "Hola, bienvenidos a Colombia."
result4 = text7.find("bienvenidos")
print(result4)
#Nota: la función devuelve -1 si no se encuentra el valor.

#funcion title
#Esta función escribe en mayúscula la primera letra de cada palabra
text8 = "welcome to the world"
result5 = text8.title()
print(result5)

#funcion isalnum()
#Esta función devuelve Verdadero si todos los caracteres de la cadena
#son alfanuméricos.
alphanumeric = "Python321"
result6 = alphanumeric.isalnum()
print(result6)

#funcion isalpha()
#Esta función devuelve Verdadero si todos los caracteres de la cadena están en
#el alfabeto.
latters ="SpaceX"
result7 = latters.isalpha()
print(result7)