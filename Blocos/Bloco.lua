import sys


class Bloco:
    """'Interface' para todos os blocos"""
    colide = False  # É impossivel passar por cima?

    def surface(self):
        """
        :return: Surface com a imagem do bloco
        """
        pass

    def __repr__(self):
        return str(self.__class__).split('.')[2]


class Estruturas:
    """'Interface' para todas as estruturas"""
    def surface(self):
        """
        :return: Surface com a imagem da estrutura
        """
        pass
