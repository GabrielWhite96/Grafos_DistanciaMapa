import sys
from util import *

class Grafo:
    def __init__(self, numVertices):
        self.numVertices = numVertices
        self.matrizAdjacencias = [[0] * numVertices for _ in range(numVertices)]
        self.matrizAdjacenciasSemPeso = [[0] * numVertices for _ in range(numVertices)]
        self.matrizIncidencia = []

def criaMatriz(numVertices):
    return Grafo(numVertices)

def verificaTipoGrafo(grafo):  # sourcery skip: use-itertools-product
    for i in range(grafo.numVertices):
        for j in range(grafo.numVertices):
            if grafo.matrizAdjacencias[i][j] > 1:
                return "multigrafo"
            elif i == j and grafo.matrizAdjacencias[i][j] > 0:
                return "pseudografo"
    
    return "grafo simples"

def verificaConexao(grafo):
    visitado = [False] * grafo.numVertices
    pilha = [0]
    visitado[0] = True

    while pilha:
        vertice = pilha.pop()
        for adjacente in range(grafo.numVertices):
            if grafo.matrizAdjacencias[vertice][adjacente] > 0 and not visitado[adjacente]:
                pilha.append(adjacente)
                visitado[adjacente] = True

    return "conexo" if all(visitado) else "desconexo"

def verificaCompleto(grafo):  # sourcery skip: use-any, use-itertools-product
    for i in range(grafo.numVertices):
        for j in range(grafo.numVertices):
            if i != j and grafo.matrizAdjacencias[i][j] != 1:
                return False
    return True

def informaOrdemTamanho(grafo):
    ordem = grafo.numVertices
    tamanho = sum(sum(row) for row in grafo.matrizAdjacencias) // 2
    return ordem, tamanho

def informaGrauVertices(grafo):
    # sourcery skip: inline-immediately-returned-variable, inline-variable, list-comprehension
    graus = []
    for i in range(grafo.numVertices):
        grau = sum(grafo.matrizAdjacenciasSemPeso[i])
        graus.append(grau)
    return graus

def maiorValor(linha):
    return 0 if len(linha) == 0 else max(linha)

def menorValor(linha):  # sourcery skip: simplify-len-comparison
    linhaCopia = [valor for valor in linha if valor != 0]
    return 0 if len(linhaCopia) == 0 else min(linhaCopia)

def imprimeMatrizAdjacencias(grafo):
    somatorio = 0
    print("Matriz de adjacências:")
    print("    ", end="")
    for i in range(grafo.numVertices):
        print(chr(ord('A') + i), end=" ")
    print()
    for i in range(grafo.numVertices):
        print("",chr(ord('A') + i), end=": ")
        for j in range(grafo.numVertices):
            print(grafo.matrizAdjacencias[i][j], end=" ")
            somatorio += grafo.matrizAdjacencias[i][j]
        print("max:", maiorValor(grafo.matrizAdjacencias[i]), "Σ", somatorio, "min:", menorValor(grafo.matrizAdjacencias[i]))
        somatorio = 0

def imprimeMatrizIncidencia(grafo, lista_peso):
    print("\nMatriz de incidência:")
    print("    ", end="")
    for i in range(len(grafo.matrizIncidencia[0])):
        print(chr(ord('A') + i), end=" ")
    print()
    for i in range(len(grafo.matrizIncidencia)):
        print("{:2d}:".format(i+1), end=" ")
        for j in range(len(grafo.matrizIncidencia[i])):
            print(grafo.matrizIncidencia[i][j], end=" ")
        print("peso:", lista_peso[i])

def adicionaAresta(grafo, u, v, peso):
    grafo.matrizAdjacencias[u][v] += peso
    grafo.matrizAdjacencias[v][u] += peso

    aresta = [0] * grafo.numVertices
    aresta[u] = 1
    aresta[v] = 1
    grafo.matrizIncidencia.append(aresta)
    
def adicionaArestaSemPeso(grafo, u, v):
    grafo.matrizAdjacenciasSemPeso[u][v] += 1
    grafo.matrizAdjacenciasSemPeso[v][u] += 1
    
def maiorValor(linha):
    return 0 if len(linha) == 0 else max(linha)

def menorValor(linha):  # sourcery skip: simplify-len-comparison
    linhaCopia = [valor for valor in linha if valor != 0]
    return 0 if len(linhaCopia) == 0 else min(linhaCopia)

def liberaMatriz(grafo):
    grafo.matrizAdjacencias = []
    grafo.matrizIncidencia = []
    grafo.numVertices = 0

def calcularMenorDistancia(grafo, origem, destino):
    distancias = [sys.maxsize] * grafo.numVertices
    distancias[origem] = 0
    visitados = [False] * grafo.numVertices

    for _ in range(grafo.numVertices - 1):
        min_distancia = sys.maxsize
        min_vertice = -1

        for i in range(grafo.numVertices):
            if not visitados[i] and distancias[i] < min_distancia:
                min_distancia = distancias[i]
                min_vertice = i

        visitados[min_vertice] = True

        for i in range(grafo.numVertices):
            if (not visitados[i] and
                    grafo.matrizAdjacencias[min_vertice][i] != 0 and
                    distancias[min_vertice] + grafo.matrizAdjacencias[min_vertice][i] < distancias[i]):
                distancias[i] = distancias[min_vertice] + grafo.matrizAdjacencias[min_vertice][i]

    return distancias[destino]

def bemVindo(numVertices, lista_cidades):
    print("Bem vindo ao menu de opções do nosso mapa, as cidades mapeadas são:")
    for i in range(numVertices):
        print(i+1, "-", lista_cidades[i].replace('\n', ''))
        
    imprimeLinha()

def imprimeMatrizDistancias(distancias, lista_cidades):
    numVertices = len(distancias)
    print("\nDistâncias:\n")
    for i in range(numVertices):
        for j in range(numVertices):
            if distancias[i][j] > 100000:
                print("∞", end=" ")
            elif distancias[i][j] != 0 :
                cidade1 = lista_cidades[i].replace('\n', '')
                cidade2 = lista_cidades[j].replace('\n', '')
                print(f"{cidade1} até cidade {cidade2} = {distancias[i][j]} km\n", end="")
        print()

def menuPrimario():
    print("\nAqui você pode ver a menor distancia entre todas as cidades ou de uma cidade a outra e mais",
          "Oque você deseja?")
    print("1 - Distancia de todas as cidades",
          "\n2 - Distancia de ponto a ponto",
          "\n3 - Outras opções")
    escolha = input("Escolha:")
    timer(2)
    limpar_terminal()
    return escolha

def menuSecundario():
    print("1 - Mostrar matriz adjacencias",
          "\n2 - Mostrar matriz incidencia",
          "\n3 - Mostrar graus dos vertices",
          "\n4 - Mostrar ordem e tamanho",
          "\n5 - Mostrar se o grafo é conexo",
          "\n6 - Mostrar se o grafo é completo",
          "\n7 - Mostrar o tipo de grafo",
          "\n8 - Mostrar TODAS as informações",
          "\n9 - Voltar",
          "\n0 - Sair")
    escolha = input("Escolha:")
    timer(2)
    limpar_terminal()
    return escolha

def perguntaContinuidade():
    escolha = input("Deseja Sair ou Continuar?\n1 - Continuar\n2 - Sair\nEscolha:")
    timer(1)
    limpar_terminal()
    return escolha == "1"

if __name__ == "__main__":  
    limpar_terminal()
    with open("cidades.txt", "r") as file:
        if file is None:
            print("Erro ao abrir o arquivo.")
            exit(1)

        numVertices = int(file.readline())
        numArestas = int(file.readline())

        grafo = criaMatriz(numVertices)
        
        lista_cidades = []
        for _ in range(numVertices):
            cidade = file.readline()
            lista_cidades.append(cidade)
            
        lista_peso = []
        for _ in range(numArestas):
            u, v, peso = map(int, file.readline().split())
            adicionaAresta(grafo, u, v, peso)
            adicionaArestaSemPeso(grafo, u, v)
            lista_peso.append(peso)

    bemVindo(numVertices, lista_cidades)
    def menu():  # sourcery skip: extract-duplicate-method, extract-method, low-code-quality
        
        escolha = menuPrimario()
        
        if escolha == "1":
            distancias = []
            for i in range(grafo.numVertices):
                distancias.append([])
                for j in range(grafo.numVertices):
                    dist = calcularMenorDistancia(grafo, i, j)
                    distancias[i].append(dist)
            imprimeMatrizDistancias(distancias, lista_cidades)
            imprimeLinha()
            if perguntaContinuidade():
                menu()
            else:
                timer(2)
                exit()
        if escolha == "2":
            for i in range(numVertices):
                print(i+1, "-", lista_cidades[i].replace('\n', ''))
            print("Informe somente o número da cidade.")
            cidade1 = int(input("Cidade Origem:"))
            cidade2 = int(input("Cidade Destino:"))
            print("A distancia entre", lista_cidades[cidade1+1], "até",  lista_cidades[cidade2+1], "é =",calcularMenorDistancia(grafo, cidade1+1, cidade2+1))
            imprimeLinha()
            if perguntaContinuidade():
                menu()
            else:
                timer(2)
                exit()
        if escolha == "3":
            escolha = menuSecundario()
            if escolha == "1":
                imprimeMatrizAdjacencias(grafo)
                imprimeLinha()
                if perguntaContinuidade():
                    menu()
                else:
                    timer(2)
                    exit()
            elif escolha == "2":
                imprimeMatrizIncidencia(grafo, lista_peso)
                imprimeLinha()
                if perguntaContinuidade():
                    menu()
                else:
                    timer(2)
                    exit()
            elif escolha == "3":
                graus = informaGrauVertices(grafo)
                for i in range(grafo.numVertices):
                    if graus[i] < 0:
                        graus[i] *= -1
                    print("Grau do vértice", i+1, "=", graus[i])
                imprimeLinha()
                if perguntaContinuidade():
                    menu()
                else:
                    timer(2)
                    exit()
            elif escolha == "4":
                ordem, tamanho = informaOrdemTamanho(grafo)
                print("Ordem do grafo:", ordem)
                print("Tamanho do grafo:", tamanho)
                imprimeLinha()
                if perguntaContinuidade():
                    menu()
                else:
                    timer(2)
                    exit()
            elif escolha == "5":
                conexao = verificaConexao(grafo)
                print("Conexão do grafo:", conexao)
                imprimeLinha()
                if perguntaContinuidade():
                    menu()
                else:
                    timer(2)
                    exit()
            elif escolha == "6":
                print("O grafo é completo") if verificaCompleto(grafo) else print("O grafo não é completo")
                imprimeLinha()
                if perguntaContinuidade():
                    menu()
                else:
                    timer(2)
                    exit()
            elif escolha == "7":
                tipoGrafo = verificaTipoGrafo(grafo)
                print("Tipo de grafo:", tipoGrafo,)
                imprimeLinha()
                if perguntaContinuidade():
                    menu()
                else:
                    timer(2)
                    exit()
            elif escolha == "8":
                for i in range(numVertices):
                    print(i+1, "-", lista_cidades[i].replace('\n', ''))
                    
                imprimeLinha()
                imprimeMatrizAdjacencias(grafo)
                imprimeLinha()
                imprimeMatrizIncidencia(grafo, lista_peso)
                imprimeLinha()
                graus = informaGrauVertices(grafo)
                for i in range(grafo.numVertices):
                    if graus[i] < 0:
                        graus[i] *= -1
                    print("Grau do vértice", i+1, "=", graus[i])
                imprimeLinha()
                ordem, tamanho = informaOrdemTamanho(grafo)
                print("Ordem do grafo:", ordem)
                print("Tamanho do grafo:", tamanho)
                imprimeLinha()
                conexao = verificaConexao(grafo)
                print("Conexão do grafo:", conexao)
                imprimeLinha()
                print("O grafo é completo") if verificaCompleto(grafo) else print("O grafo não é completo")
                imprimeLinha()
                tipoGrafo = verificaTipoGrafo(grafo)
                print("Tipo de grafo:", tipoGrafo,)
                imprimeLinha()
                if perguntaContinuidade():
                    menu()
                else:
                    timer(2)
                    exit()
            elif escolha == "9":
                menu()
            elif escolha == "0":
                exit()
    menu()


    liberaMatriz(grafo)
