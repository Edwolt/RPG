import sys


class Bloco:
    colide = False  # É impossivel passar por cima?

    def surface(self):
        """
        :return: Surface com a imagem do bloco
        """
        pass

    def __repr__(self):
        return str(self.__class__).split('.')[2]


class Estruturas:
    def surface(self):
        """
        :return: Surface com a imagem da estrutura
        """
        pass
