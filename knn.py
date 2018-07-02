
import csv
import random
import math
import operator

# Carrega a base de entrada, e realiza a separação dos dodos de entrada para o grupo de teste e treinamento 
#usando como a metrica a constante split aqui definida como 0.67
def CarregarDados(filename, split, conjuntodetreinamento=[] , conjuntodeteste=[]):
	with open(filename, 'r') as csvfile:
		lines = csv.reader(csvfile)
		dataset = list(lines)
		
		for x in range(len(dataset)-1):
			for y in range(len(dataset[x])-1):
				dataset[x][y] = float(dataset[x][y])

			if random.random() < split:
				conjuntodetreinamento.append(dataset[x])
			else:
				conjuntodeteste.append(dataset[x])

#Função que calcula a distancia eclidiana 
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)
#Função que encontra os vizinhos mais proximos e forma grupos usando as distancias mais proximas de acordo com o
#numero de K
def encontrarVizinhos(conjuntodetreinamento, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(conjuntodetreinamento)):
		dist = euclideanDistance(testInstance, conjuntodetreinamento[x], length)
		distances.append((conjuntodetreinamento[x], dist))
	distances.sort(key=operator.itemgetter(1))
	vizinhos = []
	for x in range(k):
		vizinhos.append(distances[x][0])
	return vizinhos

#Define as possiveis resposta ou seja a quem pertence utilizando uma logica de votação
def resposta(vizinhos):
	classVotes = {}
	for x in range(len(vizinhos)):
		response = vizinhos[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

#Verifica a precisão das resposta de acordo com as previsoes e os dados reais. 
def getAccuracy(conjuntodeteste, predictions):
	correct = 0
	for x in range(len(conjuntodeteste)):
		if conjuntodeteste[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(conjuntodeteste))) * 100.0
	
def main():
	
	conjuntodetreinamento=[]
	conjuntodeteste=[]
	predictions=[]
	contacc=0
	conterr=0
	split = 0.67	
	while True:
		k=int(input("Defina uma numero ímpar para ser o K:"))
		if k % 2 != 0:
			break
	
	#Para ralizar os testes devem ser alteradas as bases de dados diretamente no codigo
	CarregarDados('wine.data', split, conjuntodetreinamento, conjuntodeteste)
	print( 'Conjunto Treinado: ' + repr(len(conjuntodetreinamento)))
	print( 'Conjunto de Teste: ' + repr(len(conjuntodeteste)))
	
	
	
	print("") 
	for x in range(len(conjuntodeteste)):
		vizinhos = encontrarVizinhos(conjuntodetreinamento, conjuntodeteste[x], k)
		result = resposta(vizinhos)
		predictions.append(result)
		if result == conjuntodeteste[x][-1]:
			print('Valor obtido: {} || valor real: {} -> ACERTOU'.format(str(result), str(conjuntodeteste[x][-1])))
			contacc=int(contacc+1)
		else:
			print('Valor obtido: {} || valor real: {} -> ERROU'.format(str(result), str(conjuntodeteste[x][-1])))
			conterr=int(conterr+1)
		
	accuracy = getAccuracy(conjuntodeteste, predictions)
	print('Precisão: ' + repr(accuracy) + '%\n')
	print("Acertos:"+str(contacc)," Erros:"+str(conterr))
	
main()