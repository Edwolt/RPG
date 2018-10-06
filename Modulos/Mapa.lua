JSON = require "Libs/JSON"
from Personagens.Principal.Principal import Principal

Mapa = {}
function Mapa:new (mapa, coord)
  local obj = obj or {}
	setmetatable(obj, self)
	self.__index = self

  obj.data = require mapa
  obj.blocos = data.mapa

  for i,v in ipairs(table_name) do
    -- body...
  end

  return obj
end

function FunctionName (args)
  -- body...
end
class Mapa():
    def __init__(self, mapa, coord):
        """
        :param mapa:Nome do mapa (sem o '.json')
        :param coord:Coordenada do lugar onde a renderização ocorrerá
        :return:list de list com nome dos blocos
        """
        data = json.load(open(f'Mapa/{mapa}.json'))
        blocos = data['Mapa']
        self.__blocos = []
        for aux in blocos:  # intancia todos os blocos
            linha = []
            for b in aux:
                c = imp(f'Blocos.{b}.{b}')
                linha.append(c.Bloco())
            self.__blocos.append(linha)
        self.coord = coord
        self.principal = Principal()

    def get(self, tam):
        """
        :param tam: Tamanho necessário
        :return: mapa, personagens*
        persnoagens = lista de (personagem, (coordenadas))
        """
        return self.blocos(tam), self.personagens(tam)

    def blocos(self, tam):
        """
        :param tam: Tamanho necessário do mapa
        :return: list de list com instância de todos os blocos a ser exibidos
        """
        ii = self.coord[0] - tam[0] // 2
        ij = self.coord[1] - tam[1] // 2
        fi = ii + tam[0]
        fj = ij + tam[1]
        mapa = [i[ij:fj] for i in self.__blocos[ii:fi]]
        return mapa

    def personagens(self, tam):
        """
        :param tam: Tamanho necessário do mapa
        :return: list de list com instância de todos os blocos a ser exibidos
        """
        coord = tam[0] // 2, tam[1] // 2
        return ((self.principal, coord),)
