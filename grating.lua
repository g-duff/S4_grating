S = S4.NewSimulation()

-- Load parameters: 
pcall(loadstring(S4.arg))
-- lambda
-- a
-- radius
-- t_grating
-- RI_cover
-- RI_grating
-- RI_substrate

-- 1D simulation for now
S:SetLattice({a, 0}, {0, 0})
S:SetNumG(11)

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