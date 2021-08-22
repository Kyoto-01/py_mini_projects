from lista_duplamente_encadeada import *


class ListaCircular(ListaDuplamenteEncadeada):

	def __init__(self):
		super().__init__()

	def __iter__(self):
		if not self.is_empty():
			atual = self.cabeca
			yield atual
			while atual is not self.cauda:
				atual = atual.proximo
				yield atual

	def __repr__(self):
		retorno = ''
		for elem in self:
			retorno += f'ant:{elem.anterior} atual:{elem} prox:{elem.proximo}\n'
		return retorno

	def apontar_para_no(self, no: 'NoDuplo'):
		super().apontar_para_no(no)
		self.cauda.proximo = self.cabeca
		self.cabeca.anterior = self.cauda

	def inserir_no_inicio(self, valor: object):
		super().inserir_no_inicio(valor)
		self.cauda.proximo = self.cabeca
		self.cabeca.anterior = self.cauda

	def inserir_no_final(self, valor: object):
		novo = NoDuplo(valor)
		self.apontar_para_no(novo)


if __name__ == '__main__':

	def teste_len():
		items: 'ListaCircular' = ListaCircular()
		items.inserir_no_final('poção')
		items.inserir_no_final('espada')
		items.inserir_no_final('escudo')
		items.inserir_no_final('comida')

		print(f'A lista contém {len(items)} item(s)')

	def teste_remocao():
		items: 'ListaCircular' = ListaCircular()
		items.inserir_no_final('poção')
		items.inserir_no_final('espada')
		items.inserir_no_final('escudo')
		items.inserir_no_final('comida')

		print(repr(items))
		items.remover_do_inicio()
		print(repr(items))
		items.remover_do_final()
		print(repr(items))
		items.remover_de_posicao(1)
		print(repr(items))

	teste_len()
	print('***************')
	teste_remocao()
