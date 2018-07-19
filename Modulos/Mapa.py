import json
from importlib import import_module as imp
from Personagens.Principal.Principal import Principal


class Mapa():
    def __init__(self, mapa, coord):
        """
        :param mapa:Nome do mapa (sem o '.json')
        :param coord:Coordenada do lugar onde a renderização ocorrerá
        :return:list de list com nome dos blocos
        """
        data = json.load(open(f'Mapa/{mapa}.json'))
        blocos = data['Mapa']
        self.blocos = []
        for aux in blocos:  # intancia todos os blocos
            linha = []
            for b in aux:
                c = imp(f'Blocos.{b}.{b}')
                linha.append(c.Bloco())
            self.blocos.append(linha)
        self.coord = coord
        self.principal = Principal()

    def get(self, tam):
        return self.mapa(tam), self.personagens(tam)

    def mapa(self, tam):
        """
        :param tam: Tamanho necessário
        :return: list de list com instância de todos os blocos a ser exibidos
        """
        ii = self.coord[0] - tam[0] // 2
        ij = self.coord[1] - tam[1] // 2
        fi = ii + tam[0]
        fj = ij + tam[1]
        mapa = [i[ij:fj] for i in self.blocos[ii:fi]]
        return mapa

    def personagens(self, tam):
        coord = tam[0] // 2, tam[1] // 2
        return ((self.principal, coord),)
