#Datos de la persona
cond = False
while cond == False: #Usamos el comando while para repetir la pregunta por si el usuario ingresa un dato incorecto.
    try:
        
        nombre = str(input ("Ingrese su nombre completo: ")) #Le pedimos que ingrese el nombre completo usando el comando str para representar el texto 
        if nombre =="": #Utilizamos el comando if para evitar que el usuario deje espacios en blanco. 
            print("No se ha registrado respuesta.")
        else:
            cond = True
    except ValueError:
        print ("Ingresa un valor.")


cond = False #Usamos False para asignar valores booleanos a variables o al evaluar expresiones booleanas.
while cond == False:
    try:
        
        edad = float(input ("Ingrese su edad: ")) #Utilizamos el comando float para indicar que la edad se represente en números.
        if edad < 0: #Usamos IF para evitar que el usuario ingrese un número negativo ya que esto nos daría un resultado erroneo.
            print ("Ingresar un número valido")
        else:
            cond = True
    except ValueError: #Nos aseguramos que el usuario no coloque ninguna letra, si lo hace aparecerá un error.
        print ("Ingresa un número valido")


cond = False
while cond == False:
    try:
        
        peso = float(input ("Ingrese su peso en kilogramos: ")) #Utilizamos el comando float para indicar que la edad se represente en números.
        if peso < 0: #Usamos IF para evitar que el usuario ingrese un número negativo ya que esto nos daría un resultado erroneo.
            print ("Ingresar un número valido")
        else:
            cond = True
    except ValueError: #Nos aseguramos que el usuario no coloque ninguna letra, si lo hace aparecerá un error.
        print ("Ingresa un número valido")

cond = False
while cond == False:
    try:
        
        altura = float(input ("Ingrese su altura en metros: ")) #Utilizamos el comando float para indicar que la edad se represente en números.
        if altura < 0: #Usamos IF para evitar que el usuario ingrese un número negativo ya que esto nos daría un resultado erroneo.
            print ("Ingresar un número valido")
        else:
            cond = True
    except ValueError: #Nos aseguramos que el usuario no coloque ninguna letra, si lo hace aparecerá un error.
        print ("Ingresa un número valido")

IMC = peso / altura**2 #Utilizamos los datos que ingresó el usuario para hacer la operación y obtender el IMC.
IMC_formateado = "{:.2f}".format(IMC) #Se formatea el número para que solo nos arroje dos decimales.

print("Gracias Sr(a): " + str(nombre.title()) + " por compartir sus datos" ) #Imprimimos el nombre.
print("Su edad es : " + str(edad) + " años" ) #Imprimimos la edad.
print("Su IMC es de : " + str(IMC_formateado) ) #Imprimimos el IMC.
#Hacemos las distintas validaciones y le indicamos al usuario en que rango se encuentra.
if IMC >= 0 and IMC <= 18.49 :
    print ("Se encuentra dentro del rango de peso insuficiente.")
elif IMC >= 18.50 and IMC <= 24.99 :
    print ("Se encuentra dentro del rango de peso normal o saludable.")
elif IMC >= 25.00 and IMC <= 29.99:
    print ("Se encuentra dentro del rango de sobrepeso.")
elif IMC >= 30.00 and IMC <= 34.99 :
    print ("Se encuentra dentro del rango de obesidad grado I.")
elif IMC >= 35.00 and IMC <= 39.99:
    print ("Se encuentra dentro del rango de obesidad grado II.")
elif IMC >= 40.00:
    print ("Se encuentra dentro del rango de obesidad grado III.")

