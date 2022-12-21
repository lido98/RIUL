def select_corpus():
    coll:str = ""
    while(True):
        print ("Seleccione la coleccion de documentos(numero) que desea utilizar:\n")
        print ("1. CRAN")
        print ("2. VASWANI")
        print ("\ninput: ",end= "")
        index = input()
        
        if index == "1":
            coll = "files Cran";
            break
        if index == "2":
            coll = "files Vaswani";
            break

        print("Debe selccionar una de las opciones disponibles ( 1 o 2 )\n")    
    return coll    

def select_model():
    mod = ""
    while(True):
       print ("\nSeleccione la coleccion de documentos(numero) que desea utilizar:\n")
       print ("1. BOOLEANO")
       print ("2. VECTORIAL")
       print ("3. SEMANTICA LATENTE")
       print ("\ninput: ",end= "")
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
       print("Debe seleccionar una de las opciones disponibles ( 1, 2 o 3)\n")   
    
    return mod   