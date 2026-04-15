local zombie = script.Parent
local humanoid = zombie:WaitForChild("Humanoid")
local root = zombie:WaitForChild("HumanoidRootPart")
local players = game:GetService("Players")

local dano = 10
local distanciaAtaque = 4
local distanciaDeteccion = 150
local atacando = false
local muerto = false

-- IMPORTANTE: para que no se rompa al morir
humanoid.BreakJointsOnDeath = false

-- ANIMATOR
local animator = humanoid:FindFirstChildOfClass("Animator")
if not animator then
	animator = Instance.new("Animator")
	animator.Parent = humanoid
end

-- ANIMACIONES
local idleAnim = Instance.new("Animation")
idleAnim.AnimationId = "rbxassetid://126695743897939"

local walkAnim = Instance.new("Animation")
walkAnim.AnimationId = "rbxassetid://78842123301625"

local attackAnim = Instance.new("Animation")
attackAnim.AnimationId = "rbxassetid://139779780707531"

local idleTrack = animator:LoadAnimation(idleAnim)
local walkTrack = animator:LoadAnimation(walkAnim)
local attackTrack = animator:LoadAnimation(attackAnim)

idleTrack.Looped = true
walkTrack.Looped = true
attackTrack.Looped = false
attackTrack.Priority = Enum.AnimationPriority.Action

local function pararAnimaciones()
	if idleTrack.IsPlaying then
		idleTrack:Stop(0.1)
	end

	if walkTrack.IsPlaying then
		walkTrack:Stop(0.1)
	end

	if attackTrack.IsPlaying then
		attackTrack:Stop(0.1)
	end
end

local function reproducirIdle()
	if not atacando and not muerto then
		if walkTrack.IsPlaying then
			walkTrack:Stop(0.2)
		end

		if not idleTrack.IsPlaying then
			idleTrack:Play(0.2)
		end
	end
end

local function reproducirWalk()
	if not atacando and not muerto then
		if idleTrack.IsPlaying then
			idleTrack:Stop(0.2)
		end

		if not walkTrack.IsPlaying then
			walkTrack:Play(0.2)
		end
	end
end

local function reproducirAtaque()
	if muerto then
		return
	end

	atacando = true

	if idleTrack.IsPlaying then
		idleTrack:Stop(0.1)
	end

	if walkTrack.IsPlaying then
		walkTrack:Stop(0.1)
	end

	attackTrack:Play(0.1)
end

local function jugadorMasCercano()
	local objetivo = nil
	local distanciaMinima = math.huge

	for _, player in pairs(players:GetPlayers()) do
		local character = player.Character

		if character and character:FindFirstChild("HumanoidRootPart") and character:FindFirstChild("Humanoid") then
			if character.Humanoid.Health > 0 then
				local distancia = (character.HumanoidRootPart.Position - root.Position).Magnitude

				if distancia < distanciaMinima then
					distanciaMinima = distancia
					objetivo = character
				end
			end
		end
	end

	return objetivo, distanciaMinima
end

-- AL MORIR
humanoid.Died:Connect(function()
	muerto = true
	atacando = false

	pararAnimaciones()

	-- que no siga moviéndose ni atacando
	humanoid.WalkSpeed = 0
	humanoid:MoveTo(root.Position)

	-- opcional: que el cadáver no empuje raro
	for _, obj in ipairs(zombie:GetDescendants()) do
		if obj:IsA("BasePart") then
			obj.CanTouch = false
		end
	end
end)

idleTrack:Play()

while true do
	task.wait(0.2)

	-- si está muerto, ya no hace nada más
	if muerto or humanoid.Health <= 0 then
		break
	end

	local objetivo, distancia = jugadorMasCercano()

	if objetivo and distancia <= distanciaDeteccion then
		if not atacando then
			humanoid:MoveTo(objetivo.HumanoidRootPart.Position)

			if distancia > distanciaAtaque then
				reproducirWalk()
			else
				reproducirAtaque()

				-- comprobar otra vez que siga vivo antes de hacer daño
				if not muerto and humanoid.Health > 0 then
					objetivo.Humanoid:TakeDamage(dano)
				end

				task.wait(1)

				atacando = false

				if not muerto then
					if distancia > distanciaAtaque then
						reproducirWalk()
					else
						reproducirIdle()
					end
				end
			end
		end
	else
		humanoid:MoveTo(root.Position)
		reproducirIdle()
	end
end