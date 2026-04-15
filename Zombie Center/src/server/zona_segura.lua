local PhysicsService = game:GetService("PhysicsService")
local Lighting = game:GetService("Lighting")
local Workspace = game:GetService("Workspace")

local wallsFolder = Workspace:WaitForChild("SafeZoneWalls")
local zombiesFolder = Workspace:WaitForChild("Zombies")

local function crearGrupo(nombre)
	local ok, err = pcall(function()
		PhysicsService:RegisterCollisionGroup(nombre)
	end)
end

crearGrupo("Zombie")
crearGrupo("SafeWall")

PhysicsService:CollisionGroupSetCollidable("Default", "SafeWall", false)
PhysicsService:CollisionGroupSetCollidable("Zombie", "SafeWall", true)

local function ponerGrupoModelo(modelo, grupo)
	for _, obj in ipairs(modelo:GetDescendants()) do
		if obj:IsA("BasePart") then
			obj.CollisionGroup = grupo
		end
	end
end

local function ponerGrupoWalls()
	for _, wall in ipairs(wallsFolder:GetChildren()) do
		if wall:IsA("BasePart") then
			wall.CollisionGroup = "SafeWall"
		end
	end
end

local function ponerGrupoZombies()
	for _, zombie in ipairs(zombiesFolder:GetChildren()) do
		if zombie:IsA("Model") then
			ponerGrupoModelo(zombie, "Zombie")
		end
	end
end

local function esDeNoche()
	local hora = Lighting.ClockTime
	return hora >= 18 or hora < 6
end

local function actualizarWalls()
	local activar = not esDeNoche()

	for _, wall in ipairs(wallsFolder:GetChildren()) do
		if wall:IsA("BasePart") then
			wall.CanCollide = activar
		end
	end
end

ponerGrupoWalls()
ponerGrupoZombies()
actualizarWalls()

zombiesFolder.ChildAdded:Connect(function(zombie)
	task.wait(0.1)
	if zombie:IsA("Model") then
		ponerGrupoModelo(zombie, "Zombie")
	end
end)

while true do
	actualizarWalls()
	task.wait(1)
end