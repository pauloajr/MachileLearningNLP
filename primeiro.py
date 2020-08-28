import nltk
# cada base de dados é corpus
# corpus é um conj de documentos

artigosArq = open("artigos.txt","r")

with artigosArq as f:
    artigos = f.read()

# print(artigos[:150])

# palavras = artigos.split()
# print(palavras)

texto_exemplo = "Ola, tudo bem?"
tokens = texto_exemplo.split()
# print(tokens)

# pegando a string e separando em token
# cada elemento do vetor é token

#nltk conjunto de ferramentas de NLP

# nltk.download("punkt")
palavras_separadas = nltk.tokenize.word_tokenize(texto_exemplo)
# print(palavras_separadas)

def separa_palavras(lista_tokens):
    lista_palavras = []
    for token in lista_tokens:
        if token.isalpha() == True:
            lista_palavras.append(token)
    return lista_palavras

def normalizacao(lista_palavras):
    lista_normalizada = []
    for palavra in lista_palavras:
        lista_normalizada.append(palavra.lower())
    return lista_normalizada

# print(separa_palavras(palavras_separadas))

lista_tokens = nltk.tokenize.word_tokenize(artigos)
lista_palavras = separa_palavras(lista_tokens)
# print(f"O numero de palavras é {len(lista_palavras)}")
print(lista_palavras[:5])

lista_normalizada = normalizacao(lista_palavras)
print(set(lista_normalizada))

print(len(set(lista_normalizada)))