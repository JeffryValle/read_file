
def onFilterElements(lista):
    for item in range(len(lista)):
        element = lista[item].replace("\n", "")
        if element == -1:
            break
        else: 
            lista.pop(item)
            lista.insert(item, element)
    return lista
        

op = True
while op:
    opt = int(input("""
        ***************************************
        ***************************************
        ***** 1. Leer contenido de archivo ****
        ***** 2. Buscar fruta              ****
        ***** 3. Agregar fruta             ****
        ***** 4. Borrar fruta              ****
        ***** 5. Editar fruta              ****
        ***** 6. Salir                     ****
        ***************************************
        ***************************************
        Escoja una opcion: """ ))
    
    if opt == 1:
        with open("fruits.txt", "r") as myfile: 
            content = myfile.read()
            print("Frutas: \n",content)
        
    elif opt == 2: 
        with open("fruits.txt", "r") as myfile:
            content = myfile.readlines()
            array = onFilterElements(content)
            fruta = str(input("Fruta a buscar: ")) 
            
            if fruta in array:
                print("Fruta encontrada: ", fruta)
                print(array)
            else:
                print("Fruta NO encontrada")
        
    elif opt == 3:
        with open("fruits.txt", "a") as myfile:
            fruta = str(input("Ingresar Fruta: "))
            myfile.write(fruta + "\n")
            
    elif opt == 4:
        fruta = str(input("Ingresar Fruta a borrar: "))

        with open("fruits.txt", "r") as file:
            lineas = file.readlines()

        with open("fruits.txt", "w") as myfile:
            for l in lineas:
                if l.strip() != fruta:
                    myfile.write(l)
        print(onFilterElements(lineas))
        
    elif opt == 5:
        fruta = str(input("Ingresar Fruta vieja: "))
        fruit = str(input("Ingresar Fruta nueva: "))

        with open("fruits.txt", "r") as myfile:
            content = myfile.readlines()

        nuevas_frutas = []
        for l in content:
            if l.strip() == fruta:
                nuevas_frutas.append(fruit + "\n")
            else:
                nuevas_frutas.append(l)

        with open("fruits.txt", "w") as myfile:
            myfile.writelines(nuevas_frutas)
        
    elif opt == 6: 
        print("--------- Te esperamos nuevamente----------")
        op = False
    
    else:
        print("--------- Opcion no válida, intente de nuevo ----------")
        op = False