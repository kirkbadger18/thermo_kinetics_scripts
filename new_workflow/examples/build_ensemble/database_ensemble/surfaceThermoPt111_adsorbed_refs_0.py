
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
            0.000000000E+00,   0.000000000E+00,   0.000000000E+00,   0.000000000E+00,
            0.000000000E+00,   0.000000000E+00,   0.000000000E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
            0.000000000E+00,   0.000000000E+00,   0.000000000E+00,   0.000000000E+00,
            0.000000000E+00,   0.000000000E+00,   0.000000000E+00], Tmin=(1000.0,'K'), Tmax=(3000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.0132854616344864, 0.03262761058111663, -3.706095174588169e-05, 2.0960395825783326e-08, -4.666933506314308e-12, -73636.16105886926, -4.75362406215651], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.852353543588185, -0.005708248496508993, 1.0285808375407224e-05, -5.567159908424731e-09, 1.0106531022767602e-12, -76593.18136393932, -64.44940816059835], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-0.059599820611586994, 0.034935604893275754, -4.398557905280544e-05, 2.8727528722406607e-08, -7.522184264363574e-12, -19769.190815760907, -0.9052005642652743], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.072877573168732, -0.0066430546226117085, 1.1791965438741444e-05, -6.2377005431965774e-09, 1.1116826317998652e-12, -22690.319344945012, -61.5268883603418], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-1.877920308666455, 0.028356288698697725, -4.277510879499753e-05, 3.274075934781191e-08, -9.75815608872388e-12, 2165.588379223996, 6.329199424648975], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.6692110049201245, -0.0046629868524260334, 8.163981923386376e-06, -4.222734018967867e-09, 7.383907972091739e-13, 289.9618995796627, -35.46553410089045], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[2.9656085337498954, 0.013397832123679575, -1.3429344690682003e-05, 7.121751881737713e-09, -1.4106285584070122e-12, -26720.57606148652, -6.154667707403949], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.63538004944615, -0.004641489077444732, 8.09256458094881e-06, -4.167623618966353e-09, 7.263873560942958e-13, -28149.71604155514, -34.81282407199237], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 47.7, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[1.9262988619212185, 0.023920986270762893, -1.1102891365437597e-05, -3.274735343365107e-09, 3.4649297320221706e-12, -53957.549596319666, -0.7623716616782268], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.909732388825518, -0.01149769907640833, 2.0325691574327667e-05, -1.0702611808122697e-08, 1.8994750772814185e-12, -57537.77471575589, -67.87703678390542], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 12, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-0.2962185933988644, 0.021861819147589476, -2.3841617463750517e-05, 1.409576958390365e-08, -3.388230668255332e-12, 10086.33257920813, 6.207184485801547], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.412928956143153, -0.006234425804471642, 1.1089327437971031e-05, -5.8875786554574085e-09, 1.0512700719032776e-12, 7889.596116931369, -37.77146207903395], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 35.45 and 72.61, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[1.498046107406174, 0.02876140744368179, -2.68861983561367e-05, 1.5278311802666502e-08, -3.7822904530582235e-12, 21958.440668145617, -1.1152321426025136], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.832729154985131, -0.012370334275977501, 2.1968674778205687e-05, -1.1633971170730624e-08, 2.0721780580768446e-12, 18461.84781007111, -69.01651034223298], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 51.8 and 63.4, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[2.2137160105042617, 0.012214676187922345, 1.9068675577301008e-05, -2.8645440448761984e-08, 1.1057901122546454e-11, -13128.815677201204, -3.327331686740701], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.869139226344814, -0.017678329773877535, 3.144153037560741e-05, -1.6706168903885125e-08, 2.9833575253225206e-12, -17331.930011685043, -75.91019621237146], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 77.2, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[0.34655425022423486, 0.03320903146374052, -3.2298746440141706e-05, 1.7752091169212644e-08, -4.033794132052293e-12, 20810.092200469113, 3.586650323801086], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.940337148471109, -0.01227100059599298, 2.1814353103836214e-05, -1.1572978619261788e-08, 2.0644252739308432e-12, 17030.249050018334, -70.54967983280945], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 12, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[1.4289514345775889, 0.014037445912949188, -2.2117880511546625e-05, 1.7865950156490832e-08, -5.7147862830841945e-12, -28652.23112549835, -7.782662330904841], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.486566622474089, -0.0016811903234558259, 3.090308118223416e-06, -1.711868677549822e-09, 3.158649696949356e-13, -29564.933280494686, -27.678856345502883], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[1.2935534672257092, 0.012551181494457409, -1.3054228857274847e-05, 7.661604760907483e-09, -1.9215514596160332e-12, -688.8763008005758, -0.2389796920212941], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.516821517451049, -0.0038395553030562057, 6.87833637081396e-06, -3.6890056278649886e-09, 6.639624483559064e-13, -2040.4145460333161, -26.7584246367704], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 38.5 and 75.09, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[1.3392517506347479, 0.015618782360796477, -1.787059252180068e-05, 1.1610327846079934e-08, -3.20827392430445e-12, -22785.095971412436, -4.278239925919128], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.472501868868654, -0.004256523643468164, 7.672402782773711e-06, -4.150942931718005e-09, 7.520574349498309e-13, -24346.773433106857, -35.277748369370684], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[0.3361063437283102, 0.02264832889133044, -2.3923896928517282e-05, 1.372564500933275e-08, -3.2403177363526936e-12, -16594.314628911652, -1.8821696787908033], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.524888624968044, -0.006507330938044994, 1.1658617720730316e-05, -6.256802483730942e-09, 1.1264926555990982e-12, -18943.855417003968, -48.42251325165718], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-2.6680472878038244, 0.029069338138602973, -4.8265331321120956e-05, 3.8758909084069156e-08, -1.197493840199293e-11, -29.434709653963765, 9.729399453355859], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.904298681259508, -0.002638650544720537, 4.717292856601338e-06, -2.5126700748149e-09, 4.496592934290092e-13, -1575.6858123263455, -26.710793165152253], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[0.3390691543415923, 0.01798477612437323, -8.009977251468385e-06, -2.618497985758581e-09, 2.5890609101075768e-12, 12671.060086618376, 4.139041577988783], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.264107395010047, -0.009024685340644857, 1.6030093656987307e-05, -8.50179846886495e-09, 1.5167137091078899e-12, 9922.690169950261, -47.202080751012694], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 57.54 and 70.14, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[1.3072075375182812, 0.016596072255389574, -1.6559253185471342e-06, -8.536445042335518e-09, 4.498179606571284e-12, 4090.1946953676497, 1.0098625648933197], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.184232258898149, -0.011502131450414765, 2.039505158252215e-05, -1.0788041807467524e-08, 1.919978455058478e-12, 990.4856147857554, -55.65816457564575], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 12, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[1.9091619785380285, 0.02153481361381348, -9.82324936658643e-06, -2.19029425959559e-09, 2.4632899886523063e-12, -2942033.3902943116, -8.92748554705555], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.863871656752833, -0.010727742260458865, 1.9186856661499014e-05, -1.027692150941159e-08, 1.8476574064403995e-12, -2945382.0740491888, -70.90074101305477], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[0.5500262969193581, 0.030684202469102535, -3.992249753741026e-05, 2.5278303136043825e-08, -6.3331111188613676e-12, -14312.116908334541, 4.895455951409469], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.242175297857134, -0.0029122603612647792, 5.392008844105671e-06, -3.03119346586325e-09, 5.661929309593158e-13, -16613.356614081342, -43.404654980043354], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 71.1 and 71.28, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-1.9451797364169205, 0.0395654024230427, -3.0393046626231198e-05, 9.79287635313427e-09, -1.9579476928655026e-13, -26669.857396276428, 13.106463263468857], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.784776027743074, -0.015222694741347595, 2.7096928465977484e-05, -1.4411836968474808e-08, 2.577084860344147e-12, -31672.487204501376, -82.8573600567613], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 93.4, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-1.254793621582766, 0.03768476714424869, -3.9353818215358633e-05, 2.1670811364191383e-08, -4.778594187015983e-12, 7802.174069461278, 4.101768954903813], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.93650153546616, -0.010360492624125665, 1.8520756188654075e-05, -9.908384178320885e-09, 1.7799915628090041e-12, 3925.065730925031, -72.84125571769417], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[0.49883454048306, 0.022031201995767018, -1.630219529071573e-05, 5.401409894036828e-09, -2.950070743246158e-13, -6118.9887095755075, -0.34124302923646965], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.308085389086264, -0.009363149454304559, 1.6709016551331095e-05, -8.91840100082296e-09, 1.5986925799567168e-12, -9033.588320966519, -55.82031172675297], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-0.9101399566489929, 0.03643403579329225, -4.22975540175297e-05, 2.6415078172539904e-08, -6.695602405848433e-12, -29358.66928954159, 8.346346609316232], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.917020687604804, -0.00926655189418087, 1.6416414217512585e-05, -8.660235302430622e-09, 1.5391698772991309e-12, -32784.984922959804, -61.19161366687341], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 35.97 and 69.6, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-2.3700676918334564, 0.045287905228815074, -5.4441930156142e-05, 3.432254837964767e-08, -8.711850685294564e-12, -21045.811963586337, 8.336898697810556], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.05455082400916, -0.009769463971518944, 1.743836321958101e-05, -9.305576603496909e-09, 1.6687316066184114e-12, -25070.928883766064, -74.0555612930599], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-1.6079189052290623, 0.0365072568196629, -1.7302803044623743e-05, -2.632705951762784e-09, 3.772884782371477e-12, -1307.2457445912373, 11.717951400467895], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[18.686830394351823, -0.018861777121976845, 3.369444151006925e-05, -1.801704019499433e-08, 3.234259112968891e-12, -6962.750896894848, -93.34003071327658], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 74.1, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[0.15333093864547764, 0.023129686783266632, -3.289590795769528e-05, 2.441141448952092e-08, -7.243664001954642e-12, 15769.442164671693, -1.7896837262996748], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.537079417329014, -0.003857750779531019, 6.934770920070957e-06, -3.733040236094655e-09, 6.7380093000881e-13, 14055.140203142775, -38.320594459140004], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-1.758296794636702, 0.04202640151750035, -5.6007536385151174e-05, 3.825182908222041e-08, -1.0409416384415948e-11, 20595.216174202695, 5.85341156751963], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.077474570472168, -0.006939960216313432, 1.2365235918803366e-05, -6.5765282992753485e-09, 1.1767590618301862e-12, 17341.55583080725, -62.89449360449413], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-0.5789725109422761, 0.03719156947423709, -1.2289771963968359e-05, -8.771791809055038e-09, 6.040390410078089e-12, -8256.903464537836, 1.4727597507431014], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[21.5363816942028, -0.021593238218764646, 3.8529904325461395e-05, -2.056918248878735e-08, 3.6875582882373026e-12, -14499.83182535739, -113.39905386774977], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[1.2626258291795687, 0.02397069589838703, -3.578069676786691e-05, 2.6941743821081576e-08, -8.087010228141622e-12, -3678.1450772659327, -6.660766627246151], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.29013676340653, -0.0024479549630102345, 4.512500116241401e-06, -2.513110578094857e-09, 4.657872140968094e-13, -5274.242097483941, -41.25295452274815], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-1.798153489438984, 0.032699626005164455, -4.2566230420913136e-05, 2.9154249036912876e-08, -8.035856702282018e-12, 5064.0136117896855, 5.848060021291595], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.430231180744155, -0.006459576055061384, 1.1544899962263376e-05, -6.169056776583929e-09, 1.1071361180809737e-12, 2380.414399962232, -50.12254952389564], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-0.3088563851979457, 0.0283916874007889, -3.0151732071124332e-05, 1.7719749516283752e-08, -4.275930304276088e-12, 9404.031440616978, 1.0285424176862534], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.348629912254271, -0.008905560700516197, 1.584616974625862e-05, -8.417565551744804e-09, 1.5032447502223972e-12, 6441.029010797103, -57.93257830820272], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[0.4723974842594119, 0.027761496719987674, -4.4882510241380575e-05, 3.68137619172982e-08, -1.161323814891091e-11, 27935.478697850187, 2.4117785112268066], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.532291909983105, -0.004937822379131875, 8.640827527955757e-06, -4.462041957191014e-09, 7.786526296378301e-13, 26224.704044820046, -36.66572094479413], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 90.3, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[0.880908266679414, 0.018320052300656302, -5.853299352285859e-06, -4.762000592607702e-09, 3.300731216127062e-12, 7705.912138032893, 1.698854142380263], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.862721998600472, -0.011203107450708254, 1.9721651219843414e-05, -1.0314976584726718e-08, 1.820102655560301e-12, 4645.064467894128, -55.203994034281315], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 78.71, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[2.54964916159526, 0.01846003844850294, -2.4200109760726446e-05, 1.7347497091245413e-08, -5.041828066154608e-12, -13946.272980195823, -4.2477643742515845], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.099145643017163, -0.0044001843334030635, 7.81454060321164e-06, -4.134669468843119e-09, 7.364144304799385e-13, -15522.315051282196, -36.921024105994164], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 26.05 and 32.19, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-4.4984127088896, 0.047450522898494066, -6.331779821893872e-05, 4.414452419290103e-08, -1.2310062691422985e-11, 3574.08958027256, 16.95019036384414], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.436461478920393, -0.009004134479838097, 1.60928212197061e-05, -8.59948663735323e-09, 1.5431118907086212e-12, -188.29460678238138, -62.2566299700216], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[4.152110941060882, -0.0005487132048016898, 1.6858930590385167e-05, -1.8335786801037368e-08, 6.296303756148092e-12, -17924.620199289424, -11.442037711879966], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.40512488832978, -0.006902168774862402, 1.2352154347418257e-05, -6.62362962329398e-09, 1.1913644441634286e-12, -19405.699045911246, -34.841791130752156], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 51.8, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[0.7328851297248515, 0.03226341164733181, -3.7795877053763525e-05, 2.3986538279416032e-08, -6.161557375428117e-12, 11385.115413747153, 1.3588387160692363], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.000137061039034, -0.008557091043047986, 1.5075798741871962e-05, -7.885511119302832e-09, 1.3920669867208742e-12, 8361.510372994293, -60.26006040280568], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 37.45 and 56.05, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[2.356981745321061, 0.016581789113467013, -8.932456041939218e-06, -5.966003689912623e-10, 1.6571154171085567e-12, -50182.63890427325, -0.543207516411865], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.047791359753676, -0.007242743771753241, 1.2909101836660162e-05, -6.880215062641951e-09, 1.2328955029475026e-12, -52585.95371271731, -45.472846353459744], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 12, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[3.057378346580329, 0.012862428884006145, 4.849286950384415e-06, -1.3599718395029272e-08, 5.96899960014774e-12, -30460.463587753868, -12.435908461234193], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.113485534323576, -0.011408786775687923, 2.0203001135173403e-05, -1.0664783232592045e-08, 1.8954587248723453e-12, -33417.893289467305, -65.26660390807183], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[0.257616722538468, 0.019381161206708943, -2.9969201901782738e-05, 2.2777218830825994e-08, -6.826799542336559e-12, 33690.91634292551, -2.70420652880128], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.608145428437815, -0.0014237734758236011, 2.641982059585679e-06, -1.4828987065853545e-09, 2.765400103395678e-13, 32516.821798320576, -28.854135782839876], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-3.9682655700924205, 0.04821224322916432, -7.020382754527538e-05, 5.070190901774644e-08, -1.4459940189670561e-11, 28042.3595326327, 14.062496205310104], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.256187848213406, -0.005010574566613095, 9.091246735435043e-06, -4.959982299347285e-09, 9.052412241843371e-13, 24840.060131814553, -55.90859791130441], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-0.5903493375055966, 0.028202930949822125, -4.319205471958818e-05, 3.320670015772019e-08, -1.0016171919646766e-11, 22453.417495377325, 0.22475283272965862], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.592991393954042, -0.003510020572420052, 6.291002447858268e-06, -3.3685290767449704e-09, 6.056109381544889e-13, 20651.650872946, -39.7960420024965], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[0.4442631534202558, 0.0351433935419179, -3.8251911957030606e-05, 2.3195475658218973e-08, -5.754598186857862e-12, -1563.6498371394032, 1.9827666071889531], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.745142193595743, -0.011132969717265212, 1.9585112575904104e-05, -1.0221697678564483e-08, 1.8010348359985117e-12, -5162.188695743647, -70.19620556073879], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12.72 and 84.97, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[2.7253442534639816, 0.014265170184759474, -2.2141020445308393e-05, 1.7159763247973412e-08, -5.148140594379846e-12, -13995.525203209438, -5.880073500148155], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.853407080304208, -0.002062821909688432, 3.577712452188777e-06, -1.8218841229896364e-09, 3.147031466937131e-13, -14879.659854132053, -25.965590783471704], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 12, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[0.8461597506391333, 0.030516767779180914, -4.1881702417517896e-05, 3.038456998083873e-08, -8.772416820734819e-12, 22184.64883126651, 1.7005984843899942], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.071582906242911, -0.006359525728146864, 1.1223991720428105e-05, -5.882504318359616e-09, 1.0398336922415319e-12, 19799.792855548934, -48.97471372204803], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 24.23 and 51.07, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[0.9579364986986779, 0.03417770159679337, 2.8267603505906824e-06, -2.457700198169472e-08, 1.1560079282713076e-11, 11047.727554205501, 2.1103362978472227], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[24.884358222018623, -0.025217745838263753, 4.491342311074376e-05, -2.391311311619964e-08, 4.2785533688020905e-12, 4080.474928104857, -123.21632842360908], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 37.85 and 59.82, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[0.5564428527368827, 0.02488188419324113, -3.188387979768033e-05, 2.1907620558739207e-08, -6.062372825965667e-12, 20027.19241685883, -4.096400994709519], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.380929521863413, -0.005719366556090541, 1.0097890187526979e-05, -5.296771085574379e-09, 9.37012913345748e-13, 17910.62855721181, -48.1251454976711], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[0.4610702474827821, 0.025330918143713757, -2.952414111342533e-06, -1.2660214463929042e-08, 6.611412806112327e-12, -20945.857488634785, 3.458601622411164], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.750185052643534, -0.016155449576488602, 2.8860320922404392e-05, -1.5435831253719662e-08, 2.771547477197628e-12, -25634.156181712737, -81.59744503072963], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 92.3, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[0.36992674168653406, 0.02865853138856462, -2.7893618373901037e-05, 1.3652626507653384e-08, -2.5391216906811565e-12, -30077.931163014724, -0.37004604148440023], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.223403098671879, -0.00774166810729786, 1.3941845053646948e-05, -7.541931084038746e-09, 1.3666956123401224e-12, -33158.986310599386, -60.68009393384265], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[1.5846760207902126, 0.02138754950950943, -2.6680149499382816e-05, 1.8085986641749082e-08, -4.954679028168485e-12, -1308.3990428132315, -8.566494007825705], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.406551623095453, -0.005399648922306209, 9.490951838389432e-06, -4.944506127843273e-09, 8.7003523316202e-13, -3201.0288683360814, -47.67579637039697], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[1.280385791041996, 0.026146381291559016, -3.3204709331128187e-05, 2.1735482177749762e-08, -5.739485275935152e-12, -7487.39609621765, -6.266983747164308], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.200444140609262, -0.00438799368424037, 7.853858549695917e-06, -4.205155301690587e-09, 7.569009489132158e-13, -9640.574126602842, -50.856690261227584], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[0.6873674741262125, 0.02132346944890292, -2.3360399760553087e-05, 1.4597549431102648e-08, -3.8509542776843375e-12, 14055.252300654407, -4.107463299522097], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.374615944582587, -0.006606543048415989, 1.1797360181945329e-05, -6.297363597977889e-09, 1.1289628357603193e-12, 11841.501599272553, -48.04572552374455], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-2.7274572524716953, 0.049119319550163645, -5.721652497603516e-05, 3.620713165535818e-08, -9.375812626277735e-12, 10842.81525104137, 9.215041804559704], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.965388395078815, -0.01266512956575761, 2.2613298162312797e-05, -1.2071212014246423e-08, 2.164311373349659e-12, 6193.814232811177, -84.83327362646364], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-0.14057965370883313, 0.03395928839141769, -4.877970542687814e-05, 3.545524730076265e-08, -1.0228443092508144e-11, 30418.979638946523, -0.9856796655624507], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.244757631333488, -0.004423005476268391, 7.940488035409221e-06, -4.265902533836515e-09, 7.694698624474174e-13, 28048.763001310137, -52.21194594432034], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-0.15487855368891051, 0.024665034128503856, -2.7882905742975686e-05, 1.674350275498315e-08, -4.172544254554822e-12, -14958.976405646741, 5.361930025591265], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.176496183329407, -0.005390103654209033, 9.767429234661937e-06, -5.327193686593086e-09, 9.715802550783626e-13, -17324.044702053732, -41.796085093863034], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 20.1 and 76.7, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[0.2813950385256072, 0.023606090400724596, -3.3295873498145274e-05, 2.3593744703000332e-08, -6.599876894997081e-12, -26392.19299827283, -2.849391664352071], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.572784026130903, -0.0031657944524944312, 5.618129387781828e-06, -2.9683239438015378e-09, 5.286847314914158e-13, -28054.169018174878, -38.829756548694135], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[0.8975857479384785, 0.024674306052233225, -3.701359961395592e-05, 2.8207317800886772e-08, -8.568604159542303e-12, -9017.011994338272, -4.673145748543339], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.178182501667196, -0.002748726956674804, 5.052972658841414e-06, -2.803448324677592e-09, 5.180259484040403e-13, -10672.917491410266, -40.51071502087554], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[1.6808021563043372, 0.031212610386517608, -8.078908368598723e-06, -1.0837720993507388e-08, 6.482207132174622e-12, -41056.54731532608, -5.807876399267538], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[20.413219942556097, -0.01736018391676285, 3.107644929253181e-05, -1.6671325641389122e-08, 3.0008306359545142e-12, -46399.67737576667, -103.39683977094955], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[1.0356516612906221, 0.024037626351487797, -3.1071517502854826e-05, 2.1274644888654494e-08, -5.936341695989e-12, -17301.741260448573, 0.8423300649336518], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.320902420594736, -0.004524709457421384, 8.146698589352298e-06, -4.398957466229152e-09, 7.961296162925903e-13, -19306.65648643588, -40.562177218977006], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 29.74 and 57.23, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[1.563279221180646, 0.014266187393854025, -1.2973938191255478e-05, 7.268775468476812e-09, -1.690748235860795e-12, -10648.083370846112, -4.452608283390472], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.417075986297514, -0.007111062744199659, 1.2402765963068252e-05, -6.388062948055837e-09, 1.112839399284942e-12, -12418.664374606702, -39.25667844441427], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[3.767151168018872, 0.0041795304132046605, -5.164603061744141e-06, 4.281737107516682e-09, -1.53270538622019e-12, 19777.17389757261, -16.448669925442687], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.522345399044181, -0.0014872471505972197, 2.711551430305864e-06, -1.4880483774394292e-09, 2.725089394624866e-13, 19311.3871238674, -25.372463575771846], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[0.5872272419093931, 0.02188425374561855, -9.092097282359604e-06, -3.2013094266342026e-09, 2.9345692542648294e-12, 2944.230439484785, -3.0977389241107227], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.083489072060392, -0.011983006093131441, 2.1302955374556336e-05, -1.1309817688688326e-08, 2.0190228680020024e-12, -539.8493474971001, -67.81740135467018], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[0.569722410937789, 0.026888160051806696, -2.5056254060616178e-05, 1.1463352656716351e-08, -1.8672528800944832e-12, -18898.182467421095, -3.3542668371249835], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.974057020660581, -0.007721493775403571, 1.3817688459320575e-05, -7.405228719045624e-09, 1.3327051932182123e-12, -21878.51727423972, -61.470399266548576], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-0.5007041222485064, 0.020387505380996075, -1.8341220404454415e-05, 8.052118908019455e-09, -1.1760176166220049e-12, -22441.732195559624, 7.4226327062441815], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.403552916321383, -0.006564510724457797, 1.171835932549729e-05, -6.2584682466745926e-09, 1.1227488750043197e-12, -24771.94760103823, -37.96806552154803], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 58.4, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[0.1702965064381686, 0.0268182243912849, -2.1187990710913476e-05, 8.209912931753756e-09, -1.027764678918075e-12, 15062.558701944921, 4.199426716436971], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.950283973574049, -0.010553855620259798, 1.889093837993397e-05, -1.0126216905413026e-08, 1.821528611810081e-12, 11623.14201144497, -61.349263752501926], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 12, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[2.1585639863746304, 0.024853988358157296, 1.535261770319857e-05, -3.2530250732843954e-08, 1.350676862021949e-11, -15197.77796911487, -8.741405924676787], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[23.28324248920542, -0.024540711211524867, 4.373135677424702e-05, -2.3303703808341322e-08, 4.171503691519779e-12, -21524.27012283978, -120.20188474457468], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-2.729788178236207, 0.0477487229680002, -4.578266674370747e-05, 2.345187412267026e-08, -4.784866947105115e-12, -827.8272968143812, 9.234684278219335], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.85666165262948, -0.0157309966303632, 2.810772015631403e-05, -1.5027652331573117e-08, 2.6975423746144773e-12, -6181.146545955275, -95.48104058044015], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-3.876486774098748, 0.05041092235724696, -4.037083717101234e-05, 1.4788222259221832e-08, -1.2397097237659693e-12, -2230.417329603531, 15.749899480627498], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.660133951494895, -0.018925451027069166, 3.382116921470824e-05, -1.8093156895228866e-08, 3.249415703686625e-12, -8507.00045515715, -104.75676803324947], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[3.3727183181310663, 0.011948605519731054, 2.7150456278172386e-05, -3.885263527850272e-08, 1.494058696205336e-11, -28697.103288473998, -7.758957601829623], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[18.516664160344224, -0.01907467041735614, 3.401223935596551e-05, -1.8145942414686017e-08, 3.2514411153175722e-12, -33455.51623468162, -88.75718953272812], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 67.3, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-0.2535897313874534, 0.0331664250530546, -4.26353265906766e-05, 2.860999415456707e-08, -7.693949644060893e-12, -14782.875694250031, 5.808089455489809], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.17144192711477, -0.006471976780827487, 1.1485655604528556e-05, -6.073134201469678e-09, 1.0815666921505608e-12, -17513.35501244603, -51.16815885849472], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 15.1 and 62.25, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-2.344331580931251, 0.04526673811325238, -3.3447648876703853e-05, 1.0361211371477251e-08, -1.3049283875687934e-13, -5903.996526555315, 8.413327357263137], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.655427687549018, -0.01862190264154633, 3.322657498801844e-05, -1.773344101340103e-08, 3.1788171677175556e-12, -11822.375610952313, -104.46654041680591], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-2.230064578218667, 0.029222282416047858, -4.3315468288873805e-05, 3.314280272920028e-08, -9.964716551902342e-12, 1932.0152202917895, 8.30171716264812], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.834592696175528, -0.005149253851190691, 9.154900439171405e-06, -4.849169380144079e-09, 8.637658222411613e-13, -104.70027732414474, -36.22149496391735], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[0.04255587293466731, 0.02793280228431379, -3.942772006846689e-05, 2.937989976562643e-08, -8.786783800562858e-12, -5530.7442946885885, 4.036376718408193], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.117743977533117, -0.00500206489027314, 8.996355973457801e-06, -4.8465482727643565e-09, 8.752672658917174e-13, -7655.655696328353, -40.93666941907976], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 38.0 and 95.1, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-0.9848787280247688, 0.036014805712588804, -5.065239572480353e-05, 3.628430114231815e-08, -1.0380460380154943e-11, 36248.15432531257, 1.664668108546251], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.257828530252164, -0.004865143870368689, 8.797732294972834e-06, -4.77770420172938e-09, 8.686592687967868e-13, 33644.38992481046, -53.96726152935313], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[0.49874245991247795, 0.020575187483968492, -1.2687784179351753e-05, 2.0580096976764587e-09, 8.05244759760626e-13, 5237.227486892948, -3.116375604882137], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.222901125754033, -0.009612809130552818, 1.715947768609834e-05, -9.163517606104818e-09, 1.6433481467715682e-12, 2295.7409883718174, -58.400890305187225], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[2.366216905242268, 0.019020740681499247, -2.6531517990758492e-05, 1.9018956406066634e-08, -5.525649382498443e-12, 16036.37517800213, -10.664684905216351], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.334160815533737, -0.0023200121205334866, 4.273612948513463e-06, -2.380222376157214e-09, 4.4120735219471815e-13, 14626.85403758704, -40.310248213403455], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[1.6717609114194338, 0.024196095571897606, -3.0224106307781948e-05, 1.9895399940584717e-08, -5.340183156787859e-12, -14306.41047725602, -7.690276919545998], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.180364931483787, -0.004638309918558671, 8.31984432845496e-06, -4.468746102309751e-09, 8.058137202616262e-13, -16383.958162190818, -50.31831828854056], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[0.19306645245090961, 0.028838421998995875, -1.1311610948258136e-05, -5.046731874145793e-09, 4.143907439413397e-12, 5981.958325716183, 4.7606721747489065], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.777501237337898, -0.01574120705773587, 2.8070452760538087e-05, -1.497215281212219e-08, 2.6824589404383318e-12, 1333.628433885442, -81.23811178641964], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 12, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-0.29447422313105176, 0.014416257266545251, -2.6132258567564956e-05, 2.1900587545061747e-08, -6.98019593514676e-12, -13066.56292199151, -0.19945296939395463], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.9024434885596095, -0.00033857968757166045, 6.433677259571566e-07, -3.6632446677898547e-10, 6.90090255981083e-14, -13654.383910319877, -15.255951597680065], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[1.2303862732350404, 0.021364181138588848, -1.0987940121250137e-05, -4.0856023207660433e-10, 1.727923359950978e-12, -28484.14644066993, 0.4124434938860695], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.896116437024, -0.01060293952494541, 1.8955775325381568e-05, -1.014589156561841e-08, 1.822929746606375e-12, -31732.223198847954, -59.95427717347311], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 23.8 and 88.9, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-1.9435071260361387, 0.019776732831383245, -3.3633647812076675e-05, 2.6902708865759773e-08, -8.279588820103712e-12, 11854.359783882872, 7.17468899729019], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.8134783548689057, -0.0006939614447037847, 1.3030892875136696e-06, -7.387048270359375e-10, 1.387965682836422e-13, 10913.818753346017, -15.573868627012752], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[2.009599362550931, 0.013359751800887266, -1.623038022297414e-05, 1.100295092154081e-08, -3.144848964575786e-12, -51161.538297831234, -2.59294204334965], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.982982484199136, -0.0030987129918549896, 5.628827612542049e-06, -3.0784730588190227e-09, 5.624488513619069e-13, -52413.19520304462, -27.65201114186268], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 10.8 and 12, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[3.8640642056130954, 0.000753456181943244, -1.6557138003731004e-06, 1.5522317389969161e-09, -4.4678204278586486e-13, -5043.701704990381, -8.858065697537072], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.068796960214846, -0.0004958073404752167, 6.592349576425383e-07, -1.7259799397636866e-10, 7.629699988490827e-15, -5055.127199699664, -9.71918001187639], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 12, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[3.9971693162721293, 0.025096348548238282, 1.327400938336068e-05, -3.2292491449438716e-08, 1.3906143597752774e-11, 5798.338390415482, -7.722061591443751], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[23.93148504766841, -0.020915955341405914, 3.7374058428797565e-05, -2.000214098425695e-08, 3.5937322453820364e-12, -173.2804237922901, -112.97983760126856], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 41.92 and 44.79, where replaced by the 2D gas model.
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
4 O  u0 p2 c0 {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.9670346153625404, 0.02010733549192463, -3.430873998744845e-05, 2.7576743917528512e-08, -8.530565143161084e-12, -10157.669398268656, -5.635470610931528], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.8019396814478945, -0.0007299198999782928, 1.370214354340261e-06, -7.761672795197918e-10, 1.457420379160772e-13, -11113.96518595214, -28.75413977980474], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[2.229828010589702, 0.028570616038480778, -1.4963298962563707e-05, -5.176313642516329e-10, 2.3810120541867263e-12, 7312.263328136929, -3.8814149969962912], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.66216369529078, -0.01376703499631563, 2.461032395967154e-05, -1.3171447002263131e-08, 2.3665201200583075e-12, 3023.897816417526, -83.71181218679985], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 11.99 and 57.8, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[1.379931856876878, 0.017751034704135662, -1.20849897621581e-05, 2.5391380911160403e-09, 6.810073338581191e-13, -10706.575442002862, -0.2827749520379772], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.249400879126325, -0.007938520517119636, 1.3942004304920195e-05, -7.265193204010204e-09, 1.2784307609119226e-12, -13075.333404279958, -45.75608364958869], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 21.45 and 69.68, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-2.6719194973911913, 0.03806450613181096, -3.8243597700626554e-05, 2.040231059078257e-08, -4.289291144488061e-12, -2552.6997456698264, 10.504073795419304], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.22899506611368, -0.011870659656779135, 2.115216565464828e-05, -1.1264162101025072e-08, 2.0156694171299776e-12, -6628.993139342954, -70.11901785345802], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[1.9695874038742542, 0.020522894662730294, -1.162128054762119e-05, 6.215825757649115e-10, 1.3989989722240637e-12, -25364.566361810605, -2.354837277688844], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.866079481012617, -0.009800423856572567, 1.740457263723408e-05, -9.223255333892852e-09, 1.6448101391910563e-12, -28362.636330228248, -58.59458617424234], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 29.77 and 83.13, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-4.928535066156777, 0.05534718152841099, -7.064613041223003e-05, 4.6785374266793156e-08, -1.2437668950315839e-11, 14404.844629803763, 18.280985628689567], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.083457114486164, -0.010265295379706975, 1.8411727682612908e-05, -9.893069344828777e-09, 1.7834012939381763e-12, 9838.535058993499, -76.62810888427353], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[0.8730990245545511, 0.0193259016363898, -2.4337266409278695e-05, 1.613265810080733e-08, -4.345260262716977e-12, -19217.95030182001, -2.940452198060793], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.634569118494452, -0.0037356801113829206, 6.726671065463905e-06, -3.6343862440579493e-09, 6.579582612385249e-13, -20862.15796536253, -36.779209772119685], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[2.0573699775793144, 0.018785510110437723, -2.9380697243515823e-05, 2.350186851777543e-08, -7.340232588415319e-12, 8667.368701587955, -10.421554931384417], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.609523066033187, -0.002985916758486858, 5.278299518393445e-06, -2.7673950243381226e-09, 4.893079722596751e-13, 7449.33790035334, -37.5335052093629], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-4.325685008569385, 0.05227616954992121, -6.524815321269428e-05, 4.254890479161197e-08, -1.1179376868675206e-11, 11418.13491042579, 15.786044045814936], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.035495081023953, -0.010328866072735542, 1.8514421035614053e-05, -9.939820509564141e-09, 1.7906297172559822e-12, 6966.794557499175, -76.07100602733667], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-4.338341622878529, 0.054935616039443906, -8.043478034919602e-05, 5.94297263297502e-08, -1.7339199520627346e-11, 21364.09816773268, 15.175251696241146], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.219593046266771, -0.007225570624320216, 1.2980701378227372e-05, -6.981180433014227e-09, 1.259477509332513e-12, 17631.254206027443, -66.26216346010469], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[4.854961897036134, -0.005541347878692391, 3.0119805912451168e-05, -2.992258851269518e-08, 1.0050251429694068e-11, -12109.97604747872, -9.256206302347536], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.54139376655309, -0.010402513409079085, 1.8377739993644733e-05, -9.667651291471017e-09, 1.712113788146074e-12, -13847.909955863295, -35.56384362882458], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 12, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-1.029643429257797, 0.030564364812808678, -2.5733365236408486e-05, 1.1293796508562125e-08, -1.821806594470843e-12, -1068.8135834985303, 2.6617654177208334], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.23895439949048, -0.012066252955547127, 2.1530937349880913e-05, -1.1489313129942582e-08, 2.059020397351995e-12, -4857.258045570429, -70.27958695073116], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[2.654525781384738, 0.015399192759007755, -1.0183826670136425e-05, 1.7530317633750062e-09, 5.796144814107507e-13, -39696.085934091636, -11.081140115163478], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.183628262664506, -0.005481556393490509, 9.93504727113442e-06, -5.424764980061756e-09, 9.901839547951652e-13, -41778.769861696914, -49.97906879822565], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-0.26477234399099003, 0.030351769992554175, -2.0473774973402812e-05, 4.470350596539826e-09, 8.498098058584702e-13, -28999.468169057975, 6.5331825956054494], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.898898669499472, -0.012891073692233745, 2.299988925750164e-05, -1.2274824918481832e-08, 2.2004937612731326e-12, -33116.781662783476, -71.46368014442578], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 58.0, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-1.2534176212234776, 0.03273020710355639, -3.754929968340668e-05, 2.3211455622512245e-08, -5.930839153123202e-12, -10921.528900830286, 9.926598033908576], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.179468174894188, -0.007798116901814758, 1.4043737251620289e-05, -7.59182015080697e-09, 1.3748378944225233e-12, -14048.248138784045, -52.78358959012762], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 98.6, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-1.1589268706614626, 0.03704248615588873, -3.1233211398208235e-05, 1.2995299183184974e-08, -1.8017601299824548e-12, 1243.496527885637, 2.9590731669920705], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.804653938713708, -0.013393435838752497, 2.3947519559819192e-05, -1.281803436772642e-08, 2.3031836481675772e-12, -3263.35563808022, -83.79742663134887], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[2.3606845113620163, 0.014165730210107377, -1.892001900851417e-05, 1.3801126624201276e-08, -4.17869384927716e-12, 10993.977693041259, -5.695742664902356], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.213817876105684, -0.0025695804418744764, 4.704906575632948e-06, -2.598848026439401e-09, 4.785325044545847e-13, 9802.072851486633, -29.994800796459174], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 67.9 and 67.9, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[0.9288946551072406, 0.016318625808529635, 6.61272571693265e-06, -1.7902849148792276e-08, 7.848204724991703e-12, -8983.532828862752, 1.6939762269787586], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.774420011620451, -0.014595529984823143, 2.5847799476923094e-05, -1.364660019490522e-08, 2.4255124479537725e-12, -12763.1953250939, -65.80622703445292], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 95.95, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[1.1312884557033185, 0.018402865797038655, -2.4277881914136098e-05, 1.7224355907441603e-08, -4.970784200919454e-12, 25592.14164185977, -5.779521623383241], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.494137250133402, -0.003797247762429932, 6.797288946156249e-06, -3.638182361607298e-09, 6.538479728756012e-13, 24061.66747290308, -37.52197446358283], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[2.863304528558866, 0.0044727378996352735, -7.657888254030577e-06, 7.566551322548495e-09, -2.8240309396521113e-12, 11972.188237751529, -7.401146569539408], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.411396737184079, -0.001603184063414779, 2.888007862004574e-06, -1.556323952810142e-09, 2.807779740962135e-13, 11606.515341396287, -15.027258594306398], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 56.8 and 56.8, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-2.573926383023027, 0.047739907569547935, -4.598070554827077e-05, 2.3513549757145586e-08, -4.7455095408821535e-12, 122.00865925706307, 9.441519150073963], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.908024758287098, -0.015549251038031646, 2.777294226619841e-05, -1.4841532460530524e-08, 2.6631323285942338e-12, -5192.87026922925, -94.69758533129733], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-0.2993505590209046, 0.03629504710403604, -3.944358953629664e-05, 2.3073395624284446e-08, -5.505172706588013e-12, -8298.12960177703, -0.5243066765065816], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.089051869291655, -0.009905142176606055, 1.7696127431367106e-05, -9.456999084888627e-09, 1.6972918872508545e-12, -11940.903953797628, -73.24268995539387], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-1.4658840835034574, 0.04032671174813883, -5.167763560457026e-05, 3.3783985926401025e-08, -8.785375205100365e-12, 26066.048499007054, 4.13711567264183], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.15817215733773, -0.006887697575460912, 1.2286455919781892e-05, -6.548939146430199e-09, 1.1738114261372569e-12, 22819.2270204753, -63.78765548495377], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-2.335993439055983, 0.040954939665441205, -3.3089646050380166e-05, 1.2340872982481883e-08, -1.0794767857369436e-12, 5336.697140696911, 14.860345426691573], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.74976165362862, -0.015545093613946428, 2.7694717132723653e-05, -1.4747871407191746e-08, 2.63918260753589e-12, 267.95851210202636, -82.77161176541864], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 74.2, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[1.1382161030417726, 0.02823086411784681, -3.8437541152423726e-05, 2.68682039236264e-08, -7.519328909522116e-12, -7098.602428410497, -5.622350233611], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.261952078347944, -0.0043169733828252385, 7.734096802836405e-06, -4.144915494287179e-09, 7.462540784972105e-13, -9238.802381592828, -50.91355633239643], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[1.3347812981984684, 0.024001926445212443, -2.56561658286328e-05, 1.4867686876108568e-08, -3.5296973677212407e-12, -25213.370287022593, -0.6581843781404473], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.997098052356318, -0.006795965625441336, 1.2045699322112835e-05, -6.35963493688424e-09, 1.1313346110218602e-12, -27669.405331935846, -49.54562850561243], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 37.01 and 60.96, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[3.3768902555000624, 0.0171682889371867, 1.0226321143136753e-05, -2.3112247575112394e-08, 9.75945366188391e-12, -47895.223585450934, -7.590723086367735], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.38150930118788, -0.014838934742104926, 2.6561065817962258e-05, -1.4250112374198511e-08, 2.5651784197483225e-12, -52117.824434902795, -81.64682914391005], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 62.9 and 75.5, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[1.498597457327269, 0.032355190208176496, -2.1571861406286457e-05, 4.167224639668699e-09, 1.1892153928272364e-12, 9457.935879855606, -0.5266906827411475], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.602511855172047, -0.013353248368212247, 2.3798945196052833e-05, -1.2680910283828319e-08, 2.2710678925289256e-12, 5080.301800359357, -83.39997325193717], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 43.28 and 91.29, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[1.3860267526578336, 0.01664178789343038, -1.691942984475754e-05, 9.530135630943216e-09, -2.1792567750367198e-12, -1562.5182555601323, -0.7177355154818059], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.443721041372187, -0.005684040584492513, 1.0035186919117315e-05, -5.267786077746279e-09, 9.321823589864562e-13, -3364.977959570253, -36.46725961374762], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 32.89 and 61.93, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[0.9329049770147809, 0.02559439673034495, -2.9929209749898684e-05, 1.792249565263067e-08, -4.312904200443057e-12, 14606.888047398903, -4.32357810798039], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.189909236139325, -0.0048372763239389336, 8.704543634729743e-06, -4.700785411733901e-09, 8.512922744524252e-13, 12310.783491652204, -50.903857215140754], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[1.9093427832856456, 0.015109857567877725, -2.035991896813067e-05, 1.497540554061232e-08, -4.539493780875148e-12, -4789.243161006021, -3.189195804148941], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.079628606125411, -0.002883577778131228, 5.257881761172171e-06, -2.8882247891944793e-09, 5.294853427979958e-13, -6049.966462891853, -29.03243134700865], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 79.59 and 79.64, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[0.35372322164049375, 0.02738047612849198, -3.8612604745333416e-05, 2.927012961532056e-08, -8.860745470684606e-12, 20300.829242473577, -2.8568339245513314], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.507388865664629, -0.005965218577518859, 1.0615016854265997e-05, -5.630345050561723e-09, 1.0041366575849666e-12, 18162.945992405042, -48.18896116965864], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-2.271030070713403, 0.042753886698014144, -5.616521760529464e-05, 3.84419049838871e-08, -1.0600409439120995e-11, 25323.187638293646, 6.930604839386363], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.129061372587675, -0.0075722177760204085, 1.3601615475324468e-05, -7.320902085902189e-09, 1.3215775807826633e-12, 21886.841768603408, -64.82524264388996], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-0.5280803860139388, 0.02857832520777748, -2.2234906966676652e-05, 7.78827990007637e-09, -5.933586955109149e-13, -18803.477735117587, 7.519427148206343], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.978155171283852, -0.01072781212352432, 1.9236820173514164e-05, -1.0341454007115213e-08, 1.8645498454938642e-12, -22439.70190489781, -61.77930156020798], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 58.8 and 75.3, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[1.861981002549067, 0.012267703380084082, -1.7731758155958478e-05, 1.3155368406980722e-08, -3.9401086560086895e-12, -3719.000762122234, -9.289693099202804], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.603258612896744, -0.0013940190087287244, 2.57361390973219e-06, -1.4363157531099863e-09, 2.6664821685648044e-13, -4591.304867844086, -27.812281404438227], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[2.35949573143134, 0.026577899561492997, 4.854377666264594e-06, -2.3300751281317563e-08, 1.080241104900459e-11, -52759.300470174836, -2.729096564133741], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[21.24888246472411, -0.01932093653811285, 3.441582389180345e-05, -1.8332031567436925e-08, 3.2816944758981732e-12, -58291.121176026514, -101.87030526228588], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 12, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[0.260795407294895, 0.029660018341478824, -3.746238665500519e-05, 2.358568716943405e-08, -5.979147732482204e-12, -58130.73724771253, 4.317532672755538], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.046796775039743, -0.003516390240860405, 6.491780792346322e-06, -3.6335189500432518e-09, 6.76298154237971e-13, -60506.21112087965, -44.6732378419345], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 89.5 and 92.5, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[0.389190259446194, 0.029211254914251448, -3.686302879714125e-05, 2.577719019943844e-08, -7.388346878745011e-12, -13392.123891926138, 3.258447821188545], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.099162358583222, -0.007408051053148315, 1.3248023640618584e-05, -7.084641349504617e-09, 1.2717661007009525e-12, -16012.691861936655, -50.37072313107062], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 12, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[0.6898546774949614, 0.011560714377428642, -1.8172061719401435e-05, 1.4019483176817962e-08, -4.13411839483846e-12, -20800.216898267357, 2.129066713741203], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[3.959400247703484, -0.0016598690893850207, 2.8312677453421154e-06, -1.4039375937826006e-09, 2.3701080762369444e-13, -21478.95120449252, -13.688877268046175], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 80.8 and 80.8, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[0.11893718001909742, 0.025418087054303352, -9.608108765723116e-06, -4.295199952043176e-09, 3.4643572732750982e-12, -6615.402345169291, -0.7380722583745722], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.060757899368161, -0.014857615759064174, 2.6463057211562785e-05, -1.4088104044335564e-08, 2.519977482300052e-12, -10805.991668995117, -78.21199707349695], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-0.45568630164550283, 0.02637115066174373, -2.1193123690588342e-05, 8.246531833200582e-09, -8.510588067611735e-13, -2606.367457220602, 6.940746767287196], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.091019819690525, -0.01103304876740023, 1.948440586976517e-05, -1.0237438115646235e-08, 1.8128748895400622e-12, -5921.944636151031, -57.168054135035064], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 76.79, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[0.9935294751058993, 0.019188084816283695, -2.429249743945245e-05, 1.5478049847536502e-08, -3.9995055878261354e-12, -13420.9533674434, 1.4913827637688772], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.354995216271919, -0.002362726178049896, 4.361169587569009e-06, -2.439647321955973e-09, 4.538698078124497e-13, -14969.48674053771, -30.36886643675733], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 63.4 and 94.07, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[2.768653947606864, 0.015420898484374366, 5.767884406987432e-06, -1.582704523344787e-08, 6.751805711746606e-12, -24959.901355851103, -5.059392156151786], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.847749730767104, -0.013358195660341412, 2.386893017994287e-05, -1.2769340121429688e-08, 2.2930531883285244e-12, -28555.807764292866, -68.67480546585463], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 30.5 and 72.0, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[1.3310389871284336, 0.02414674768408531, -3.5063758636819454e-05, 2.529019734254638e-08, -7.2690325980673265e-12, 21947.358261227353, -6.608669248279268], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.420686007412868, -0.0021196843479321, 3.92392411285226e-06, -2.19955314084138e-09, 4.098201473816919e-13, 20331.700078818187, -41.5660882468205], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[2.44141854220255, 0.020141843913278733, 1.0044469403094477e-05, -2.4632473249163318e-08, 1.0643652625930144e-11, -30015.609956103515, -2.162546111922108], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[18.59926847910891, -0.017944219882386928, 3.1880937783288313e-05, -1.6915783501952463e-08, 3.0187083572847523e-12, -34813.43437164863, -87.27518355359506], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 12, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[0.8242951099574658, 0.02601749300527664, -3.764243998419186e-05, 2.8538878383302336e-08, -8.616187624488347e-12, 30669.45551484125, 0.7718232648180283], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.101373002597061, -0.004568081627180263, 8.155009679525738e-06, -4.3442135090420495e-09, 7.779513439557439e-13, 28761.293563254854, -40.10485955334094], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 54.13 and 75.02, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[2.2307544743659604, 0.0177836583378775, -5.881534702396193e-06, -3.712415964603129e-09, 2.534902843187581e-12, -2939971.842900823, -3.5023962567656817], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.925748183648746, -0.010525828837205998, 1.8814014384300188e-05, -1.006660382450407e-08, 1.8080350821928545e-12, -2943010.0222009555, -59.11930331879363], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 60.41 and 70.27, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[1.6381283117903973, 0.011236540999882597, 3.6648449110672684e-06, -1.1120657164061452e-08, 4.8571719563073046e-12, -15829.352984843665, -2.018462765805575], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.252954055242416, -0.009480301245285656, 1.690122904893019e-05, -9.011985872256571e-09, 1.6141330283557347e-12, -18376.44568902677, -47.32105129502442], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 12, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-0.09380422645655731, 0.032541847168821005, -1.9508073897544554e-05, 1.903359007053183e-09, 2.0178511639379337e-12, -30575.936366230864, 5.477417787388841], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.82362367101502, -0.015032614497090181, 2.6732691434690313e-05, -1.4198368362631653e-08, 2.535846969827513e-12, -35197.88919358185, -81.69221157328715], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 96.1, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-3.093280425463346, 0.04054757010622046, -5.061867190583264e-05, 3.338407760784367e-08, -8.850732646781267e-12, 8113.305201189273, 11.044474401813387], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.340397884578838, -0.008856598645418729, 1.5767249042201104e-05, -8.379519466619446e-09, 1.497433921245116e-12, 4624.336905965942, -61.114477479073706], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[1.8458767372850708, 0.029847037326815415, -1.628806010721106e-05, -5.160668468083551e-10, 2.7107066591369744e-12, 7094.648050065323, -2.262003683764995], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.564137692426172, -0.013464318111545016, 2.3999175935713838e-05, -1.2790808184361646e-08, 2.2913064369846966e-12, 2755.5515119482498, -83.47573585477258], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 26.19 and 53.11, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[0.8122506955543128, 0.02240816943062223, -2.560540942880465e-05, 1.5737133860457185e-08, -3.913543100697581e-12, 23896.315861060255, -4.914017566653332], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.420923212429473, -0.005908523822882394, 1.046789814968811e-05, -5.523251266525401e-09, 9.815551844217065e-13, 21757.63073616161, -48.2375606548202], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[0.317983846735941, 0.03378081534288077, -1.4799606364102304e-05, -3.849161364949014e-09, 3.936379000535339e-12, -27915.009088807165, 3.571976723407051], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.33780951407374, -0.01743439496847118, 3.119767889978881e-05, -1.6722666366251315e-08, 3.0079833819606806e-12, -33255.60264772552, -95.0724895176481], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 63.5, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-4.872530990892688, 0.05562110739421251, -6.411740846381472e-05, 3.90946383572137e-08, -9.649864241012551e-12, 15867.904094098198, 18.42848547630861], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.033258703301904, -0.013087062152820073, 2.345928982521811e-05, -1.2599720747615063e-08, 2.27017642762139e-12, 10663.54805288936, -86.81233037475383], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[1.896996739997094, 0.03136537278382553, -3.453660942774874e-05, 1.9380361175384516e-08, -4.250745588851856e-12, -76929.32565633487, -0.6822241363354031], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.834156803790703, -0.007126677188197933, 1.2639040075364843e-05, -6.681795799650268e-09, 1.1906517912991903e-12, -79918.41746742613, -60.909943049286625], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 37.3, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[0.25283229666288626, 0.02196083615973431, -2.995078065363372e-05, 2.1358393509160473e-08, -6.125745743990052e-12, 23342.997751228977, -2.7225950490934006], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.479256089411759, -0.0038018937413140906, 6.806689659551415e-06, -3.6435473720286575e-09, 6.55030932313473e-13, 21639.778689645835, -38.61818128250688], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-0.6497117249237396, 0.03554659990718592, -4.414269779955767e-05, 2.9390359305178724e-08, -8.001765916532122e-12, -22616.509344500024, 1.8076763055253844], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.113681847665207, -0.007676997669967362, 1.3787877482169512e-05, -7.421194660794445e-09, 1.3394167722781966e-12, -25743.643935356828, -62.165190770507756], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-0.4143646504391006, 0.02978662513337611, -2.426107781057716e-05, 8.221441058744636e-09, -2.817850119907206e-13, -23343.737766014143, 7.219061486102086], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.02501358042193, -0.009793659831366664, 1.746096472219298e-05, -9.310410292910886e-09, 1.6689305407764036e-12, -26907.50129806671, -61.54133917364804], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 51.0, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-0.010038189100136949, 0.027915951531930452, -3.7008074488711405e-05, 2.5702899149076164e-08, -7.117882672158515e-12, -4315.566375420634, -1.4839360217744035], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.464334987044788, -0.005614607763967092, 9.924580262969034e-06, -5.215372068432199e-09, 9.23919913422026e-13, -6547.670866915949, -48.570715664837955], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-3.4051441867506687, 0.04772428949095811, -6.435599244295838e-05, 4.4497979633388086e-08, -1.2296011431267573e-11, 23009.91275774554, 11.83631806740638], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.134869945397682, -0.007526918734214151, 1.3520541327617193e-05, -7.277197774704259e-09, 1.3138262992731103e-12, 19358.48495390641, -65.34142221278498], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-1.3776098886368717, 0.03725658652985831, -5.301683192936588e-05, 3.85554917024431e-08, -1.1193462823300138e-11, -17102.12034480543, 3.9622718582433567], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.198849403969138, -0.0051171729320485795, 9.263940504965069e-06, -5.0384010408484036e-09, 9.169576549613017e-13, -19775.568294397723, -53.268010225904405], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[2.9235621432406558, 0.010682159200923573, -1.2508195264134097e-05, 8.481349940248927e-09, -2.4795755726447766e-12, 10117.691077125512, -2.176705532413216], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.086216049965828, -0.0028051611886094944, 5.098960366817714e-06, -2.7909116737160684e-09, 5.101968931763034e-13, 9049.75639850997, -23.23758003557941], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 12, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-4.002408677490902, 0.05221889029432987, -5.891216152170394e-05, 3.510354870268884e-08, -8.419341612775355e-12, 8102.881487686799, 15.082182270411696], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.948667925410765, -0.012883729841450977, 2.3028327387071622e-05, -1.2316759623567079e-08, 2.2120213375841774e-12, 3118.4231412424415, -85.45366806877081], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-3.245426384204051, 0.045740712834498994, -5.2067883947796485e-05, 3.1011581474928596e-08, -7.431173731919927e-12, 16989.950627039707, 14.227506587622628], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.973737140880834, -0.010520315933265557, 1.8851700221784848e-05, -1.0120427938433465e-08, 1.8231167545404697e-12, 12693.584352025086, -72.51992728662636], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-0.30041267219461726, 0.03619615590865914, -4.2884290614633444e-05, 2.7141695140855092e-08, -6.9348485287612505e-12, -15250.702836759989, 5.483638123809034], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.191116478662066, -0.00886431129376755, 1.572914727183049e-05, -8.318780340183333e-09, 1.4811271173832512e-12, -18567.887274193927, -62.24263074822453], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 12, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[0.3590540257949575, 0.02501724558325151, -3.0958732097421955e-05, 2.0028686967552077e-08, -5.265201469262237e-12, -51673.67603770169, 3.5273397923429943], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.162655170509804, -0.004701472115288032, 8.43556603180363e-06, -4.5336682675397614e-09, 8.179721904287085e-13, -53825.39696605386, -40.59755552507954], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 36.7 and 64.6, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-0.2669603995977954, 0.02565870801958168, -3.674608935455706e-05, 2.652568290254523e-08, -7.56687767999864e-12, 3300.9413964062, -0.5999011793374347], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.589736849915704, -0.0034428159868763204, 6.154124915009688e-06, -3.286438594982207e-09, 5.898563049065437e-13, 1516.618304333605, -39.322435872071274], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-3.4844800615041733, 0.049611889732152026, -4.654198224495485e-05, 2.2377925953709398e-08, -4.031094902323673e-12, 10597.189745143514, 13.750530599079799], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.886825386143364, -0.015838525349653923, 2.8325178735322496e-05, -1.5167316715817635e-08, 2.7260964210844285e-12, 5030.243914339979, -95.03459977498957], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-4.026345852130751, 0.05033082458207469, -5.385881175406507e-05, 3.034074169322768e-08, -6.849180944623612e-12, 7215.378849539093, 15.773763750300937], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.896382116926404, -0.013266253993094522, 2.3747362731514907e-05, -1.273077806299318e-08, 2.2905149321293325e-12, 2162.4061032445115, -84.98132493441409], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[0.4037688676760159, 0.03434773773851396, -1.589336246930867e-05, -2.439739319804509e-09, 3.409550419775087e-12, -3081.8704450885516, -2.8137786594113816], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.778567406824635, -0.018507705596055097, 3.304254534574856e-05, -1.7651525659651444e-08, 3.1660737399852312e-12, -8489.27466771868, -103.1311915038271], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[2.7297147696519377, 0.00871051343311338, -1.2913175453546782e-05, 1.0729495025872316e-08, -3.3943334254438184e-12, -34929.29588744998, -6.044799612763288], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.854969755224978, -0.00328848381545218, 5.569914961149537e-06, -2.7300853163986143e-09, 4.558987651233143e-13, -35621.23373951804, -21.351875463188104], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 62.1, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[0.30879664392685074, 0.02322706509541745, -3.556983029780882e-05, 2.7753561257652567e-08, -8.585455263387942e-12, 38422.56637631896, 2.8113667115042826], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.115613052483903, -0.0028051889306977304, 5.1327175697923406e-06, -2.8290128457317497e-09, 5.200085899533489e-13, 36888.911780130264, -30.60964977099387], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 88.08 and 88.09, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-1.474201961982, 0.04214499553666714, -5.019755499211276e-05, 3.192281341305998e-08, -8.249907701429748e-12, 20380.84802934717, 6.364660594500848], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.113333075003883, -0.009852181996039523, 1.7609580523667854e-05, -9.414965035138605e-09, 1.690377726709007e-12, 16535.91077987631, -71.92241894304287], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-0.519314834916621, 0.02373440154230643, -2.1291541552457033e-05, 9.945549656773737e-09, -1.7005320762653042e-12, 840.758254752407, 7.353465918619669], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.145639013685717, -0.008751777752201852, 1.5480383746780023e-05, -8.152097424373833e-09, 1.4464151515511565e-12, -1943.3920549512068, -46.97139646417915], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 24.5 and 55.12, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[1.0741274556154226, 0.022965576621378367, -1.226054757009958e-05, -1.2460321254068214e-09, 2.540360283243004e-12, -41099.314064792874, 1.0295483336788607], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.048629858130068, -0.009848436466291938, 1.7567229443078926e-05, -9.375556766457565e-09, 1.6816185962709e-12, -44405.27276354143, -60.86273230063496], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 42 and 64.2, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-4.808912278042506, 0.05371459353605078, -6.677816098958218e-05, 4.327825054890335e-08, -1.1302327129758538e-11, 16779.37952090278, 17.849352887871994], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.06624457744102, -0.010480168414856744, 1.8819273521040792e-05, -1.0130741835739328e-08, 1.8288358396851678e-12, 12195.140972937286, -76.61936010742753], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[3.3887792136318815, 0.01485070641094015, -1.8053000059341263e-05, 1.2700296345617517e-08, -3.7160309551698134e-12, -1226.6183788260428, -8.571580661198439], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.15463316222184, -0.004498769503690917, 8.014673958751756e-06, -4.261303331910299e-09, 7.615166703060956e-13, -2662.0686485113674, -37.550570154019205], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 46.11 and 61.53, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-0.37382678931843344, 0.02339769200062535, -1.9573560022432037e-05, 7.627197853066382e-09, -7.421147030228781e-13, -26660.385543812623, 6.579102040857676], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.314149933698681, -0.00856871942980447, 1.5185530659546908e-05, -8.022793154086057e-09, 1.4272203295633218e-12, -29472.889367003605, -47.98962958885739], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 25.3 and 72.1, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-4.54183580580912, 0.051607273914036134, -6.994889444434749e-05, 4.8515824081931226e-08, -1.345649286443873e-11, 23528.29478567492, 16.518000967056906], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.143041715946012, -0.007834179492609523, 1.4122672211551491e-05, -7.640534691801687e-09, 1.3848751382857308e-12, 19611.104508164623, -66.32293547709148], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[0.6073983748266779, 0.02411345927287939, -3.622637570503358e-05, 2.7097576274861152e-08, -7.934382317831279e-12, -1371.3873457316595, -4.173499030987131], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.644644146460896, -0.00292011023055385, 5.169681907520428e-06, -2.71890477792758e-09, 4.8236485420246e-13, -2919.7634077101593, -38.61488973774408], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-1.0343560218929846, 0.029548892131749573, -3.73889564039001e-05, 2.505427718265676e-08, -6.773304139784386e-12, 7895.015122989119, 2.756953188339309], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.384991875695635, -0.006270168565917598, 1.116351316816939e-05, -5.931883768825337e-09, 1.0601000397067635e-12, 5380.900452183212, -49.30415707085957], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-0.40783338936069924, 0.03381796177566502, -1.823647656949719e-05, -2.1781846529093148e-10, 2.782378494270432e-12, -7985.9079162965245, 3.033953625708631], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.695307434040636, -0.016187407276919873, 2.891215814791522e-05, -1.5456094995766764e-08, 2.774248536517414e-12, -12991.380661706655, -90.50560326982341], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-1.0434374026493027, 0.01723690360052522, -3.068695772385648e-05, 2.5388243450826957e-08, -8.015095531721528e-12, 13792.314617154501, 3.0546208304969795], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.871025080313816, -0.0004595838978198254, 8.69502488284576e-07, -4.943281589774701e-10, 9.304088132376496e-14, 13056.291432492268, -15.466780891621022], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-0.04445291330890715, 0.019436759636543545, -1.910285737816519e-05, 1.1126926094899282e-08, -2.737358950621882e-12, -4595.947780013635, -0.17338587893149882], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.657045298440389, -0.007903077857146055, 1.4010043902444527e-05, -7.400160778622852e-09, 1.3151659242308404e-12, -6843.894261711379, -44.335254827017394], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[1.763419916108504, 0.02194644896971896, -2.103316059025516e-05, 1.0462346509861043e-08, -2.00841426822862e-12, 5377.685923451847, -2.2565505771061964], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.110541682511121, -0.006805474008018572, 1.2093550174710817e-05, -6.4122945494689966e-09, 1.1443172374703573e-12, 2952.4026879553858, -49.79891523032289], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 18.68 and 56.21, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-2.075699468841117, 0.0173580773432723, -2.60920641289811e-05, 1.8928216959212944e-08, -5.388359897162687e-12, -4286.294865234183, 8.153606339477799], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.72247451292015, -0.0010681624758178813, 1.98652806084117e-06, -1.1204801968168722e-09, 2.0981090637377155e-13, -5338.339539090954, -15.320705237203459], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[0.9423372093417816, 0.024934873439595245, -2.7919420506031615e-05, 1.571957171297777e-08, -3.4902289391958163e-12, 8381.206215753338, -4.565914187237254], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.170222985076812, -0.004832591811867653, 8.689196070698183e-06, -4.688316791092099e-09, 8.486224638721293e-13, 6068.382718910367, -51.12881725472743], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[0.4822990653678686, 0.025871551275316016, -3.936036578869574e-05, 3.0462959888373194e-08, -9.365327957588931e-12, -9142.353555924652, -3.5737733587071077], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.07083252446875, -0.0030085351441165842, 5.515413036637334e-06, -3.048064421867343e-09, 5.614704876502467e-13, -10857.04035857463, -40.86266658834069], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-3.0278046479993956, 0.04868277469861706, -4.6469732640494874e-05, 2.287515846982304e-08, -4.2387759968676164e-12, 726.6488879756172, 11.50704836401285], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.77877011493777, -0.015532217068479896, 2.7689854090808286e-05, -1.4757543334486113e-08, 2.6427560802981618e-12, -4660.423199536661, -94.26062897527922], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-2.7556935991113143, 0.02931258322046972, -4.843786135235457e-05, 3.8446894497971926e-08, -1.1723805953822719e-11, 7275.728557610058, 10.096496473865535], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.82839327433021, -0.002459594928613155, 4.346762608100843e-06, -2.275310115888111e-09, 4.018659752232502e-13, 5738.272872880644, -26.3700032711956], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[4.1773318603426315, -0.0012986530515048478, 2.5984608392452018e-06, -9.710009093615648e-10, -9.263358309585801e-14, 9941.264134506422, -7.83612800569839], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.407824912387671, -0.0015051356127585688, 2.682567158041752e-06, -1.4261829223692334e-09, 2.5443162032394223e-13, 9830.35938605735, -9.198927164061498], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 9.93, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[1.6859786277295976, 0.02529646880479501, -3.439872458351851e-05, 2.4726462848270053e-08, -7.1681376112575634e-12, 31234.77666100757, -8.130952558650884], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.122123532985965, -0.00468041388002082, 8.377743678764665e-06, -4.483216274102139e-09, 8.058110283909199e-13, 29235.880396728076, -50.074055960974285], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-3.120983965065448, 0.0394848933739722, -5.4671345607136475e-05, 3.872997294685073e-08, -1.0891107460331284e-11, 7870.986964589762, 11.198399654770983], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.507335599117875, -0.006294461586585287, 1.1259999982182852e-05, -6.0234545814608755e-09, 1.0820098750351573e-12, 4948.963099250019, -51.296729471229675], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-0.14003259781995392, 0.03586162976285296, -1.110213649910173e-05, -8.973999424703651e-09, 5.916364620439651e-12, -8934.267906806283, -0.9771971470804104], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[21.50654575009937, -0.021538701603027975, 3.841341727677806e-05, -2.0490478347803802e-08, 3.67104278562163e-12, -15057.68106600643, -113.46375175747491], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-0.5930036410581151, 0.03571236960278033, -2.889191769594888e-05, 1.0353989429736873e-08, -6.877484692857649e-13, 16879.260269984945, 4.071108868409565], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.85974095884644, -0.012892229650711164, 2.2989923173693153e-05, -1.2260637510712424e-08, 2.1968922551084385e-12, 12511.596930512278, -80.09969687760427], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-1.0485328055132146, 0.028672112331914724, -3.4822695375238e-05, 2.2596349194893594e-08, -5.960530680138021e-12, 14522.73035660617, 2.5065656904453433], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.414361625368043, -0.006532492926442629, 1.1674964208927848e-05, -6.240271609019611e-09, 1.1201413670854261e-12, 11955.939485048584, -49.97073415880118], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-0.38281873097973235, 0.031836903255905324, -4.0139100775514415e-05, 2.761968717216655e-08, -7.788499012395533e-12, 24519.534991793036, 5.7596551275679975], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.118039767476619, -0.007405974962924992, 1.3261664190104087e-05, -7.10518525048067e-09, 1.2776281650071471e-12, 21707.853284393612, -51.83453946208431], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 12 and 99.7, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[0.7048343312415307, 0.02837620141751559, -3.786450943705259e-05, 2.654410975880462e-08, -7.541790109089064e-12, 49017.84147041395, -4.371824159907775], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.196869682883323, -0.004925420385497629, 8.881818762179351e-06, -4.805481378893616e-09, 8.710592807486574e-13, 46749.3355269918, -51.665372399992535], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-1.2361696169517336, 0.039119296434737376, -3.5944529743081236e-05, 1.7078239755369327e-08, -3.0713001586413213e-12, 3848.536363931569, 3.545055245445899], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.907361423360797, -0.013048576275606369, 2.3318786109779105e-05, -1.2471542891600819e-08, 2.239508305499705e-12, -640.2129699148736, -83.81982158179875], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-1.0128277676925945, 0.03960545324597654, -2.417957983456616e-05, 3.2356519006891704e-09, 1.993148701640024e-12, -2593.088448738701, 3.3418135904894815], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.594114206279386, -0.018498140954927595, 3.2957999557778124e-05, -1.7553526856730903e-08, 3.1414002936479626e-12, -8226.44874875328, -102.82843075469069], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[0.2631703605638592, 0.02672958182700725, -2.8237311149280387e-05, 1.6164539099028483e-08, -3.69835412294961e-12, 18232.9083845173, -2.446254248524509], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.199486664560558, -0.00834204165036218, 1.4711414998931733e-05, -7.709954680296753e-09, 1.3627206815362359e-12, 15472.570253735417, -57.7014946348258], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[-1.2597947854333738, 0.04291106119431591, -6.112561275165804e-05, 4.481050517474996e-08, -1.3045467484040785e-11, 34274.53574250721, 3.5252823923395864], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.261909294145998, -0.006846950029475665, 1.2247928231585106e-05, -6.547805246035515e-09, 1.1756090977137418e-12, 31169.352569254705, -63.24393195054924], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
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
            NASAPolynomial(coeffs=[1.6007913647264238, 0.014704845247362775, -1.4669740619649858e-05, 6.819304873825679e-09, -1.1479810158032677e-12, -14687.35948972185, -0.7662966231657862], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.295792299032074, -0.002585551342010212, 4.764106999098976e-06, -2.6619189543735904e-09, 4.947908487145042e-13, -16173.359751444357, -29.782781634321623], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
The two lowest frequencies, 31.35 and 43.35, where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-0.6781890175202242, 0.03266563196550599, -3.482124141809576e-05, 1.9201333508222552e-08, -4.230282790729234e-12, -13982.351304527147, 1.4808105805831966], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.110986738352649, -0.007888949731143548, 1.4190178176923743e-05, -7.661299725253428e-09, 1.3863367885039082e-12, -17239.041684559383, -63.26475767872117], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by [author] at [institution] using statistical mechanics methods within the class Adsorbate.
Based on DFT calculations by [author] from [institution]. DFT calculations were performed with [dft_calculator]
using [pseudopotentals] and [functional] for an optimized [supercell size] following the procedure outlined 
by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
kpoints=[], n layers (m bottom layers fixed), ecutwfc=[] Ry, smearing=[type], mixing_mode=[],
fmax=2.5e-2.
""",
    metal = "Pt",
    facet = "111",
)

