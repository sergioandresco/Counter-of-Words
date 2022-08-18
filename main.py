import nltk
nltk.download('stopwords')
import nltk
nltk.download('punkt')

with open('data_analizar.txt', 'r') as archivo: #asigna el archivo abierto a una variable archivo
    texto = archivo.read() #leer el archivo
    import re
    from nltk.corpus import stopwords # importar las libreria nltk que es para analizar lenguaje natural
    #stopwards son palabras comunes del lenguaje, para que no las tenga en cuenta
    from nltk.tokenize import word_tokenize # tokeniza las palabras o las separa
    import string
    caracter = "" #
    stop_words = set(stopwords.words('spanish'))# se asignna el idioma español para el analisis
    word_tokens = word_tokenize(texto) # tokeniza o se separan las palabras
    word_tokens = list(filter(lambda token: token not in string.punctuation, word_tokens)) #hace filtrado de espacios, puntuacion las palabras comunes
    filtro = [] # se declara un array
    filtro.sort()
    for palabra in word_tokens:
            filtro.append(palabra)# agrega la palabra que cumpla con el filtro
    filtro.sort()#ordena el array
    from collections import Counter #libreria para contar las palabras
    c = Counter(filtro) #cuenta las palabras
    with open('revision.csv', 'w') as f:
        for k, v in c.items():
            f.write(f'{k} {v}\n')
