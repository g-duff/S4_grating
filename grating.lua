S = S4.NewSimulation()

-- Define parameters

-- Number of harmonics
n_harm = 11

-- Geometrical parameters
a = 450            -- Period
radius = 75        -- Radius
t_grating = 150    -- Grating thickness 

-- Material parameters
RI_cover = 1.33
RI_grating = 2.0
RI_substrate = 1.45

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

outfile = io.open('spectrum.txt', 'w')

-- Write header
outfile:write('wav\tinc\t\t\t\t\ttrn\t\t\t\t\tref\n')

-- Scan wavelength
for lambda = 600,700,1 do
	freq = 1/lambda
	S:SetFrequency(freq)

	transmission = S:GetPowerFlux('substrate')
	inc, reflection = S:GetPowerFlux('cover')

	-- Save to file
	outfile:write(lambda, '\t', inc, '\t', transmission, '\t', -reflection, '\n')
end

outfile:close()