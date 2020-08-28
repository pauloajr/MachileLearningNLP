import nltk
# cada base de dados é corpus
# corpus é um conj de documentos

artigosArq = open("artigos.txt","r")

with artigosArq as f:
    artigos  = f.read()

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
lista_normalizada = normalizacao(lista_palavras)
dicionario = set(lista_normalizada)

# Lgica -> Lógica
# tabela de quatro colunas Esquerdo Direto Operaçao Resultado

def insere_letras(fatias):
    novas_palavras = []
    letras = "abcdefghijklmnopqrstuvwxyzáâàãéêèẽíîìĩóôõòúûùũç"
    for E,D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D)
    return novas_palavras

palavra_exemplo = "lgica"
def gerador_palavras(palavra):
    fatias = []
    for i in range (len(palavra)+1):
        fatias.append((palavra[:i],palavra[i:]))
    palavras_geradas = insere_letras(fatias)
    return palavras_geradas

palavras_geradas = gerador_palavras(palavra_exemplo)
# print(palavras_geradas)

total_palavras = len(lista_normalizada)
frequencia = nltk.FreqDist(lista_normalizada)
def probabilidade(palavra_gerada):
    #frequencia_palavra/total_de_palavras
    return frequencia[palavra_gerada]/total_palavras

def corretor(palavra):
    palavra = palavra.lower()
    palavras_geradas = gerador_palavras(palavra)
    palavra_correta = max(palavras_geradas, key=probabilidade)
    return palavra_correta


def cria_dados_teste(nome_arquivo):
    lista_palavras_teste = []
    f = open(nome_arquivo,"r")
    for linha in f:
        correta, errada = linha.split()
        lista_palavras_teste.append((correta,errada))
    f.close()
    return lista_palavras_teste



lista_teste = cria_dados_teste("palavras.txt")

def avaliador(testes):
    numero_de_palavras = len(testes)
    acertou = 0
    lsterrada = []
    for correta, errada in testes:
        corrigida = corretor(errada)
        if correta == corretor(errada):
            acertou += 1
        else:
            lsterrada.append(errada)
    taxa_acerto = round(acertou*100/numero_de_palavras,2)
    print(f"taxa de acerto {taxa_acerto}% de {numero_de_palavras} palavras")
    print("Então ele acerta apenas", int((taxa_acerto/100)*numero_de_palavras), "palavras")
    # print(lsterrada)

avaliador(lista_teste)
