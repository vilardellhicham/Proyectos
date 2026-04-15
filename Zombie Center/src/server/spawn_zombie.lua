local ServerStorage = game:GetService("ServerStorage")
local Workspace = game:GetService("Workspace")
local Lighting = game:GetService("Lighting")

local zombieModelo = ServerStorage:WaitForChild("Zombie")
local carpetaSpawns = Workspace:WaitForChild("Zombie Spawns")
local carpetaZombies = Workspace:WaitForChild("Zombies")

local function esDeNoche()
	local hora = Lighting.ClockTime
	return hora >= 18 or hora < 6
end

local function obtenerSpawnAleatorio()
	local spawns = carpetaSpawns:GetChildren()

	if #spawns == 0 then
		return nil
	end

	return spawns[math.random(1, #spawns)]
end

local function contarZombies()
	return #carpetaZombies:GetChildren()
end

while true do
	local maxZombies = 20
	local tiempoEspera = 8

	if esDeNoche() then
		maxZombies = 40
		tiempoEspera = 3
	end

	if contarZombies() < maxZombies then
		local spawn = obtenerSpawnAleatorio()

		if spawn then
			local nuevoZombie = zombieModelo:Clone()
			nuevoZombie.Parent = carpetaZombies
			nuevoZombie:MoveTo(spawn.Position + Vector3.new(0, 3, 0))
		end
	end

	task.wait(tiempoEspera)
end