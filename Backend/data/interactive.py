
def select():
    coll:str = ""
    mod:str = ""
    cases = False
    while(True):
        print ("Seleccione la coleccion de documentos(numero) que desea utilizar:\n")
        print ("1. CRAN\n")
        print ("2. VASWANI\n")
        print ("\n")
        index = input()
        if index == "1":
            coll = "CRAN";
            break
        if index == "2":
            coll = "VASWANI";
            break

        print("Debe selccionar una de las opciones disponibles ( 1 o 2 )")    
    
    while(True):
        print ("Seleccione la coleccion de documentos(numero) que desea utilizar:\n")
        print ("1. BOOLEANO\n")
        print ("2. VECTORIAL\n")
        print ("3. SEMANTICA LATENTE\n")
        print ("\n")
        index = input()
        if index == "1":
            mod = "BOOLEAN";
            break
        if index == "2":
            mod = "VECTORIAL";
            break
        if index == "3":
            mod = "LSI";
            break    
        print("Debe seleccionar una de las opciones disponibles ( 1, 2 o 3)")    
    
    while(True):
        print ("Desea ejecutar los casos de prueba:\n")
        print ("1. Si\n")
        print ("2. No\n")
        print ("\n")
        index = input()
        if index == "1":
            cases = True;
            break
        if index == "2":
            cases = False;
            break
        print("Debe seleccionar una de las opciones disponibles ( 1 o 2)")    
    
    return [coll,mod,cases]
