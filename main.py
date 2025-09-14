
# myfile = open("fruits.txt")
# content = myfile.read()
# lista = list(content.splitlines())

# lectura
with open("fruits.txt", "r") as myfile: 
    content = myfile.read()

print(content)


# escritura
with open("fruits.txt", "a") as myfile: 
    text = input("Ingrese una fruta:")
    myfile.write(f"\n{text}")
    
print(myfile)