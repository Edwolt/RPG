local Janela = require "Modulos/Janela"
fps = true

function love.load()
	Janela:tamanho({x = 500, y = 500})
end

function love.draw()
	if fps then
		love.graphics.print({{255, 255, 255}, love.timer.getFPS()}, 0, 0)
	end
end

function love.update(dt)

	--resizes
end

function love.keypressed(key)
	if key == 'escape' then
		love.event.quit()
	elseif key == 'f11' then
		love.window.setFullscreen(true)
	elseif key == 'f5' then
		love.event.quit('restart')
	-- elseif key == 'f1' then "ajuda" end
	end
end

function love.resize(w, h)
	-- body...
end

--[[
function love.focus(bool)
end

function love.keypressed(key, unicode)
end

function love.keyreleased(key, unicode)
end

function love.mousepressed(x, y, button)

end

function love.mousereleased(x, y, button)
end

function love.quit()
end

function insideBox(px, py, x, y, wx, wy)
  if px > x and px < x + wx then
    if py > y and py < y + wy then
      return true
    end
  end
  return false
end
--]]
