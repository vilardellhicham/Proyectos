local Lighting = game:GetService("Lighting")

local eraDeNoche = nil
Lighting.ClockTime = 9
while true do
	task.wait(0.1)
	Lighting.ClockTime = Lighting.ClockTime + 0.02

	if Lighting.ClockTime >= 24 then
		Lighting.ClockTime = Lighting.ClockTime - 24
	end

	local esDeNoche = Lighting.ClockTime >= 18 or Lighting.ClockTime < 6

	if esDeNoche ~= eraDeNoche then
		eraDeNoche = esDeNoche

		if esDeNoche then
			print("Es de noche", Lighting.ClockTime)
		else
			print("Es de día", Lighting.ClockTime)
		end
	end
end