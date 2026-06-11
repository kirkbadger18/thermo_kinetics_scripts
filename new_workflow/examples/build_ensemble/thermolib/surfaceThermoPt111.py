
#!/usr/bin/env python
# encoding: utf-8
name = " "
shortDesc = u" "
longDesc = u"""
    
"""

entry(
    index = 1,
    label = "vacant",
    molecule =
    """
    1 X  u0 p0 c0
    """,
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
            0, 0, 0, 0,
            0, 0, 0], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
            0, 0, 0,   0,
            0, 0, 0], Tmin=(1000.0,'K'), Tmax=(3000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (3000.0, 'K'),
    ),
    metal = "Pt",
    facet = "111",
)
entry(
    index = 2,
    label = "XOC(OH)O",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {6,S}
2 O u0 p2 c0 {4,S} {5,S}
3 O u0 p2 c0 {4,D}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
5 H u0 p0 c0 {2,S}
6 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.0132821388160569, 0.03262761444819034, -3.70609620229599e-05, 2.0960399945931917e-08, -4.666935318875744e-12, -70967.17608921703, -4.753605859081658], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.852338703820633, -0.005708227788078347, 1.0285787142546047e-05, -5.567150394898063e-09, 1.0106515277124002e-12, -73924.19104203272, -64.44932362201482], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 3,
    label = "OHXCXNH",
    molecule = 
"""
1 X  u0  p0  c0  {5,D}
2 X  u0  p0  c0  {6,S}
3 H  u0  p0  c0  {4,S}
4 O  u0  p2  c0  {3,S} {5,S}
5 C  u0  p0  c0  {1,D} {4,S} {6,S}
6 N  u0  p1  c0  {2,S} {5,S} {7,S}
7 H  u0  p0  c0  {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.059603378477773736, 0.034935609033896455, -4.398559005685721e-05, 2.872753313401961e-08, -7.522175408214756e-12, -26553.18437287356, -0.9051810948806436], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.072883238272052, -0.0066430625083292415, 1.1791973540592518e-05, -6.2377041806638626e-09, 1.1116832344948537e-12, -29474.3188175315, -61.52692538119648], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 4,
    label = "XNH2",
    molecule = 
"""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.8779231964907284, 0.028356292059529015, -4.277511772669091e-05, 3.274076292859684e-08, -9.758152641713668e-12, -2857.4494217066567, 6.329215234815479], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.669208134866729, -0.004662982841009374, 8.163977816838163e-06, -4.222732181899948e-09, 7.383904944349786e-13, -4733.076666910141, -35.465519957953674], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 5,
    label = "HOOHX",
    molecule = 
"""
1 X  u0 p0 c0
2 O  u0 p2 c0 {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.965607169305528, 0.013397833711610185, -1.3429348910743593e-05, 7.1217535735940225e-09, -1.4106275643253041e-12, -20699.096105989232, -6.1546602361344185], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.635377420774269, -0.004641485401087584, 8.092560818044735e-06, -4.167621935915142e-09, 7.263870776245651e-13, -22128.235761717882, -34.81280986368097], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 47.7,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 6,
    label = "H2C(OH)OHX",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S} 
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 X u0 p0 c0 
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.9262964257920037, 0.023920989105911238, -1.1102898900090449e-05, -3.2747323226728277e-09, 3.4649234275040854e-12, -50572.401234955745, -0.7623583062370898], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.909711557027842, -0.011497669997516056, 2.0325661765180163e-05, -1.0702598454695946e-08, 1.8994728664480473e-12, -54152.61705768449, -67.87691592985098], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 7,
    label = "XCHNH",
    molecule = 
"""
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 N  u0  p1 c0 {2,D} {5,S}
4 H  u0  p0 c0 {2,S}
5 H  u0  p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.29622081982164633, 0.02186182173868537, -2.3841624349809043e-05, 1.4095772344583549e-08, -3.3882292775728435e-12, 2820.7446442340993, 6.20719667745149], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.412924206055754, -0.006234419168429111, 1.1089320642025945e-05, -5.887575614148772e-09, 1.0512695705615748e-12, 624.0089613584714, -37.771436165066646], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 35.45 and 72.61,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 8,
    label = "CHCCH3X",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {4,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 X u0 p0 c0 
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.4980431783247965, 0.028761410852525884, -2.6886207415432296e-05, 1.5278315434594736e-08, -3.782295348730434e-12, 13453.989361855023, -1.1152160899839618], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.832709469075109, -0.012370306795815036, 2.1968646610824228e-05, -1.1633958554052888e-08, 2.072175971251275e-12, 9957.404786355226, -69.01639675194647], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 51.8 and 63.4,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 9,
    label = "CH3CH3X",
    molecule = 
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {3,S}
9 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.213714766554295, 0.012214677635618211, 1.906867172991721e-05, -2.864543890631113e-08, 1.1057901507003212e-11, -17804.997460416307, -3.327324874228742], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.869135753367733, -0.017678324888408148, 3.1441525396766254e-05, -1.6706166686709798e-08, 2.983357157765762e-12, -22008.110925885758, -75.91017691123528], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 77.2,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 10,
    label = "CH2CCH2X",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,D} 
3 C u0 p0 c0 {2,D} {6,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 X u0 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.3465508681937564, 0.03320903539972369, -3.229875690035423e-05, 1.775209536279152e-08, -4.033785375564616e-12, 12114.060391936744, 3.586668830308689], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.940343194822113, -0.012271008997495392, 2.18143617452858e-05, -1.1572982503327585e-08, 2.064425915505187e-12, 8334.211257020399, -70.5497189473227], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 11,
    label = "XCO",
    molecule = 
"""
1 X  u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 O  u0  p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.4289500049941222, 0.014037447576690015, -2.211788493307807e-05, 1.7865951929107985e-08, -5.714789235501603e-12, -29337.783202731196, -7.78265449506427], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.48655590159597, -0.0016811753694007709, 3.0902927809275455e-06, -1.7118618035337593e-09, 3.158638326234654e-13, -30250.480711420772, -27.67879431440744], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 12,
    label = "HXNO",
    molecule = 
"""
1 X  u0  p0 c0  {3,D}
2 H  u0  p0 c0  {3,S}
3 N  u0  p0 c+1  {1,D} {2,S} {4,S}
4 O  u0  p3 c-1  {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.2935521890047679, 0.012551182982042065, -1.3054232810658336e-05, 7.661606345846852e-09, -1.9215519976261293e-12, -1949.1794341585764, -0.23897268998167043], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.516816120868313, -0.0038395477705153408, 6.878328650796626e-06, -3.6890021703325427e-09, 6.639618777921635e-13, -3300.715789600549, -26.75839396379392], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 38.5 and 75.09,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 13,
    label = "XCHO",
    molecule = 
"""
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 O  u0  p2 c0 {2,D}
4 H  u0  p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.339250160007176, 0.015618784211958003, -1.787059744142033e-05, 1.1610329818388465e-08, -3.2082745859831687e-12, -23929.23485999337, -4.27823121254485], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.472495173378918, -0.004256514294681343, 7.67239320040194e-06, -4.15093863969437e-09, 7.520567235450011e-13, -25490.90998137112, -35.277710319913915], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 14,
    label = "XCH2XO",
    molecule = 
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 O  u0 p2 c0 {2,S} {3,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.336104037206985, 0.02264833157564371, -2.3923904062309394e-05, 1.3725647869324616e-08, -3.24031677194947e-12, -18407.676136141177, -1.8821570475887368], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.524882752948642, -0.006507322736492783, 1.1658609319411942e-05, -6.25679872302614e-09, 1.1264920350747862e-12, -20757.215603038865, -48.42248077834853], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 15,
    label = "XCH",
    molecule = 
"""
1 X  u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.668050248245743, 0.02906934158394708, -4.826534047741306e-05, 3.875891275489789e-08, -1.1974940133636796e-11, -2202.555837509903, 9.72941567148859], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.904285233893887, -0.0026386317845829206, 4.717273616560156e-06, -2.5126614520237118e-09, 4.496578657019606e-13, -3748.8020481796216, -26.71071650546929], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 16,
    label = "CH2NHX",
    molecule = 
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 N  u0 p1 c0 {2,D} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.33906732275997425, 0.01798477825595378, -8.009982916328749e-06, -2.618495714675942e-09, 2.589058695332754e-12, 5067.07629386286, 4.139051614167242], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.264096776148266, -0.009024670506335649, 1.6030078456067276e-05, -8.501791662058619e-09, 1.5167125792205402e-12, 2318.710640888721, -47.2020197322819], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 57.54 and 70.14,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 17,
    label = "CH2CH2X",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 X u0 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.3072058473633485, 0.016596074222378177, -1.655930545991473e-06, -8.536442946610478e-09, 4.4981760076166914e-12, -1280.8591294500839, 1.0098718291946085], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.184219340604525, -0.011502113412652405, 2.0395033099924633e-05, -1.07880335315863e-08, 1.9199770884658133e-12, -4380.562590407206, -55.65808981144987], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 18,
    label = "XNXNCH3",
    molecule = 
"""
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,S}
3 N  u0 p1 c0 {1,D} {4,S}
4 N  u0 p1 c0 {2,S} {3,S} {5,S}
5 C  u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6 H  u0 p0 c0 {5,S}
7 H  u0 p0 c0 {5,S}
8 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.9091597854182405, 0.021534816166149242, -9.823256149640216e-06, -2.1902915402179213e-09, 2.463293213656941e-12, 7224.5717711539, -8.927473541433368], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.8638706713468, -0.010727740861067628, 1.918685524601173e-05, -1.0276920883878388e-08, 1.8476573029537742e-12, 3875.8867850055412, -70.90073735079142], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 19,
    label = "XOXONXO",
    molecule = 
"""
1 X  u0  p0 c0  {4,S}
2 X  u0  p0 c0  {5,S}
3 X  u0  p0 c0  {7,S}
4 O  u0  p2 c0  {1,S} {6,S}
5 O  u0  p2 c0  {2,S} {6,S}
6 N  u0  p1 c0  {4,S} {5,S} {7,S}
7 O  u0  p2 c0  {3,S} {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.5500231720187959, 0.030684206105841463, -3.99225072023528e-05, 2.5278307010786185e-08, -6.333111712595872e-12, -11139.491307862136, 4.895473068055269], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.242163565452627, -0.002912243993637214, 5.391992059112484e-06, -3.0311859439479518e-09, 5.661916867178293e-13, -13440.727179890926, -43.40458862882762], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 71.1 and 71.28,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 20,
    label = "XCH2CH2OH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {2,S} {6,S} {7,S} {9,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
9 X u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.945183765784283, 0.039565407112390746, -3.03930590885776e-05, 9.79288134938609e-09, -1.9580349623810398e-13, -30405.632742853122, 13.10648535006097], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.78474497567341, -0.015222651402037893, 2.709688403494845e-05, -1.4411817063468926e-08, 2.5770815660618024e-12, -35408.2490108514, -82.857180297327], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 93.4,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 21,
    label = "XCCHCH2",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {7,T}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 X u0 p0 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.2547974594252762, 0.03768477161070287, -3.93538300853427e-05, 2.1670816122968157e-08, -4.778586531948073e-12, -752.6801514386655, 4.10178996012694], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.93650384605931, -0.010360495826388488, 1.8520759493049464e-05, -9.908385668323627e-09, 1.7799918125583177e-12, -4629.792818919964, -72.84127316857649], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 22,
    label = "XCCH3",
    molecule = 
"""
1 X  u0 p0 c0 {3,T}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,T} {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.45723705208517446, 0.022226226542089316, -1.6672125815364453e-05, 5.721350274429687e-09, -3.993259712628866e-13, -11043.637571357007, -2.273251186122538], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.3070908359545, -0.0093662342059687, 1.6714987459785614e-05, -8.921820946018977e-09, 1.5993389382243973e-12, -13965.238916365972, -57.941090981236144], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 23,
    label = "OHXCNH2",
    molecule = 
"""
1 X  u0  p0  c0  {4,D}
2 H  u0  p0  c0  {3,S}
3 O  u0  p2  c0  {2,S} {4,S}
4 C  u0  p0  c0  {1,D} {3,S} {5,S}
5 N  u0  p1  c0  {4,S} {6,S} {7,S}
6 H  u0  p0  c0  {5,S}
7 H  u0  p0  c0  {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.9101436671161726, 0.03643404011150783, -4.229756549355626e-05, 2.6415082773360968e-08, -6.6956014433453335e-12, -35254.17694278089, 8.346366930110008], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.91701007435875, -0.00926653706859623, 1.641639902594674e-05, -8.660228499999005e-09, 1.539168749140775e-12, -38680.489820862014, -61.19155452417664], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 35.97 and 69.6,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 24,
    label = "XCH2XCOH",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {6,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
3 C u0 p0 c0 {1,S} {2,S} {8,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 X u0 p0 c0 {2,S}
8 X u0 p0 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.370072303985213, 0.045287910596407036, -5.444194442097456e-05, 3.432255409854695e-08, -8.711850798245208e-12, -25028.719903749658, 8.336923959367985], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.054535017277079, -0.00976944190759886, 1.7438340603680773e-05, -9.305566473333517e-09, 1.6687299317235396e-12, -29053.831984251083, -74.05547230281076], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 25,
    label = "XCHCH2CH3",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {9,S} {10,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
10 X u0 p0 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.6079226231525483, 0.03650726114655381, -1.7302814543711623e-05, -2.6327013416913424e-09, 3.772889866974306e-12, -9100.71689461996, 11.717971753958178], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[18.686827955849985, -0.018861773680335724, 3.369443801472732e-05, -1.8017038643905838e-08, 3.234258858636861e-12, -14756.22371910293, -93.34001995994643], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 74.1,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 26,
    label = "XCHXN",
    molecule = 
"""
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.15332858310194414, 0.02312968952463336, -3.289591524310939e-05, 2.441141741029369e-08, -7.243662148765799e-12, 7438.269806764215, -1.7896708283530005], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.537075162700196, -0.003857744837904004, 6.9347648321421656e-06, -3.733037510228149e-09, 6.738004794435977e-13, 5723.968254506039, -38.3205716008726], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 27,
    label = "NHXCXNH",
    molecule = 
"""
1 X  u0  p0  c0  {5,S}
2 X  u0  p0  c0  {6,S}
3 H  u0  p0  c0  {4,S}
4 N  u0  p1  c0  {3,S} {5,D}
5 C  u0  p0  c0  {1,S} {4,D} {6,S}
6 N  u0  p1  c0  {2,S} {5,S} {7,S}
7 H  u0  p0  c0  {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.7583010746346701, 0.04202640649853385, -5.6007549622670626e-05, 3.82518343892414e-08, -1.0409415095254682e-11, 6416.114011275009, 5.853435007059303], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.07746269192123, -0.006939943635357624, 1.236521892226283e-05, -6.576520685800326e-09, 1.1767578021891588e-12, 3162.4566526253548, -62.8944275280393], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 28,
    label = "XCH2CH2CH3",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {11,S}
3 C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.5789762985562977, 0.03719157388223185, -1.2289783678598454e-05, -8.771787112559921e-09, 6.0404016816608195e-12, -16729.959559090537, 1.4727804737150247], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[21.53639136789115, -0.021593251659390987, 3.852991815375113e-05, -2.0569188705878607e-08, 3.687559317805305e-12, -22972.89619440899, -113.39911485663337], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 29,
    label = "XNXCO",
    molecule = 
"""
1 X  u0  p0  c0  {3,D}
2 X  u0  p0  c0  {4,S}
3 N  u0  p1  c0  {1,D} {4,S}
4 C  u0  p0  c0  {2,S} {3,S} {5,D}
5 O  u0  p2  c0  {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.2626233879870643, 0.023970698739431546, -3.5780704318182904e-05, 2.6941746848058587e-08, -8.087009960850628e-12, -11006.273105587134, -6.660753257056404], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.29012905650921, -0.002447944211152241, 4.512489091232046e-06, -2.5131056378761975e-09, 4.657863977308473e-13, -12602.367918854969, -41.25291131865794], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 30,
    label = "XCXCH2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,T}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 X u0 p0 c0 {1,S}
6 X u0 p0 c0 {2,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.798156819591712, 0.03269962988077464, -4.2566240720676274e-05, 2.915425316615059e-08, -8.035869759058999e-12, -981.5993897069385, 5.848078286750203], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.430193864353257, -0.006459524000938785, 1.15448465749276e-05, -6.169032849306648e-09, 1.1071321585628248e-12, -3665.1811109898736, -50.122331998208224], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 31,
    label = "XCHCH2",
    molecule = 
"""
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 C  u0  p0 c0 {2,D} {5,S} {6,S}
4 H  u0  p0 c0 {2,S}
5 H  u0  p0 c0 {3,S}
6 H  u0  p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.30885927662681495, 0.028391690765813347, -3.0151741013964643e-05, 1.771975310154138e-08, -4.275926497500082e-12, 2890.2145970498877, 1.0285582468853116], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.34862772966723, -0.00890555764803352, 1.5846166631462863e-05, -8.417564162870206e-09, 1.5032445290368195e-12, -72.78897333437635, -57.93256823787196], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 32,
    label = "CHCHX",
    molecule = 
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,T} {4,S}
3 C  u0 p0 c0 {2,T} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.4723946570089228, 0.027761500010324784, -4.488251898572861e-05, 3.681376542297081e-08, -1.1613241209937689e-11, 21967.463805755026, 2.4117940024795494], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.532276249354998, -0.004937800530834081, 8.640805124047922e-06, -4.462031917930421e-09, 7.786509699998019e-13, 20256.695346634016, -36.66563106010004], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 90.3,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 33,
    label = "NH2NH2X",
    molecule = 
"""
1 X  u0 p0 c0
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 N  u0 p1 c0 {2,S} {6,S} {7,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.8809064009530958, 0.01832005447197403, -5.853305122751859e-06, -4.761998279178285e-09, 3.300733634111998e-12, -826.6415095553382, 1.6988643564214563], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.862720506682408, -0.011203105342302134, 1.9721649077576812e-05, -1.0314975633640902e-08, 1.8201024967927935e-12, -3887.489875509963, -55.20398705530151], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 78.71,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 34,
    label = "OCNHX",
    molecule = 
"""
1 X  u0  p0  c0
2 O  u0  p2  c0  {3,D}
3 C  u0  p0  c0  {2,D} {4,D}
4 N  u0  p1  c0  {3,D} {5,S}
5 H  u0  p0  c0  {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5496472816120783, 0.018460040636415147, -2.420011557528892e-05, 1.7347499422346073e-08, -5.041828697680698e-12, -19738.42940857665, -4.247754076100012], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.099138030435192, -0.00440017370726316, 7.814529710623416e-06, -4.1346645895368875e-09, 7.364136231451159e-13, -21314.46887539248, -36.920980913117546], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 26.05 and 32.19,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 35,
    label = "XCH2XCH",
    molecule = 
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {2,D} {3,S} {7,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.498417541283888, 0.047450528522402884, -6.331781316495387e-05, 4.414453018485055e-08, -1.2310067041985113e-11, -2411.503730815884, 16.95021684006932], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.43643647000544, -0.009004099585864357, 1.6092785440764184e-05, -8.59947060577506e-09, 1.543109239900355e-12, -6173.878281931633, -62.25648674441216], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 36,
    label = "CH2OX",
    molecule = 
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 O  u0 p2 c0 {2,D}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.152110996942741, -0.000548713269838846, 1.6858930763222785e-05, -1.833578687032829e-08, 6.296303898491239e-12, -18010.214410126802, -11.442038018232552], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.405125342133548, -0.006902169392499726, 1.2352154993938465e-05, -6.6236299189175004e-09, 1.1913644938348446e-12, -19491.293461147146, -34.8417937714809], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 51.8,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 37,
    label = "NH2XCNH",
    molecule = 
"""
1 X  u0  p0  c0  {5,S}
2 H  u0  p0  c0  {4,S}
3 H  u0  p0  c0  {4,S}
4 N  u0  p1  c0  {2,S} {3,S} {5,S}
5 C  u0  p0  c0  {1,S} {4,S} {6,D}
6 N  u0  p1  c0  {5,D} {7,S}
7 H  u0  p0  c0  {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.7328818439967254, 0.03226341547123992, -3.779588721612529e-05, 2.39865423535709e-08, -6.161561259148655e-12, -968.2080565061104, 1.3588567200874806], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.000118202323204, -0.00855706472628288, 1.50757717607447e-05, -7.885499031168206e-09, 1.392064987916781e-12, -3991.8055449228277, -60.25995205042936], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 37.45 and 56.05,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 38,
    label = "HCOOHX",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 X u0 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.356980056620526, 0.016581791078763862, -8.932461264885762e-06, -5.965982750789433e-10, 1.6571152953229613e-12, -47308.024111674924, -0.5431982669458293], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.047785403239047, -0.007242735447338841, 1.2909093310612405e-05, -6.880211246610009e-09, 1.2328948708400386e-12, -49711.33705929546, -45.472812777004705], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 39,
    label = "CH3OHX",
    molecule = 
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 O  u0 p2 c0 {2,S} {7,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.0573770366622774, 0.012862430408477442, 4.849282898966965e-06, -1.359971677078574e-08, 5.9690013787272024e-12, -30311.486594762202, -12.435901290161363], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.113484637206701, -0.011408785499328795, 2.0202999846960784e-05, -1.0664782664591096e-08, 1.8954586318005556e-12, -33268.91686789811, -65.26659990202504], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 40,
    label = "XCXC",
    molecule = 
"""
1 X  u0  p0 c0 {3,D}
2 X  u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,D} {4,D}
4 C  u0  p0 c0 {2,D} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.25761474874738755, 0.01938116350379463, -2.996920800648192e-05, 2.2777221278246303e-08, -6.826796760384756e-12, 28603.23977159043, -2.7041957235955687], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.608144321932299, -0.0014237719299395385, 2.6419804765132873e-06, -1.4828979981593626e-09, 2.765398935749608e-13, 27429.14424258368, -28.854131173898477], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 41,
    label = "XCXCHXC",
    molecule = 
"""
1 C u0 p0 c0 {5,T} {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3 C u0 p0 c0 {2,S} {7,T}
4 H u0 p0 c0 {2,S}
5 X u0 p0 c0 {1,T}
6 X u0 p0 c0 {2,S}
7 X u0 p0 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.9682704800610584, 0.04821224894335466, -7.020384273121975e-05, 5.07019151059013e-08, -1.445994708952662e-11, 20989.562942465123, 14.062523111455508], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.256157496066718, -0.0050105322334465935, 9.091203317717695e-06, -4.959962840140173e-09, 9.052380082508832e-13, 17787.276005380358, -55.908423137907015], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 42,
    label = "XCHXC",
    molecule = 
"""
1 X  u0  p0 c0 {3,S}
2 X  u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,S} {4,D} {5,S}
4 C  u0  p0 c0 {2,D} {3,D}
5 H  u0  p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.5903522097119523, 0.028202934292478124, -4.3192063602978775e-05, 3.320670371914228e-08, -1.0016174457682312e-11, 17113.543667014717, 0.22476856917821175], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.592976630010214, -0.003509999976756217, 6.290981326499577e-06, -3.3685196113277216e-09, 6.056093728215036e-13, 15311.78271860034, -39.79595746603347], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 43,
    label = "NH2XCNH2",
    molecule = 
"""
1 X  u0  p0  c0  {5,D}
2 H  u0  p0  c0  {4,S}
3 H  u0  p0  c0  {4,S}
4 N  u0  p1  c0  {2,S} {3,S} {5,S}
5 C  u0  p0  c0  {1,D} {4,S} {6,S}
6 N  u0  p1  c0  {5,S} {7,S} {8,S}
7 H  u0  p0  c0  {6,S}
8 H  u0  p0  c0  {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.4442595743928324, 0.03514339770716558, -3.825192302653209e-05, 2.319548009607335e-08, -5.75459180946177e-12, -14128.379685335178, 1.9827861973732404], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.745142833148192, -0.011132970575763266, 1.958511347707567e-05, -1.0221698091739705e-08, 1.8010348989170152e-12, -17726.92176521786, -70.1962128774334], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12.72 and 84.97,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 44,
    label = "XOOH",
    molecule = 
"""
1 X  u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.725342800689044, 0.014265171875489696, -2.214102493856669e-05, 1.7159765049347425e-08, -5.14814312649392e-12, -10262.389789654895, -5.88006553811517], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.853397119729436, -0.0020628080151690866, 3.577698202321133e-06, -1.8218777366792332e-09, 3.1470209026330443e-13, -11146.52022383995, -25.965533274356986], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 45,
    label = "NHCNHX",
    molecule = 
"""
1 X  u0  p0  c0
2 H  u0  p0  c0  {3,S}
3 N  u0  p1  c0  {2,S} {4,D}
4 C  u0  p0  c0  {3,D} {5,D}
5 N  u0  p1  c0  {4,D} {6,S}
6 H  u0  p0  c0  {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.846156642790234, 0.030516771396075195, -4.18817120297212e-05, 3.038457383443344e-08, -8.772416329839914e-12, 8892.833382330717, 1.700615505499023], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.071573387185454, -0.006359512441013695, 1.1223978101642147e-05, -5.882498218542703e-09, 1.0398326844665556e-12, 6507.980056408234, -48.97466045490009], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 24.23 and 51.07,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 46,
    label = "NH2NCH3CH3X",
    molecule = 
"""
1 X  u0 p0 c0
2 N  u0 p1 c0 {6,S} {7,S} {3,S}
3 N  u0 p1 c0 {2,S} {4,S} {5,S}
4 C  u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
5 C  u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {4,S}
9 H  u0 p0 c0 {4,S}
10 H  u0 p0 c0 {4,S}
11 H  u0 p0 c0 {5,S}
12 H  u0 p0 c0 {5,S}
13 H  u0 p0 c0 {5,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.9579330180191061, 0.03417770564757993, 2.8267495852693448e-06, -2.4576997665800892e-08, 1.15600742930037e-11, -3869.220416435536, 2.110355371825184], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[24.884336455473225, -0.025217715425044775, 4.4913391958504446e-05, -2.391309917222889e-08, 4.2785510613671765e-12, -10836.464085721367, -123.21620308424588], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 37.85 and 59.82,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 47,
    label = "XNNH2",
    molecule = 
"""
1 X  u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 N  u0 p1 c0 {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.5564403187484964, 0.02488188714228014, -3.188388763500215e-05, 2.1907623700767777e-08, -6.06237530691845e-12, 10135.826484813117, -4.096387110835597], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.380916008529832, -0.0057193476971602155, 1.0097870851768122e-05, -5.296762422400411e-09, 9.370114791384883e-13, 8019.267892742533, -48.125068033908434], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 48,
    label = "XOCH2CH3",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {9,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.4610676677654211, 0.025330921145967775, -2.95242209009532e-06, -1.2660211265186084e-08, 6.6114131458296666e-12, -24805.098426265857, 3.4586157511771223], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.750176987330857, -0.016155438293009517, 2.8860309377503062e-05, -1.5435826091871815e-08, 2.7715466243288713e-12, -29493.39483790385, -81.59739986318627], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 92.3,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 49,
    label = "H2C(XO)XO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 O u0 p2 c0 {2,S} {7,S}
6 X u0 p0 c0 {1,S}
7 X u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.36992382308205635, 0.028658534785216086, -2.789362740079327e-05, 1.3652630126583081e-08, -2.5391238552483443e-12, -30533.345909955147, -0.37003005164447345], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.223388913202939, -0.007741648307491574, 1.3941824756717029e-05, -7.54192199179161e-09, 1.3666941082028279e-12, -33614.39573598887, -60.680012872942854], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 50,
    label = "XCNH2",
    molecule = 
"""
1 X  u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 N  u0 p1 c0 {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.584673842667386, 0.021387552044394017, -2.668015623605442e-05, 1.808598934252459e-08, -4.9546824564792595e-12, -7436.838431306114, -8.56648207120059], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.406537419558042, -0.005399629101361455, 9.490931515118908e-06, -4.944497021698531e-09, 8.700337254353496e-13, -9329.462331037283, -47.67571447318059], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 51,
    label = "XNXCOH",
    molecule = 
"""
1 X  u0  p0  c0  {3,D}
2 X  u0  p0  c0  {4,D}
3 N  u0  p1  c0  {1,D} {4,S}
4 C  u0  p0  c0  {2,D} {3,S} {5,S}
5 O  u0  p2  c0  {4,S} {6,S}
6 H  u0  p0  c0  {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.2803831282764202, 0.026146384390467715, -3.320471756674164e-05, 2.1735485479466045e-08, -5.739487491855816e-12, -14128.200663893545, -6.266969158485124], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.200430727595318, -0.0043879749651592175, 7.853839355053178e-06, -4.205146700723268e-09, 7.568995228467198e-13, -16281.373583890425, -50.85661351700185], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 52,
    label = "XNCH2",
    molecule = 
"""
1 X  u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 N  u0 p1 c0 {1,S} {2,D}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.6873653025294285, 0.021323471976192207, -2.3360406477040266e-05, 1.4597552123790646e-08, -3.850955446746286e-12, 5488.966154187559, -4.107451403104054], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.37460626889264, -0.0066065295407903984, 1.179734633756829e-05, -6.297357397301241e-09, 1.12896181035644e-12, 3275.218936965224, -48.045670412522796], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 53,
    label = "XCH2XCCH2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {8,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {9,S} {3,D}
3 C u0 p0 c0 {2,D} {6,S} {7,S} 
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 X u0 p0 c0 {1,S}
9 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.7274622548171465, 0.049119325371859465, -5.721654044768814e-05, 3.6207137858058645e-08, -9.375809842604731e-12, 1266.5054634711596, 9.215069197535115], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.965377047817515, -0.012665113714302009, 2.2613281924845392e-05, -1.2071204745862839e-08, 2.1643101723100343e-12, -3382.493438929854, -84.83321141026437], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 54,
    label = "XNXCNH",
    molecule = 
"""
1 X  u0  p0  c0  {3,D}
2 X  u0  p0  c0  {4,S}
3 N  u0  p1  c0  {1,D} {4,S}
4 C  u0  p0  c0  {2,S} {3,S} {5,D}
5 N  u0  p1  c0  {4,D} {6,S}
6 H  u0  p0  c0  {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.1405831121465602, 0.033959292416325615, -4.877971612341176e-05, 3.545525158907157e-08, -1.0228439728204221e-11, 16315.888428157908, -0.9856607299109612], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.24475267233186, -0.004422998551696639, 7.940480940184433e-06, -4.26589935688731e-09, 7.694693377023069e-13, 13945.671696466969, -52.211920000743376], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 55,
    label = "XCCHO",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {5,T}
4 H u0 p0 c0 {2,S}
5 X u0 p0 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.1548810655929222, 0.024665037051840227, -2.7882913511991704e-05, 1.6743505869627745e-08, -4.172550138149023e-12, -17579.59560068276, 5.3619437952284805], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.176475948765468, -0.00539007542637278, 9.767400287521005e-06, -5.3271807146336225e-09, 9.715781104542564e-13, -19944.654979427527, -41.795967836379724], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 20.1 and 76.7,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 56,
    label = "XCOH",
    molecule = 
"""
1 X  u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.28139263446484447, 0.023606093198555125, -3.329588093361693e-05, 2.3593747683929012e-08, -6.599879438782627e-12, -26338.94761564112, -2.8493784919840888], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.57277082900458, -0.0031657760447325266, 5.6181105101654745e-06, -2.9683154839025576e-09, 5.2868333401445e-13, -28000.91843239935, -38.82968082223016], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 57,
    label = "XCXCO",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {5,T}
4 X u0 p0 c0 {2,S}
5 X u0 p0 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.8975832350898159, 0.024674308976670726, -3.701360738589572e-05, 2.8207320916726853e-08, -8.56860477682647e-12, -12291.197994039325, -4.673131984136443], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.17817278705946, -0.0027487134031397584, 5.0529587603136555e-06, -2.803442096559865e-09, 5.180249180917092e-13, -13947.100257168804, -40.51066000845178], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 58,
    label = "H2C(XO)OCH3",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {10,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {9,S}
3 H u0 p0 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {2,S}
10 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.6807989775914365, 0.031212614085878283, -8.078918199972394e-06, -1.0837717052028392e-08, 6.4822075098957106e-12, -42938.960705395075, -5.807858989802799], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[20.413209915942357, -0.017360169914598392, 3.107643496100142e-05, -1.667131923137997e-08, 3.000829590399239e-12, -48282.08790176174, -103.39678357761134], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 59,
    label = "ONOHX",
    molecule = 
"""
1 X  u0 p0 c0
2 O  u0 p2 c0 {3,D}
3 N  u0 p1 c0 {2,D} {4,S}
4 O  u0 p2 c0 {3,S} {5,S}
5 H  u0 p0 c0 {4,S}


""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.0356492132819912, 0.024037629200464355, -3.1071525074251956e-05, 2.127464792409261e-08, -5.936340198877723e-12, -17011.57526311954, 0.8423434700267176], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.32089714381821, -0.004524702085478232, 8.146691035409909e-06, -4.398954083740913e-09, 7.961290547003047e-13, -19016.48960266231, -40.56214840614903], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 29.74 and 57.23,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 60,
    label = "NH3X",
    molecule = 
"""
1 X  u0 p0 c0
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.563277768302388, 0.014266189084703357, -1.297394268483268e-05, 7.2687772699944656e-09, -1.6907441235130718e-12, -15060.26674187145, -4.452600333917612], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.417079278937878, -0.007111067319578444, 1.2402770669666947e-05, -6.3880650637720095e-09, 1.1128397494000864e-12, -16830.850693006927, -39.2566993633798], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 61,
    label = "XCN",
    molecule = 
"""
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,T}
3 N  u0  p1 c0 {2,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.767150742372571, 0.004179530908569143, -5.164604378217358e-06, 4.281737635298446e-09, -1.5327068827384986e-12, 12122.47926143606, -16.448667591168054], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.522340971904843, -0.0014872409729567407, 2.7115450958464748e-06, -1.4880455390745584e-09, 2.7250846956428665e-13, 11656.694537778145, -25.37243780029487], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 62,
    label = "XNHCH3",
    molecule = 
"""
1 X  u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 N  u0 p1 c0 {1,S} {2,S} {7,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.5872250132023423, 0.021884256339370783, -9.092104175481355e-06, -3.201306663136786e-09, 2.9345642363430316e-12, -4861.967379643853, -3.097726707288616], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.083471500413467, -0.011982981568694118, 2.130293023859158e-05, -1.1309806430634165e-08, 2.019021010621252e-12, -8346.03946382814, -67.8172995834919], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 63,
    label = "XNHCHO",
    molecule = 
"""
1 X  u0  p0  c0  {3,S}
2 H  u0  p0  c0  {3,S}
3 N  u0  p1  c0  {1,S} {2,S} {5,S}
4 H  u0  p0  c0  {5,S}
5 C  u0  p0  c0  {3,S} {4,S} {6,D}
6 O  u0  p2  c0  {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.5697196726291491, 0.026888163238631135, -2.505626252987531e-05, 1.146335605210907e-08, -1.8672548903182554e-12, -26386.700131056532, -3.354251835093125], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.974043749120295, -0.0077214752537399685, 1.3817669473435759e-05, -7.405220214460908e-09, 1.3327037888206146e-12, -29367.029964984424, -61.47032343457707], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 64,
    label = "XCHOH",
    molecule = 
"""
1 X  u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.5007061985259844, 0.0203875077973531, -1.8341226826130557e-05, 8.05212148252645e-09, -1.1760122693690211e-12, -23313.13407947019, 7.42264406771336], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.403556573032391, -0.0065645158086063546, 1.17183645532985e-05, -6.2584705957162855e-09, 1.122749263845731e-12, -25643.35312827412, -37.96808920560764], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 58.4,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 65,
    label = "XCXCCH3",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {7,T} 
2 C u0 p0 c0 {1,S} {8,D} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S} 
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 X u0 p0 c0 {1,T}
8 X u0 p0 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.17029377525203263, 0.026818227569819247, -2.118799915814212e-05, 8.209916318310437e-09, -1.0277617592212064e-12, 5547.584461627022, 4.1994416697191355], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.950280567865766, -0.010553850841279262, 1.889093349720556e-05, -1.0126214725431623e-08, 1.8215282476579488e-12, 2108.1674156730005, -61.34924629932815], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 66,
    label = "CH3CH2CH3X",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 X u0 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.1585614552286883, 0.02485399130388187, 1.5352609874672988e-05, -3.2530247594325694e-08, 1.3506766435523373e-11, -22561.10807756208, -8.741392056954975], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[23.283229534991747, -0.024540693077868107, 4.373133821768709e-05, -2.3303695510259222e-08, 4.1715023104297174e-12, -28887.595276786073, -120.20181062152284], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 67,
    label = "CH2XCCH3",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {9,S}
3 C u0 p0 c0 {2,D} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.729793040998688, 0.047748728627248174, -4.578268178364427e-05, 2.3451880152285657e-08, -4.784870749797674e-12, -9365.580291054948, 9.234710919693295], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.85663761889357, -0.015730963078653456, 2.8107685766893508e-05, -1.5027636928535814e-08, 2.697539826495407e-12, -14718.890459895561, -95.48090316641051], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 68,
    label = "XCH2CH2XCH2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {10,S}
3 C u0 p0 c0 {1,S} {8,S} {9,S} {11,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
10 X u0 p0 c0 {2,S}
11 X u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.87649190798121, 0.05041092833202155, -4.0370853049490226e-05, 1.4788228625032917e-08, -1.2397049347867394e-12, -12094.558739289461, 15.749927590086838], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.66012614426986, -0.018925440102690868, 3.382115804337741e-05, -1.8093151903175618e-08, 3.2494148830155017e-12, -18371.14176998185, -104.75672689983918], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 69,
    label = "CH3OCH3X",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
3 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {2,S}
10 X u0 p0 c0 
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.3727171012781385, 0.01194860693589067, 2.7150452514596973e-05, -3.8852633769656305e-08, 1.494058469006216e-11, -31095.273460145785, -7.758950932483417], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[18.516655476128754, -0.019074658254398358, 3.4012226914245165e-05, -1.8145936853226977e-08, 3.2514401894230582e-12, -35853.68270204746, -88.75713937578965], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 67.3,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 70,
    label = "OHXCNH",
    molecule = 
"""
1 X  u0  p0  c0  {4,S}
2 H  u0  p0  c0  {3,S}
3 O  u0  p2  c0  {2,S} {4,S}
4 C  u0  p0  c0  {1,S} {3,S} {5,D}
5 N  u0  p1  c0  {4,D} {6,S}
6 H  u0  p0  c0  {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.2535931090791713, 0.033166428983989624, -4.2635337037470735e-05, 2.8609998342755266e-08, -7.693958851743003e-12, -20564.392921086164, 5.808107973721631], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.171412133321526, -0.0064719352202689305, 1.1485612981891048e-05, -6.0731150998083144e-09, 1.081563533316656e-12, -23294.858850849218, -51.167985889369774], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 15.1 and 62.25,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 71,
    label = "CH3XCHXCH2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {10,S}
3 C u0 p0 c0 {2,S} {8,S} {9,S} {11,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
10 X u0 p0 c0 {2,S}
11 X u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.344336190926412, 0.04526674347833033, -3.344766313486098e-05, 1.0361217087690635e-08, -1.3048407300447009e-13, -15477.227457033436, 8.413352589469767], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.65542958645535, -0.01862190525542446, 3.322657770420552e-05, -1.773344224662297e-08, 3.178817378615654e-12, -21395.61127063893, -104.46655619952196], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 72,
    label = "XCH2",
    molecule = 
"""
1 X  u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.230067554236452, 0.029222285879518774, -4.33154774933406e-05, 3.314280641933064e-08, -9.964713162186928e-12, -626.7613216025711, 8.301733455974734], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.834589411639772, -0.00514924926211478, 9.154895741071403e-06, -4.8491672783580415e-09, 8.637654768470861e-13, -2663.477431517318, -36.22147845498701], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 73,
    label = "XCHCO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
5 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.04255302823853574, 0.027932805594952984, -3.942772886677102e-05, 2.937990329292741e-08, -8.786786258580484e-12, -10082.468668896241, 4.0363923040219465], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.117729461045178, -0.005002044637666469, 8.99633520685214e-06, -4.846538967647318e-09, 8.752657281838953e-13, -12207.37450881007, -40.9365863214174], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 38.0 and 95.1,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 74,
    label = "XCHXCXC",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {5,D} {4,S}
2 C u0 p0 c0 {1,S} {3,S} {6,D}
3 C u0 p0 c0 {2,S} {7,T}
4 H u0 p0 c0 {1,S}
5 X u0 p0 c0 {1,D}
6 X u0 p0 c0 {2,D}
7 X u0 p0 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.9848823957977769, 0.036014809981119555, -5.065240706878557e-05, 3.628430569021752e-08, -1.038046169822867e-11, 26973.20042712046, 1.664688200003285], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.25781351760424, -0.004865122921467677, 8.797710813870003e-06, -4.777694576221335e-09, 8.68657674739829e-13, 24369.441196142885, -53.96717630562679], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 75,
    label = "XNCH3",
    molecule = 
"""
1 X  u0 p0 c0 {3,D}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 N  u0 p1 c0 {1,D} {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.4987403645215517, 0.02057518992256862, -1.2687790660142427e-05, 2.058012295878718e-09, 8.052488824448949e-13, -3245.3609260313565, -3.1163641363067622], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.22290226484407, -0.009612810696986896, 1.715947931096462e-05, -9.163518342562197e-09, 1.6433482690117591e-12, -6186.849724648275, -58.40089911574482], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 76,
    label = "XNNO",
    molecule = 
"""
1 X  u0  p0  c0  {2,D}
2 N  u0  p1  c0  {1,D} {3,S}
3 N  u0  p1  c0  {2,S} {4,D}
4 O  u0  p2  c0  {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.3662149681567333, 0.019020742935867013, -2.653152398193189e-05, 1.9018958807979596e-08, -5.525647036737049e-12, 9332.952887575104, -10.664674300189802], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.334158959428054, -0.0023200095273370794, 4.273610292768672e-06, -2.3802211876351535e-09, 4.412071561099113e-13, 7923.431196673271, -40.31023913438368], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 77,
    label = "XNHXCO",
    molecule = 
"""
1 X  u0  p0  c0  {4,S}
2 X  u0  p0  c0  {5,S}
3 H  u0  p0  c0  {4,S}
4 N  u0  p1  c0  {1,S} {3,S} {5,S}
5 C  u0  p0  c0  {2,S} {4,S} {6,D}
6 O  u0  p2  c0  {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.6717584472722575, 0.024196098439655787, -3.0224113929093245e-05, 1.9895402996021003e-08, -5.340187307455098e-12, -21112.866956039732, -7.690263414902659], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.18034832262653, -0.004638286745146815, 8.319820564851001e-06, -4.4687354533682325e-09, 8.058119574382185e-13, -23190.40764427214, -50.3182224383382], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 78,
    label = "XCHCHCH3",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 X u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.19306351552681508, 0.02883842541696513, -1.1311620031808518e-05, -5.046728232480822e-09, 4.1439068909993586e-12, -3191.1723946219117, 4.7606882617354085], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.777490200659685, -0.015741191624172802, 2.8070436957471546e-05, -1.4972145741035512e-08, 2.6824577662790475e-12, -7839.498686863102, -81.23804939085386], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 79,
    label = "XO",
    molecule = 
"""
1 X  u0 p0 c0 {2,D}
2 O  u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.2944756912929656, 0.014416258975183505, -2.6132263108414372e-05, 2.1900589365515376e-08, -6.980195992476666e-12, -13066.562523655452, -0.1994449279737156], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.902438421740939, -0.0003385726210179092, 6.43360477448012e-07, -3.663212176891723e-10, 6.900848803300778e-14, -13654.381950843575, -15.255923057858514], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 80,
    label = "CH3XCO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 X u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.2303840974925047, 0.021364183670701403, -1.0987946850558625e-05, -4.085575342462738e-10, 1.7279226465245644e-12, -32282.401663659468, 0.4124554121112016], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.896107647619662, -0.010602927242390975, 1.8955762745224325e-05, -1.0145885935032006e-08, 1.822928814492563e-12, -35530.47542256525, -59.95422731762176], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 23.8 and 88.9,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 81,
    label = "XC",
    molecule = 
"""
1 X  u0 p0 c0 {2,Q}
2 C  u0 p0 c0 {1,Q}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.9435091401126336, 0.019776735175353385, -3.3633654041374426e-05, 2.690271136312718e-08, -8.279586519600723e-12, 8836.27010194323, 7.174700024095191], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.8134761534241264, -0.0006939583733566436, 1.30308613815354e-06, -7.387034158394115e-10, 1.3879633501116816e-13, 7895.728646738098, -15.573857577758485], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 82,
    label = "CO2X",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
4 X u0 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.0095980019845503, 0.013359753384305327, -1.6230384431042425e-05, 1.100295260858819e-08, -3.144848106372021e-12, -48891.555691779344, -2.5929345930520586], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.982979600482389, -0.0030987089636898475, 5.628823486160688e-06, -3.0784712116700837e-09, 5.624485461804745e-13, -50143.212130793225, -27.65199541812654], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 10.8 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 83,
    label = "H2X",
    molecule = 
"""
1 X  u0 p0 c0
2 H  u0 p0 c0 {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8640641288806377, 0.000753456271243711, -1.6557140376965991e-06, 1.5522318341406327e-09, -4.4678219820768147e-13, -3929.4848656522245, -8.858065276956662], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.068796390056559, -0.0004958065446495855, 6.592341419391949e-07, -1.725976286189919e-10, 7.629639633524452e-15, -3940.910113971764, -9.719176714004277], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 84,
    label = "ONNCH3CH3X",
    molecule = 
"""
1 X  u0 p0 c0
2 O  u0 p2 c0 {3,D}
3 N  u0 p1 c0 {2,D} {4,S}
4 N  u0 p1 c0 {3,S} {5,S} {6,S}
5 C  u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
6 C  u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
7 H  u0 p0 c0 {5,S}
8 H  u0 p0 c0 {5,S}
9 H  u0 p0 c0 {5,S}
10 H  u0 p0 c0 {6,S}
11 H  u0 p0 c0 {6,S}
12 H  u0 p0 c0 {6,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9971667604441734, 0.025096351522686924, 1.327400147849864e-05, -3.229248828031911e-08, 1.3906143055484269e-11, -4427.764773508978, -7.722047591779937], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[23.93147529529223, -0.020915941685986497, 3.7374044459560956e-05, -2.0002134739614815e-08, 3.593731207543028e-12, -10399.380379962255, -112.97978243967577], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 41.92 and 44.79,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 85,
    label = "XOXO",
    molecule = 
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 O  u0 p2 c0 {1,S} {4,S}
4 O  u0 p2 c0 {2,S} {3,S}""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.2231455169463437, 0.018341447841647436, -3.0386325748395055e-05, 2.3891585307086276e-08, -7.268136510643082e-12, -7574.588552628849, -5.827727911134208], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.7929537712364505, -0.0007752730210599631, 1.4506987999484195e-06, -8.206145968477627e-10, 1.539514533647738e-13, -8504.745508497808, -27.814758438131133], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 86,
    label = "CH3NXNOH",
    molecule = 
"""
1 X  u0  p0  c0  {7,D}
2 N  u0  p2  c-1  {3,S} {7,S}
3 C  u0  p0  c0  {2,S} {4,S} {5,S} {6,S}
4 H  u0  p0  c0  {3,S}
5 H  u0  p0  c0  {3,S}
6 H  u0  p0  c0  {3,S}
7 N  u0  p0  c+1  {1,D} {2,S} {8,S}
8 O  u0  p2  c0  {7,S} {9,S}
9 H  u0  p0  c0  {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.229825100938746, 0.02857061942471177, -1.4963307961765392e-05, -5.176277564032557e-10, 2.381012195592759e-12, -2062.3717939646867, -3.8813990607513915], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.662154125491448, -0.013767021623286328, 2.4610310266771934e-05, -1.317144087550648e-08, 2.3665191096040582e-12, -6350.734473723902, -83.71175843550023], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 11.99 and 57.8,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 87,
    label = "H2NOHX",
    molecule = 
"""
1 X  u0 p0 c0
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {2,S} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.3799300490995994, 0.017751036808012963, -1.2084995353393713e-05, 2.539140332685803e-09, 6.810103108968516e-13, -12454.535751900376, -0.28276505649544603], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.249400701919917, -0.007938520257210327, 1.3942004052877396e-05, -7.265193097568502e-09, 1.2784307472830213e-12, -14823.295070579745, -45.75608438388285], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 21.45 and 69.68,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 88,
    label = "XCH2XCH2",
    molecule = 
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {4,S}
8 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.671923373906593, 0.03806451064327246, -3.8243609690221696e-05, 2.0402315397508814e-08, -4.289290897870988e-12, -9344.349622514754, 10.504095027094214], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.228982457871668, -0.011870642041170823, 2.115214760590694e-05, -1.1264154019990138e-08, 2.0156680761643477e-12, -13420.639317879915, -70.1189470742668], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 89,
    label = "OCHNH2X",
    molecule = 
"""
1 X  u0  p0  c0
2 O  u0  p2  c0  {3,D}
3 C  u0  p0  c0  {2,D} {4,S} {5,S}
4 H  u0  p0  c0  {3,S}
5 N  u0  p1  c0  {3,S} {6,S} {7,S}
6 H  u0  p0  c0  {5,S}
7 H  u0  p0  c0  {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.9695853138086932, 0.0205228970951337, -1.1621287011943349e-05, 6.215851673640726e-10, 1.3989998969380091e-12, -30660.778857010533, -2.354825831963712], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.866074256235924, -0.00980041654320586, 1.7404565153065928e-05, -9.223251987029436e-09, 1.6448095822345696e-12, -33658.84768373201, -58.59455732707728], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 29.77 and 83.13,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 90,
    label = "XCHXCHXCH",
    molecule = 
"""
1 C u0 p0 c0 {7,D} {2,S} {4,S}
2 C u0 p0 c0 {8,S} {1,S} {3,S} {5,S}
3 C u0 p0 c0 {9,D} {2,S} {6,S}
4 H u0 p0 c0 {1,S} 
5 H u0 p0 c0 {2,S} 
6 H u0 p0 c0 {3,S} 
7 X u0 p0 c0 {1,D}
8 X u0 p0 c0 {2,S}
9 X u0 p0 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.928540702752197, 0.05534718808824353, -7.06461478455427e-05, 4.6785381255932114e-08, -1.2437674535129727e-11, 5292.948861243362, 18.28101651206359], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.083426927809178, -0.010265253259335689, 1.8411684492939716e-05, -9.893049992225787e-09, 1.7833980915636025e-12, 726.6510783449339, -76.62793581406693], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 91,
    label = "XCHXO",
    molecule = 
"""
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 O  u0 p2 c0 {2,S} {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.8730970563913626, 0.019325903926924782, -2.433727249657027e-05, 1.6132660541232428e-08, -4.3452632072736365e-12, -20446.619816852606, -2.94044141236658], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.634556592034008, -0.0037356626340408357, 6.726653143472722e-06, -3.6343782130709962e-09, 6.579569323097696e-13, -22090.822291367596, -36.779137589176756], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 92,
    label = "XCNH",
    molecule = 
"""
1 X  u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 N  u0  p1 c0 {2,D} {4,S}
4 H  u0  p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.0573680644497503, 0.018785512336925957, -2.9380703160596206e-05, 2.3501870889973202e-08, -7.340235401105846e-12, 1799.1463534314448, -10.42154444737714], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.609510989685855, -0.0029858999120175238, 5.27828224206432e-06, -2.767387282111314e-09, 4.89306692025521e-13, 581.1205428417607, -37.533435633814946], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 93,
    label = "XCCHXCH2",
    molecule = 
"""
1 C u0 p0 c0 {7,D} {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {8,S} {5,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 X u0 p0 c0 {1,D}
8 X u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.325690332410893, 0.05227617574577326, -6.524816967869794e-05, 4.2548911392955294e-08, -1.1179369344420272e-11, 2784.159752692525, 15.786073190299277], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.035492123657766, -0.010328861922127128, 1.8514416797103598e-05, -9.939818618198685e-09, 1.790629402763902e-12, -1667.1832746747914, -76.07099376870829], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 94,
    label = "XCHXCXCH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {6,D} {4,S}
2 C u0 p0 c0 {1,S} {3,S} {7,D}
3 C u0 p0 c0 {2,S} {8,D} {5,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {3,S}
6 X u0 p0 c0 {1,D}
7 X u0 p0 c0 {2,D}
8 X u0 p0 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.338347217560166, 0.05493562255049885, -8.043479765287541e-05, 5.942973326695645e-08, -1.7339193550556327e-11, 12568.266928198473, 15.175282327220621], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.219586078218885, -0.007225560891365661, 1.2980691407311966e-05, -6.981175969304602e-09, 1.2594767716027926e-12, 8835.422244589323, -66.26212772907982], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 95,
    label = "CH4X",
    molecule = 
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.854962461371593, -0.005541348535465471, 3.011980765787564e-05, -2.992258921244716e-08, 1.0050250292925996e-11, -14354.343144955867, -9.256209391037203], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.54139337024375, -0.01040251283633434, 1.837773942532161e-05, -9.667651045328302e-09, 1.7121137503578788e-12, -16092.276392475003, -35.56384074430227], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 96,
    label = "XCHCH3",
    molecule = 
"""
1 X  u0 p0 c0 {3,D}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,D} {2,S} {7,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.0296465419536625, 0.03056436843534247, -2.5733374863603103e-05, 1.1293800368173688e-08, -1.8218077540432425e-12, -6451.16430405032, 2.661782468638178], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.238941552762988, -0.012066235015657971, 2.153091896887421e-05, -1.1489304900136156e-08, 2.0590190380730824e-12, -10239.604325438326, -70.27951400675978], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 97,
    label = "HC(O)XO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,S} {5,S}
3 C u0 p0 c0 {1,D} {2,S} {4,S}
4 H u0 p0 c0 {3,S}
5 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.6545242131205566, 0.015399194584141936, -1.018383152058808e-05, 1.7530337079552375e-09, 5.796151215755024e-13, -38399.49832230123, -11.081131526847855], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.183624235462183, -0.005481550766966762, 9.935041509590802e-06, -5.424762401917044e-09, 9.901835300359757e-13, -40482.181333372166, -49.97904651496785], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 98,
    label = "CH3XCOH",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {7,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {2,S} {8,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {1,S}
8 X u0 p0 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.2647754350356402, 0.030351773589888487, -2.0473784533629483e-05, 4.470354429308169e-09, 8.498143248400961e-13, -32512.741220143544, 6.533199516718724], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.898897231761438, -0.012891071659887727, 2.299988719668995e-05, -1.2274824005449935e-08, 2.2004936122579036e-12, -36630.05642095303, -71.4636746884245], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 58.0,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 99,
    label = "XCHCHO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {6,D}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 O u0 p2 c0 {2,D} 
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 X u0 p0 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.2534209544904569, 0.032730210982790324, -3.7549309992801566e-05, 2.321145975562514e-08, -5.9308399666582925e-12, -14127.152113634742, 9.926616292237732], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.179455287286821, -0.007798098913204271, 1.4043718812801308e-05, -7.591811891569331e-09, 1.3748365291506193e-12, -17253.86706331218, -52.78351661485842], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 98.6,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 100,
    label = "XCXCHCH3",
    molecule = 
"""
1 C u0 p0 c0 {8,T} {2,S}
2 C u0 p0 c0 {1,S} {9,S} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S} 
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 X u0 p0 c0 {1,T}
9 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.1589306430934916, 0.0370424905462181, -3.12332230658859e-05, 1.2995303860849604e-08, -1.8017575271373604e-12, -7290.124625399019, 2.959093823934715], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.80464637776645, -0.013393425263628071, 2.3947508736440405e-05, -1.281802952701938e-08, 2.3031828473915517e-12, -11796.975736716511, -83.79738561465682], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 101,
    label = "XCNO",
    molecule = 
"""
1 X  u0  p0  c0  {2,T}
2 C  u0  p0  c0  {1,T}, {3,S}
3 N  u0  p1  c0  {2,S} {4,D}
4 O  u0  p2  c0  {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.360683068714212, 0.014165731889051325, -1.892002347045031e-05, 1.3801128413020781e-08, -4.178695529704014e-12, 5624.946121901378, -5.695734760019386], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.213809647981861, -0.0025695689625320735, 4.704894804539271e-06, -2.5988427518532685e-09, 4.785316324962005e-13, 4433.044568874037, -29.99475352902745], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 67.9 and 67.9,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 102,
    label = "CH3NH2X",
    molecule = 
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 N  u0 p1 c0 {2,S} {7,S} {8,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.9288929932077815, 0.01631862774263431, 6.6127205768783405e-06, -1.7902847088098996e-08, 7.848205115270006e-12, -16303.105075747731, 1.6939853286406148], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.774415145648046, -0.01459552316874508, 2.5847792511727323e-05, -1.3646597084652586e-08, 2.42551193591374e-12, -20082.766282438308, -65.80619989351544], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 95.95,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 103,
    label = "XNNH",
    molecule = 
"""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 N  u0 p1 c0 {2,D} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.1312865815426474, 0.01840286797817462, -2.4277887710690205e-05, 1.722435823131042e-08, -4.9707878084454026e-12, 16308.708324575455, -5.77951135124305], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.494123716390367, -0.003797228881063589, 6.797269583929042e-06, -3.6381736850185154e-09, 6.538465376547789e-13, 14778.239964335953, -37.52189622794443], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 104,
    label = "XNN",
    molecule = 
"""
1 X  u0  p0  c0  {2,D}
2 N  u0  p0  c+1  {1,D}, {3,D}
3 N  u0  p2  c-1  {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.8633040730520567, 0.0044727384297514215, -7.65788966285876e-06, 7.566551887360406e-09, -2.824030320982694e-12, 2100.9284251900926, -7.401144075893692], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.411396431291331, -0.0016031836340185189, 2.888007424531916e-06, -1.5563237580538682e-09, 2.8077794257156996e-13, 1735.2553283482785, -15.027257233215492], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 56.8 and 56.8,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 105,
    label = "XCHXCHCH3",
    molecule = 
"""
1 C u0 p0 c0 {9,D} {2,S} {4,S}
2 C u0 p0 c0 {1,S} {3,S} {10,S} {5,S}
3 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 X u0 p0 c0 {1,D}
10 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.5739312448879508, 0.04773991322775247, -4.598072058543406e-05, 2.351355578566828e-08, -4.7454963845956605e-12, -8370.227132449476, 9.441545753128848], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.908034587091507, -0.015549264710131305, 2.777295632069162e-05, -1.4841538773975302e-08, 2.6631333748265644e-12, -13685.115276169157, -94.6976482818124], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 106,
    label = "XOCHCH2",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u0 p0 c0 {2,D} {5,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.29935425533347815, 0.03629505140577918, -3.9443600968546555e-05, 2.3073400207566012e-08, -5.505164095632448e-12, -12642.137005437078, -0.5242864483491534], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.089056568124821, -0.009905148708692501, 1.7696134150779686e-05, -9.457002105402365e-09, 1.697292389023077e-12, -16284.916863457292, -73.24272139895612], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 107,
    label = "XNHXCXNH",
    molecule = 
"""
1 X  u0  p0  c0  {5,S}
2 X  u0  p0  c0  {6,D}
3 X  u0  p0  c0  {7,S}
4 H  u0  p0  c0  {5,S}
5 N  u0  p1  c0  {1,S} {4,S} {6,S}
6 C  u0  p0  c0  {2,D} {5,S} {7,S}
7 N  u0  p1  c0  {3,S} {6,S} {8,S}
8 H  u0  p0  c0  {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.4658881904039123, 0.04032671652772304, -5.167764830672131e-05, 3.3783991018804145e-08, -8.78536639063177e-12, 12181.426913157424, 4.137138149238149], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.158175885963995, -0.00688770276139021, 1.2286461252588527e-05, -6.548941542810867e-09, 1.1738118244187488e-12, 8934.600125636513, -63.787681585915784], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 108,
    label = "XCH2CHCH2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {2,D} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.3359976099348523, 0.040954944519479695, -3.308965895040512e-05, 1.2340878154190055e-08, -1.0794845463097146e-12, -4231.746765002263, 14.860368286450937], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.749732048016103, -0.01554505229772852, 2.7694674777696646e-05, -1.4747852433105328e-08, 2.63917947214116e-12, -9300.472747249361, -82.77144070050932], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 74.2,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 109,
    label = "XOXCNH",
    molecule = 
"""
1 X  u0  p0  c0  {3,S}
2 X  u0  p0  c0  {4,S}
3 O  u0  p2  c0  {1,S} {4,S}
4 C  u0  p0  c0  {2,S} {3,S} {5,D}
5 N  u0  p1  c0  {4,D} {6,S}
6 H  u0  p0  c0  {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.1382132279909492, 0.028230867463811926, -3.843755004460994e-05, 2.6868207488574734e-08, -7.519327025758515e-12, -13762.760055476752, -5.622334490317954], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.261946129698629, -0.004316965080427518, 7.734088293961143e-06, -4.144911683523959e-09, 7.462534503008572e-13, -15902.95910010894, -50.913523959473565], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 110,
    label = "OXCNH2",
    molecule = 
"""
1 X  u0  p0  c0  {3,S}
2 O  u0  p2  c0  {3,D}
3 C  u0  p0  c0  {1,S} {2,D} {4,S}
4 N  u0  p1  c0  {3,S} {5,S} {6,S}
5 H  u0  p0  c0  {4,S}
6 H  u0  p0  c0  {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.3347788538257543, 0.02400192928995664, -2.56561733887836e-05, 1.4867689907027367e-08, -3.5296958527612083e-12, -30934.05126175619, -0.6581709929966859], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.997092813486743, -0.006795958307164792, 1.2045691827302481e-05, -6.35963158273436e-09, 1.1313340583748807e-12, -33390.08543800528, -49.54559991381272], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 37.01 and 60.96,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 111,
    label = "HCO2CH3X",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
9 X u0 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.376888507070602, 0.01716829097199307, 1.0226315735457644e-05, -2.31122454071209e-08, 9.75945662354606e-12, -48291.412994080354, -7.590713515849725], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.381509273065006, -0.014838934676127916, 2.656106577806364e-05, -1.4250112368781772e-08, 2.5651784247275115e-12, -52514.015236704, -81.64683071188084], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 62.9 and 75.5,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 112,
    label = "CH3XNXNOH",
    molecule = 
"""
1 X  u0  p0  c0  {7,S}
2 X  u0  p0  c0  {8,S}
3 C  u0  p0  c0  {7,S} {4,S} {5,S} {6,S}
4 H  u0  p0  c0  {3,S}
5 H  u0  p0  c0  {3,S}
6 H  u0  p0  c0  {3,S}
7 N  u0  p1  c0  {1,S} {3,S} {8,S}
8 N  u0  p1  c0  {2,S} {7,S} {9,S}
9 O  u0  p2  c0  {8,S} {10,S}
10 H  u0  p0  c0  {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.4985941622526862, 0.03235519404296074, -2.1571871597556333e-05, 4.167228725437758e-09, 1.1892209212351688e-12, -1408.5025332421214, -0.5266726461247799], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.602511742287444, -0.013353248184176617, 2.3798945032155278e-05, -1.2680910221528142e-08, 2.271067885592054e-12, -5786.139199075309, -83.3999758350555], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 43.28 and 91.29,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 113,
    label = "XONH2",
    molecule = 
"""
1 X  u0  p0  c0  {2,S}
2 O  u0  p2  c0  {1,S} {3,S}
3 N  u0  p1  c0  {2,S} {4,S} {5,S}
4 H  u0  p0  c0  {3,S}
5 H  u0  p0  c0  {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.386025057846731, 0.016641789865839772, -1.691943508660429e-05, 9.530137732441303e-09, -2.1792566643465093e-12, -4007.99180388779, -0.7177262330070526], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.44371553114693, -0.005684032888295971, 1.0035179034516899e-05, -5.267782547915829e-09, 9.321817757249796e-13, -5810.449891752194, -36.46722868035879], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 32.89 and 61.93,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 114,
    label = "OXNNH",
    molecule = 
"""
1 X  u0  p0 c0  {3,S}
2 O  u0  p3 c-1  {3,S}
3 N  u0  p0 c+1  {1,S} {2,S} {4,D}  
4 N  u0  p1 c0  {3,D} {5,S}
5 H  u0  p0 c0  {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.9329023704637375, 0.025594399763831377, -2.9929217811647463e-05, 1.7922498884658204e-08, -4.3129046270679965e-12, 7182.596578839141, -4.3235638307301105], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.189899578328756, -0.0048372628483032785, 8.704529819934222e-06, -4.70077922286624e-09, 8.512912531443968e-13, 4886.495150686189, -50.90380263208374], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 115,
    label = "XNCO",
    molecule = 
"""
1 X  u0  p0  c0  {2,S}
2 N  u0  p1  c0  {1,S} {3,D}
3 C  u0  p0  c0  {2,D} {4,D}
4 O  u0  p2  c0  {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.9093412444872058, 0.015109859358721396, -2.0359923727449643e-05, 1.497540744865976e-08, -4.539494264660256e-12, -12913.267816766678, -3.189187375000939], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.079622442658005, -0.0028835691765253762, 5.257872942765865e-06, -2.8882208385109374e-09, 5.294846893709078e-13, -14173.989023066151, -29.03239639146591], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 79.59 and 79.64,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 116,
    label = "XCCH2",
    molecule = 
"""
1 X  u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 C  u0  p0 c0 {2,D} {4,S} {5,S}
4 H  u0  p0 c0 {3,S}
5 H  u0  p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.353720433193718, 0.027380479373668155, -3.861261336966412e-05, 2.9270133072873463e-08, -8.860743055927948e-12, 13994.31295456025, -2.856818656648496], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.507384264072636, -0.005965212151141966, 1.0615010272909038e-05, -5.630342105226881e-09, 1.0041361735304452e-12, 11856.42995386208, -48.1889366842378], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 117,
    label = "XCXCCH2",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 C u0 p0 c0 {2,S} {7,T}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 X u0 p0 c0 {2,S}
7 X u0 p0 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.2710344247988186, 0.042753891765269336, -5.6165231071956046e-05, 3.844191038277121e-08, -1.0600416122648065e-11, 16249.423312403918, 6.930628700462604], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.129033324279652, -0.007572178644341316, 1.3601575346551853e-05, -7.320884103194313e-09, 1.3215746053417432e-12, 12813.089104521558, -64.82508096392019], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 118,
    label = "XCH2CHO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
3 C u0 p0 c0 {1,D} {2,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.5280832964499694, 0.02857832859492173, -2.2234915968304163e-05, 7.788283508886629e-09, -5.93358709205692e-13, -22437.334515606326, 7.519443089057723], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.978145297319083, -0.010727798332984888, 1.9236806046693476e-05, -1.0341447683316024e-08, 1.8645488021368837e-12, -26073.555687972465, -61.77924600538357], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 58.8 and 75.3,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 119,
    label = "XNO",
    molecule = 
"""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 O  u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.8619797531975506, 0.01226770483407149, -1.773176202005306e-05, 1.315536995612894e-08, -3.940107642579075e-12, -6275.990851212231, -9.289686258349786], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.603256419033999, -0.0013940159460681886, 2.5736107706121614e-06, -1.4363143471003888e-09, 2.666479842882661e-13, -7148.294773433381, -27.812269651080857], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 120,
    label = "CH3OCH2OHX",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4 O u0 p2 c0 {3,S} {10,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 X u0 p0 c0 
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.359493024720845, 0.026577902711539418, 4.854369294738433e-06, -2.3300747925097863e-08, 1.0802412500241882e-11, -52590.39818387121, -2.729081742005988], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[21.248876184416513, -0.019320927733525405, 3.441581489566954e-05, -1.8332027550769172e-08, 3.2816938103512397e-12, -58122.21767694889, -101.87027078781432], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 121,
    label = "XOC(O)XO",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {4,S}
2  O u0 p2 c0 {1,D} 
3  O u0 p2 c0 {1,S} {5,S}
4  O u0 p2 c0 {1,S} {6,S}
5  X u0 p0 c0 {3,S}
6  X u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.26079238669804067, 0.02966002185682939, -3.7462395997348304e-05, 2.3585690914845046e-08, -5.979149689033182e-12, -55608.207661542474, 4.3175492208091715], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.046782671886772, -0.0035163705656289647, 6.491760615417757e-06, -3.6335099080933313e-09, 6.762966584087594e-13, -57983.67633684451, -44.6731573615769], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 89.5 and 92.5,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 122,
    label = "CH2COX",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 X u0 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.3891872845515294, 0.029211258376415077, -3.686303799813517e-05, 2.577719388817712e-08, -7.388347087907539e-12, -18013.440080419805, 3.2584641154733998], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.0991518870024, -0.007408036435348514, 1.3248008658893356e-05, -7.0846346396538015e-09, 1.271764992207576e-12, -20634.004780063682, -50.37066409898756], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 123,
    label = "XOH",
    molecule = 
"""
1 X  u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.6898535001436462, 0.011560715747622905, -1.8172065360808256e-05, 1.4019484636684314e-08, -4.1341182941071035e-12, -18153.37696516464, 2.129073162043106], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[3.959396473787725, -0.0016598638232622237, 2.83126234608295e-06, -1.4039351747093804e-09, 2.3701040763643917e-13, -18832.11017649684, -13.688856094870856], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 80.8 and 80.8,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 124,
    label = "XCH2CH3",
    molecule = 
"""
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C  u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.11893459142418157, 0.025418090066889925, -9.608116771933841e-06, -4.295196742293207e-09, 3.464357462477983e-12, -12617.296351488458, -0.7380580806880177], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.060749507479485, -0.014857604022812533, 2.6463045199679808e-05, -1.408809867202183e-08, 2.5199765942401104e-12, -16807.88322381735, -78.2119499804451], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 125,
    label = "XCH2NH2",
    molecule = 
"""
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 N  u0 p1 c0 {2,S} {6,S} {7,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.4556889873013476, 0.02637115378729022, -2.1193131996997146e-05, 8.246535163307095e-09, -8.510567522705759e-13, -9619.36058313265, 6.940761472903407], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.091014829045449, -0.011033041791600598, 1.9484398734063737e-05, -1.0237434925971296e-08, 1.8128743684909556e-12, -12934.937222220371, -57.16802725202871], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 76.79,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 126,
    label = "XOXNO",
    molecule = 
"""
1 X  u0  p0 c0  {3,S}
2 X  u0  p0 c0  {4,D}
3 O  u0  p2 c0  {1,S} {4,S}
4 N  u0  p0 c+1  {3,S} {2,D} {5,S}
5 O  u0  p3 c-1  {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.9935275209780121, 0.019188087090484827, -2.4292503483335336e-05, 1.5478052270571518e-08, -3.999504806554147e-12, -12323.709591164194, 1.491393465229386], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.354990179402851, -0.0023627191484181793, 4.361162380825014e-06, -2.4396440933341437e-09, 4.5386927366933493e-13, -13872.241809925927, -30.368838554150337], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 63.4 and 94.07,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 127,
    label = "CH3CHOX",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 X u0 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.7686523771328186, 0.015420900312077459, 5.767879549704185e-06, -1.5827043286126327e-08, 6.7518071869769546e-12, -27533.951424720082, -5.0593835573814285], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.84774734404763, -0.013358192301668933, 2.386892675943612e-05, -1.2769338599276014e-08, 2.2930529372262883e-12, -31129.857809768124, -68.67479290471243], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 30.5 and 72.0,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 128,
    label = "XNXNO",
    molecule = 
"""
1 X  u0  p0  c0  {3,D}
2 X  u0  p0  c0  {4,D}
3 N  u0  p1  c0  {1,D} {4,S} 
4 N  u0  p0  c+1  {2,D} {3,S} {5,S}
5 O  u0  p3  c-1  {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.3310365280067524, 0.02414675054599538, -3.5063766242587676e-05, 2.5290200391753758e-08, -7.26903102232295e-12, 15092.726187370823, -6.608655782473958], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.420680853651005, -0.0021196771568185117, 3.923916739995684e-06, -2.199549837548649e-09, 4.098196015657322e-13, 13477.068818153597, -41.56606016706463], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 129,
    label = "CH3CH2OHX",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {9,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {1,S}
10 X u0 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.4414164909443667, 0.020141846300514372, 1.0044463058803559e-05, -2.4632470705674976e-08, 1.0643655451973795e-11, -32356.64134461422, -2.1625348825050494], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[18.599267162738386, -0.017944217996744175, 3.188093588226114e-05, -1.6915782664718715e-08, 3.0187082130244765e-12, -37154.466704714025, -87.27517780931359], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 130,
    label = "XNCNH",
    molecule = 
"""
1 X  u0  p0  c0  {2,S}
2 N  u0  p1  c0  {1,S} {3,D}
3 C  u0  p0  c0  {2,D} {4,D}
4 N  u0  p1  c0  {3,D} {5,S}
5 H  u0  p0  c0  {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.824292460317689, 0.02601749608891088, -3.764244817921074e-05, 2.8538881668749783e-08, -8.616189007413881e-12, 16315.13191154171, 0.7718377799596219], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.101361292443928, -0.0045680652881194975, 8.154992926727776e-06, -4.344206002856444e-09, 7.779501031579715e-13, 14406.97416173834, -40.104792869372005], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 54.13 and 75.02,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 131,
    label = "XNNCH3",
    molecule = 
"""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 N  u0 p1 c0 {2,D} {4,S}
4 C  u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 H  u0 p0 c0 {4,S}
6 H  u0 p0 c0 {4,S}
7 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.2307526632663266, 0.017783660445621286, -5.8815403039087805e-06, -3.7124137189088388e-09, 2.5349066309163098e-12, 10544.60057640031, -3.175210907234449], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.925749605822386, -0.010525830802496002, 1.8814016420061135e-05, -1.0066604745935756e-08, 1.8080352395345379e-12, 7506.419051612669, -58.79213808622047], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 60.41 and 70.27,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 132,
    label = "XOCH3",
    molecule = 
"""
1 X  u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 O  u0 p2 c0 {1,S} {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.7273785148877367, 0.010788735354898502, 4.9967108828586935e-06, -1.2468126656547278e-08, 5.318867454032739e-12, -18875.02875852478, -1.5351955816669687], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.340294884584132, -0.00950160319712203, 1.697403456690111e-05, -9.07934305084049e-09, 1.6301823466076707e-12, -21444.675960166733, -46.9368606502489], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 51.1 and 54.5,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 133,
    label = "CH3XCHOH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {9,S}
3 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
9 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.09380754054011578, 0.0325418510257262, -1.9508084147603755e-05, 1.9033631163800556e-09, 2.017848614406121e-12, -34082.08670395655, 5.477435944078252], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.823607363161834, -0.015032591722587536, 2.6732668099565248e-05, -1.4198357914414404e-08, 2.5358452426433642e-12, -38704.033383840135, -81.69211835243186], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 96.1,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 134,
    label = "XCH2XNH",
    molecule = 
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 N  u0 p1 c0 {2,S} {3,S} {7,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.093284554855984, 0.040547574911979994, -5.061868467754752e-05, 3.338408272812267e-08, -8.850728226061783e-12, -541.4488841059094, 11.04449701028243], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.340392757497492, -0.008856591480446027, 1.576724170854937e-05, -8.37951618646151e-09, 1.4974333824980495e-12, -4030.4177220112606, -61.11445120381964], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 135,
    label = "CH3XNNOH",
    molecule = 
"""
1 X  u0  p0  c0  {2,D}
2 N  u0  p0  c+1  {1,D} {3,S} {7,S}
3 C  u0  p0  c0  {2,S} {4,S} {5,S} {6,S}
4 H  u0  p0  c0  {3,S}
5 H  u0  p0  c0  {3,S}
6 H  u0  p0  c0  {3,S}
7 N  u0  p2  c-1  {2,S} {8,S}
8 O  u0  p2  c0  {7,S} {9,S}
9 H  u0  p0  c0  {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.8458736976425771, 0.029847040864329207, -1.628806950845996e-05, -5.160630777782037e-10, 2.7107071993275384e-12, -2142.430685089259, -2.261987036327792], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.56412848342619, -0.013464305239539199, 2.3999162756146917e-05, -1.2790802287437008e-08, 2.291305462464261e-12, -6481.52469068694, -83.47568436687708], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 26.19 and 53.11,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 136,
    label = "XNHXNH",
    molecule = 
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 N  u0 p1 c0 {1,S} {4,S} {5,S}
4 N  u0 p1 c0 {2,S} {3,S} {6,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.8122484134908616, 0.02240817208647222, -2.560541648695253e-05, 1.573713669012945e-08, -3.9135440329412915e-12, 14152.972991418834, -4.914005065663471], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.420913639253023, -0.00590851045959325, 1.0467884451987092e-05, -5.523245130977161e-09, 9.815541695290048e-13, 12014.291207158787, -48.23750625756504], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 137,
    label = "CH3CH2XCO",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 C u0 p0 c0 {1,D} {2,S} {10,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
10 X u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.3179804064752164, 0.0337808193466292, -1.4799617004411486e-05, -3.849157099163547e-09, 3.93637648998797e-12, -33918.12452934654, 3.571995571107836], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.33779285285688, -0.017434371694113212, 3.119765505656061e-05, -1.672265569235557e-08, 3.0079816165686478e-12, -39258.711852699154, -95.07239433429336], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 63.5,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 138,
    label = "XCHCH2XCH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {8,D}
3 C u0 p0 c0 {1,S} {7,S} {9,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 X u0 p0 c0 {2,D}
9 X u0 p0 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.872536655384702, 0.05562111398651003, -6.411742598340763e-05, 3.909464538095682e-08, -9.649860709050681e-12, 6941.619536087236, 18.428516494465626], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.033246614537457, -0.013087045267915006, 2.3459272528477657e-05, -1.2599713004773305e-08, 2.2701751492970414e-12, 1737.2654808454863, -86.81226442045676], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 139,
    label = "OC(OH)OHX",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {4,S} {6,S}
3 O u0 p2 c0 {4,D}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 X u0 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.8969935457260645, 0.03136537650129557, -3.4536619307243186e-05, 1.9380365136144386e-08, -4.250746365163833e-12, -71446.1925182757, -0.6822066393777533], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.834144459748813, -0.00712665996163563, 1.2639022416819117e-05, -6.681787889537329e-09, 1.1906504853640317e-12, -74435.28022253876, -60.909873151562834], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 37.3,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 140,
    label = "XNHXN",
    molecule = 
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,D}
3 N  u0 p1 c0 {1,S} {4,S} {5,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.25283006015604187, 0.02196083876256632, -2.995078757088064e-05, 2.1358396282336687e-08, -6.1257447536872715e-12, 13593.483104326204, -2.7225828014208826], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.479250514525144, -0.0038018859574486426, 6.8066816816392985e-06, -3.643543798852429e-09, 6.550303406277692e-13, 11890.265260558876, -38.61815049599427], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 141,
    label = "OXCXCH2",
    molecule = 
"""
1 X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 C u0 p0 c0 {1,S} {4,S} {5,D}
4 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
5 O u0 p2 c0 {3,D}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.6497153450141888, 0.035546604120223445, -4.414270899606324e-05, 2.939036379394475e-08, -8.001754984206834e-12, -26238.76897832118, 1.8076961116185153], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.11369144591575, -0.00767701103697003, 1.3787891209052118e-05, -7.421200820811269e-09, 1.3394177916973617e-12, -29365.911660517995, -62.16525112731247], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 142,
    label = "XCCH2OH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {2,S} {7,T}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 X u0 p0 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.4143676839292862, 0.029786628663730223, -2.426108719279687e-05, 8.221444820144557e-09, -2.817862319670817e-13, -25626.63470906436, 7.219078103319432], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.02500088722102, -0.009793642109474915, 1.7460946560560346e-05, -9.310402159535727e-09, 1.6689291964108132e-12, -29190.39381882001, -61.541267057571915], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 51.0,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 143,
    label = "XNHOH",
    molecule = 
"""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.010041032080093394, 0.02791595484057199, -3.7008083281707176e-05, 2.570290267425526e-08, -7.117885244079258e-12, -6799.959163445844, -1.4839204453352997], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.464320248836604, -0.005614587199193173, 9.9245591770994e-06, -5.2153626206299305e-09, 9.23918350847828e-13, -9032.0579726796, -48.57063125531307], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 144,
    label = "XCHCHXC",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {7,T}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 X u0 p0 c0 {2,S}
7 X u0 p0 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.4051490470255836, 0.047724295147314466, -6.435600747520544e-05, 4.449798565993566e-08, -1.229600974858338e-11, 13932.554468351993, 11.83634468441823], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.134856888890395, -0.007526900516033633, 1.352052265274789e-05, -7.2771894094033805e-09, 1.3138249202344664e-12, 10281.129821696812, -65.34134973287247], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 145,
    label = "XCHXCO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,D}
3 C u0 p0 c0 {1,D} {2,S} {6,S}
4 H u0 p0 c0 {2,S}
5 X u0 p0 c0 {2,D}
6 X u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.377613682873679, 0.03725659094556663, -5.301684366448474e-05, 3.85554964071359e-08, -1.1193467269780293e-11, -21030.51942070027, 3.962292648538873], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.198827717145198, -0.005117142676443838, 9.263909477123228e-06, -5.03838713590732e-09, 9.16955353646548e-13, -23703.95869584113, -53.26788563457137], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 146,
    label = "NNOX",
    molecule = 
"""
1 X  u0  p0  c0
2 N  u0  p2  c-1  {3,D}
3 N  u0  p0  c+1  {2,D} {4,D}
4 O  u0  p2  c0  {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.9235610553621525, 0.01068216046698936, -1.2508198628811793e-05, 8.48135128917812e-09, -2.479573346741727e-12, 6451.526179720909, -2.1766995783633227], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.0862168181954, -0.002805162252729235, 5.0989614637722275e-06, -2.7909121678571102e-09, 5.101969745948299e-13, 5383.590212543781, -23.23758565322258], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 147,
    label = "XCHCHXCH2",
    molecule = 
"""
1 C u0 p0 c0 {8,S} {2,D} {4,S}
2 C u0 p0 c0 {1,D} {3,S} {5,S}
3 C u0 p0 c0 {2,S} {9,S} {6,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 X u0 p0 c0 {1,S}
9 X u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.002413995498696, 0.05221889648339103, -5.8912177969662134e-05, 3.510355529677287e-08, -8.419339629356664e-12, -1583.8468315135315, 15.082211393890638], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.948653910382953, -0.012883710275849664, 2.30283073399041e-05, -1.2316750647550109e-08, 2.212019858759127e-12, -6568.301872505993, -85.45359037375812], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 148,
    label = "XCHCHXCH",
    molecule = 
"""
1 C u0 p0 c0 {7,D} {2,S} {4,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {8,S} {2,D} {6,S}
4 H u0 p0 c0 {1,S} 
5 H u0 p0 c0 {2,S} 
6 H u0 p0 c0 {3,S} 
7 X u0 p0 c0 {1,D}
8 X u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.2454310424697583, 0.045740718255756645, -5.206789835525127e-05, 3.101158725098536e-08, -7.43117665629453e-12, 6383.047042929103, 14.227532107306452], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.973715561836796, -0.010520285819897423, 1.8851669349884655e-05, -1.0120414107899575e-08, 1.8231144688019987e-12, 2086.6886894395393, -72.51980418671917], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 149,
    label = "CH2XCOH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.30041635843613135, 0.03619616019868196, -4.288430201573472e-05, 2.7141699711617187e-08, -6.934849338825931e-12, -19065.39730973619, 5.483658315417512], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.191102408307225, -0.008864291649055325, 1.572912713587234e-05, -8.318771320936293e-09, 1.4811256231144176e-12, -22382.577104062955, -62.24255112474064], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 150,
    label = "XCOOH",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,S} {4,S}
4 H u0 p0 c0 {3,S}
5 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.35905147802137405, 0.025017248548333162, -3.0958739977378896e-05, 2.002869012669601e-08, -5.2651983806115445e-12, -50225.62556199516, 3.5273537407172775], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.162652730015594, -0.004701468704464756, 8.435562541654682e-06, -4.533666706921367e-09, 8.179719347759545e-13, -52377.34721527477, -40.59754358949283], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 36.7 and 64.6,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 151,
    label = "XOXNH",
    molecule = 
"""
1 X  u0  p0  c0  {3,S}
2 X  u0  p0  c0  {4,S}
3 O  u0  p2  c0  {1,S} {4,S}
4 N  u0  p1  c0  {2,S} {3,S} {5,S}
5 H  u0  p0  c0  {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.2669630126984997, 0.025658711060691144, -3.674609743656314e-05, 2.652568614267245e-08, -7.566882843329833e-12, -856.8771116857789, -0.5998868568564104], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.589717718492281, -0.0034427893006683118, 6.154097545559309e-06, -3.286426328580151e-09, 5.898542759689933e-13, -2641.1919622842615, -39.322325238792374], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 152,
    label = "XCHCH2XCH2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {9,S}
3 C u0 p0 c0 {1,S} {8,S} {10,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 X u0 p0 c0 {2,S}
10 X u0 p0 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.484485114012842, 0.04961189561222539, -4.65419978717544e-05, 2.2377932218595584e-08, -4.031092980904033e-12, 950.2265899090655, 13.750558268509494], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.886812140218346, -0.015838506842304444, 2.832515977929691e-05, -1.5167308231428934e-08, 2.7260950183678272e-12, -4616.716141422545, -95.03452637890805], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 153,
    label = "XCCH2XCH2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {9,T}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 X u0 p0 c0 {2,S}
9 X u0 p0 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.026350977856424, 0.05033083054735824, -5.3858827607316166e-05, 3.034074804890288e-08, -6.8491831794954975e-12, -812.633364292504, 15.773791828959922], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.896360332347012, -0.013266223584548383, 2.3747331561928986e-05, -1.2730764101309729e-08, 2.290512623175143e-12, -5865.5984546053205, -84.98120108238106], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 154,
    label = "CH3XCCH3",
    molecule = 
"""
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3 C u0 p0 c0 {1,S} {2,S} {10,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
10 X u0 p0 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.40376536967951093, 0.034347741809455025, -1.589337328818797e-05, -2.439734982430757e-09, 3.4095542131728e-12, -11336.639210087782, -2.8137595079379913], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.77856313212703, -0.018507699595861404, 3.3042539225048794e-05, -1.7651522931350595e-08, 3.1660732917247853e-12, -16744.043936103117, -103.1311696686628], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 155,
    label = "H2OX",
    molecule = 
"""
1 X  u0 p0 c0
2 O  u0 p2 c0 {3,S} {4,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.7297138825671468, 0.008710514465497024, -1.291317819719363e-05, 1.0729496125819492e-08, -3.39433446606103e-12, -31457.548687752344, -6.044794752032761], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.854964676995411, -0.003288476727423586, 5.569907695763815e-06, -2.730082062056071e-09, 4.558982273494338e-13, -32149.48450841932, -21.35184628967326], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 62.1,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 156,
    label = "XNCN",
    molecule = 
"""
1 X  u0  p0  c0  {2,D}
2 N  u0  p1  c0  {1,D} {3,S}
3 C  u0  p0  c0  {2,S} {4,T}
4 N  u0  p1  c0  {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.30879427846626484, 0.023227067848325393, -3.556983761389428e-05, 2.7753564190724293e-08, -8.58545640929891e-12, 22898.394145263956, 2.8113796696926467], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.115602779295008, -0.0028051745981831867, 5.132702872236503e-06, -2.829006259459821e-09, 5.200075004342621e-13, 21364.74320291197, -30.60959130885633], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 88.08 and 88.09,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 157,
    label = "XCHCCH2",
    molecule = 
"""
1 C u0 p0 c0 {3,D} {4,S} {7,S}
2 C u0 p0 c0 {3,D} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.4742062540575103, 0.04214500053175585, -5.019756826698666e-05, 3.1922818735063856e-08, -8.249905627795002e-12, 10559.4784562285, 6.364684098641106], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.11332271622567, -0.009852167524871164, 1.7609565696925904e-05, -9.414958396811886e-09, 1.6903766265120003e-12, 6714.5433583955055, -71.92236187706696], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 158,
    label = "XCHNH2",
    molecule = 
"""
1 X  u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 N  u0 p1 c0 {2,S} {5,S} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.5193172520442837, 0.023734404355342437, -2.1291549028341602e-05, 9.94555265390745e-09, -1.7005321482851575e-12, -6268.490723327917, 7.3534791576741245], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.145630696608784, -0.008751766131929682, 1.54803718423858e-05, -8.152092095089769e-09, 1.4464142686037081e-12, -9052.63848138253, -46.97134963735187], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 24.5 and 55.12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 159,
    label = "XOCH2OH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {7,S} 
3 O u0 p2 c0 {1,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.0741251167856873, 0.022965579343290663, -1.2260554803817235e-05, -1.2460292253565517e-09, 2.5403566710368206e-12, -39525.49845529264, 1.0295611508796672], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.048614734292261, -0.009848415350408759, 1.7567207799851504e-05, -9.375547072388493e-09, 1.6816169905928739e-12, -42831.450862658974, -60.862645123248136], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 42 and 64.2,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 160,
    label = "XCHCH2XC",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,D}
3 C u0 p0 c0 {1,S} {8,T}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 X u0 p0 c0 {2,D}
8 X u0 p0 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.808917748373903, 0.053714599902385717, -6.677817790865915e-05, 4.327825733184735e-08, -1.130233577297329e-11, 9619.112392159726, 17.849382866639438], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.066208846469156, -0.010480118559539833, 1.881922239694593e-05, -1.0130718926452086e-08, 1.828832046803562e-12, 5034.888760363905, -76.6191540700652], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 161,
    label = "NCOHX",
    molecule = 
"""
1 X  u0  p0  c0
2 N  u0  p1  c0  {3,T}
3 C  u0  p0  c0  {2,T} {4,S}
4 O  u0  p2  c0  {3,S} {5,S}
5 H  u0  p0  c0  {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.3887777012256572, 0.014850708171068365, -1.8053004737031874e-05, 1.2700298220935e-08, -3.716030318814928e-12, -7392.433200349613, -8.57157237881663], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.154629319398145, -0.00449876413570766, 8.0146684604216e-06, -4.261300870858486e-09, 7.615162641286214e-13, -8827.882607925585, -37.55054890583075], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 46.11 and 61.53,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 162,
    label = "XCH2OH",
    molecule = 
"""
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {2,S} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.37382917215532696, 0.023397694773753867, -1.9573567392259445e-05, 7.627200807680551e-09, -7.421143739131525e-13, -27513.515780149737, 6.579115091304888], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.314142529124842, -0.00856870908864423, 1.5185520067013606e-05, -8.022788412750033e-09, 1.4272195483623104e-12, -30326.017516002656, -47.98958812415533], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 25.3 and 72.1,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 163,
    label = "XCCH2XC",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,T}
3 C u0 p0 c0 {1,S} {7,T}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 X u0 p0 c0 {2,T}
7 X u0 p0 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.541841061529845, 0.05160728003060958, -6.994891069966049e-05, 4.85158305988308e-08, -1.3456497319240965e-11, 17548.89693736918, 16.518029762099676], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.143015074848885, -0.007834142324240255, 1.4122634097373617e-05, -7.640517612449328e-09, 1.3848723134761679e-12, 13631.716839013938, -66.32278300778111], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 164,
    label = "XNOH",
    molecule = 
"""
1 X  u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.6073959190950321, 0.024113462130844535, -3.622638330031743e-05, 2.7097579319862448e-08, -7.934381327464133e-12, -4443.77431099836, -4.173485582593109], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.644637833087604, -0.002920101421341297, 5.169672876049725e-06, -2.7189007316892194e-09, 4.823641859136411e-13, -5992.148930808039, -38.61485479394129], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 165,
    label = "XCHXNH",
    molecule = 
"""
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 N  u0 p1 c0 {2,S} {3,S} {6,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.0343590311726811, 0.029548895633929394, -3.738896571124078e-05, 2.505428091404425e-08, -6.7733044547221584e-12, -421.8283763916819, 2.756969671164323], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.384981081689604, -0.0062701534989397616, 1.1163497723477089e-05, -5.931876850455135e-09, 1.0600988950662274e-12, -2935.93962989151, -49.30409616407421], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 166,
    label = "XCCH2CH3",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {9,T}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 X u0 p0 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.4078368334046704, 0.03381796578381747, -1.8236487221509343e-05, -2.1781419481646084e-10, 2.782374927270981e-12, -15394.26340793086, 3.0339724962175385], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.695288648796936, -0.016187381050989588, 2.8912131274443475e-05, -1.545608296238792e-08, 2.7742465514950727e-12, -20399.728770998496, -90.5054955162382], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 167,
    label = "XN",
    molecule = 
"""
1 X  u0 p0 c0 {2,T}
2 N  u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.0434391580678266, 0.017236905643470923, -3.068696315315614e-05, 2.5388245627464015e-08, -8.015096461815905e-12, 8863.690654850896, 3.0546304469819057], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.871017301698067, -0.00045957304951942124, 8.694913605296623e-07, -4.94323170989376e-10, 9.30400561761373e-14, 8127.670266366513, -15.466736587844444], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 168,
    label = "XCH3",
    molecule = 
"""
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.04445489276185006, 0.01943676194021713, -1.9102863500374985e-05, 1.1126928549339282e-08, -2.7373609307351296e-12, -7912.647925653787, -0.1733750333071784], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.657034648985562, -0.007903062987556124, 1.4010028663218991e-05, -7.400153953696461e-09, 1.3151647947324833e-12, -10160.590244047151, -44.33519376803277], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 169,
    label = "ONNH2X",
    molecule = 
"""
1 X  u0 p0 c0
2 O  u0 p2 c0 {3,D}
3 N  u0 p1 c0 {2,D} {4,S}
4 N  u0 p1 c0 {3,S} {5,S} {6,S}
5 H  u0 p0 c0 {4,S}
6 H  u0 p0 c0 {4,S}


""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.7634176810672415, 0.021946451570843618, -2.1033167502967104e-05, 1.0462349281217349e-08, -2.0084145369249484e-12, -1248.5790852933467, -2.256538334973248], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.11053358784989, -0.006805462707882655, 1.2093538595183724e-05, -6.412289364227745e-09, 1.1443163823129447e-12, -3673.859741249439, -49.79886953498589], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 18.68 and 56.21,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 170,
    label = "XH",
    molecule = 
"""
1 X  u0 p0 c0 {2,S}
2 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.075701236599891, 0.017358079400578773, -2.609206959644694e-05, 1.8928219151161522e-08, -5.388359243334392e-12, -4286.294385953249, 8.153616020422866], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.7224698531980533, -0.001068155975828598, 1.986521394943791e-06, -1.1204772095332365e-09, 2.0981041257906194e-13, -5338.337959020086, -15.320679400956458], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 171,
    label = "XNHNO",
    molecule = 
"""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {5,S}
3 N  u0 p1 c0 {2,S} {4,D}
4 O  u0 p2 c0 {3,D}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.9423346699570359, 0.02493487639491411, -2.7919428360043676e-05, 1.571957486170818e-08, -3.4902263334995127e-12, 881.6433815686996, -4.565900283855495], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.170219610476307, -0.0048325870949339446, 8.689191240948876e-06, -4.688314630071139e-09, 8.4862210661604e-13, -1431.180329435676, -51.12879978565127], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 172,
    label = "XCCO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,D}
3 C u0 p0 c0 {1,D} {2,D}
4 X u0 p0 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.4822964305908491, 0.02587155434165326, -3.936037393774588e-05, 3.0462963155377796e-08, -9.365331471877763e-12, -13050.060585165716, -3.5737589207601044], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.07081661266945, -0.0030085129494901177, 5.515390274181092e-06, -3.0480542204079653e-09, 5.614688010457989e-13, -14764.740902953226, -40.862575025965135], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 173,
    label = "XCH2XCHXCH2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {10,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  X u0 p0 c0 {1,S}
10 X u0 p0 c0 {2,S}
11 X u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.0278096058865027, 0.04868278046857124, -4.646974797464267e-05, 2.2875164617387645e-08, -4.238776330984361e-12, -9930.448913946944, 11.507075519643987], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.778752685293135, -0.015532192728255128, 2.768982915049771e-05, -1.4757532167138965e-08, 2.6427542340485924e-12, -15317.515565301794, -94.260530730216], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 174,
    label = "XNH",
    molecule = 
"""
1 X  u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.755696584325541, 0.02931258669464399, -4.84378705852652e-05, 3.844689819950921e-08, -1.1723809056491327e-11, 1433.9639181474388, 10.096512830387793], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.828377003858721, -0.002459572235886796, 4.346739333449326e-06, -2.2752996842710652e-09, 4.018642509209477e-13, -103.48536821365542, -26.369909929000492], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 175,
    label = "NNX",
    molecule = 
"""
1 X  u0 p0 c0 
2 N  u0 p1 c0 {3,T}
3 N  u0 p1 c0 {2,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.177331992598396, -0.0012986532054234208, 2.5984612482967176e-06, -9.710010733545473e-10, -9.263379990534644e-14, 2010.8841459624982, -7.836128729651465], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.407824922141336, -0.0015051356220845875, 2.6825671704148484e-06, -1.4261829291752541e-09, 2.5443162091545603e-13, 1899.9794971684478, -9.198927094799298], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 9.93,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 176,
    label = "XNXCXNH",
    molecule = 
"""
1 X  u0  p0  c0  {4,D}
2 X  u0  p0  c0  {5,D}
3 X  u0  p0  c0  {6,S}
4 N  u0  p1  c0  {1,D} {5,S}
5 C  u0  p0  c0  {2,D} {4,S} {6,S}
6 N  u0  p1  c0  {3,S} {5,S} {7,S}
7 H  u0  p0  c0  {6,S} 
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.6859760515195177, 0.025296471802971843, -3.4398732551427645e-05, 2.4726466042657776e-08, -7.168136846025081e-12, 16296.596479058866, -8.13093844993648], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.122116356278868, -0.004680403866579923, 8.377733415299198e-06, -4.483211677086074e-09, 8.058102717843452e-13, 14297.70202654053, -50.07401602772124], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 177,
    label = "XCHXCH",
    molecule = 
"""
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 C  u0 p0 c0 {2,D} {3,S} {6,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.1209879862344923, 0.03948489805378244, -5.467135804412915e-05, 3.8729977932935336e-08, -1.0891099749414743e-11, 1883.1435106040624, 11.19842166398584], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.507337417078714, -0.006294464106528833, 1.1260002579030159e-05, -6.023455750872429e-09, 1.082010068231787e-12, -1038.8845628506424, -51.296744183199266], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 178,
    label = "CH3XCHCH3",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.1400362499920048, 0.03586163401322123, -1.1102147794825963e-05, -8.973994896167067e-09, 5.916366200757223e-12, -17348.9806971133, -0.977177146795837], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[21.50653652732509, -0.021538688697864905, 3.841340407827459e-05, -2.0490472449157003e-08, 3.671041814415652e-12, -23472.391811071706, -113.4637007990611], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 179,
    label = "XCHCHCH2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u0 p0 c0 {1,S} {5,S} {8,D}
3 C u0 p0 c0 {1,D} {6,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 X u0 p0 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.5930072780301965, 0.035712373835462545, -2.8891928944665743e-05, 1.0353993939432713e-08, -6.877535382356412e-13, 7214.8242215966675, 4.071128798576763], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.859718536630805, -0.012892198355494286, 2.298989109372911e-05, -1.2260623140565328e-08, 2.1968898796633675e-12, 2847.170076035509, -80.09956779067612], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 180,
    label = "XCH2XN",
    molecule = 
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.048535725500923, 0.028672115730176494, -3.482270440640814e-05, 2.2596352815551332e-08, -5.960529024806645e-12, 5190.313725543159, 2.5065816803148726], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.414355064771192, -0.0065324837634211244, 1.1674954821309034e-05, -6.2402674061796265e-09, 1.1201406725326385e-12, 2623.5240554623433, -49.970698213619706], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 181,
    label = "XCCCH2",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {6,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 X u0 p0 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.3828219732720616, 0.03183690702926364, -4.013911080353506e-05, 2.7619691192472573e-08, -7.788500545993845e-12, 14758.705509430738, 5.759672889040027], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.118025751357365, -0.007405955399938974, 1.3261644135403257e-05, -7.1051762665016375e-09, 1.2776266786152328e-12, 11947.028772911584, -51.834459720299336], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 99.7,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 182,
    label = "XCHCXC",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {5,S} {4,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {6,D}
4 H u0 p0 c0 {1,S}
5 X u0 p0 c0 {1,S}
6 X u0 p0 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.7048314413894516, 0.028376204780706408, -3.786451837501783e-05, 2.6544113342093204e-08, -7.541789535878568e-12, 37991.99215302152, -4.3718083329572766], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.19686106748589, -0.004925408360661187, 8.881806435863004e-06, -4.805475857370816e-09, 8.71058367975777e-13, 35723.4885464104, -51.66532426442821], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 183,
    label = "XCHXCCH3",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {4,S} {8,S}
2 C u0 p0 c0 {1,D} {3,S} {9,S}  
3 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 X u0 p0 c0 {1,S}
9 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.2361736008876079, 0.039119301071213676, -3.594454206491473e-05, 1.707824469528317e-08, -3.0713012365748303e-12, -5050.420080387294, 3.545077068093097], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.907345799408459, -0.013048554459586291, 2.3318763754336694e-05, -1.2471532880957137e-08, 2.2395066509179553e-12, -9539.164171805663, -83.8197330615869], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 184,
    label = "CH3CHCH2X",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
10 X u0 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.0128318011385724, 0.03960545794007049, -2.4179592309526814e-05, 3.2356569019992192e-09, 1.993147578264105e-12, -11692.467280459161, 3.3418356843999426], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.594098314175667, -0.018498118747171062, 3.2957976810558034e-05, -1.7553516674984645e-08, 3.141398607090435e-12, -17325.822237033535, -102.82834070762412], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 185,
    label = "XNHNH2",
    molecule = 
"""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 N  u0 p1 c0 {2,S} {5,S} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.2631676384047204, 0.026729584995038004, -2.8237319568592716e-05, 1.6164542474389308e-08, -3.698356854365778e-12, 9114.585888858403, -2.446239333520934], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.19947200837146, -0.008342021193629449, 1.471139402890261e-05, -7.709945286671133e-09, 1.3627191279000461e-12, 6354.25349120556, -57.70141059634063], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 186,
    label = "XCHCXCH",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {6,S} {4,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {7,S} {5,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {3,S}
6 X u0 p0 c0 {1,S}
7 X u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.2597991555257857, 0.04291106628020105, -6.112562626782867e-05, 4.4810510593462616e-08, -1.30454831688958e-11, 23094.539594321926, 3.525306358870278], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.261863218894595, -0.006846885764862458, 1.2247862318925582e-05, -6.547775704184015e-09, 1.1756042126397042e-12, 19989.377811619772, -63.24366361646152], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 187,
    label = "XNO2",
    molecule = 
"""
1 X  u0  p0 c0  {2,S}
2 N  u0  p0 c+1  {1,S} {3,D} {4,S}
3 O  u0  p2 c0  {2,D}
4 O  u0  p3 c-1  {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.6007898671749248, 0.014704846990202641, -1.4669745251396025e-05, 6.8193067307309135e-09, -1.14798047400528e-12, -12610.822959932784, -0.7662884219583095], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.295788322982971, -0.0025855457915561135, 4.764101310182035e-06, -2.661916406358756e-09, 4.947904274570403e-13, -14096.822274740854, -29.78275958089408], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 31.35 and 43.35,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 188,
    label = "XCHCHXO",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {4,S} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {5,S}
3 O u0 p2 c0 {2,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 X u0 p0 c0 {1,S}
7 X u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.6781923442105725, 0.03266563583708485, -3.4821251707147723e-05, 1.920133763315766e-08, -4.230295518156721e-12, -18830.11657197944, 1.4808288264278042], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.110950086361376, -0.007888898601392046, 1.4190125740615599e-05, -7.66127622554861e-09, 1.3863329006911743e-12, -22086.78981832706, -63.26454408255799], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

