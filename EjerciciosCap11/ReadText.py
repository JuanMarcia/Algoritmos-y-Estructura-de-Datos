import string

# Abre el archivo de texto y lo lee
with open('Juan.txt', 'r') as file:
    text = file.read()

# Inicializa un diccionario vacío para contar las palabras
word_count = {}

text = text.lower().translate(str.maketrans('', '', string.punctuation))

for word in text.split():
    
    if word not in word_count:
        word_count[word] = 1
  
    else:
        word_count[word] += 1

for word, count in word_count.items():
    print(f'{word}: {count}')
