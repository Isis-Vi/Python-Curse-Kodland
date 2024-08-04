#¿Cómo podemos ayudar a los mayores a entender las palabras modernas?

meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            }
            
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
    
else: 
    print("Esa palabra no está en el diccionario. ¡Se actualizará pronto!")
