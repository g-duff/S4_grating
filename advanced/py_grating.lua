S = S4.NewSimulation()

-- Load parameters: 
pcall(loadstring(S4.arg))
-- lambda
-- n_harm
-- a
-- radius
-- t_grating
-- RI_cover
-- RI_grating
-- RI_substrate

-- 1D simulation for now
S:SetLattice({a, 0}, {0, 0})
S:SetNumG(n_harm)

-- !! Convention !!
-- Materials have upper case names.
-- Layers have lower case names

-- Set up materials
S:AddMaterial('Cover', {RI_cover*RI_cover, 0})
S:AddMaterial('Grating', {RI_grating*RI_grating, 0})
S:AddMaterial('Substrate', {RI_substrate*RI_substrate, 0})

-- Layers
S:AddLayer('cover', 0, 'Cover')
S:AddLayer('grating', t_grating, 'Grating')
S:AddLayer('substrate', 0, 'Substrate')

-- Structure

S:SetLayerPatternRectangle(
	'grating',
	'Cover',
	{a/2, 0},
	0,
	{radius, 0}
)

-- Source
S:SetExcitationPlanewave(
	{0, 0}, -- phi in [0,180), theta in [0,360)
    {0, 0}, -- s-polarization amplitude and phase in degrees
    {1, 0}  -- p-polarization
)

-- Scan wavelength

freq = 1/lambda
S:SetFrequency(freq)

transmission = S:GetPowerFlux('substrate')
inc, reflection = S:GetPowerFlux('cover')
print(lambda, inc, transmission, -reflection)

-- Field plots
freq = 1/lambda
S:SetFrequency(freq)

-- Output epsilon
if eps_plot == 1 then
	local eps_outfile = io.open("epsilon.txt","w")
	for z = a/2, -1*a/2, -1 do
		for x = 1, a, 1 do
			eps_outfile:write(S:GetEpsilon({x,0,z}), '\t')
		end
		eps_outfile:write('\n')
	end
end

if all_field_plot == 1 then
	for z = a/2, -1*a/2, -1 do
		S:GetFieldPlane(z, {a, 1}, 'FileAppend', 'fields')
	end
end