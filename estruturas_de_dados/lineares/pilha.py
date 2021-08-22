from estrutura_linear import *


class Pilha(EstruturaLinear):

	def push(self, valor: object):
		novo = No(valor, self.cabeca)
		self.cabeca = novo

	def pop(self) -> 'No':
		self.assert_not_empty()

		removido = self.cabeca
		self.cabeca = self.cabeca.proximo
		return removido

	def remover_ate_elemento(self, elemento):
		posicao = self.index_of(elemento)
		if posicao >= 0:
			for elem in self:
				self.pop()
				if (elem is elemento) or (elem.carga == elemento):
					break


if __name__ == '__main__':

	def palindromo(frase):
		frase = frase.replace(' ', '')
		frase_invertida = ''

		pilha = Pilha()
		for char in frase:
			pilha.push(char)
		for char in pilha:
			frase_invertida += pilha.pop().carga

		return frase == frase_invertida


	def teste_pilha_remover():
		pilha = Pilha()
		pilha.push('aa')
		pilha.push('bb')
		pilha.push('cc')
		pilha.push('dd')
		pilha.push('ee')

		print(pilha)
		pilha.remover_ate_elemento('cc')
		print(pilha)


	def teste_palindromo():
		frase = 'socorram me subi no onibus em marrocos'
		if palindromo(frase):
			print(f'\"{frase}\" é palindromo')
		else:
			print(f'\"{frase}\" não é palindromo')

	teste_pilha_remover()
	print('*******************')
	teste_palindromo()
