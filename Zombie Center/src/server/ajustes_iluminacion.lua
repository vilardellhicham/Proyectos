local Lighting = game:GetService("Lighting")
local atmosphere = Lighting:FindFirstChildOfClass("Atmosphere")

if not atmosphere then
	atmosphere = Instance.new("Atmosphere")
	atmosphere.Parent = Lighting
end

while true do
	task.wait(1)

	if Lighting.ClockTime >= 18 or Lighting.ClockTime < 5 then
		-- Noche
		atmosphere.Density = 0.9
		atmosphere.Offset = 0
		atmosphere.Haze = 3
		atmosphere.Glare = 0.07
		atmosphere.Color = Color3.fromRGB(65, 66, 65)
		atmosphere.Decay = Color3.fromRGB(0, 0, 0)
	else
		-- Día
		atmosphere.Density = 0.5
		atmosphere.Offset = 0
		atmosphere.Haze = 0
		atmosphere.Glare = 0.07
		atmosphere.Color = Color3.fromRGB(102, 145, 141)
		atmosphere.Decay = Color3.fromRGB(85, 106, 106)
	end
end

---

local Lighting = game:GetService("Lighting")
local atmosphere = Lighting:FindFirstChildOfClass("Atmosphere")

if not atmosphere then
	atmosphere = Instance.new("Atmosphere")
	atmosphere.Parent = Lighting
end

local esNoche = false

while true do
	task.wait(0.5)

	local hora = Lighting.ClockTime

	if (hora >= 18 or hora < 6) and not esNoche then
		esNoche = true
		print("CAMBIO A NOCHE")

		atmosphere.Density = 0.9
		atmosphere.Offset = 0
		atmosphere.Haze = 3
		atmosphere.Glare = 0.5
		atmosphere.Color = Color3.fromRGB(65, 66, 65)
		atmosphere.Decay = Color3.fromRGB(0, 0, 0)

	elseif hora >= 6 and hora < 18 and esNoche then
		esNoche = false
		print("CAMBIO A DIA")

		atmosphere.Density = 0.5
		atmosphere.Offset = 0
		atmosphere.Haze = 0
		atmosphere.Glare = 0.1
		atmosphere.Color = Color3.fromRGB(102, 145, 141)
		atmosphere.Decay = Color3.fromRGB(85, 106, 106)
	end
end