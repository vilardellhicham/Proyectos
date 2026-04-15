-- // Models
local Gun = script.Parent
local Handle = Gun:FindFirstChild("Handle")
local Bullet = Gun:FindFirstChild("Bullet")
local GlockModel = Gun:FindFirstChild("GlockModel")
local MuzzleFlashEffect = Gun:FindFirstChild("MuzzleFlashEffect")

-- // Sounds
local MagOut = Handle:FindFirstChild("MagOut")
local Magin = Handle:FindFirstChild("Magin")
local FireS = Handle:FindFirstChild("Fire")
local Click = Handle:FindFirstChild("Click")

local FireEvent = script.FireEvent
local Reload = script.Reload

local AmmoFolder = script.AmmoFolder
local Configuration = script.Configuration

-- // Services
local Debris = game:GetService("Debris")
local TweenService = game:GetService("TweenService")

local AnimationFolder = script.Animations

-- // Gun Configurations (set true = enabled, set false = disabled)
local showbeam = true
local headshots = true
local lockfirstperson = false
local magsize = 17
local maxdistance = 55
local showbullets = true
local selfdmg = false
local smoketrail = true
local debugging = false

local CanReload = true -- do not touch
local CanShoot = true  -- do not touch
local Debounce = false -- do not touch

local Player:Player = nil
local Character:Model = nil
local Humanoid = nil
local AmmoGui = script.AmmoGui:Clone()
AmmoGui.Name = "AmmoGui_Clone"
AmmoGui.Label.Text = "Ammo: "..AmmoFolder.Ammo.Value.."/"..AmmoFolder.Mag.Value

Gun.CanBeDropped = false -- // do not touch

local function _fire(tag_owner, endpos)
    Handle.Fire:Play()
    local startPos = Gun.MuzzleFlashEffect.Position
    local direction = endpos - startPos
    local distance = math.min(direction.Magnitude, maxdistance)
    local clampedEnd = startPos + direction.Unit * distance

    local part = Instance.new("Part")
    part.Material = Enum.Material.Neon
    part.Color = Color3.fromRGB(255, 250, 175)
    part.Anchored = true
    part.CanCollide = false
    part.Size = Vector3.new(0.05, 0.05, distance)
    if showbeam then
        part.Transparency = 0.5
    else
        part.Transparency = 1
    end

    part.CFrame = CFrame.lookAt(startPos, clampedEnd) * CFrame.new(0, 0, -distance/2)
    part.Parent = workspace
    
    part.Touched:Connect(function(hit)
        local humanoid = hit.Parent:FindFirstChildOfClass("Humanoid")
        if not humanoid then return end
        local isOwner = (hit.Parent.Name == tag_owner.Name)
        local dmg = Configuration.Damage.Value
        if isOwner and selfdmg then
            if headshots and hit.Name == "Head" then
                dmg *= 2
                if debugging then
                    print("headshot - x2 damage")
                end
            end
            humanoid:TakeDamage(dmg)
        elseif not isOwner then
            if headshots and hit.Name == "Head" then
                dmg *= 2
                if debugging then
                    print("headshot - x2 damage")
                end
            end
            humanoid:TakeDamage(dmg)
        end
    end)

    
    if showbeam then
        TweenService:Create(part,TweenInfo.new(0.07),{Transparency = 1}):Play()
    end
    Debris:AddItem(part, 0.05)
    
    if showbullets then
        local BulletEffect = Gun.Bullet:Clone()
        BulletEffect.Parent = workspace
        BulletEffect.WeldConstraint:Destroy()
        BulletEffect.Transparency = 0
        Handle.Drop:Play()
        
        task.spawn(function()
            task.wait(3) -- // wait for 3 seconds to continue this part only
            TweenService:Create(BulletEffect,TweenInfo.new(5),{Transparency = 1}):Play()
            Debris:AddItem(BulletEffect, 6)
        end)
    end
    
    AmmoFolder.Ammo.Value = AmmoFolder.Ammo.Value - 1
    
    GlockModel.Slide.Transparency = 1
    GlockModel.SlideEffect.Transparency = 0
    MuzzleFlashEffect.Flash.Enabled = true
    MuzzleFlashEffect.Particle.Enabled = true
    MuzzleFlashEffect.PointLight.Enabled = true
    task.wait(0.05)
    GlockModel.Slide.Transparency = 0
    GlockModel.SlideEffect.Transparency = 1
    MuzzleFlashEffect.Flash.Enabled = false
    MuzzleFlashEffect.Particle.Enabled = false
    MuzzleFlashEffect.PointLight.Enabled = false
end

local function _stopAnims()
    for i, track in ipairs(Humanoid.Animator:GetPlayingAnimationTracks()) do
        track:Stop()
    end
end

Gun.Equipped:Connect(function()
    Player = game:GetService("Players"):GetPlayerFromCharacter(Gun.Parent)
    Character = Player.Character
    Humanoid = Character:FindFirstChildOfClass("Humanoid")
    
    local Animation_Idle = Humanoid:LoadAnimation(AnimationFolder.Idle)
    Animation_Idle.Looped = true
    Animation_Idle.Priority = Enum.AnimationPriority.Action
    Animation_Idle:Play()
    if lockfirstperson then
        Player.CameraMode = Enum.CameraMode.LockFirstPerson
    end
    if Player then
        AmmoGui.Parent = Player.PlayerGui
    end
end)

Gun.Unequipped:Connect(function()
    AmmoGui.Parent = script
    _stopAnims()
    if lockfirstperson then
        Player.CameraMode = Enum.CameraMode.Classic
    end
end)

AmmoFolder.Ammo.Changed:Connect(function()
    if AmmoFolder.Ammo.Value < 1 then
        task.wait(0.3)
        Click:Play()
        GlockModel.Slide.Transparency = 1
        GlockModel.SlideEffect.Transparency = 0
    end
    AmmoGui.Label.Text = "Ammo: "..AmmoFolder.Ammo.Value.."/"..AmmoFolder.Mag.Value
    if debugging then
        print(AmmoFolder.Ammo.Value .. " ammo left")
    end
end)

AmmoFolder.Mag.Changed:Connect(function()
    AmmoGui.Label.Text = "Ammo: "..AmmoFolder.Ammo.Value.."/"..AmmoFolder.Mag.Value
    if debugging then
        print(AmmoFolder.Mag.Value .. " mag size changed")
    end
end)

FireEvent.OnServerEvent:Connect(function(player, pos)
    if Debounce == false and CanShoot then
        Debounce = true
        if AmmoFolder.Ammo.Value > 0 then
            if debugging then
                print(player.Name .. " fired")
            end
            _fire(player, pos)
            
            local fireAnim = player.Character:FindFirstChildOfClass("Humanoid"):LoadAnimation(AnimationFolder.Fire)
            fireAnim.Priority = Enum.AnimationPriority.Action4
            fireAnim:Play()
            
            if smoketrail and not MuzzleFlashEffect.SmokeTrail.Enabled then
                task.spawn(function()
                    MuzzleFlashEffect.SmokeTrail.Enabled = true
                    task.wait(5)
                    MuzzleFlashEffect.SmokeTrail.Enabled = false
                end)
            end
        else
            if debugging then
                print(player.Name .. " fired, no ammo")
            end
            Click:Play()
        end
        
        task.wait(Configuration.Delay.Value)
        Debounce = false
    end
end)

Reload.OnServerEvent:Connect(function(player)
    if CanReload and AmmoFolder.Mag.Value >= 1 and AmmoFolder.Ammo.Value ~= magsize then
        CanShoot = false
        CanReload = false
        script.Reloading.Value = true -- // this is for the local script
        MagOut:Play()

        GlockModel.Magazine.Transparency = 1
        local Mag = GlockModel.Magazine:Clone()
        Mag.WeldConstraint:Destroy()
        Mag.Parent = workspace
        Mag.Transparency = 0

        -- // take a bit longer to reload if you wasted all ammo
        task.spawn(function() -- // plays the sound
            task.wait(1)
            Magin:Play()
            GlockModel.Magazine.Transparency = 0

            task.wait(3)
            TweenService:Create(Mag,TweenInfo.new(5),{Transparency = 1}):Play()
            Debris:AddItem(Mag, 6)
        end)
        if AmmoFolder.Ammo.Value > 1 then
            local reloadAnimAmmo = player.Character:FindFirstChildOfClass("Humanoid"):LoadAnimation(AnimationFolder.Reload_WithAmmo)
            reloadAnimAmmo.Priority = Enum.AnimationPriority.Action4
            reloadAnimAmmo:Play()
            task.wait(2.5)
        elseif AmmoFolder.Ammo.Value < 1 then
            local reloadAnim = player.Character:FindFirstChildOfClass("Humanoid"):LoadAnimation(AnimationFolder.Reload_NoAmmo)
            reloadAnim.Priority = Enum.AnimationPriority.Action4
            reloadAnim:Play()
            task.wait(3.5)
        end
        
        task.spawn(function()
            task.wait(0.05)
            Click:Play()
            GlockModel.Slide.Transparency = 0
            GlockModel.SlideEffect.Transparency = 1
        end)
        -- // math time (actual reload)
        local needed = magsize
        local available = AmmoFolder.Mag.Value

        local toLoad = math.min(needed, available)
        AmmoFolder.Ammo.Value = toLoad
        AmmoFolder.Mag.Value = available - toLoad
        
        CanShoot = true
        CanReload = true
        script.Reloading.Value = false
    end
end)