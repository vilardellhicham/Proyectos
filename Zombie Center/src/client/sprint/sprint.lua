---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 

local UIS = game:GetService('UserInputService')
local Player = game.Players.LocalPlayer
local Character = Player.Character

---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 

UIS.InputBegan:connect(function(input) -- When a player has pressed Left Shift it will play the animation and it will set the normal walking speed (16) to 35.
 if input.KeyCode == Enum.KeyCode.LeftShift then
  Character.Humanoid.WalkSpeed = 26
  local Anim = Instance.new('Animation')
		Anim.AnimationId = 'rbxassetid://12559679883'
  PlayAnim = Character.Humanoid:LoadAnimation(Anim)
  PlayAnim:Play()
 end
end)

---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 

UIS.InputEnded:connect(function(input)
 if input.KeyCode == Enum.KeyCode.LeftShift then
  Character.Humanoid.WalkSpeed = 12
  PlayAnim:Stop()
 end
end)

---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 