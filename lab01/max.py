#coding: utf-8

FIRST_POSITION = 0;

def maximo(collection):
	maximo = collection[FIRST_POSITION]
	for index in range(len(collection)):
		if (maximo < collection[index]):
			maximo = collection[index]
			
	return maximo
