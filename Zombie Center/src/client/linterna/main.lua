local Player = game.Players.LocalPlayer
local UserInput = game:GetService("UserInputService")



UserInput.InputBegan:Connect(function(Input)
	if script.Parent.Parent.Name == "Backpack" then
	else
		if Input.KeyCode == Enum.KeyCode.F then							
			if script.Parent.Handle.SpotLight.Enabled == true then		
				script.Parent.Handle.SpotLight.Enabled = false			
				script.Parent.Handle.Sound:Play()
			else
				script.Parent.Handle.SpotLight.Enabled = true
				script.Parent.Handle.Sound:Play()
			end
		end
	end
	
end)