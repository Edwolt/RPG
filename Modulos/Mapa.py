import json
from importlib import import_module as imp


class Mapa():
    def __init__(self, mapa, coord):
        """
        :param mapa:Nome do mapa (sem o '.json')
        :param coord:Coordenada do lugar onde a renderização ocorrerá
        :return:list de list com nome dos blocos
        """
        data = json.load(open(f'Mapa/{mapa}.json'))
        self.blocos = data['Mapa']
        self.coord = coord

    def mapa(self, tam):
        ii = self.coord[0] - tam[0] // 2
        ij = self.coord[1] - tam[1] // 2
        fi = ii + tam[0]
        fj = ij + tam[1]

        tiles = [[None] * tam[1] for _ in range(tam[0])]
        for i in range(fi - ii):
            for j in range(fj - ij):
                aux = self.blocos[ii + i][ij + j]
                c = imp(f'Blocos.{aux}.{aux}')
                tiles[i][j] = c.Bloco()
        return tiles
