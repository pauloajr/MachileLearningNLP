import nltk

artigosArq = open("artigos.txt","r")

with artigosArq as f:
    artigos  = f.read()

texto_exemplo = "Ola, tudo bem?"
tokens = texto_exemplo.split()

palavras_separadas = nltk.tokenize.word_tokenize(texto_exemplo)

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

lista_tokens = nltk.tokenize.word_tokenize(artigos)
lista_palavras = separa_palavras(lista_tokens)
lista_normalizada = normalizacao(lista_palavras)
dicionario = set(lista_normalizada)

# Lgica -> Lógica
# tabela de quatro colunas Esquerdo Direto Operaçao Resultado

letras = "abcdefghijklmnopqrstuvwxyzáâàãéêèẽíîìĩóôõòúûùũç"

def insere_letras(fatias):
    novas_palavras = []
    for E,D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D)
    return novas_palavras

## em cima ele corrigi adicionando letra

def deleta_caracter(fatias):
    novas_palavras = []
    for E,D in fatias:
        if E != "" or D != "":
            novas_palavras.append(E + D[1:])
    return novas_palavras

## em cima ele corrigi removendo letra

def trocar_letra(fatias):
    novas_palavras = []
    for E,D in fatias:
        if D != "":
            for letra in letras:
                 novas_palavras.append(E + letra + D[1:])
    return novas_palavras
## em cima ele corrigi trocando uma letra e 

def inverte_pos_letra(fatias):
    novas_palavras = []
    for E,D in fatias:
        if E != "" and D != "":
            novas_palavras.append(E[:-1] + D[0] + E[-1] + D[1:])
    return novas_palavras
## em cima ele corrigi invertendo letra

def gerador_palavras(palavra):
    fatias = []
    for i in range (len(palavra)+1):
        fatias.append((palavra[:i],palavra[i:]))
    
    palavras_geradas = insere_letras(fatias)
    palavras_geradas += deleta_caracter(fatias)
    palavras_geradas += trocar_letra(fatias)
    palavras_geradas += inverte_pos_letra(fatias)
    return palavras_geradas

def gerador_turbinado(palavras_geradas):
    novas_palavras = []
    for palavra in palavras_geradas:
        novas_palavras += gerador_palavras(palavra)
    return novas_palavras


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

# print(corretor("lgóica"))

vocabulario = set(lista_normalizada)
def novo_corretor(palavra):
    palavra = palavra.lower()
    palavras_geradas = gerador_palavras(palavra)
    palavras_geradas_turbinado = gerador_turbinado(palavras_geradas)
    todas_palavras = set(palavras_geradas_turbinado + palavras_geradas)
    #filtro
    candidatos = [palavra]
    for palavra in todas_palavras:
        if palavra in vocabulario:
            candidatos.append(palavra)
    #print(len(candidatos))
    palavra_correta = max(candidatos, key=probabilidade)
    return palavra_correta

# print(novo_corretor("olóiigica"))

# pra baixo é tudo questao de teste
def cria_dados_teste(nome_arquivo):
    lista_palavras_teste = []
    f = open(nome_arquivo,"r")
    for linha in f:
        correta, errada = linha.split()
        lista_palavras_teste.append((correta,errada))
    f.close()
    return lista_palavras_teste

lista_teste = cria_dados_teste("palavras.txt")

def avaliador(testes, vocabulario):
    numero_de_palavras = len(testes)
    acertou = 0
    desconhecida = 0
    lsterrada = []
    for correta, errada in testes:
        corrigida = corretor(errada)
        desconhecida += (correta not in vocabulario)
        if correta == corrigida:
            acertou += 1
    taxa_acerto = round(acertou*100/numero_de_palavras,2)
    taxa_desconhecida = round(desconhecida*100/numero_de_palavras,2)
    print(f"taxa de acerto {taxa_acerto}% de {numero_de_palavras} palavras")
    print(f"Taxa de palavras desconhecida {taxa_desconhecida}%")
    print("Então ele acerta apenas", int((taxa_acerto/100)*numero_de_palavras), "palavras")
    # print(lsterrada)

vocabulario = set(lista_normalizada)
# avaliador(lista_teste, vocabulario)

# lgica

print(novo_corretor("lóiiigica"))
print(corretor("lóiigica"))
