-- // Declarations
local Gun = script.Parent
local Main = Gun:FindFirstChild("Main")
local FireEvent = Main:FindFirstChild("FireEvent")
local Reload = Main:FindFirstChild("Reload")

local Player = game.Players.LocalPlayer
local MobileGui = script.MobileGui:Clone()
MobileGui.Name = "MobileGui_Clone"
local UserInputService = game:GetService("UserInputService")
local Cursor = Player:GetMouse()

local IsEquipped = false -- // do not touch this
local ReloadKey = Enum.KeyCode.R -- // you can change this to whatever key you want to reload
local TweenService = game:GetService("TweenService")
local RunService = game:GetService("RunService")

local _initialized = false
local _recoilPitch = 0
local _recoilYaw = 0
local _recoilBack = 0

local _prevRecoilCFrame = CFrame.new()
local _damping = 10
local _stiffness = 60

local function _deg2rad(d) return d * math.pi / 180 end

local function _ensureInit()
	if _initialized then return end
	_initialized = true

	RunService:BindToRenderStep("GunRecoil_" .. Gun.Name, Enum.RenderPriority.Camera.Value + 1, function(dt)
		local camera = workspace.CurrentCamera
		if not camera then return end

		local naturalCFrame = camera.CFrame * _prevRecoilCFrame:Inverse()

		local pitchRad = _deg2rad(-_recoilPitch)
		local yawRad = _deg2rad(_recoilYaw)

		local rotCFrame = CFrame.Angles(pitchRad, yawRad, 0)
		local backCFrame = CFrame.new(0, 0, -_recoilBack)
		local newRecoilCFrame = rotCFrame * backCFrame

		camera.CFrame = naturalCFrame * newRecoilCFrame
		_prevRecoilCFrame = newRecoilCFrame

		local decay = 1 - math.exp(-_damping * dt)
		_recoilPitch = _recoilPitch * (1 - decay)
		_recoilYaw = _recoilYaw * (1 - decay)
		_recoilBack = _recoilBack * (1 - decay * (_stiffness / 60))
	end)
end

function ApplyRecoil(a, b, c)
    if Gun.Main.AmmoFolder.Ammo.Value < 1 then return end
    local pitchDeg, yawDeg, backOffset
    if type(a) == "table" then
        local t = a
        pitchDeg = t.Pitch or 0
        yawDeg = t.Yaw or 0
        backOffset = t.Back or 0
        if t.damping then _damping = t.damping end
        if t.stiffness then _stiffness = t.stiffness end
    else
        pitchDeg = a or 0
        yawDeg = b or 0
        backOffset = c or 0
    end

    _ensureInit()
    _recoilPitch = _recoilPitch + pitchDeg
    _recoilYaw = _recoilYaw + yawDeg
    _recoilBack = _recoilBack + backOffset
end

-- // Events
Gun.Equipped:Connect(function()
    if UserInputService.TouchEnabled then
        MobileGui.Parent = Player.PlayerGui
    end
    IsEquipped = true
end)

Gun.Unequipped:Connect(function()
	MobileGui.Parent = script
	IsEquipped = false

	RunService:UnbindFromRenderStep("GunRecoil_" .. Gun.Name)
	_initialized = false
	_recoilPitch = 0
	_recoilYaw = 0
	_recoilBack = 0
	_prevRecoilCFrame = CFrame.new()
end)

Cursor.Button1Down:Connect(function()
	if IsEquipped and not UserInputService.TouchEnabled then
		FireEvent:FireServer(Cursor.Hit.Position)
		if not Gun.Main.Reloading.Value then
			ApplyRecoil(4.5, math.random(-2,2), 0.2)
		end
	end
end)

UserInputService.InputBegan:Connect(function(Input, gameProcessed)
    if IsEquipped then
        if gameProcessed then return end
        if Input.KeyCode == ReloadKey then
            Reload:FireServer(Player)
        end
    end
end)