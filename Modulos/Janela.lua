jogo = nil

Janela = {}

function Janela:new(obj)
	local obj = obj or {}
	setmetatable(obj, self)
	self.__index = self
	--new.tela = jogo()

	obj.__fullscreen = false
	obj.tam = {x = 100, y = 100}
	
	return obj
end

function Janela:tamanho(tam, fullscreen)
	self.tam = tam
	if fullscreen == nil then
		print("fullscreen = nil")
	elseif fullscreen then
		print(fullscreen)
		self.__fullscreen = true
		love.window.setFullscreen(self.__fullscreen)
	else
		-- Muda para redimensionavel
	end
end

function Janela:executar()
	--self.display.blit(self.tela.surface(), (0, 0))
	--pygame.display.flip()
end

function Janela.fullscreen()
	self.__fullscreen = not self.__fullscreen
	self.tamanho(self.tam, self._w_fullscreen)
	return self.__fullscreen
end

function Janela:resize(size)
	self.tam = size
	self.tamanho(self.tam, self.__fullscreen)
	self.tela.tamanho(self.tam)
end

function Janela:draw()
	-- Não tenho ideia do que fazer
end

return Janela:new()
