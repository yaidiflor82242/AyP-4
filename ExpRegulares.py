<<<<<<< HEAD
import re
texto= "python hola, es genial"

resultado=re.match("python",texto)
print (resultado)


texto= "python hola, es genial"

resultado=re.search("python",texto)
print (resultado.start())

texto= "python hola, es genial"

resultado=re.findall("python",texto)
print ("encontrado" ,resultado)


texto= "python hola, es genial"

resultado=re.findall("python",texto, re.IGNORECASE)
print (resultado)


texto1= "terngo 3 manzanas,12 naranjas y 100 uvas"

resultado=re.findall(r"\d+",texto1)
=======
import re
texto= "python hola, es genial"

resultado=re.match("python",texto)
print (resultado)


texto= "python hola, es genial"

resultado=re.search("python",texto)
print (resultado.start())

texto= "python hola, es genial"

resultado=re.findall("python",texto)
print ("encontrado" ,resultado)


texto= "python hola, es genial"

resultado=re.findall("python",texto, re.IGNORECASE)
print (resultado)


texto1= "terngo 3 manzanas,12 naranjas y 100 uvas"

resultado=re.findall(r"\d+",texto1)
>>>>>>> 58ebd13913bad99d083ae427cad2ded0bec80532
print ("encontrado", resultado)