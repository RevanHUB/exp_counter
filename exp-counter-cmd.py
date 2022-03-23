print("Bienvenido al calculador de exp:");
exp = input("Inserta la exp del mob: ");
print(exp);
contador = 0;
option = input("Añade la kill con + o sal con -:");
while option == '+':
    exp = int(exp);
    contador = contador + 1;
    total = (exp * contador);
    total = int(total);
    estimada = int();
    estimada = total * 60;
    print('La exp actual es de: ');  
    print(total);
    option = input("Añade con + o sal con -:");

estimada = str(estimada)
total = str(total)
print("Total exp estimada a la hora: " + estimada);
print("Total de exp de la sesión: "+ total);
input("Enter to close.");
