local character = script.Parent
local humanoid = character:WaitForChild("Humanoid")
local head = character:WaitForChild("Head")
local runService = game:GetService("RunService")

humanoid.CameraOffset = Vector3.new(0, 0, -0.6)

local function aplicarPrimeraPersona()
	for _, obj in ipairs(character:GetDescendants()) do
		if obj:IsA("BasePart") then
			if obj == head then
				obj.LocalTransparencyModifier = 1

			elseif obj:FindFirstAncestorOfClass("Accessory") then
				obj.LocalTransparencyModifier = 1

			else
				obj.LocalTransparencyModifier = 0
			end

		elseif obj:IsA("Decal") and obj.Parent == head then
			obj.Transparency = 1
		end
	end
end

runService.RenderStepped:Connect(aplicarPrimeraPersona)