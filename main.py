
# myfile = open("fruits.txt")
# content = myfile.read()
# lista = list(content.splitlines())

op = True

# Funcion que purga los datos provenientes del archivo
def onFilterElements(lista):
    for item in range(len(lista)):
        element = lista[item].replace("\n", "")
        if element == -1:
            break
        else: 
            lista.pop(item)
            lista.insert(item, element)
    return lista
        
# def onSearchFruta(fruta):


while op:
    opt = int(input("""
        ***************************************
        ***************************************
        ***** 1. Leer contenido de archivo ****
        ***** 2. Buscar fruta              ****
        ***** 3. Agregar fruta             ****
        ***** 4. Borrar fruta              ****
        ***** 5. Editar fruta              ****
        ***************************************
        ***************************************
        Escoja una opcion: """ ))
    
    if opt == 1:
      # lectura
        with open("fruits.txt", "r") as myfile: 
            content = myfile.read()
            print("Frutas: \n",content)
    elif opt == 2: 
        with open("fruits.txt", "r") as myfile:
            content = myfile.readlines()
            array = onFilterElements(content)
            fruta = str(input("Fruta a buscar: "))
            # fruit = array[f"{fruta}"]
            
            for value in array:
                if value.lower() == fruta.lower():
                    print("Fruta Encontrada: ", value)
                    break
            

    elif opt == 3:
        print()
                
                    
        



# # lectura
# with open("fruits.txt", "r") as myfile: 
#     content = myfile.read()

# print(content)


# # escritura
# with open("fruits.txt", "a") as myfile: 
#     text = input("Ingrese una fruta:")
#     myfile.write(f"\n{text}")
    
# print(myfile)