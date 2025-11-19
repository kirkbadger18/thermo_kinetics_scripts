
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.0132854616344893, 0.03262761058111659, -3.706095174588158e-05, 2.0960395825783326e-08, -4.666933506314308e-12, -74975.84346896186, -4.7536240621565184], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.852353543588329, -0.00570824849650918, 1.0285808375407427e-05, -5.567159908424826e-09, 1.0106531022767602e-12, -77932.86377403198, -64.44940816059918], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.0132854616344893, 0.03262761058111659, -3.706095174588158e-05, 2.0960395825783326e-08, -4.666933506314308e-12, -66474.27951568394, -4.7536240621565184], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.852353543588329, -0.00570824849650918, 1.0285808375407427e-05, -5.567159908424826e-09, 1.0106531022767602e-12, -69431.29982075407, -64.44940816059918], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.05959982061160269, 0.034935604893275844, -4.39855790528056e-05, 2.8727528722406607e-08, -7.522184264363574e-12, -15563.569671345875, -0.9052005642652068], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.072877573168544, -0.00664305462261147, 1.1791965438741197e-05, -6.237700543196466e-09, 1.1116826317998652e-12, -18484.698200529885, -61.5268883603407], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.05959982061160269, 0.034935604893275844, -4.39855790528056e-05, 2.8727528722406607e-08, -7.522184264363574e-12, -23149.64872715172, -0.9052005642652068], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.072877573168544, -0.00664305462261147, 1.1791965438741197e-05, -6.237700543196466e-09, 1.1116826317998652e-12, -26070.777256335732, -61.5268883603407], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-1.8779203086664225, 0.028356288698697506, -4.277510879499703e-05, 3.274075934781191e-08, -9.75815608872388e-12, 8812.11889849577, 6.329199424648831], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.669211004920813, -0.004662986852426903, 8.163981923387267e-06, -4.222734018968265e-09, 7.383907972091739e-13, 6936.492418851074, -35.46553410089453], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-1.8779203086664225, 0.028356288698697506, -4.277510879499703e-05, 3.274075934781191e-08, -9.75815608872388e-12, 877.6358606693611, 6.329199424648831], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.669211004920813, -0.004662986852426903, 8.163981923387267e-06, -4.222734018968265e-09, 7.383907972091739e-13, -997.9906189753337, -35.46553410089453], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[2.9656085337498914, 0.013397832123679605, -1.3429344690682074e-05, 7.121751881737713e-09, -1.4106285584070122e-12, -22690.545093915578, -6.154667707403931], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.635380049446058, -0.004641489077444636, 8.092564580948746e-06, -4.1676236189663395e-09, 7.263873560942958e-13, -24119.685073984147, -34.81282407199182], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[2.9656085337498914, 0.013397832123679605, -1.3429344690682074e-05, 7.121751881737713e-09, -1.4106285584070122e-12, -14517.748667532003, -6.154667707403931], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.635380049446058, -0.004641489077444636, 8.092564580948746e-06, -4.1676236189663395e-09, 7.263873560942958e-13, -15946.888647600572, -34.81282407199182], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.926298861921214, 0.023920986270762924, -1.1102891365437688e-05, -3.274735343361719e-09, 3.4649297320221706e-12, -46042.53277543295, -0.7623716616782339], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.909732388832854, -0.011497699076417572, 2.032569157433714e-05, -1.0702611808126942e-08, 1.8994750772814185e-12, -49622.75789487315, -67.8770367839491], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.926298861921214, 0.023920986270762924, -1.1102891365437688e-05, -3.274735343361719e-09, 3.4649297320221706e-12, -41548.8212148419, -0.7623716616782339], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.909732388832854, -0.011497699076417572, 2.032569157433714e-05, -1.0702611808126942e-08, 1.8994750772814185e-12, -45129.0463342821, -67.8770367839491], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.2962185933988715, 0.02186181914758953, -2.3841617463750646e-05, 1.4095769583907038e-08, -3.388230668255332e-12, 17063.773007944492, 6.207184485801549], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.412928956150449, -0.006234425804480822, 1.1089327437980425e-05, -5.8875786554616106e-09, 1.0512700719032776e-12, 14867.036545663761, -37.771462079077395], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.2962185933988715, 0.02186181914758953, -2.3841617463750646e-05, 1.4095769583907038e-08, -3.388230668255332e-12, 5410.932194073093, 6.207184485801549], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.412928956150449, -0.006234425804480822, 1.1089327437980425e-05, -5.8875786554616106e-09, 1.0512700719032776e-12, 3214.1957317923643, -37.771462079077395], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.4980461074061682, 0.028761407443681834, -2.688619835613685e-05, 1.5278311802666502e-08, -3.7822904530582235e-12, 28335.268851233115, -1.1152321426024887], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.832729154984882, -0.012370334275977175, 2.196867477820534e-05, -1.1633971170730466e-08, 2.0721780580768446e-12, 24838.67599315874, -69.01651034223151], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.4980461074061682, 0.028761407443681834, -2.688619835613685e-05, 1.5278311802666502e-08, -3.7822904530582235e-12, 17258.741347187457, -1.1152321426024887], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.832729154984882, -0.012370334275977175, 2.196867477820534e-05, -1.1633971170730466e-08, 2.0721780580768446e-12, 13762.148489113079, -69.01651034223151], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[2.2137160105042675, 0.012214676187922303, 1.9068675577301113e-05, -2.8645440448763678e-08, 1.1057901122546454e-11, -1709.877835754378, -3.3273316867407114], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.869139226341218, -0.01767832977387301, 3.144153037560276e-05, -1.6706168903883034e-08, 2.9833575253225206e-12, -5912.992170236261, -75.91019621235004], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[2.2137160105042675, 0.012214676187922303, 1.9068675577301113e-05, -2.8645440448763678e-08, 1.1057901122546454e-11, -9028.774658879169, -3.3273316867407114], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.869139226341218, -0.01767832977387301, 3.144153037560276e-05, -1.6706168903883034e-08, 2.9833575253225206e-12, -13231.888993361052, -75.91019621235004], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.34655425022431197, 0.03320903146374003, -3.229874644014059e-05, 1.7752091169205867e-08, -4.033794132052293e-12, 26959.124905120574, 3.586650323800802], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.940337148457722, -0.012271000595976094, 2.1814353103818894e-05, -1.1572978619254032e-08, 2.0644252739308432e-12, 23179.281754677082, -70.54967983272971], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.34655425022431197, 0.03320903146374003, -3.229874644014059e-05, 1.7752091169205867e-08, -4.033794132052293e-12, 15882.597401074916, 3.586650323800802], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.940337148457722, -0.012271000595976094, 2.1814353103818894e-05, -1.1572978619254032e-08, 2.0644252739308432e-12, 12102.754250631418, -70.54967983272971], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.4289514345775818, 0.014037445912949231, -2.2117880511546713e-05, 1.7865950156490832e-08, -5.7147862830841945e-12, -29039.584650615157, -7.782662330904809], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.486566622473974, -0.0016811903234556856, 3.0903081182232816e-06, -1.7118686775497669e-09, 3.158649696949356e-13, -29952.28680561143, -27.6788563455022], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.4289514345775818, 0.014037445912949231, -2.2117880511546713e-05, 1.7865950156490832e-08, -5.7147862830841945e-12, -28691.180667698496, -7.782662330904809], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.486566622473974, -0.0016811903234556856, 3.0903081182232816e-06, -1.7118686775497669e-09, 3.158649696949356e-13, -29603.882822694773, -27.6788563455022], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.2935534672256999, 0.012551181494457475, -1.3054228857275018e-05, 7.661604760904095e-09, -1.9215514596160332e-12, 4505.922569365798, -0.23897969202122304], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.5168215174433115, -0.0038395553030464496, 6.878336370803954e-06, -3.689005627860506e-09, 6.639624483559064e-13, 3154.384324137254, -26.758424636724342], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.2935534672256999, 0.012551181494457475, -1.3054228857275018e-05, 7.661604760904095e-09, -1.9215514596160332e-12, 618.5648344787127, -0.23897969202122304], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.5168215174433115, -0.0038395553030464496, 6.878336370803954e-06, -3.689005627860506e-09, 6.639624483559064e-13, -732.9734107498325, -26.758424636724342], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.3392517506347437, 0.015618782360796482, -1.787059252180066e-05, 1.1610327846079934e-08, -3.20827392430445e-12, -22120.579098116385, -4.278239925919107], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.472501868868721, -0.004256523643468286, 7.672402782773906e-06, -4.150942931718123e-09, 7.520574349498309e-13, -23682.25655981084, -35.27774836937108], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.3392517506347437, 0.015618782360796482, -1.787059252180066e-05, 1.1610327846079934e-08, -3.20827392430445e-12, -21752.538660073493, -4.278239925919107], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.472501868868721, -0.004256523643468286, 7.672402782773906e-06, -4.150942931718123e-09, 7.520574349498309e-13, -23314.21612176795, -35.27774836937108], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.33610634372831166, 0.02264832889133042, -2.392389692851722e-05, 1.372564500933275e-08, -3.2403177363526936e-12, -14529.085378154647, -1.8821696787908078], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.52488862496814, -0.006507330938045106, 1.1658617720730415e-05, -6.256802483730977e-09, 1.1264926555990982e-12, -16878.626166247013, -48.422513251657755], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.33610634372831166, 0.02264832889133042, -2.392389692851722e-05, 1.372564500933275e-08, -3.2403177363526936e-12, -14141.40848498552, -1.8821696787908078], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.52488862496814, -0.006507330938045106, 1.1658617720730415e-05, -6.256802483730977e-09, 1.1264926555990982e-12, -16490.949273077887, -48.422513251657755], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-2.6680472878038217, 0.029069338138602956, -4.826533132112092e-05, 3.8758909084069156e-08, -1.197493840199293e-11, 3012.3241001737156, 9.729399453355848], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.9042986812595295, -0.0026386505447205592, 4.717292856601354e-06, -2.512670074814904e-09, 4.496592934290092e-13, 1466.0729975013246, -26.71079316515238], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-2.6680472878038217, 0.029069338138602956, -4.826533132112092e-05, 3.8758909084069156e-08, -1.197493840199293e-11, -686.3972198489473, 9.729399453355848], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.9042986812595295, -0.0026386505447205592, 4.717292856601354e-06, -2.512670074814904e-09, 4.496592934290092e-13, -2232.6483225213383, -26.71079316515238], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.339069154341588, 0.01798477612437326, -8.009977251468463e-06, -2.618497985761969e-09, 2.5890609101075768e-12, 21341.695404381673, 4.1390415779888325], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.264107395002439, -0.009024685340635264, 1.603009365697747e-05, -8.501798468860542e-09, 1.5167137091078899e-12, 18593.325487717688, -47.20208075096739], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.339069154341588, 0.01798477612437326, -8.009977251468463e-06, -2.618497985761969e-09, 2.5890609101075768e-12, 9708.491044740404, 4.1390415779888325], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.264107395002439, -0.009024685340635264, 1.603009365697747e-05, -8.501798468860542e-09, 1.5167137091078899e-12, 6960.12112807642, -47.20208075096739], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.3072075375182828, 0.01659607225538956, -1.6559253185471037e-06, -8.536445042335518e-09, 4.498179606571284e-12, 11272.451311287687, 1.0098625648933126], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.184232258898184, -0.011502131450414807, 2.039505158252219e-05, -1.0788041807467539e-08, 1.919978455058478e-12, 8172.742230705771, -55.65816457564598], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.3072075375182828, 0.01659607225538956, -1.6559253185471037e-06, -8.536445042335518e-09, 4.498179606571284e-12, 3914.2815814948262, 1.0098625648933126], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.184232258898184, -0.011502131450414807, 2.039505158252219e-05, -1.0788041807467539e-08, 1.919978455058478e-12, 814.572500912911, -55.65816457564598], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.9091619785380343, 0.021534813613813434, -9.823249366586295e-06, -2.1902942596023663e-09, 2.4632899886523063e-12, 30701.951435342504, -8.927485547055522], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.863871656738088, -0.010727742260440263, 1.9186856661479928e-05, -1.0276921509403038e-08, 1.8476574064403995e-12, 27353.26768047311, -70.900741012967], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.9091619785380343, 0.021534813613813434, -9.823249366586295e-06, -2.1902942596023663e-09, 2.4632899886523063e-12, 11094.991129414559, -8.927485547055522], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.863871656738088, -0.010727742260440263, 1.9186856661479928e-05, -1.0276921509403038e-08, 1.8476574064403995e-12, 7746.307374545164, -70.900741012967], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.5500262969193481, 0.030684202469102608, -3.992249753741044e-05, 2.5278303136043825e-08, -6.3331111188613676e-12, -12367.016169354238, 4.895455951409511], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.242175297856868, -0.0029122603612644444, 5.392008844105333e-06, -3.031193465863102e-09, 5.661929309593158e-13, -14668.255875100895, -43.40465498004178], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.5500262969193481, 0.030684202469102608, -3.992249753741044e-05, 2.5278303136043825e-08, -6.3331111188613676e-12, -8140.486843236442, 4.895455951409511], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.242175297856868, -0.0029122603612644444, 5.392008844105333e-06, -3.031193465863102e-09, 5.661929309593158e-13, -10441.726548983099, -43.40465498004178], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-1.9451797364169352, 0.03956540242304279, -3.0393046626231364e-05, 9.792876353127494e-09, -1.9579476928655026e-13, -17770.824231622697, 13.10646326346898], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.78477602772791, -0.015222694741328471, 2.7096928465957854e-05, -1.4411836968466e-08, 2.577084860344147e-12, -22773.454039839417, -82.85736005667101], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-1.9451797364169352, 0.03956540242304279, -3.0393046626231364e-05, 9.792876353127494e-09, -1.9579476928655026e-13, -21042.59574822377, 13.10646326346898], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.78477602772791, -0.015222694741328471, 2.7096928465957854e-05, -1.4411836968466e-08, 2.577084860344147e-12, -26045.22555644049, -82.85736005667101], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-1.2547936215827744, 0.037684767144248746, -3.935381821535873e-05, 2.1670811364191383e-08, -4.778594187015983e-12, 13531.26669830363, 4.101768954903848], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.936501535466054, -0.010360492624125524, 1.8520756188653936e-05, -9.90838417832083e-09, 1.7799915628090041e-12, 9654.158359767443, -72.84125571769354], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-1.2547936215827744, 0.037684767144248746, -3.935381821535873e-05, 2.1670811364191383e-08, -4.778594187015983e-12, 2435.102738235646, 4.101768954903848], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.936501535466054, -0.010360492624125524, 1.8520756188653936e-05, -9.90838417832083e-09, 1.7799915628090041e-12, -1442.005600300543, -72.84125571769354], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.4988345404830799, 0.02203120199576683, -1.6302195290715152e-05, 5.4014098940402165e-09, -2.950070743246158e-13, 871.5665669958164, -0.3412430292365851], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.308085389094629, -0.009363149454315057, 1.6709016551341747e-05, -8.918401000827673e-09, 1.5986925799567168e-12, -2043.0330443997154, -55.82031172680274], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.4988345404830799, 0.02203120199576683, -1.6302195290715152e-05, 5.4014098940402165e-09, -2.950070743246158e-13, -6506.239618819375, -0.3412430292365851], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.308085389094629, -0.009363149454315057, 1.6709016551341747e-05, -8.918401000827673e-09, 1.5986925799567168e-12, -9420.839230214908, -55.82031172680274], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.9101399566489873, 0.03643403579329222, -4.2297554017529666e-05, 2.6415078172539904e-08, -6.695602405848433e-12, -22061.912099529654, 8.346346609316207], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.917020687604829, -0.0092665518941809, 1.641641421751263e-05, -8.660235302430652e-09, 1.5391698772991309e-12, -25488.227732947882, -61.19161366687353], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.9101399566489873, 0.03643403579329222, -4.2297554017529666e-05, 2.6415078172539904e-08, -6.695602405848433e-12, -29628.354702001467, 8.346346609316207], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.917020687604829, -0.0092665518941809, 1.641641421751263e-05, -8.660235302430652e-09, 1.5391698772991309e-12, -33054.670335419694, -61.19161366687353], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-2.370067691833459, 0.045287905228815095, -5.4441930156142054e-05, 3.432254837964767e-08, -8.711850685294564e-12, -16233.55885332025, 8.336898697810568], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.054550824009052, -0.009769463971518799, 1.7438363219580855e-05, -9.30557660349684e-09, 1.6687316066184114e-12, -20258.675773499926, -74.05556129305924], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-2.370067691833459, 0.045287905228815095, -5.4441930156142054e-05, 3.432254837964767e-08, -8.711850685294564e-12, -19544.603281965985, 8.336898697810568], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.054550824009052, -0.009769463971518799, 1.7438363219580855e-05, -9.30557660349684e-09, 1.6687316066184114e-12, -23569.72020214566, -74.05556129305924], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-1.6079189052290737, 0.03650725681966295, -1.730280304462386e-05, -2.6327059517695602e-09, 3.772884782371477e-12, 11299.660887904065, 11.71795140046801], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[18.686830394336674, -0.018861777121957767, 3.3694441510049684e-05, -1.801704019498555e-08, 3.234259112968891e-12, 5644.155735608674, -93.3400307131864], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-1.6079189052290737, 0.03650725681966295, -1.730280304462386e-05, -2.6327059517695602e-09, 3.772884782371477e-12, 262.40629231867683, 11.71795140046801], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[18.686830394336674, -0.018861777121957767, 3.3694441510049684e-05, -1.801704019498555e-08, 3.234259112968891e-12, -5393.0988599767115, -93.3400307131864], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.1533309386454741, 0.02312968678326665, -3.289590795769531e-05, 2.441141448952092e-08, -7.243664001954642e-12, 19711.33104205507, -1.7896837262996588], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.537079417328969, -0.0038577507795309633, 6.934770920070903e-06, -3.733040236094633e-09, 6.7380093000881e-13, 17997.029080526172, -38.320594459139734], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.1533309386454741, 0.02312968678326665, -3.289590795769531e-05, 2.441141448952092e-08, -7.243664001954642e-12, 8038.853773057435, -1.7896837262996588], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.537079417328969, -0.0038577507795309633, 6.934770920070903e-06, -3.733040236094633e-09, 6.7380093000881e-13, 6324.55181152854, -38.320594459139734], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-1.7582967946366366, 0.042026401517499944, -5.600753638515023e-05, 3.825182908222041e-08, -1.0409416384415948e-11, 28105.56145218135, 5.853411567519336], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.077474570473491, -0.006939960216315113, 1.2365235918805114e-05, -6.576528299276142e-09, 1.1767590618301862e-12, 24851.901108785212, -62.89449360450202], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-1.7582967946366366, 0.042026401517499944, -5.600753638515023e-05, 3.825182908222041e-08, -1.0409416384415948e-11, 8478.964692023272, 5.853411567519336], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.077474570473491, -0.006939960216315113, 1.2365235918805114e-05, -6.576528299276142e-09, 1.1767590618301862e-12, 5225.304348627133, -62.89449360450202], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.5789725109422789, 0.03719156947423711, -1.2289771963968407e-05, -8.771791809048261e-09, 6.040390410078089e-12, 5244.871029853704, 1.4727597507430517], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[21.536381694217713, -0.02159323821878347, 3.852990432548073e-05, -2.056918248879602e-08, 3.6875582882373026e-12, -998.0573309739448, -113.39905386783853], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.5789725109422789, 0.03719156947423711, -1.2289771963968407e-05, -8.771791809048261e-09, 6.040390410078089e-12, -5772.747109709351, 1.4727597507430517], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[21.536381694217713, -0.02159323821878347, 3.852990432548073e-05, -2.056918248879602e-08, 3.6875582882373026e-12, -12015.675470537002, -113.39905386783853], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.2626258291795631, 0.023970695898387073, -3.5780696767867036e-05, 2.6941743821084965e-08, -8.087010228141622e-12, -4039.069006755565, -6.660766627246156], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.290136763413816, -0.002447954963019431, 4.512500116250858e-06, -2.513110578099106e-09, 4.657872140968094e-13, -5635.166026977534, -41.25295452279153], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.2626258291795631, 0.023970695898387073, -3.5780696767867036e-05, 2.6941743821084965e-08, -8.087010228141622e-12, -11664.420972813878, -6.660766627246156], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.290136763413816, -0.002447954963019431, 4.512500116250858e-06, -2.513110578099106e-09, 4.657872140968094e-13, -13260.517993035846, -41.25295452279153], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-1.7981534894390012, 0.03269962600516455, -4.2566230420913326e-05, 2.91542490369061e-08, -8.035856702282018e-12, 8586.203222029619, 5.848060021291731], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.430231182423013, -0.006459576055042201, 1.1544899962243683e-05, -6.169056776575097e-09, 1.1071361163869078e-12, 5902.604008855158, -50.12254953508379], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-1.7981534894390012, 0.03269962600516455, -4.2566230420913326e-05, 2.91542490369061e-08, -8.035856702282018e-12, 1188.7605819842956, 5.848060021291731], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.430231182423013, -0.006459576055042201, 1.1544899962243683e-05, -6.169056776575097e-09, 1.1071361163869078e-12, -1494.838631190164, -50.12254953508379], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.3088563851978815, 0.0283916874007885, -3.0151732071123384e-05, 1.771974951629053e-08, -4.275930304276088e-12, 14076.344265808717, 1.0285424176859035], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.348629912270564, -0.008905560700536734, 1.584616974627966e-05, -8.417565551754216e-09, 1.5032447502223972e-12, 11113.341835980029, -57.93257830829966], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.3088563851978815, 0.0283916874007885, -3.0151732071123384e-05, 1.771974951629053e-08, -4.275930304276088e-12, 6698.538079993526, 1.0285424176859035], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.348629912270564, -0.008905560700536734, 1.584616974627966e-05, -8.417565551754216e-09, 1.5032447502223972e-12, 3735.5356501648366, -57.93257830829966], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.472397484259402, 0.027761496719987733, -4.488251024138066e-05, 3.68137619172982e-08, -1.161323814891091e-11, 30301.853411456035, 2.4117785112268493], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.532291909983012, -0.004937822379131742, 8.640827527955598e-06, -4.462041957190934e-09, 7.786526296378301e-13, 28591.07875842594, -36.66572094479358], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.472397484259402, 0.027761496719987733, -4.488251024138066e-05, 3.68137619172982e-08, -1.161323814891091e-11, 22904.41077141071, 2.4117785112268493], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.532291909983012, -0.004937822379131742, 8.640827527955598e-06, -4.462041957190934e-09, 7.786526296378301e-13, 21193.636118380615, -36.66572094479358], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.880908266679414, 0.018320052300656305, -5.853299352285862e-06, -4.76200059261109e-09, 3.300731216127062e-12, 22808.93252342345, 1.6988541423802932], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.86272199859298, -0.011203107450698802, 1.9721651219833707e-05, -1.031497658472236e-08, 1.820102655560301e-12, 19748.08485328875, -55.20399403423673], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.880908266679414, 0.018320052300656305, -5.853299352285862e-06, -4.76200059261109e-09, 3.300731216127062e-12, 6939.966447770629, 1.6988541423802932], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.86272199859298, -0.011203107450698802, 1.9721651219833707e-05, -1.031497658472236e-08, 1.820102655560301e-12, 3879.1187776359293, -55.20399403423673], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[2.549649161595254, 0.018460038448502983, -2.4200109760726565e-05, 1.7347497091245413e-08, -5.041828066154608e-12, -11136.054278664964, -4.24776437425156], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.09914564301697, -0.00440018433340282, 7.814540603211383e-06, -4.134669468842997e-09, 7.364144304799385e-13, -12712.096349751235, -36.92102410599301], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[2.549649161595254, 0.018460038448502983, -2.4200109760726565e-05, 1.7347497091245413e-08, -5.041828066154608e-12, -18741.769789597045, -4.24776437425156], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.09914564301697, -0.00440018433340282, 7.814540603211383e-06, -4.134669468842997e-09, 7.364144304799385e-13, -20317.811860683316, -36.92102410599301], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-4.4984127088896, 0.04745052289849407, -6.331779821893876e-05, 4.4144524192894254e-08, -1.2310062691422985e-11, 9518.036121054529, 16.9501903638442], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.436461478905347, -0.009004134479819131, 1.6092821219686652e-05, -8.599486637344516e-09, 1.5431118907086212e-12, 5755.651934007748, -62.25662996993202], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-4.4984127088896, 0.04745052289849407, -6.331779821893876e-05, 4.4144524192894254e-08, -1.2310062691422985e-11, 2140.2299352393384, 16.9501903638442], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.436461478905347, -0.009004134479819131, 1.6092821219686652e-05, -8.599486637344516e-09, 1.5431118907086212e-12, -1622.1542518074439, -62.25662996993202], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[4.152110941060885, -0.0005487132048017087, 1.6858930590385225e-05, -1.8335786801037157e-08, 6.296303756148092e-12, -14450.016583094948, -11.442037711879983], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.405124888330336, -0.006902168774863108, 1.2352154347418985e-05, -6.623629623294305e-09, 1.1913644441634286e-12, -15931.095429717068, -34.84179113075547], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[4.152110941060885, -0.0005487132048017087, 1.6858930590385225e-05, -1.8335786801037157e-08, 6.296303756148092e-12, -14062.339689925822, -11.442037711879983], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.405124888330336, -0.006902168774863108, 1.2352154347418985e-05, -6.623629623294305e-09, 1.1913644441634286e-12, -15543.41853654794, -34.84179113075547], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.7328851297248244, 0.03226341164733199, -3.779587705376396e-05, 2.3986538279409256e-08, -6.161557375428117e-12, 22966.487678183035, 1.3588387160694158], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.000137061023471, -0.00855709104302838, 1.507579874185188e-05, -7.885511119293845e-09, 1.3920669867208742e-12, 19942.882637438604, -60.26006040271306], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.7328851297248244, 0.03226341164733199, -3.779587705376396e-05, 2.3986538279409256e-08, -6.161557375428117e-12, 3359.527372255086, 1.3588387160694158], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.000137061023471, -0.00855709104302838, 1.507579874185188e-05, -7.885511119293845e-09, 1.3920669867208742e-12, 335.9223315106574, -60.26006040271306], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[2.356981745321052, 0.016581789113467055, -8.93245604193931e-06, -5.966003689946505e-10, 1.6571154171085567e-12, -47332.854284269364, -0.5432075164117869], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.04779135974607, -0.007242743771743657, 1.2909101836650357e-05, -6.880215062637572e-09, 1.2328955029475026e-12, -49736.16909270931, -45.472846353414454], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[2.356981745321052, 0.016581789113467055, -8.93245604193931e-06, -5.966003689946505e-10, 1.6571154171085567e-12, -42878.41563393078, -0.5432075164117869], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.04779135974607, -0.007242743771743657, 1.2909101836650357e-05, -6.880215062637572e-09, 1.2328955029475026e-12, -45281.730442370725, -45.472846353414454], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[3.0573783465802915, 0.012862428884006407, 4.84928695038375e-06, -1.3599718395029272e-08, 5.96899960014774e-12, -22903.39628234497, -12.435908461234026], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.113485534322619, -0.011408786775686736, 2.0203001135172224e-05, -1.0664783232591535e-08, 1.8954587248723453e-12, -25860.825984057905, -65.26660390806612], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[3.0573783465802915, 0.012862428884006407, 4.84928695038375e-06, -1.3599718395029272e-08, 5.96899960014774e-12, -22476.446478923375, -12.435908461234026], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.113485534322619, -0.011408786775686736, 2.0203001135172224e-05, -1.0664783232591535e-08, 1.8954587248723453e-12, -25433.87618063631, -65.26660390806612], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.25761672253846946, 0.019381161206708936, -2.9969201901782745e-05, 2.2777218830822605e-08, -6.826799542336559e-12, 34362.73291248703, -2.704206528801257], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.608145428430299, -0.001423773475814122, 2.641982059575953e-06, -1.482898706580994e-09, 2.765400103395678e-13, 33188.638367886175, -28.85413578279513], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.25761672253846946, 0.019381161206708936, -2.9969201901782745e-05, 2.2777218830822605e-08, -6.826799542336559e-12, 26926.01736218924, -2.704206528801257], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.608145428430299, -0.001423773475814122, 2.641982059575953e-06, -1.482898706580994e-09, 2.765400103395678e-13, 25751.92281758838, -28.85413578279513], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-3.9682655700924263, 0.04821224322916436, -7.020382754527549e-05, 5.070190901773966e-08, -1.4459940189670561e-11, 32007.966641472583, 14.06249620531019], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.25618784819828, -0.005010574566594026, 9.09124673541548e-06, -4.959982299338515e-09, 9.052412241843371e-13, 28805.667240662653, -55.90859791121436], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-3.9682655700924263, 0.04821224322916436, -7.020382754527549e-05, 5.070190901773966e-08, -1.4459940189670561e-11, 20872.52977294433, 14.06249620531019], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.25618784819828, -0.005010574566594026, 9.09124673541548e-06, -4.959982299338515e-09, 9.052412241843371e-13, 17670.2303721344, -55.90859791121436], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.5903493375056066, 0.02820293094982219, -4.3192054719588326e-05, 3.320670015772697e-08, -1.0016171919646766e-11, 24823.72847139246, 0.22475283272964264], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.5929913939688, -0.003510020572438653, 6.291002447877343e-06, -3.3685290767535198e-09, 6.056109381544889e-13, 23021.961848953124, -39.79604200258437], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.5903493375056066, 0.02820293094982219, -4.3192054719588326e-05, 3.320670015772697e-08, -1.0016171919646766e-11, 17406.649376220903, 0.22475283272964264], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.5929913939688, -0.003510020572438653, 6.291002447877343e-06, -3.3685290767535198e-09, 6.056109381544889e-13, 15604.882753781567, -39.79604200258437], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.44426315342025297, 0.035143393541917915, -3.825191195703062e-05, 2.319547565822575e-08, -5.754598186857862e-12, 11946.605812464453, 1.9827666071889034], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.74514219361069, -0.01113296971728403, 1.9585112575923382e-05, -1.022169767857312e-08, 1.8010348359985117e-12, 8348.066953852102, -70.19620556082776], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.44426315342025297, 0.035143393541917915, -3.825191195703062e-05, 2.319547565822575e-08, -5.754598186857862e-12, -7640.718037441162, 1.9827666071889034], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.74514219361069, -0.01113296971728403, 1.9585112575923382e-05, -1.022169767857312e-08, 1.8010348359985117e-12, -11239.256896053514, -70.19620556082776], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[2.725344253463979, 0.014265170184759477, -2.2141020445308363e-05, 1.7159763247973412e-08, -5.148140594379846e-12, -14626.420760053494, -5.880073500148141], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.853407080304272, -0.0020628219096885067, 3.5777124521888544e-06, -1.8218841229896744e-09, 3.147031466937131e-13, -15510.55541097614, -25.965590783472088], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[2.725344253463979, 0.014265170184759477, -2.2141020445308363e-05, 1.7159763247973412e-08, -5.148140594379846e-12, -6473.260789692248, -5.880073500148141], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.853407080304272, -0.0020628219096885067, 3.5777124521888544e-06, -1.8218841229896744e-09, 3.147031466937131e-13, -7357.395440614895, -25.965590783472088], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.8461597506391261, 0.030516767779180953, -4.188170241751797e-05, 3.038456998083873e-08, -8.772416820734819e-12, 30359.992773715698, 1.700598484390028], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.071582906242801, -0.006359525728146733, 1.1223991720427978e-05, -5.882504318359561e-09, 1.0398336922415319e-12, 27975.13679799818, -48.97471372204738], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.8461597506391261, 0.030516767779180953, -4.188170241751797e-05, 3.038456998083873e-08, -8.772416820734819e-12, 10733.39601355762, 1.700598484390028], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.071582906242801, -0.006359525728146733, 1.1223991720427978e-05, -5.882504318359561e-09, 1.0398336922415319e-12, 8348.540037840105, -48.97471372204738], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.9579364986986095, 0.03417770159679381, 2.826760350589623e-06, -2.457700198169472e-08, 1.1560079282713076e-11, 32226.063276299024, 2.110336297847528], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[24.884358222017116, -0.025217745838261856, 4.4913423110741845e-05, -2.3913113116198802e-08, 4.2785533688020905e-12, 25258.81065019916, -123.21632842360013], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.9579364986986095, 0.03417770159679381, 2.826760350589623e-06, -2.457700198169472e-08, 1.1560079282713076e-11, 8998.927469061146, 2.110336297847528], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[24.884358222017116, -0.025217745838261856, 4.4913423110741845e-05, -2.3913113116198802e-08, 4.2785533688020905e-12, 2031.6748429612817, -123.21632842360013], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.5564428527368741, 0.024881884193241183, -3.1883879797680434e-05, 2.1907620558739207e-08, -6.062372825965667e-12, 29589.277865339714, -4.09640099470948], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.380929521863289, -0.005719366556090383, 1.0097890187526818e-05, -5.296771085574308e-09, 9.37012913345748e-13, 27472.71400569276, -48.125145497670374], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.5564428527368741, 0.024881884193241183, -3.1883879797680434e-05, 2.1907620558739207e-08, -6.062372825965667e-12, 13681.03887943443, -4.09640099470948], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.380929521863289, -0.005719366556090383, 1.0097890187526818e-05, -5.296771085574308e-09, 9.37012913345748e-13, 11564.47501978748, -48.125145497670374], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.46107024748277925, 0.025330918143713778, -2.95241411134256e-06, -1.2660214463929042e-08, 6.611412806112327e-12, -13083.936144160652, 3.458601622411173], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.75018505264351, -0.016155449576488578, 2.886032092240437e-05, -1.5435831253719646e-08, 2.771547477197628e-12, -17772.234837238586, -81.5974450307295], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.46107024748277925, 0.025330918143713778, -2.95241411134256e-06, -1.2660214463929042e-08, 6.611412806112327e-12, -16355.707660761725, 3.458601622411173], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.75018505264351, -0.016155449576488578, 2.886032092240437e-05, -1.5435831253719646e-08, 2.771547477197628e-12, -21044.006353839657, -81.5974450307295], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.3699267416865255, 0.028658531388564657, -2.7893618373901115e-05, 1.3652626507646608e-08, -2.5391216906811565e-12, -29658.085078126347, -0.370046041484299], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.223403098656842, -0.007741668107278932, 1.3941845053627606e-05, -7.541931084030117e-09, 1.3666956123401224e-12, -32739.14022570285, -60.680093933753156], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.3699267416865255, 0.028658531388564657, -2.7893618373901115e-05, 1.3652626507646608e-08, -2.5391216906811565e-12, -25203.646427787764, -0.370046041484299], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.223403098656842, -0.007741668107278932, 1.3941845053627606e-05, -7.541931084030117e-09, 1.3666956123401224e-12, -28284.701575364266, -60.680093933753156], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.5846760207902084, 0.021387549509509458, -2.6680149499382863e-05, 1.8085986641749082e-08, -4.954679028168485e-12, 7454.866078763966, -8.566494007825689], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.406551623095396, -0.005399648922306131, 9.490951838389342e-06, -4.944506127843228e-09, 8.7003523316202e-13, 5562.236253241148, -47.67579637039664], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.5846760207902084, 0.021387549509509458, -2.6680149499382863e-05, 1.8085986641749082e-08, -4.954679028168485e-12, -4197.9747351074375, -8.566494007825689], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.406551623095396, -0.005399648922306131, 9.490951838389342e-06, -4.944506127843228e-09, 8.7003523316202e-13, -6090.604560630256, -47.67579637039664], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.2803857910420373, 0.026146381291558756, -3.3204709331127583e-05, 2.1735482177742986e-08, -5.739485275935152e-12, -5122.180068996522, -6.266983747164432], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.200444140595133, -0.004387993684222539, 7.853858549677602e-06, -4.205155301682368e-09, 7.569009489132158e-13, -7275.358099374035, -50.85669026114345], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.2803857910420373, 0.026146381291558756, -3.3204709331127583e-05, 2.1735482177742986e-08, -5.739485275935152e-12, -12727.895579928603, -6.266983747164432], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.200444140595133, -0.004387993684222539, 7.853858549677602e-06, -4.205155301682368e-09, 7.569009489132158e-13, -14881.073610306117, -50.85669026114345], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.687367474126204, 0.021323469448902975, -2.336039976055324e-05, 1.4597549431102648e-08, -3.8509542776843375e-12, 19506.87030701636, -4.107463299522058], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.374615944582363, -0.0066065430484157075, 1.1797360181945044e-05, -6.297363597977766e-09, 1.1289628357603193e-12, 17293.11960563462, -48.04572552374324], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.687367474126204, 0.021323469448902975, -2.336039976055324e-05, 1.4597549431102648e-08, -3.8509542776843375e-12, 7854.029493144964, -4.107463299522058], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.374615944582363, -0.0066065430484157075, 1.1797360181945044e-05, -6.297363597977766e-09, 1.1289628357603193e-12, 5640.278791763223, -48.04572552374324], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-2.7274572524717122, 0.04911931955016374, -5.721652497603537e-05, 3.62071316553514e-08, -9.375812626277735e-12, 17426.87722274739, 9.21504180455984], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.965388395063554, -0.012665129565738375, 2.261329816229308e-05, -1.2071212014237589e-08, 2.164311373349659e-12, 12777.876204525468, -84.83327362637277], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-2.7274572524717122, 0.04911931955016374, -5.721652497603537e-05, 3.62071316553514e-08, -9.375812626277735e-12, 6350.349718701734, 9.21504180455984], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.965388395063554, -0.012665129565738375, 2.261329816229308e-05, -1.2071212014237589e-08, 2.164311373349659e-12, 1701.3487004798135, -84.83327362637277], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.14057965370883882, 0.03395928839141774, -4.877970542687829e-05, 3.545524730076265e-08, -1.0228443092508144e-11, 36007.115645229365, -0.9856796655624303], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.244757631333274, -0.0044230054762681255, 7.940488035408964e-06, -4.265902533836407e-09, 7.694698624474174e-13, 33636.89900759309, -52.21194594431905], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.14057965370883882, 0.03395928839141774, -4.877970542687829e-05, 3.545524730076265e-08, -1.0228443092508144e-11, 16360.88243084115, -0.9856796655624303], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.244757631333274, -0.0044230054762681255, 7.940488035408964e-06, -4.265902533836407e-09, 7.694698624474174e-13, 13990.665793204878, -52.21194594431905], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.15487855368882772, 0.02466503412850334, -2.7882905742974466e-05, 1.67435027549696e-08, -4.172544254554822e-12, -12735.889626188708, 5.361930025591014], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.176496183301216, -0.005390103654173492, 9.767429234625479e-06, -5.327193686576743e-09, 9.715802550783626e-13, -15100.957922580372, -41.79608509369516], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.15487855368882772, 0.02466503412850334, -2.7882905742974466e-05, 1.67435027549696e-08, -4.172544254554822e-12, -16086.20696329471, 5.361930025591014], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.176496183301216, -0.005390103654173492, 9.767429234625479e-06, -5.327193686576743e-09, 9.715802550783626e-13, -18451.275259686372, -41.79608509369516], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.28139503852560294, 0.023606090400724623, -3.329587349814532e-05, 2.359374470300372e-08, -6.599876894997081e-12, -23927.635259897124, -2.84939166435208], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.572784026138338, -0.003165794452503801, 5.618129387791434e-06, -2.968323943805841e-09, 5.286847314914158e-13, -25589.611279803205, -38.82975654873838], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.28139503852560294, 0.023606090400724623, -3.329587349814532e-05, 2.359374470300372e-08, -6.599876894997081e-12, -23559.594821854233, -2.84939166435208], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.572784026138338, -0.003165794452503801, 5.618129387791434e-06, -2.968323943805841e-09, 5.286847314914158e-13, -25221.570841760316, -38.82975654873838], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.8975857479384713, 0.02467430605223327, -3.701359961395603e-05, 2.8207317800893548e-08, -8.568604159542303e-12, -9416.35662428313, -4.673145748543366], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.178182501682011, -0.0027487269566934865, 5.052972658860588e-06, -2.8034483246861914e-09, 5.180259484040403e-13, -11072.262121363161, -40.51071502096373], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.8975857479384713, 0.02467430605223327, -3.701359961395603e-05, 2.8207317800893548e-08, -8.568604159542303e-12, -12786.310416515362, -4.673145748543366], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.178182501682011, -0.0027487269566934865, 5.052972658860588e-06, -2.8034483246861914e-09, 5.180259484040403e-13, -14442.215913595395, -40.51071502096373], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.6808021563044655, 0.031212610386516765, -8.0789083685967e-06, -1.0837720993507388e-08, 6.482207132174622e-12, -33457.50252613175, -5.80787639926811], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[20.413219942559014, -0.01736018391676655, 3.107644929253564e-05, -1.667132564139086e-08, 3.0008306359545142e-12, -38800.63258657386, -103.39683977096684], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.6808021563044655, 0.031212610386516765, -8.0789083685967e-06, -1.0837720993507388e-08, 6.482207132174622e-12, -32662.512283771164, -5.80787639926811], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[20.413219942559014, -0.01736018391676655, 3.107644929253564e-05, -1.667132564139086e-08, 3.0008306359545142e-12, -38005.64234421328, -103.39683977096684], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.035651661290625, 0.02403762635148776, -3.10715175028547e-05, 2.1274644888654494e-08, -5.936341695989e-12, -13684.098710012237, 0.8423300649336412], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.320902420594948, -0.004524709457421657, 8.146698589352583e-06, -4.39895746622928e-09, 7.961296162925903e-13, -15689.013935999656, -40.56217721897826], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.035651661290625, 0.02403762635148776, -3.10715175028547e-05, 2.1274644888654494e-08, -5.936341695989e-12, -13504.694686833767, 0.8423300649336412], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.320902420594948, -0.004524709457421657, 8.146698589352583e-06, -4.39895746622928e-09, 7.961296162925903e-13, -15509.609912821186, -40.56217721897826], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.5632792211806477, 0.014266187393854, -1.2973938191255383e-05, 7.2687754684802e-09, -1.690748235860795e-12, -1402.0934696459235, -4.452608283390505], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.417075986305159, -0.007111062744209318, 1.2402765963078194e-05, -6.388062948060308e-09, 1.112839399284942e-12, -3172.674473410656, -39.25667844445977], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.5632792211806477, 0.014266187393854, -1.2973938191255383e-05, 7.2687754684802e-09, -1.690748235860795e-12, -9316.940054138297, -4.452608283390505], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.417075986305159, -0.007111062744209318, 1.2402765963078194e-05, -6.388062948060308e-09, 1.112839399284942e-12, -11087.521057903028, -39.25667844445977], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[3.7671511680188914, 0.004179530413204547, -5.16460306174389e-06, 4.281737107517529e-09, -1.53270538622019e-12, 22348.916596369447, -16.448669925442786], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.522345399046397, -0.0014872471506000141, 2.7115514303087297e-06, -1.4880483774407132e-09, 2.725089394624866e-13, 21883.12982266304, -25.372463575785044], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[3.7671511680188914, 0.004179530413204547, -5.16460306174389e-06, 4.281737107517529e-09, -1.53270538622019e-12, 10656.802872245578, -16.448669925442786], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.522345399046397, -0.0014872471506000141, 2.7115514303087297e-06, -1.4880483774407132e-09, 2.725089394624866e-13, 10191.01609853917, -25.372463575785044], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.5872272419093946, 0.021884253745618573, -9.092097282359689e-06, -3.2013094266308145e-09, 2.9345692542648294e-12, 13361.94067432726, -3.0977389241107636], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.083489072067747, -0.011983006093140706, 2.1302955374565833e-05, -1.1309817688692583e-08, 2.0190228680020024e-12, 9877.860887341381, -67.81740135471398], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.5872272419093946, 0.021884253745618573, -9.092097282359689e-06, -3.2013094266308145e-09, 2.9345692542648294e-12, 1748.3727707083235, -3.0977389241107636], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.083489072067747, -0.011983006093140706, 2.1302955374565833e-05, -1.1309817688692583e-08, 2.0190228680020024e-12, -1735.7070162775544, -67.81740135471398], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.5697224109377661, 0.026888160051806834, -2.5056254060616507e-05, 1.1463352656729904e-08, -1.8672528800944832e-12, -15489.018951560318, -3.3542668371249977], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.974057020690037, -0.007721493775440698, 1.3817688459358648e-05, -7.405228719062684e-09, 1.3327051932182123e-12, -18469.353758394933, -61.47039926672395], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.5697224109377661, 0.026888160051806834, -2.5056254060616507e-05, 1.1463352656729904e-08, -1.8672528800944832e-12, -23075.098007366163, -3.3542668371249977], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.974057020690037, -0.007721493775440698, 1.3817688459358648e-05, -7.405228719062684e-09, 1.3327051932182123e-12, -26055.43281420078, -61.47039926672395], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.5007041222485064, 0.020387505380996075, -1.8341220404454415e-05, 8.052118908019455e-09, -1.1760176166220049e-12, -19415.383041669178, 7.4226327062441815], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.403552916321377, -0.006564510724457786, 1.1718359325497268e-05, -6.258468246674575e-09, 1.1227488750043197e-12, -21745.598447147782, -37.968065521548], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.5007041222485064, 0.020387505380996075, -1.8341220404454415e-05, 8.052118908019455e-09, -1.1760176166220049e-12, -19027.706148500052, 7.4226327062441815], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.403552916321377, -0.006564510724457786, 1.1718359325497268e-05, -6.258468246674575e-09, 1.1227488750043197e-12, -21357.921553978656, -37.968065521548], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.1702965064381586, 0.026818224391284964, -2.1187990710913625e-05, 8.209912931753756e-09, -1.027764678918075e-12, 19244.250766409474, 4.199426716437015], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.950283973573839, -0.010553855620259525, 1.8890938379933674e-05, -1.0126216905412885e-08, 1.821528611810081e-12, 15804.834075909634, -61.349263752500676], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.1702965064381586, 0.026818224391284964, -2.1187990710913625e-05, 8.209912931753756e-09, -1.027764678918075e-12, 8148.086806341483, 4.199426716437015], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.950283973573839, -0.010553855620259525, 1.8890938379933674e-05, -1.0126216905412885e-08, 1.821528611810081e-12, 4708.670115841645, -61.349263752500676], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[2.158563986374605, 0.024853988358157476, 1.5352617703198102e-05, -3.2530250732843954e-08, 1.350676862021949e-11, 137.41185126711844, -8.741405924676677], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[23.28324248920475, -0.024540711211524024, 4.373135677424616e-05, -2.3303703808340938e-08, 4.171503691519779e-12, -6189.080302457438, -120.20188474457066], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[2.158563986374605, 0.024853988358157476, 1.5352617703198102e-05, -3.2530250732843954e-08, 1.350676862021949e-11, -10860.56983048141, -8.741405924676677], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[23.28324248920475, -0.024540711211524024, 4.373135677424616e-05, -2.3303703808340938e-08, 4.171503691519779e-12, -17187.061984205968, -120.20188474457066], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-2.7297881782361464, 0.0477487229679998, -4.578266674370648e-05, 2.3451874122656707e-08, -4.784866947105115e-12, 9167.879740495275, 9.234684278219188], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.85666165260097, -0.01573099663032726, 2.8107720156277172e-05, -1.5027652331556597e-08, 2.6975423746144773e-12, 3814.5604913698735, -95.4810405802704], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-2.7297881782361464, 0.0477487229679998, -4.578266674370648e-05, 2.3451874122656707e-08, -4.784866947105115e-12, -1889.0113075280515, 9.234684278219188], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.85666165260097, -0.01573099663032726, 2.8107720156277172e-05, -1.5027652331556597e-08, 2.6975423746144773e-12, -7242.330556653453, -95.4810405802704], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-3.876486774098759, 0.05041092235724704, -4.037083717101258e-05, 1.4788222259221832e-08, -1.2397097237659693e-12, 8106.704408403479, 15.749899480627548], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.66013395149451, -0.018925451027068645, 3.3821169214707656e-05, -1.8093156895228588e-08, 3.249415703686625e-12, 1830.121282850061, -104.75676803324718], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-3.876486774098759, 0.05041092235724704, -4.037083717101258e-05, 1.4788222259221832e-08, -1.2397097237659693e-12, -2930.5501871819097, 15.749899480627548], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.66013395149451, -0.018925451027068645, 3.3821169214707656e-05, -1.8093156895228588e-08, 3.249415703686625e-12, -9207.133312735328, -104.75676803324718], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[3.372718318131053, 0.011948605519731134, 2.7150456278172206e-05, -3.885263527850272e-08, 1.494058696205336e-11, -17399.02898305566, -7.758957601829563], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[18.516664160343957, -0.019074670417355798, 3.401223935596512e-05, -1.8145942414685825e-08, 3.2514411153175722e-12, -22157.44192926314, -88.75718953272656], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[3.372718318131053, 0.011948605519731134, 2.7150456278172206e-05, -3.885263527850272e-08, 1.494058696205336e-11, -20651.164047218794, -7.758957601829563], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[18.516664160343957, -0.019074670417355798, 3.401223935596512e-05, -1.8145942414685825e-08, 3.2514411153175722e-12, -25409.57699342627, -88.75718953272656], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.2535897313874391, 0.0331664250530545, -4.263532659067634e-05, 2.860999415456707e-08, -7.693949644060893e-12, -9430.817556119538, 5.808089455489748], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.171441927115158, -0.00647197678082797, 1.1485655604529038e-05, -6.0731342014698865e-09, 1.0815666921505608e-12, -12161.296874315747, -51.16815885849702], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.2535897313874391, 0.0331664250530545, -4.263532659067634e-05, 2.860999415456707e-08, -7.693949644060893e-12, -17016.896611925386, 5.808089455489748], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.171441927115158, -0.00647197678082797, 1.1485655604529038e-05, -6.0731342014698865e-09, 1.0815666921505608e-12, -19747.375930121594, -51.16815885849702], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-2.3443315809312595, 0.04526673811325242, -3.3447648876703874e-05, 1.0361211371484028e-08, -1.3049283875687934e-13, 4380.067841646112, 8.413327357263116], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.655427687564014, -0.018621902641565248, 3.322657498803786e-05, -1.773344101340974e-08, 3.1788171677175556e-12, -1538.3112427590113, -104.46654041689519], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-2.3443315809312595, 0.04526673811325242, -3.3447648876703874e-05, 1.0361211371484028e-08, -1.3049283875687934e-13, -6657.186753939275, 8.413327357263116], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.655427687564014, -0.018621902641565248, 3.322657498803786e-05, -1.773344101340974e-08, 3.1788171677175556e-12, -12575.565838344399, -104.46654041689519], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-2.2300645782186788, 0.029222282416047938, -4.3315468288874015e-05, 3.31428027291935e-08, -9.964716551902342e-12, 6419.375594582315, 8.30171716264823], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.834592696160247, -0.0051492538511714245, 9.154900439151632e-06, -4.849169380135208e-09, 8.637658222411613e-13, 4382.660096974666, -36.22149496382639], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-2.2300645782186788, 0.029222282416047938, -4.3315468288874015e-05, 3.31428027291935e-08, -9.964716551902342e-12, 2740.290729685885, 8.30171716264823], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.834592696160247, -0.0051492538511714245, 9.154900439151632e-06, -4.849169380135208e-09, 8.637658222411613e-13, 703.5752320782358, -36.22149496382639], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.04255587293465304, 0.027932802284313885, -3.942772006846711e-05, 2.937989976562643e-08, -8.786783800562858e-12, -5862.050977941603, 4.036376718408254], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.117743977532806, -0.005002064890272754, 8.996355973457415e-06, -4.846548272764188e-09, 8.752672658917174e-13, -7986.962379581206, -40.93666941907792], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.04255587293465304, 0.027932802284313885, -3.942772006846711e-05, 2.937989976562643e-08, -8.786783800562858e-12, -9212.368315047606, 4.036376718408254], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.117743977532806, -0.005002064890272754, 8.996355973457415e-06, -4.846548272764188e-09, 8.752672658917174e-13, -11337.279716687208, -40.93666941907792], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.9848787280247717, 0.03601480571258881, -5.06523957248035e-05, 3.6284301142324924e-08, -1.0380460380154943e-11, 37165.18239744143, 1.6646681085462038], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.257828530267187, -0.004865143870387635, 8.797732294992285e-06, -4.777704201738108e-09, 8.686592687967868e-13, 34561.41799693118, -53.96726152944254], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.9848787280247717, 0.03601480571258881, -5.06523957248035e-05, 3.6284301142324924e-08, -1.0380460380154943e-11, 26029.745528913172, 1.6646681085462038], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.257828530267187, -0.004865143870387635, 8.797732294992285e-06, -4.777704201738108e-09, 8.686592687967868e-13, 23425.981128402917, -53.96726152944254], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.4987424599124593, 0.020575187483968613, -1.268778417935204e-05, 2.0580096976730705e-09, 8.05244759760626e-13, 12843.038147401696, -3.116375604882025], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.222901125746136, -0.009612809130542856, 1.715947768608812e-05, -9.163517606100242e-09, 1.6433481467715682e-12, 9901.551648884837, -58.400890305140216], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.4987424599124593, 0.020575187483968613, -1.268778417935204e-05, 2.0580096976730705e-09, 8.05244759760626e-13, 1209.8337877604247, -3.116375604882025], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.222901125746136, -0.009612809130542856, 1.715947768608812e-05, -9.163517606100242e-09, 1.6433481467715682e-12, -1731.6527107564325, -58.400890305140216], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[2.366216905242251, 0.019020740681499365, -2.6531517990758787e-05, 1.9018956406066634e-08, -5.525649382498443e-12, 21477.548063463008, -10.66468490521628], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.334160815533311, -0.002320012120532959, 4.273612948512938e-06, -2.380222376156985e-09, 4.4120735219471815e-13, 20068.026923048143, -40.31024821340094], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[2.366216905242251, 0.019020740681499365, -2.6531517990758787e-05, 1.9018956406066634e-08, -5.525649382498443e-12, 9596.79792537081, -10.66468490521628], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.334160815533311, -0.002320012120532959, 4.273612948512938e-06, -2.380222376156985e-09, 4.4120735219471815e-13, 8187.276784955946, -40.31024821340094], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.671760911419438, 0.024196095571897572, -3.0224106307781846e-05, 1.9895399940588105e-08, -5.340183156787859e-12, -12167.061395429997, -7.690276919546048], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.180364931491424, -0.004638309918568294, 8.319844328464815e-06, -4.468746102314158e-09, 8.058137202616262e-13, -14244.609080368937, -50.31831828858603], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.671760911419438, 0.024196095571897572, -3.0224106307781846e-05, 1.9895399940588105e-08, -5.340183156787859e-12, -19772.77690636208, -7.690276919546048], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.180364931491424, -0.004638309918568294, 8.319844328464815e-06, -4.468746102314158e-09, 8.058137202616262e-13, -21850.324591301018, -50.31831828858603], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.19306645245111803, 0.028838421998994525, -1.1311610948254996e-05, -5.046731874152569e-09, 4.143907439413397e-12, 14419.225106249321, 4.760672174748043], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.77750123732734, -0.015741207057722553, 2.807045276052443e-05, -1.4972152812116074e-08, 2.6824589404383318e-12, 9770.895214424392, -81.23811178635668], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.19306645245111803, 0.028838421998994525, -1.1311610948254996e-05, -5.046731874152569e-09, 4.143907439413397e-12, 3362.334058225998, 4.760672174748043], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.77750123732734, -0.015741207057722553, 2.807045276052443e-05, -1.4972152812116074e-08, 2.6824589404383318e-12, -1285.9958335989322, -81.23811178635668], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.2944742231310568, 0.01441625726654529, -2.6132258567565067e-05, 2.1900587545061747e-08, -6.98019593514676e-12, -16286.448704697383, -0.1994529693939322], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.9024434885594417, -0.0003385796875714501, 6.433677259569432e-07, -3.663244667788907e-10, 6.90090255981083e-14, -16874.269693025664, -15.255951597679068], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.2944742231310568, 0.01441625726654529, -2.6132258567565067e-05, 2.1900587545061747e-08, -6.98019593514676e-12, -12219.686946631826, -0.1994529693939322], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.9024434885594417, -0.0003385796875714501, 6.433677259569432e-07, -3.663244667788907e-10, 6.90090255981083e-14, -12807.507934960106, -15.255951597679068], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.230386273235039, 0.021364181138588848, -1.0987940121250096e-05, -4.0856023207660433e-10, 1.727923359950978e-12, -23794.99126492129, 0.4124434938860766], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.896116437024084, -0.010602939524945506, 1.8955775325381663e-05, -1.0145891565618452e-08, 1.822929746606375e-12, -27043.06802309936, -59.954277173473585], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.230386273235039, 0.021364181138588848, -1.0987940121250096e-05, -4.0856023207660433e-10, 1.727923359950978e-12, -27106.035693567024, 0.4124434938860766], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.896116437024084, -0.010602939524945506, 1.8955775325381663e-05, -1.0145891565618452e-08, 1.822929746606375e-12, -30354.112451745095, -59.954277173473585], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-1.9435071260361403, 0.019776732831383256, -3.36336478120767e-05, 2.6902708865759773e-08, -8.279588820103712e-12, 11599.419217836257, 7.174688997290197], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.8134783548688582, -0.0006939614447037248, 1.3030892875136078e-06, -7.387048270359094e-10, 1.387965682836422e-13, 10658.87818729943, -15.573868627012471], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-1.9435071260361403, 0.019776732831383256, -3.36336478120767e-05, 2.6902708865759773e-08, -8.279588820103712e-12, 7881.061442687362, 7.174688997290197], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.8134783548688582, -0.0006939614447037248, 1.3030892875136078e-06, -7.387048270359094e-10, 1.387965682836422e-13, 6940.520412150534, -15.573868627012471], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[2.0095993625509263, 0.013359751800887295, -1.623038022297421e-05, 1.100295092154081e-08, -3.144848964575786e-12, -53252.82714227864, -2.592942043349627], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.982982484199035, -0.003098712991854859, 5.6288276125419164e-06, -3.0784730588189656e-09, 5.624488513619069e-13, -54504.48404749198, -27.652011141862076], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[2.0095993625509263, 0.013359751800887295, -1.623038022297421e-05, 1.100295092154081e-08, -3.144848964575786e-12, -48837.66140129643, -2.592942043349627], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.982982484199035, -0.003098712991854859, 5.6288276125419164e-06, -3.0784730588189656e-09, 5.624488513619069e-13, -50089.31830650976, -27.652011141862076], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[3.8640642056131584, 0.0007534561819428265, -1.6557138003720825e-06, 1.5522317389958574e-09, -4.4678204278586486e-13, -861.4503090147955, -8.858065697537338], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.068796960213998, -0.0004958073404741864, 6.59234957641556e-07, -1.7259799397596298e-10, 7.629699988490827e-15, -872.8758037235912, -9.719180011871295], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[3.8640642056131584, 0.0007534561819428265, -1.6557138003720825e-06, 1.5522317389958574e-09, -4.4678204278586486e-13, -822.1773987623304, -8.858065697537338], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.068796960213998, -0.0004958073404741864, 6.59234957641556e-07, -1.7259799397596298e-10, 7.629699988490827e-15, -833.6028934711262, -9.719180011871295], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[3.9971693162720885, 0.025096348548238535, 1.3274009383360151e-05, -3.229249144943194e-08, 1.3906143597752774e-11, 24456.188057482843, -7.72206159144363], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[23.931485047682692, -0.02091595534142395, 3.7374058428816125e-05, -2.0002140984265296e-08, 3.5937322453820364e-12, 18484.56924326731, -112.9798376013536], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[3.9971693162720885, 0.025096348548238535, 1.3274009383360151e-05, -3.229249144943194e-08, 1.3906143597752774e-11, 5256.541097161964, -7.72206159144363], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[23.931485047682692, -0.02091595534142395, 3.7374058428816125e-05, -2.0002140984265296e-08, 3.5937322453820364e-12, -715.0777170535657, -112.9798376013536], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
4 O  u0 p2 c0 {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.967034615362547, 0.02010733549192458, -3.4308739987448315e-05, 2.7576743917525124e-08, -8.530565143161084e-12, -12941.884620720235, -5.635470610931528], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.80193968165238, -0.0007299198999691197, 1.3702143543308481e-06, -7.761672795155717e-10, 1.4574203770431897e-13, -13898.180408569177, -28.75413978117127], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.967034615362547, 0.02010733549192458, -3.4308739987448315e-05, 2.7576743917525124e-08, -8.530565143161084e-12, -4808.361104589126, -5.635470610931528], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.80193968165238, -0.0007299198999691197, 1.3702143543308481e-06, -7.761672795155717e-10, 1.4574203770431897e-13, -5764.656892438068, -28.75413978117127], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[2.2298280105896993, 0.02857061603848079, -1.4963298962563756e-05, -5.176313642584092e-10, 2.3810120541867263e-12, 20969.83324209756, -3.88141499699622], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.662163695275716, -0.013767034996296631, 2.461032395965204e-05, -1.3171447002254381e-08, 2.3665201200583075e-12, 16681.467730386332, -83.71181218671018], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[2.2298280105896993, 0.02857061603848079, -1.4963298962563756e-05, -5.176313642584092e-10, 2.3810120541867263e-12, 5449.2711493614015, -3.88141499699622], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.662163695275716, -0.013767034996296631, 2.461032395965204e-05, -1.3171447002254381e-08, 2.3665201200583075e-12, 1160.9056376501721, -83.71181218671018], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.3799318568768906, 0.01775103470413556, -1.2084989762157814e-05, 2.539138091112652e-09, 6.810073338581191e-13, -1873.3837144069967, -0.28277495203800207], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.249400879119277, -0.00793852051711074, 1.394200430491105e-05, -7.2651932040060965e-09, 1.2784307609119226e-12, -4242.141676680261, -45.75608364954671], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.3799318568768906, 0.01775103470413556, -1.2084989762157814e-05, 2.539138091112652e-09, 6.810073338581191e-13, -5721.468539041618, -0.28277495203800207], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.249400879119277, -0.00793852051711074, 1.394200430491105e-05, -7.2651932040060965e-09, 1.2784307609119226e-12, -8090.226501314883, -45.75608364954671], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-2.6719194973911855, 0.03806450613181091, -3.824359770062638e-05, 2.040231059078257e-08, -4.289291144488061e-12, 4224.044871674576, 10.50407379541928], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.228995066113947, -0.011870659656779477, 2.115216565464864e-05, -1.1264162101025237e-08, 2.0156694171299776e-12, 147.75147800130435, -70.11901785345958], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-2.6719194973911855, 0.03806450613181091, -3.824359770062638e-05, 2.040231059078257e-08, -4.289291144488061e-12, -3134.1248581182854, 10.50407379541928], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.228995066113947, -0.011870659656779477, 2.115216565464864e-05, -1.1264162101025237e-08, 2.0156694171299776e-12, -7210.418251791557, -70.11901785345958], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.969587403874247, 0.02052289466273032, -1.1621280547621207e-05, 6.215825757615234e-10, 1.3989989722240637e-12, -17750.328784269524, -2.3548372776887767], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.866079481005135, -0.00980042385656314, 1.7404572637224417e-05, -9.22325533388852e-09, 1.6448101391910563e-12, -20748.39875268311, -58.5945861741978], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.969587403874247, 0.02052289466273032, -1.1621280547621207e-05, 6.215825757615234e-10, 1.3989989722240637e-12, -25316.771386741337, -2.3548372776887767], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.866079481005135, -0.00980042385656314, 1.7404572637224417e-05, -9.22325533388852e-09, 1.6448101391910563e-12, -28314.84135515492, -58.5945861741978], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-4.928535066156786, 0.05534718152841105, -7.064613041223017e-05, 4.67853742667796e-08, -1.2437668950315839e-11, 20007.42067086423, 18.28098562868972], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.083457114456088, -0.010265295379669075, 1.8411727682574056e-05, -9.893069344811372e-09, 1.7834012939381763e-12, 15441.111100070288, -76.62810888409447], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-4.928535066156786, 0.05534718152841105, -7.064613041223017e-05, 4.67853742667796e-08, -1.2437668950315839e-11, 8911.256710796242, 18.28098562868972], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.083457114456088, -0.010265295379669075, 1.8411727682574056e-05, -9.893069344811372e-09, 1.7834012939381763e-12, 4344.947140002299, -76.62810888409447], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.8730990245546361, 0.019325901636389226, -2.4337266409277266e-05, 1.6132658100797165e-08, -4.345260262716977e-12, -18251.072154775753, -2.940452198061079], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.634569118474064, -0.003735680111357191, 6.726671065437476e-06, -3.6343862440460883e-09, 6.579582612385249e-13, -19895.27981830717, -36.779209771998254], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.8730990245546361, 0.019325901636389226, -2.4337266409277266e-05, 1.6132658100797165e-08, -4.345260262716977e-12, -17883.03171673286, -2.940452198061079], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.634569118474064, -0.003735680111357191, 6.726671065437476e-06, -3.6343862440460883e-09, 6.579582612385249e-13, -19527.23938026428, -36.779209771998254], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[2.0573699775793095, 0.01878551011043775, -2.938069724351587e-05, 2.350186851777543e-08, -7.340232588415319e-12, 14469.566046293092, -10.421554931384392], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.609523066033134, -0.0029859167584867937, 5.278299518393383e-06, -2.767395024338096e-09, 4.893079722596751e-13, 13251.535245058505, -37.533505209362595], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[2.0573699775793095, 0.01878551011043775, -2.938069724351587e-05, 2.350186851777543e-08, -7.340232588415319e-12, 2797.088777295455, -10.421554931384392], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.609523066033134, -0.0029859167584867937, 5.278299518393383e-06, -2.767395024338096e-09, 4.893079722596751e-13, 1579.057976060869, -37.533505209362595], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-4.325685008569402, 0.05227616954992133, -6.524815321269459e-05, 4.254890479161197e-08, -1.1179376868675206e-11, 17659.76202925609, 15.78604404581501], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.035495081023502, -0.010328866072734963, 1.8514421035613457e-05, -9.939820509563878e-09, 1.7906297172559822e-12, 13208.421676329703, -76.07100602733398], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-4.325685008569402, 0.05227616954992133, -6.524815321269459e-05, 4.254890479161197e-08, -1.1179376868675206e-11, 6563.5980691880995, 15.78604404581501], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.035495081023502, -0.010328866072734963, 1.8514421035613457e-05, -9.939820509563878e-09, 1.7906297172559822e-12, 2112.2577162617144, -76.07100602733398], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-4.3383416228785405, 0.05493561603944398, -8.04347803491962e-05, 5.94297263297502e-08, -1.7339199520627346e-11, 25220.350541629054, 15.175251696241196], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.21959304626652, -0.007225570624319904, 1.2980701378227055e-05, -6.981180433014081e-09, 1.259477509332513e-12, 21487.506579923946, -66.26216346010321], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-4.3383416228785405, 0.05493561603944398, -8.04347803491962e-05, 5.94297263297502e-08, -1.7339199520627346e-11, 14104.550127330935, 15.175251696241196], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.21959304626652, -0.007225570624319904, 1.2980701378227055e-05, -6.981180433014081e-09, 1.259477509332513e-12, 10371.706165625828, -66.26216346010321], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[4.8549618970361985, -0.005541347878692846, 3.0119805912452307e-05, -2.992258851269603e-08, 1.0050251429694068e-11, -4796.951945799234, -9.256206302347813], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.541393766552916, -0.010402513409078933, 1.8377739993644713e-05, -9.667651291471074e-09, 1.712113788146074e-12, -6534.8858541836835, -35.56384362882349], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[4.8549618970361985, -0.005541347878692846, 3.0119805912452307e-05, -2.992258851269603e-08, 1.0050251429694068e-11, -8436.763901339298, -9.256206302347813], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.541393766552916, -0.010402513409078933, 1.8377739993644713e-05, -9.667651291471074e-09, 1.712113788146074e-12, -10174.697809723748, -35.56384362882349], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-1.029643429257797, 0.03056436481280869, -2.5733365236408553e-05, 1.1293796508562125e-08, -1.821806594470843e-12, 7111.250425653134, 2.6617654177208347], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.238954399490348, -0.012066252955546966, 2.153093734988074e-05, -1.1489313129942497e-08, 2.059020397351995e-12, 3322.8059635813097, -70.27958695073038], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-1.029643429257797, 0.03056436481280869, -2.5733365236408553e-05, 1.1293796508562125e-08, -1.821806594470843e-12, -246.91930413972545, 2.6617654177208347], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.238954399490348, -0.012066252955546966, 2.153093734988074e-05, -1.1489313129942497e-08, 2.059020397351995e-12, -4035.36376621155, -70.27958695073038], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[2.6545257813847285, 0.015399192759007823, -1.0183826670136605e-05, 1.753031763371618e-09, 5.796144814107507e-13, -39946.21606006641, -11.081140115163407], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.183628262656756, -0.0054815563934807335, 9.935047271124395e-06, -5.4247649800572645e-09, 9.901839547951652e-13, -42028.899987667486, -49.97906879817951], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[2.6545257813847285, 0.015399192759007823, -1.0183826670136605e-05, 1.753031763371618e-09, 5.796144814107507e-13, -35511.41386395796, -11.081140115163407], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.183628262656756, -0.0054815563934807335, 9.935047271124395e-06, -5.4247649800572645e-09, 9.901839547951652e-13, -37594.09779155904, -49.97906879817951], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.26477234399100147, 0.03035176999255425, -2.0473774973403015e-05, 4.470350596539826e-09, 8.498098058584702e-13, -21913.44222207678, 6.5331825956055], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.898898669499161, -0.012891073692233341, 2.2999889257501197e-05, -1.2274824918481617e-08, 2.2004937612731326e-12, -26030.755715802123, -71.46368014442395], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.26477234399100147, 0.03035176999255425, -2.0473774973403015e-05, 4.470350596539826e-09, 8.498098058584702e-13, -25204.850194700182, 6.5331825956055], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.898898669499161, -0.012891073692233341, 2.2999889257501197e-05, -1.2274824918481617e-08, 2.2004937612731326e-12, -29322.163688425528, -71.46368014442395], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-1.2534176212234847, 0.03273020710355643, -3.754929968340677e-05, 2.321145562250547e-08, -5.930839153123202e-12, -7269.169225923084, 9.926598033908668], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.179468174879117, -0.00779811690179576, 1.4043737251600803e-05, -7.591820150798237e-09, 1.3748378944225233e-12, -10395.888463868669, -52.78358959003789], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-1.2534176212234847, 0.03273020710355643, -3.754929968340677e-05, 2.321145562250547e-08, -5.930839153123202e-12, -10599.850107902854, 9.926598033908668], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.179468174879117, -0.00779811690179576, 1.4043737251600803e-05, -7.591820150798237e-09, 1.3748378944225233e-12, -13726.569345848438, -52.78358959003789], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-1.1589268706614568, 0.03704248615588869, -3.1233211398208106e-05, 1.2995299183184974e-08, -1.8017601299824548e-12, 8877.639206531863, 2.9590731669920447], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.804653938713914, -0.013393435838752776, 2.3947519559819504e-05, -1.2818034367726568e-08, 2.3031836481675772e-12, 4370.7870405659, -83.79742663135006], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-1.1589268706614568, 0.03704248615588869, -3.1233211398208106e-05, 1.2995299183184974e-08, -1.8017601299824548e-12, -2198.888297513793, 2.9590731669920447], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.804653938713914, -0.013393435838752776, 2.3947519559819504e-05, -1.2818034367726568e-08, 2.3031836481675772e-12, -6705.740463479757, -83.79742663135006], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[2.3606845113620176, 0.014165730210107362, -1.8920019008514142e-05, 1.3801126624201276e-08, -4.17869384927716e-12, 12521.694910331888, -5.69574266490236], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.213817876105713, -0.0025695804418745093, 4.7049065756329745e-06, -2.59884802643941e-09, 4.785325044545847e-13, 11329.790068777245, -29.994800796459366], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[2.3606845113620176, 0.014165730210107362, -1.8920019008514142e-05, 1.3801126624201276e-08, -4.17869384927716e-12, 4896.342944273576, -5.69574266490236], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.213817876105713, -0.0025695804418745093, 4.7049065756329745e-06, -2.59884802643941e-09, 4.785325044545847e-13, 3704.438102718932, -29.994800796459366], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.9288946551072278, 0.016318625808529733, 6.612725716932379e-06, -1.7902849148795664e-08, 7.848204724991703e-12, 3884.0306358355565, 1.6939762269788439], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.774420011612554, -0.014595529984813184, 2.584779947691287e-05, -1.3646600194900631e-08, 2.4255124479537725e-12, 104.36813960868676, -65.80622703440591], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.9288946551072278, 0.016318625808529733, 6.612725716932379e-06, -1.7902849148795664e-08, 7.848204724991703e-12, -7709.90081176105, 1.6939762269788439], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.774420011612554, -0.014595529984813184, 2.584779947691287e-05, -1.3646600194900631e-08, 2.4255124479537725e-12, -11489.56330798792, -65.80622703440591], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.1312884557033114, 0.018402865797038696, -2.427788191413619e-05, 1.7224355907441603e-08, -4.970784200919454e-12, 33731.40709021285, -5.779521623383209], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.494137250133281, -0.003797247762429778, 6.797288946156097e-06, -3.6381823616072336e-09, 6.538479728756012e-13, 32200.93292125622, -37.52197446358211], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.1312884557033114, 0.018402865797038696, -2.427788191413619e-05, 1.7224355907441603e-08, -4.970784200919454e-12, 17803.531649181336, -5.779521623383209], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.494137250133281, -0.003797247762429778, 6.797288946156097e-06, -3.6381823616072336e-09, 6.538479728756012e-13, 16273.057480224707, -37.52197446358211], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[2.863304528558866, 0.0044727378996352735, -7.657888254030589e-06, 7.566551322548495e-09, -2.8240309396521113e-12, 16779.653371353776, -7.401146569539408], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.411396737184059, -0.0016031840634147642, 2.8880078620045804e-06, -1.556323952810155e-09, 2.807779740962135e-13, 16413.98047499854, -15.027258594306273], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[2.863304528558866, 0.0044727378996352735, -7.657888254030589e-06, 7.566551322548495e-09, -2.8240309396521113e-12, 832.1414751960257, -7.401146569539408], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.411396737184059, -0.0016031840634147642, 2.8880078620045804e-06, -1.556323952810155e-09, 2.807779740962135e-13, 466.46857884079236, -15.027258594306273], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-2.5739263830230383, 0.047739907569548025, -4.598070554827103e-05, 2.351354975713881e-08, -4.7455095408821535e-12, 10209.79909330446, 9.441519150074074], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.908024758271736, -0.015549251038012276, 2.7772942266178536e-05, -1.484153246052161e-08, 2.6631323285942338e-12, 4894.920164826477, -94.6975853312059], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-2.5739263830230383, 0.047739907569548025, -4.598070554827103e-05, 2.351354975713881e-08, -4.7455095408821535e-12, -847.0919547188665, 9.441519150074074], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.908024758271736, -0.015549251038012276, 2.7772942266178536e-05, -1.484153246052161e-08, 2.6631323285942338e-12, -6161.970883196849, -94.6975853312059], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.2993505590209032, 0.036295047104036034, -3.944358953629666e-05, 2.3073395624284446e-08, -5.505172706588013e-12, -4523.045638723517, -0.5243066765065851], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.089051869291591, -0.009905142176605984, 1.769612743136704e-05, -9.4569990848886e-09, 1.6972918872508545e-12, -8165.819990744079, -73.24268995539349], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.2993505590209032, 0.036295047104036034, -3.944358953629666e-05, 2.3073395624284446e-08, -5.505172706588013e-12, -7834.090067369252, -0.5243066765065851], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.089051869291591, -0.009905142176605984, 1.769612743136704e-05, -9.4569990848886e-09, 1.6972918872508545e-12, -11476.864419389814, -73.24268995539349], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-1.4658840835034903, 0.04032671174813905, -5.1677635604570834e-05, 3.3783985926401025e-08, -8.785375205100365e-12, 34208.886238578474, 4.137115672641978], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.158172157336903, -0.006887697575459862, 1.2286455919780816e-05, -6.5489391464297215e-09, 1.1738114261372569e-12, 30962.06476004715, -63.78765548494883], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-1.4658840835034903, 0.04032671174813905, -5.1677635604570834e-05, 3.3783985926401025e-08, -8.785375205100365e-12, 14582.289478420393, 4.137115672641978], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.158172157336903, -0.006887697575459862, 1.2286455919780816e-05, -6.5489391464297215e-09, 1.1738114261372569e-12, 11335.467999889066, -63.78765548494883], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-2.335993439055977, 0.04095493966544115, -3.308964605037999e-05, 1.2340872982475107e-08, -1.0794767857369436e-12, 13661.219544224989, 14.860345426691612], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.74976165361396, -0.015545093613927969, 2.7694717132704748e-05, -1.4747871407183279e-08, 2.63918260753589e-12, 8592.48091563806, -82.7716117653313], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-2.335993439055977, 0.04095493966544115, -3.308964605037999e-05, 1.2340872982475107e-08, -1.0794767857369436e-12, 2604.328496201661, 14.860345426691612], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.74976165361396, -0.015545093613927969, 2.7694717132704748e-05, -1.4747871407183279e-08, 2.63918260753589e-12, -2464.4101323852683, -82.7716117653313], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.138216103041777, 0.02823086411784676, -3.8437541152423604e-05, 2.6868203923619623e-08, -7.519328909522116e-12, -4832.459445754759, -5.622350233610955], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.261952078333145, -0.004316973382806578, 7.73409680281726e-06, -4.144915494278597e-09, 7.462540784972105e-13, -6972.659398929055, -50.91355633230831], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.138216103041777, 0.02823086411784676, -3.8437541152423604e-05, 2.6868203923619623e-08, -7.519328909522116e-12, -12438.174956686837, -5.622350233610955], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.261952078333145, -0.004316973382806578, 7.73409680281726e-06, -4.144915494278597e-09, 7.462540784972105e-13, -14578.374909861133, -50.91355633230831], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.3347812981984684, 0.024001926445212443, -2.56561658286328e-05, 1.4867686876108568e-08, -3.5296973677212407e-12, -19854.774902882287, -0.6581843781404473], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.997098052356328, -0.006795965625441362, 1.2045699322112889e-05, -6.359634936884278e-09, 1.1313346110218602e-12, -22310.809947795547, -49.545628505612484], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.3347812981984684, 0.024001926445212443, -2.56561658286328e-05, 1.4867686876108568e-08, -3.5296973677212407e-12, -27440.853958688134, -0.6581843781404473], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.997098052356328, -0.006795965625441362, 1.2045699322112889e-05, -6.359634936884278e-09, 1.1313346110218602e-12, -29896.889003601398, -49.545628505612484], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[3.3768902555000424, 0.01716828893718684, 1.0226321143136432e-05, -2.3112247575109005e-08, 9.75945366188391e-12, -41908.54783513986, -7.590723086367682], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.381509301194935, -0.01483893474211383, 2.65610658179714e-05, -1.4250112374202607e-08, 2.5651784197483225e-12, -46131.14868459556, -81.64682914395209], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[3.3768902555000424, 0.01716828893718684, 1.0226321143136432e-05, -2.3112247575109005e-08, 9.75945366188391e-12, -41133.19404880161, -7.590723086367682], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.381509301194935, -0.01483893474211383, 2.65610658179714e-05, -1.4250112374202607e-08, 2.5651784197483225e-12, -45355.79489825731, -81.64682914395209], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.4985974573272718, 0.032355190208176496, -2.1571861406286484e-05, 4.167224639668699e-09, 1.1892153928272364e-12, 21167.29453056535, -0.5266906827411653], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.60251185517201, -0.013353248368212221, 2.379894519605285e-05, -1.2680910283828348e-08, 2.2710678925289256e-12, 16789.660451069114, -83.39997325193697], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.4985974573272718, 0.032355190208176496, -2.1571861406286484e-05, 4.167224639668699e-09, 1.1892153928272364e-12, 5646.732437829192, -0.5266906827411653], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.60251185517201, -0.013353248368212221, 2.379894519605285e-05, -1.2680910283828348e-08, 2.2710678925289256e-12, 1269.0983583329544, -83.39997325193697], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.3860267526578358, 0.016641787893430366, -1.6919429844757538e-05, 9.530135630943216e-09, -2.1792567750367198e-12, 4228.465813422466, -0.7177355154818166], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.443721041372171, -0.005684040584492491, 1.0035186919117291e-05, -5.2677860777462666e-09, 9.321823589864562e-13, 2426.006109412351, -36.467259613747544], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.3860267526578358, 0.016641787893430366, -1.6919429844757538e-05, 9.530135630943216e-09, -2.1792567750367198e-12, 360.744533661613, -0.7177355154818166], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.443721041372171, -0.005684040584492491, 1.0035186919117291e-05, -5.2677860777462666e-09, 9.321823589864562e-13, -1441.7151703485024, -36.467259613747544], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.932904977014775, 0.025594396730344988, -2.9929209749898772e-05, 1.7922495652637445e-08, -4.312904200443057e-12, 21206.44354990204, -4.323578107980424], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.189909236154165, -0.004837276323957634, 8.704543634748917e-06, -4.700785411742493e-09, 8.512922744524252e-13, 18910.338994147285, -50.9038572152291], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.932904977014775, 0.025594396730344988, -2.9929209749898772e-05, 1.7922495652637445e-08, -4.312904200443057e-12, 9345.329866936081, -4.323578107980424], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.189909236154165, -0.004837276323957634, 8.704543634748917e-06, -4.700785411742493e-09, 8.512922744524252e-13, 7049.225311181326, -50.9038572152291], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.9093427832856398, 0.015109857567877763, -2.0359918968130758e-05, 1.4975405540619096e-08, -4.539493780875148e-12, -6469.204563180063, -3.1891958041489765], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.079628606140264, -0.002883577778149964, 5.257881761191409e-06, -2.8882247892031097e-09, 5.294853427979958e-13, -7729.927865073956, -29.032431347097084], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.9093427832856398, 0.015109857567877763, -2.0359918968130758e-05, 1.4975405540619096e-08, -4.539493780875148e-12, -14094.556529238374, -3.1891958041489765], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.079628606140264, -0.002883577778149964, 5.257881761191409e-06, -2.8882247892031097e-09, 5.294853427979958e-13, -15355.279831132268, -29.032431347097084], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.3537232216404795, 0.02738047612849207, -3.8612604745333626e-05, 2.9270129615313785e-08, -8.860745470684606e-12, 22778.48016638872, -2.856833924551207], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.50738886564937, -0.005965218577499618, 1.0615016854246257e-05, -5.630345050552874e-09, 1.0041366575849666e-12, 20640.59691632846, -48.18896116956779], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.3537232216404795, 0.02738047612849207, -3.8612604745333626e-05, 2.9270129615313785e-08, -8.860745470684606e-12, 15381.037526343393, -2.856833924551207], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.50738886564937, -0.005965218577499618, 1.0615016854246257e-05, -5.630345050552874e-09, 1.0041366575849666e-12, 13243.154276283136, -48.18896116956779], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-2.2710300707133886, 0.04275388669801405, -5.6165217605294374e-05, 3.8441904983893874e-08, -1.0600409439120995e-11, 28792.19488368034, 6.930604839386239], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.12906137260305, -0.007572217776039778, 1.360161547534432e-05, -7.320902085911084e-09, 1.3215775807826633e-12, 25355.84901398175, -64.82524264398151], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-2.2710300707133886, 0.04275388669801405, -5.6165217605294374e-05, 3.8441904983893874e-08, -1.0600409439120995e-11, 17676.394469382216, 6.930604839386239], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.12906137260305, -0.007572217776039778, 1.360161547534432e-05, -7.320902085911084e-09, 1.3215775807826633e-12, 14240.04859968363, -64.82524264398151], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.5280803860139417, 0.0285783252077775, -2.2234906966676733e-05, 7.78827990007637e-09, -5.933586955109149e-13, -14262.856314903354, 7.519427148206355], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.978155171283714, -0.010727812123524144, 1.9236820173513977e-05, -1.0341454007115124e-08, 1.8645498454938642e-12, -17899.080484683505, -61.77930156020717], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.5280803860139417, 0.0285783252077775, -2.2234906966676733e-05, 7.78827990007637e-09, -5.933586955109149e-13, -17573.900743549086, 7.519427148206355], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.978155171283714, -0.010727812123524144, 1.9236820173513977e-05, -1.0341454007115124e-08, 1.8645498454938642e-12, -21210.124913329237, -61.77930156020717], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.8619810025490673, 0.012267703380084078, -1.7731758155958465e-05, 1.315536840698411e-08, -3.9401086560086895e-12, -1403.047619485804, -9.289693099202832], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.60325861290425, -0.0013940190087381843, 2.573613909741894e-06, -1.436315753114337e-09, 2.6664821685648044e-13, -2275.351725211731, -27.812281404482913], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.8619810025490673, 0.012267703380084078, -1.7731758155958465e-05, 1.315536840698411e-08, -3.9401086560086895e-12, -5310.041809499121, -9.289693099202832], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.60325861290425, -0.0013940190087381843, 2.573613909741894e-06, -1.436315753114337e-09, 2.6664821685648044e-13, -6182.345915225048, -27.812281404482913], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[2.359495731431357, 0.026577899561492875, 4.854377666264913e-06, -2.3300751281310787e-08, 1.080241104900459e-11, -41555.37286781438, -2.7290965641338794], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[21.248882464739534, -0.01932093653813231, 3.441582389182342e-05, -1.8332031567445875e-08, 3.2816944758981732e-12, -47087.19357367442, -101.87030526237768], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[2.359495731431357, 0.026577899561492875, 4.854377666264913e-06, -2.3300751281310787e-08, 1.080241104900459e-11, -40740.74617301586, -2.7290965641338794], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[21.248882464739534, -0.01932093653813231, 3.441582389182342e-05, -1.8332031567445875e-08, 3.2816944758981732e-12, -46272.56687887589, -101.87030526237768], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.26079540729489786, 0.029660018341478807, -3.746238665500517e-05, 2.358568716943405e-08, -5.979147732482204e-12, -61661.39778150717, 4.317532672755526], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.046796775039754, -0.003516390240860414, 6.491780792346332e-06, -3.6335189500432592e-09, 6.76298154237971e-13, -64036.871654674294, -44.67323784193456], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.26079540729489786, 0.029660018341478807, -3.746238665500517e-05, 2.358568716943405e-08, -5.979147732482204e-12, -53179.4702824594, 4.317532672755526], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.046796775039754, -0.003516390240860414, 6.491780792346332e-06, -3.6335189500432592e-09, 6.76298154237971e-13, -55554.94415562652, -44.67323784193456], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.3891902594461783, 0.029211254914251555, -3.686302879714153e-05, 2.577719019942489e-08, -7.388346878745011e-12, -11453.579119358375, 3.258447821188735], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.099162358552885, -0.007408051053110082, 1.3248023640579377e-05, -7.084641349487045e-09, 1.2717661007009525e-12, -14074.147089352438, -50.37072313089001], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.3891902594461783, 0.029211254914251555, -3.686302879714153e-05, 2.577719019942489e-08, -7.388346878745011e-12, -14784.260001338145, 3.258447821188735], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.099162358552885, -0.007408051053110082, 1.3248023640579377e-05, -7.084641349487045e-09, 1.2717661007009525e-12, -17404.827971332208, -50.37072313089001], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.6898546774949579, 0.011560714377428666, -1.8172061719401493e-05, 1.4019483176817962e-08, -4.13411839483846e-12, -19391.987758912564, 2.129066713741218], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[3.9594002477034005, -0.0016598690893849198, 2.83126774534202e-06, -1.4039375937825617e-09, 2.3701080762369444e-13, -20070.722065137685, -13.688877268045676], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.6898546774949579, 0.011560714377428666, -1.8172061719401493e-05, 1.4019483176817962e-08, -4.13411839483846e-12, -15305.589545720775, 2.129066713741218], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[3.9594002477034005, -0.0016598690893849198, 2.83126774534202e-06, -1.4039375937825617e-09, 2.3701080762369444e-13, -15984.323851945896, -13.688877268045676], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.11893718001907885, 0.02541808705430347, -9.608108765723387e-06, -4.295199952049952e-09, 3.4643572732750982e-12, 2606.0113017834246, -0.7380722583744292], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.060757899352813, -0.014857615759044823, 2.6463057211542945e-05, -1.408810404432668e-08, 2.519977482300052e-12, -1584.578022034082, -78.21199707340558], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.11893718001907885, 0.02541808705430347, -9.608108765723387e-06, -4.295199952049952e-09, 3.4643572732750982e-12, -4732.521971987104, -0.7380722583744292], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.060757899352813, -0.014857615759044823, 2.6463057211542945e-05, -1.408810404432668e-08, 2.519977482300052e-12, -8923.11129580461, -78.21199707340558], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.4556863016454771, 0.02637115066174354, -2.1193123690587854e-05, 8.24653183318703e-09, -8.510588067611735e-13, 8833.128465453385, 6.940746767287202], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.091019819661316, -0.011033048767363404, 1.9484405869727385e-05, -1.0237438115629293e-08, 1.8128748895400622e-12, 5517.551286538819, -57.16805413486118], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.4556863016454771, 0.02637115066174354, -2.1193123690587854e-05, 8.24653183318703e-09, -8.510588067611735e-13, -2780.439438165553, 6.940746767287202], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.091019819661316, -0.011033048767363404, 1.9484405869727385e-05, -1.0237438115629293e-08, 1.8128748895400622e-12, -6096.016617080119, -57.16805413486118], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.9935294751058956, 0.019188084816283715, -2.42924974394525e-05, 1.547804984753989e-08, -3.9995055878261354e-12, -10642.654045860187, 1.4913827637688648], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.354995216279332, -0.002362726178059236, 4.3611695875785825e-06, -2.4396473219602613e-09, 4.538698078124497e-13, -12191.187418958521, -30.368866436801472], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.9935294751058956, 0.019188084816283715, -2.42924974394525e-05, 1.547804984753989e-08, -3.9995055878261354e-12, -10482.88647780795, 1.4913827637688648], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.354995216279332, -0.002362726178059236, 4.3611695875785825e-06, -2.4396473219602613e-09, 4.538698078124497e-13, -12031.419850906284, -30.368866436801472], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[2.7686539476068672, 0.015420898484374354, 5.767884406987405e-06, -1.5827045233451258e-08, 6.751805711746606e-12, -17830.974372370838, -5.059392156151771], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.847749730759535, -0.01335819566033185, 2.386893017993304e-05, -1.2769340121425279e-08, 2.2930531883285244e-12, -21426.880780808497, -68.67480546580957], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[2.7686539476068672, 0.015420898484374354, 5.767884406987405e-06, -1.5827045233451258e-08, 6.751805711746606e-12, -21122.382344994236, -5.059392156151771], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.847749730759535, -0.01335819566033185, 2.386893017993304e-05, -1.2769340121425279e-08, 2.2930531883285244e-12, -24718.288753431894, -68.67480546580957], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.331038987128432, 0.024146747684085316, -3.506375863681946e-05, 2.529019734254638e-08, -7.2690325980673265e-12, 27194.866443829233, -6.608669248279261], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.420686007412883, -0.002119684347932115, 3.923924112852273e-06, -2.199553140841385e-09, 4.098201473816919e-13, 25579.208261420055, -41.566088246820584], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.331038987128432, 0.024146747684085316, -3.506375863681946e-05, 2.529019734254638e-08, -7.2690325980673265e-12, 15314.116305737041, -6.608669248279261], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.420686007412883, -0.002119684347932115, 3.923924112852273e-06, -2.199553140841385e-09, 4.098201473816919e-13, 13698.458123327866, -41.566088246820584], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[2.4414185422025114, 0.020141843913278987, 1.004446940309389e-05, -2.4632473249166706e-08, 1.0643652625930144e-11, -19847.52031104623, -2.162546111921909], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[18.599268479100633, -0.01794421988237652, 3.1880937783277695e-05, -1.6915783501947735e-08, 3.0187083572847523e-12, -24645.34472658686, -87.2751835535458], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[2.4414185422025114, 0.020141843913278987, 1.004446940309389e-05, -2.4632473249166706e-08, 1.0643652625930144e-11, -23099.655375209375, -2.162546111921909], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[18.599268479100633, -0.01794421988237652, 3.1880937783277695e-05, -1.6915783501947735e-08, 3.0187083572847523e-12, -27897.479790750003, -87.2751835535458], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.8242951099574672, 0.02601749300527663, -3.764243998419181e-05, 2.8538878383309112e-08, -8.616187624488347e-12, 35544.964733412984, 0.7718232648179626], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.101373002612124, -0.004568081627199246, 8.155009679545203e-06, -4.344213509050772e-09, 7.779513439557439e-13, 33636.80278181841, -40.10485955343061], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.8242951099574672, 0.02601749300527663, -3.764243998419181e-05, 2.8538878383309112e-08, -8.616187624488347e-12, 15898.731519024766, 0.7718232648179626], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.101373002612124, -0.004568081627199246, 8.155009679545203e-06, -4.344213509050772e-09, 7.779513439557439e-13, 13990.569567430195, -40.10485955343061], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[2.230754474365933, 0.017783658337877685, -5.881534702396693e-06, -3.712415964603129e-09, 2.534902843187581e-12, 34181.37725018586, -3.1752208193723153], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.925748183648, -0.010525828837205065, 1.8814014384299243e-05, -1.006660382450365e-08, 1.8080350821928545e-12, 31143.19795005394, -58.79212788139595], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[2.230754474365933, 0.017783658337877685, -5.881534702396693e-06, -3.712415964603129e-09, 2.534902843187581e-12, 14574.416944257917, -3.1752208193723153], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.925748183648, -0.010525828837205065, 1.8814014384299243e-05, -1.006660382450365e-08, 1.8080350821928545e-12, 11536.23764412599, -58.79212788139595], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.638128311790396, 0.011236540999882609, 3.664844911067219e-06, -1.1120657164061452e-08, 4.8571719563073046e-12, -13009.163868131947, -2.018462765805568], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.252954055242327, -0.009480301245285542, 1.6901229048930064e-05, -9.011985872256507e-09, 1.6141330283557347e-12, -15556.256572315004, -47.321051295023864], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.638128311790396, 0.011236540999882609, 3.664844911067219e-06, -1.1120657164061452e-08, 4.8571719563073046e-12, -12601.850520732689, -2.018462765805568], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.252954055242327, -0.009480301245285542, 1.6901229048930064e-05, -9.011985872256507e-09, 1.6141330283557347e-12, -15148.943224915743, -47.321051295023864], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.09380422645656587, 0.03254184716882104, -1.9508073897544622e-05, 1.9033590070599593e-09, 2.0178511639379337e-12, -21414.790478337585, 5.477417787388822], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.823623671029893, -0.015032614497108913, 2.673269143470952e-05, -1.419836836264027e-08, 2.535846969827513e-12, -26036.74330569664, -81.69221157337572], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.09380422645656587, 0.03254184716882104, -1.9508073897544622e-05, 1.9033590070599593e-09, 2.0178511639379337e-12, -24686.561994938656, 5.477417787388822], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.823623671029893, -0.015032614497108913, 2.673269143470952e-05, -1.419836836264027e-08, 2.535846969827513e-12, -29308.514822297715, -81.69221157337572], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-3.0932804254633512, 0.04054757010622049, -5.061867190583267e-05, 3.338407760784367e-08, -8.850732646781267e-12, 15806.666396656985, 11.04447440181341], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.340397884578818, -0.0088565986454187, 1.5767249042201063e-05, -8.379519466619423e-09, 1.497433921245116e-12, 12317.698101433658, -61.114477479073585], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-3.0932804254633512, 0.04054757010622049, -5.061867190583267e-05, 3.338407760784367e-08, -8.850732646781267e-12, 4173.462037015715, 11.04447440181341], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.340397884578818, -0.0088565986454187, 1.5767249042201063e-05, -8.379519466619423e-09, 1.497433921245116e-12, 684.4937417923884, -61.114477479073585], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.8458767372850369, 0.029847037326815637, -1.6288060107211608e-05, -5.160668468083551e-10, 2.7107066591369744e-12, 20830.54180828037, -2.262003683764842], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.56413769242538, -0.01346431811154401, 2.3999175935712788e-05, -1.2790808184361166e-08, 2.2913064369846966e-12, 16491.44527016371, -83.4757358547679], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.8458767372850369, 0.029847037326815637, -1.6288060107211608e-05, -5.160668468083551e-10, 2.7107066591369744e-12, 5309.979715544206, -2.262003683764842], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.56413769242538, -0.01346431811154401, 2.3999175935712788e-05, -1.2790808184361166e-08, 2.2913064369846966e-12, 970.8831774275459, -83.4757358547679], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.8122506955542943, 0.02240816943062234, -2.560540942880489e-05, 1.573713386046396e-08, -3.913543100697581e-12, 33482.281062829876, -4.914017566653307], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.420923212444105, -0.005908523822900844, 1.0467898149707035e-05, -5.523251266533882e-09, 9.815551844217065e-13, 31343.595937923288, -48.23756065490732], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.8122506955542943, 0.02240816943062234, -2.560540942880489e-05, 1.573713386046396e-08, -3.913543100697581e-12, 17574.042076924587, -4.914017566653307], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.420923212444105, -0.005908523822900844, 1.0467898149707035e-05, -5.523251266533882e-09, 9.815551844217065e-13, 15435.356952017997, -48.23756065490732], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.3179838467359952, 0.03378081534288041, -1.4799606364101423e-05, -3.849161364955791e-09, 3.936379000535339e-12, -18698.129613729867, 3.571976723406868], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.33780951406004, -0.017434394968453903, 3.119767889977107e-05, -1.6722666366243355e-08, 3.0079833819606806e-12, -24038.723172640766, -95.0724895175665], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.3179838467359952, 0.03378081534288041, -1.4799606364101423e-05, -3.849161364955791e-09, 3.936379000535339e-12, -25688.258904583738, 3.571976723406868], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.33780951406004, -0.017434394968453903, 3.119767889977107e-05, -1.6722666366243355e-08, 3.0079833819606806e-12, -31028.852463494637, -95.0724895175665], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-4.872530990892688, 0.05562110739421251, -6.411740846381472e-05, 3.90946383572137e-08, -9.649864241012551e-12, 23353.074271043777, 18.42848547630861], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.033258703301918, -0.013087062152820088, 2.3459289825218143e-05, -1.259972074761509e-08, 2.27017642762139e-12, 18148.71822983493, -86.81233037475391], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-4.872530990892688, 0.05562110739421251, -6.411740846381472e-05, 3.90946383572137e-08, -9.649864241012551e-12, 12276.546766998123, 18.42848547630861], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.033258703301918, -0.013087062152820088, 2.3459289825218143e-05, -1.259972074761509e-08, 2.27017642762139e-12, 7072.190725789273, -86.81233037475391], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.8969967399970498, 0.03136537278382585, -3.453660942774956e-05, 1.938036117537774e-08, -4.250745588851856e-12, -74106.16156106902, -0.6822241363351544], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.83415680377455, -0.007126677188177576, 1.2639040075343967e-05, -6.681795799640911e-09, 1.1906517912991903e-12, -77095.25337215152, -60.909943049190474], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.8969967399970498, 0.03136537278382585, -3.453660942774956e-05, 1.938036117537774e-08, -4.250745588851856e-12, -65584.96115176879, -0.6822241363351544], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.83415680377455, -0.007126677188177576, 1.2639040075343967e-05, -6.681795799640911e-09, 1.1906517912991903e-12, -68574.05296285129, -60.909943049190474], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.25283229666286844, 0.02196083615973443, -2.9950780653634024e-05, 2.1358393509157084e-08, -6.125745743990052e-12, 31057.3642198225, -2.7225950490932895], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.479256089403834, -0.003801893741304097, 6.806689659541158e-06, -3.6435473720240567e-09, 6.55030932313473e-13, 29354.145158243646, -38.61818128245971], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.25283229666286844, 0.02196083615973443, -2.9950780653634024e-05, 2.1358393509157084e-08, -6.125745743990052e-12, 15129.488778790983, -2.7225950490932895], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.479256089403834, -0.003801893741304097, 6.806689659541158e-06, -3.6435473720240567e-09, 6.55030932313473e-13, 13426.269717212133, -38.61818128245971], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.6497117249237597, 0.03554659990718607, -4.4142697799558037e-05, 2.93903593051855e-08, -8.001765916532122e-12, -19939.475992720465, 1.807676305525411], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.113681847679658, -0.007676997669985588, 1.3787877482188212e-05, -7.421194660802826e-09, 1.3394167722781966e-12, -23066.61058358512, -62.165190770593796], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.6497117249237597, 0.03554659990718607, -4.4142697799558037e-05, 2.93903593051855e-08, -8.001765916532122e-12, -23270.156874700235, 1.807676305525411], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.113681847679658, -0.007676997669985588, 1.3787877482188212e-05, -7.421194660802826e-09, 1.3394167722781966e-12, -26397.29146556489, -62.165190770593796], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.41436465043911636, 0.029786625133376217, -2.426107781057743e-05, 8.221441058744636e-09, -2.817850119907206e-13, -16730.052506572538, 7.219061486102157], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.025013580421547, -0.009793659831366196, 1.7460964722192518e-05, -9.310410292910685e-09, 1.6689305407764036e-12, -20293.816038624907, -61.54133917364577], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.41436465043911636, 0.029786625133376217, -2.426107781057743e-05, 8.221441058744636e-09, -2.817850119907206e-13, -20041.096935218273, 7.219061486102157], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.025013580421547, -0.009793659831366196, 1.7460964722192518e-05, -9.310410292910685e-09, 1.6689305407764036e-12, -23604.860467270642, -61.54133917364577], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.010038189100148368, 0.027915951531930515, -3.7008074488711533e-05, 2.570289914908294e-08, -7.117882672158515e-12, 2089.004792198144, -1.4839360217744142], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.46433498705958, -0.005614607763985756, 9.924580262988197e-06, -5.215372068440793e-09, 9.23919913422026e-13, -143.09969930520128, -48.57071566492603], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.010038189100148368, 0.027915951531930515, -3.7008074488711533e-05, 2.570289914908294e-08, -7.117882672158515e-12, -1778.7164875627082, -1.4839360217744142], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.46433498705958, -0.005614607763985756, 9.924580262988197e-06, -5.215372068440793e-09, 9.23919913422026e-13, -4010.820979066053, -48.57071566492603], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-3.4051441867506744, 0.047724289490958145, -6.43559924429585e-05, 4.449797963339486e-08, -1.2296011431267573e-11, 26293.997497168948, 11.83631806740635], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.134869945412417, -0.0075269187342327185, 1.3520541327636236e-05, -7.277197774712797e-09, 1.3138262992731103e-12, 22642.56969332182, -65.34142221287271], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-3.4051441867506744, 0.047724289490958145, -6.43559924429585e-05, 4.449797963339486e-08, -1.2296011431267573e-11, 15178.197082870829, 11.83631806740635], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.134869945412417, -0.0075269187342327185, 1.3520541327636236e-05, -7.277197774712797e-09, 1.3138262992731103e-12, 11526.7692790237, -65.34142221287271], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-1.3776098886368788, 0.03725658652985835, -5.301683192936591e-05, 3.855549170243632e-08, -1.1193462823300138e-11, -16131.238918801138, 3.9622718582434455], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.198849403954185, -0.005117172932029725, 9.263940504945724e-06, -5.038401040839732e-09, 9.169576549613017e-13, -18804.686868385317, -53.26801022581537], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-1.3776098886368788, 0.03725658652985835, -5.301683192936591e-05, 3.855549170243632e-08, -1.1193462823300138e-11, -19481.556255907137, 3.9622718582434455], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.198849403954185, -0.005117172932029725, 9.263940504945724e-06, -5.038401040839732e-09, 9.169576549613017e-13, -22155.004205491314, -53.26801022581537], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[2.923562143240646, 0.010682159200923623, -1.2508195264134207e-05, 8.481349940250621e-09, -2.4795755726447766e-12, 18172.594095451204, -2.176705532413184], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.086216049969408, -0.0028051611886139994, 5.098960366822314e-06, -2.7909116737181186e-09, 5.101968931763034e-13, 17104.659416833718, -23.237580035600725], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[2.923562143240646, 0.010682159200923623, -1.2508195264134207e-05, 8.481349940250621e-09, -2.4795755726447766e-12, 6291.843957359014, -2.176705532413184], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.086216049969408, -0.0028051611886139994, 5.098960366822314e-06, -2.7909116737181186e-09, 5.101968931763034e-13, 5223.909278741525, -23.237580035600725], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-4.002408677490918, 0.05221889029432998, -5.891216152170422e-05, 3.5103548702661736e-08, -8.419341612775355e-12, 15044.412847751943, 15.082182270412012], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.9486679253505, -0.012883729841375003, 2.302832738699371e-05, -1.2316759623532165e-08, 2.2120213375841774e-12, 10059.954501340277, -85.45366806841204], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-4.002408677490918, 0.05221889029432998, -5.891216152170422e-05, 3.5103548702661736e-08, -8.419341612775355e-12, 3967.8853437062844, 15.082182270412012], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.9486679253505, -0.012883729841375003, 2.302832738699371e-05, -1.2316759623532165e-08, 2.2120213375841774e-12, -1016.5730027053796, -85.45366806841204], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-3.2454263842040563, 0.045740712834499, -5.206788394779641e-05, 3.1011581474928596e-08, -7.431173731919927e-12, 20416.843310595334, 14.227506587622653], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.973737140881015, -0.010520315933265804, 1.8851700221785156e-05, -1.0120427938433633e-08, 1.8231167545404697e-12, 16120.477035580614, -72.51992728662742], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-3.2454263842040563, 0.045740712834499, -5.206788394779641e-05, 3.1011581474928596e-08, -7.431173731919927e-12, 9320.679350527347, 14.227506587622653], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.973737140881015, -0.010520315933265804, 1.8851700221785156e-05, -1.0120427938433633e-08, 1.8231167545404697e-12, 5024.313075512629, -72.51992728662742], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.300412672194553, 0.036196155908658725, -4.2884290614632455e-05, 2.714169514084154e-08, -6.9348485287612505e-12, -10493.784244084001, 5.483638123808867], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.191116478633521, -0.00886431129373155, 1.5729147271793533e-05, -8.318780340166752e-09, 1.4811271173832512e-12, -13810.96868150243, -62.242630748054566], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.300412672194553, 0.036196155908658725, -4.2884290614632455e-05, 2.714169514084154e-08, -6.9348485287612505e-12, -13804.828672729736, 5.483638123808867], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.191116478633521, -0.00886431129373155, 1.5729147271793533e-05, -8.318780340166752e-09, 1.4811271173832512e-12, -17122.013110148167, -62.242630748054566], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.3590540257949546, 0.02501724558325153, -3.0958732097422e-05, 2.0028686967558853e-08, -5.265201469262237e-12, -51173.14693725486, 3.52733979234295], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.1626551705247, -0.004701472115306819, 8.43556603182292e-06, -4.533668267548416e-09, 8.179721904287085e-13, -53324.86786561512, -40.59755552516822], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.3590540257949546, 0.02501724558325153, -3.0958732097422e-05, 2.0028686967558853e-08, -5.265201469262237e-12, -46738.344741146415, 3.52733979234295], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.1626551705247, -0.004701472115306819, 8.43556603182292e-06, -4.533668267548416e-09, 8.179721904287085e-13, -48890.06566950667, -40.59755552516822], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.26696039959774404, 0.025658708019581325, -3.6746089354556215e-05, 2.652568290254523e-08, -7.56687767999864e-12, 5577.636761212806, -0.5999011793376585], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.589736849916923, -0.0034428159868778517, 6.1541249150112485e-06, -3.2864385949829006e-09, 5.898563049065437e-13, 3793.3136691395684, -39.32243587207851], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.26696039959774404, 0.025658708019581325, -3.6746089354556215e-05, 2.652568290254523e-08, -7.56687767999864e-12, 1690.2790263257211, -0.5999011793376585], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.589736849916923, -0.0034428159868778517, 6.1541249150112485e-06, -3.2864385949829006e-09, 5.898563049065437e-13, -94.04406574751556, -39.32243587207851], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-3.484480061504159, 0.049611889732151956, -4.654198224495474e-05, 2.2377925953709398e-08, -4.031094902323673e-12, 19059.41222674367, 13.750530599079733], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.886825386143485, -0.015838525349654065, 2.8325178735322635e-05, -1.5167316715817698e-08, 2.7260964210844285e-12, 13492.466395940059, -95.0345997749903], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-3.484480061504159, 0.049611889732151956, -4.654198224495474e-05, 2.2377925953709398e-08, -4.031094902323673e-12, 8002.521178720344, 13.750530599079733], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.886825386143485, -0.015838525349654065, 2.8325178735322635e-05, -1.5167316715817698e-08, 2.7260964210844285e-12, 2435.5753479167342, -95.0345997749903], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-4.026345852130678, 0.050330824582074225, -5.385881175406401e-05, 3.034074169321413e-08, -6.849180944623612e-12, 15991.25612537314, 15.773763750300732], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.89638211689794, -0.01326625399305861, 2.3747362731478014e-05, -1.2730778062976612e-08, 2.2905149321293325e-12, 10938.283379094026, -84.98132493424458], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-4.026345852130678, 0.050330824582074225, -5.385881175406401e-05, 3.034074169321413e-08, -6.849180944623612e-12, 4914.728621327482, 15.773763750300732], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.89638211689794, -0.01326625399305861, 2.3747362731478014e-05, -1.2730778062976612e-08, 2.2905149321293325e-12, -138.24412495163233, -84.98132493424458], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.40376886767600445, 0.03434773773851405, -1.589336246930892e-05, -2.4397393198112853e-09, 3.409550419775087e-12, 9127.394461753105, -2.8137786594112715], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.778567406809294, -0.018507705596035758, 3.304254534572872e-05, -1.7651525659642544e-08, 3.1660737399852312e-12, 3719.99023913129, -103.13119150373578], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.40376886767600445, 0.03434773773851405, -1.589336246930892e-05, -2.4397393198112853e-09, 3.409550419775087e-12, -1909.8601338322842, -2.8137786594112715], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.778567406809294, -0.018507705596035758, 3.304254534572872e-05, -1.7651525659642544e-08, 3.1660737399852312e-12, -7317.2643564540995, -103.13119150373578], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[2.7297147696519386, 0.008710513433113376, -1.2913175453546773e-05, 1.0729495025872316e-08, -3.3943334254438184e-12, -30573.923109300955, -6.044799612763292], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.854969755224983, -0.0032884838154521837, 5.569914961149535e-06, -2.7300853163986106e-09, 4.558987651233143e-13, -31265.860961369017, -21.351875463188136], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[2.7297147696519386, 0.008710513433113376, -1.2913175453546773e-05, 1.0729495025872316e-08, -3.3943334254438184e-12, -26467.888441879033, -6.044799612763292], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.854969755224983, -0.0032884838154521837, 5.569914961149535e-06, -2.7300853163986106e-09, 4.558987651233143e-13, -27159.826293947095, -21.351875463188136], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.3087966439268551, 0.023227065095417408, -3.556983029780869e-05, 2.775356125764918e-08, -8.585455263387942e-12, 40036.873972901936, 2.811366711504294], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.115613052476612, -0.0028051889306885385, 5.132717569782909e-06, -2.8290128457275187e-09, 5.200085899533489e-13, 38503.21937671721, -30.609649770950455], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.3087966439268551, 0.023227065095417408, -3.556983029780869e-05, 2.775356125764918e-08, -8.585455263387942e-12, 20371.004302491383, 2.811366711504294], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.115613052476612, -0.0028051889306885385, 5.132717569782909e-06, -2.8290128457275187e-09, 5.200085899533489e-13, 18837.34970630665, -30.609649770950455], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-1.4742019619819957, 0.042144995536667125, -5.019755499211274e-05, 3.192281341306676e-08, -8.249907701429748e-12, 24619.544109124883, 6.3646605945007675], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.113333075018854, -0.009852181996058411, 1.760958052368724e-05, -9.414965035147297e-09, 1.690377726709007e-12, 20774.606859645908, -71.922418943132], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-1.4742019619819957, 0.042144995536667125, -5.019755499211274e-05, 3.192281341306676e-08, -8.249907701429748e-12, 13523.380149056893, 6.3646605945007675], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.113333075018854, -0.009852181996058411, 1.760958052368724e-05, -9.414965035147297e-09, 1.690377726709007e-12, 9678.442899577916, -71.922418943132], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.5193148349166338, 0.023734401542306514, -2.1291541552457206e-05, 9.945549656770349e-09, -1.7005320762653042e-12, 10037.24936615564, 7.353465918619756], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.145639013678018, -0.008751777752192158, 1.5480383746770106e-05, -8.152097424369403e-09, 1.4464151515511565e-12, 7253.0990564562, -46.971396464133335], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.5193148349166338, 0.023734401542306514, -2.1291541552457206e-05, 9.945549656770349e-09, -1.7005320762653042e-12, -1595.954993485631, 7.353465918619756], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.145639013678018, -0.008751777752192158, 1.5480383746770106e-05, -8.152097424369403e-09, 1.4464151515511565e-12, -4380.1053031850715, -46.971396464133335], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.0741274556154028, 0.022965576621378495, -1.2260547570099876e-05, -1.2460321254102096e-09, 2.540360283243004e-12, -37025.82161356864, 1.029548333678978], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.048629858122181, -0.009848436466281987, 1.7567229443068718e-05, -9.375556766452995e-09, 1.6816185962709e-12, -40331.78031231293, -60.86273230058802], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.0741274556154028, 0.022965576621378495, -1.2260547570099876e-05, -1.2460321254102096e-09, 2.540360283243004e-12, -32551.746507207732, 1.029548333678978], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.048629858122181, -0.009848436466281987, 1.7567229443068718e-05, -9.375556766452995e-09, 1.6816185962709e-12, -35857.70520595202, -60.86273230058802], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-4.808912278042515, 0.05371459353605084, -6.677816098958233e-05, 4.3278250548889796e-08, -1.1302327129758538e-11, 24576.165046188362, 17.84935288787215], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.066244577410863, -0.010480168414818717, 1.881927352100178e-05, -1.0130741835721841e-08, 1.8288358396851678e-12, 19991.926498239227, -76.61936010724799], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-4.808912278042515, 0.05371459353605084, -6.677816098958233e-05, 4.3278250548889796e-08, -1.1302327129758538e-11, 13480.001086120372, 17.84935288787215], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.066244577410863, -0.010480168414818717, 1.881927352100178e-05, -1.0130741835721841e-08, 1.8288358396851678e-12, 8895.762538171237, -76.61936010724799], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[3.388779213631883, 0.014850706410940143, -1.8053000059341232e-05, 1.2700296345620905e-08, -3.7160309551698134e-12, 1500.6859894454872, -8.571580661198478], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.154633162229366, -0.004498769503700408, 8.014673958761491e-06, -4.261303331914661e-09, 7.615166703060956e-13, 65.23571975608138, -37.550570154064005], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[3.388779213631883, 0.014850706410940143, -1.8053000059341232e-05, 1.2700296345620905e-08, -3.7160309551698134e-12, -6105.029521486593, -8.571580661198478], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.154633162229366, -0.004498769503700408, 8.014673958761491e-06, -4.261303331914661e-09, 7.615166703060956e-13, -7540.479791175999, -37.550570154064005], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.3738267893184363, 0.02339769200062538, -1.9573560022432125e-05, 7.627197853066382e-09, -7.421147030228781e-13, -21697.64834288419, 6.579102040857689], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.314149933698543, -0.008568719429804302, 1.5185530659546744e-05, -8.022793154085987e-09, 1.4272203295633218e-12, -24510.1521660751, -47.98962958885656], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.3738267893184363, 0.02339769200062538, -1.9573560022432125e-05, 7.627197853066382e-09, -7.421147030228781e-13, -21290.334995484925, 6.579102040857689], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.314149933698543, -0.008568719429804302, 1.5185530659546744e-05, -8.022793154085987e-09, 1.4272203295633218e-12, -24102.838818675835, -47.98962958885656], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-4.541835805809122, 0.05160727391403616, -6.99488944443476e-05, 4.8515824081931226e-08, -1.345649286443873e-11, 30906.13201862977, 16.518000967056917], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.143041715945822, -0.007834179492609282, 1.4122672211551237e-05, -7.640534691801569e-09, 1.3848751382857308e-12, 26988.941741119575, -66.32293547709035], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-4.541835805809122, 0.05160727391403616, -6.99488944443476e-05, 4.8515824081931226e-08, -1.345649286443873e-11, 19790.331604331644, 16.518000967056917], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.143041715945822, -0.007834179492609282, 1.4122672211551237e-05, -7.640534691801569e-09, 1.3848751382857308e-12, 15873.141326821455, -66.32293547709035], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.6073983748266721, 0.024113459272879424, -3.6226375705033655e-05, 2.7097576274857764e-08, -7.934382317831279e-12, 2094.804079024217, -4.173499030987074], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.644644146453326, -0.0029201102305442955, 5.16968190751061e-06, -2.718904777923171e-09, 4.8236485420246e-13, 546.4280170498196, -38.614889737699016], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.6073983748266721, 0.024113459272879424, -3.6226375705033655e-05, 2.7097576274857764e-08, -7.934382317831279e-12, -1792.5536558628692, -4.173499030987074], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.644644146453326, -0.0029201102305442955, 5.16968190751061e-06, -2.718904777923171e-09, 4.8236485420246e-13, -3340.9297178372663, -38.614889737699016], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-1.0343560218929917, 0.02954889213174962, -3.7388956403900184e-05, 2.5054277182663535e-08, -6.773304139784386e-12, 13866.164044362864, 2.7569531883392795], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.38499187571051, -0.0062701685659363425, 1.1163513168188612e-05, -5.931883768833952e-09, 1.0601000397067635e-12, 11352.049373548884, -49.30415707094812], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-1.0343560218929917, 0.02954889213174962, -3.7388956403900184e-05, 2.5054277182663535e-08, -6.773304139784386e-12, 2213.3232304914636, 2.7569531883392795], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.38499187571051, -0.0062701685659363425, 1.1163513168188612e-05, -5.931883768833952e-09, 1.0601000397067635e-12, -300.7914403225168, -49.30415707094812], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.4078333893607506, 0.03381796177566529, -1.8236476569497745e-05, -2.1781846529770775e-10, 2.782378494270432e-12, 2840.1353655936186, 3.0339536257089286], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.695307434024926, -0.01618740727690008, 2.8912158147894964e-05, -1.5456094995757705e-08, 2.774248536517414e-12, -2165.3373798080065, -90.50560326972989], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.4078333893607506, 0.03381796177566529, -1.8236476569497745e-05, -2.1781846529770775e-10, 2.782378494270432e-12, -8216.755682429706, 3.0339536257089286], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.695307434024926, -0.01618740727690008, 2.8912158147894964e-05, -1.5456094995757705e-08, 2.774248536517414e-12, -13222.228427831331, -90.50560326972989], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-1.0434374026493032, 0.017236903600525225, -3.068695772385649e-05, 2.538824345082357e-08, -8.015095531721528e-12, 16440.993568933594, 3.0546208304970115], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.8710250803063295, -0.000459583897810385, 8.695024882748882e-07, -4.943281589731255e-10, 9.304088132376496e-14, 15704.970384275422, -15.466780891576455], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-1.0434374026493032, 0.017236903600525225, -3.068695772385649e-05, 2.538824345082357e-08, -8.015095531721528e-12, 8467.237621750824, 3.0546208304970115], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.8710250803063295, -0.000459583897810385, 8.695024882748882e-07, -4.943281589731255e-10, 9.304088132376496e-14, 7731.214437092653, -15.466780891576455], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.044452913308908576, 0.019436759636543545, -1.9102857378165163e-05, 1.1126926094899282e-08, -2.737358950621882e-12, 638.4123148595478, -0.1733858789314926], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.657045298440448, -0.007903077857146142, 1.4010043902444632e-05, -7.4001607786229035e-09, 1.3151659242308404e-12, -1609.5341668382298, -44.33525482701773], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.044452913308908576, 0.019436759636543545, -1.9102857378165163e-05, 1.1126926094899282e-08, -2.737358950621882e-12, -3021.0360967028473, -0.1733858789314926], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.657045298440448, -0.007903077857146142, 1.4010043902444632e-05, -7.4001607786229035e-09, 1.3151659242308404e-12, -5268.982578400625, -44.33525482701773], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.763419916108498, 0.021946448969719, -2.103316059025525e-05, 1.0462346509861043e-08, -2.00841426822862e-12, 14981.528924365435, -2.2565505771061716], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.110541682510993, -0.006805474008018404, 1.2093550174710639e-05, -6.412294549468917e-09, 1.1443172374703573e-12, 12556.24568886904, -49.79891523032214], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.763419916108498, 0.021946448969719, -2.103316059025525e-05, 1.0462346509861043e-08, -2.00841426822862e-12, 3140.0516965257093, -2.2565505771061716], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.110541682510993, -0.006805474008018404, 1.2093550174710639e-05, -6.412294549468917e-09, 1.1443172374703573e-12, 714.7684610293145, -49.79891523032214], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-2.075699468841116, 0.017358077343272296, -2.609206412898108e-05, 1.8928216959216332e-08, -5.388359897162687e-12, -2323.7182606359897, 8.153606339477767], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.7224745129276777, -0.0010681624758273717, 1.9865280608509053e-06, -1.120480196821236e-09, 2.0981090637377155e-13, -3375.7629344968427, -15.320705237248276], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-2.075699468841116, 0.017358077343272296, -2.609206412898108e-05, 1.8928216959216332e-08, -5.388359897162687e-12, -2304.0818055097575, 8.153606339477767], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.7224745129276777, -0.0010681624758273717, 1.9865280608509053e-06, -1.120480196821236e-09, 2.0981090637377155e-13, -3356.1264793706105, -15.320705237248276], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.9423372093417675, 0.02493487343959535, -2.7919420506031866e-05, 1.5719571712970995e-08, -3.4902289391958163e-12, 15021.688328007882, -4.565914187237134], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.170222985061477, -0.004832591811848306, 8.689196070678313e-06, -4.688316791083182e-09, 8.486224638721293e-13, 12708.86483117323, -51.128817254636154], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.9423372093417675, 0.02493487343959535, -2.7919420506031866e-05, 1.5719571712970995e-08, -3.4902289391958163e-12, 3160.5746450419224, -4.565914187237134], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.170222985061477, -0.004832591811848306, 8.689196070678313e-06, -4.688316791083182e-09, 8.486224638721293e-13, 847.7511482072714, -51.128817254636154], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.48229906536793415, 0.02587155127531559, -3.9360365788694726e-05, 3.0462959888373194e-08, -9.365327957588931e-12, -10453.536217874123, -3.573773358707397], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.0708325244702, -0.0030085351441184282, 5.5154130366392516e-06, -3.0480644218682132e-09, 5.614704876502467e-13, -12168.22302052486, -40.86266658834928], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.48229906536793415, 0.02587155127531559, -3.9360365788694726e-05, 3.0462959888373194e-08, -9.365327957588931e-12, -13823.490010106358, -3.573773358707397], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.0708325244702, -0.0030085351441184282, 5.5154130366392516e-06, -3.0480644218682132e-09, 5.614704876502467e-13, -15538.176812757094, -40.86266658834928], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-3.0278046479993272, 0.04868277469861659, -4.646973264049378e-05, 2.2875158469816263e-08, -4.2387759968676164e-12, 8509.694212930355, 11.50704836401261], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.77877011492434, -0.015532217068462958, 2.7689854090790898e-05, -1.4757543334478308e-08, 2.6427560802981618e-12, 3122.622125425396, -94.26062897519923], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-3.0278046479993272, 0.04868277469861659, -4.646973264049378e-05, 2.2875158469816263e-08, -4.2387759968676164e-12, -2547.1968350929696, 11.50704836401261], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.77877011492434, -0.015532217068462958, 2.7689854090790898e-05, -1.4757543334478308e-08, 2.6427560802981618e-12, -7934.268922597928, -94.26062897519923], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-2.7556935991113143, 0.02931258322046972, -4.843786135235457e-05, 3.8446894497971926e-08, -1.1723805953822719e-11, 10926.887071939307, 10.096496473865535], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.828393274330211, -0.0024595949286131567, 4.346762608100847e-06, -2.2753101158881143e-09, 4.018659752232502e-13, 9389.431387209892, -26.3700032711956], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-2.7556935991113143, 0.02931258322046972, -4.843786135235457e-05, 3.8446894497971926e-08, -1.1723805953822719e-11, 2972.767578986667, 10.096496473865535], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.828393274330211, -0.0024595949286131567, 4.346762608100847e-06, -2.2753101158881143e-09, 4.018659752232502e-13, 1435.3118942572528, -26.3700032711956], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[4.177331860342677, -0.0012986530515051672, 2.5984608392459963e-06, -9.710009093628354e-10, -9.263358309585801e-14, 16492.955863944906, -7.8361280056985745], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.407824912386021, -0.0015051356127564913, 2.6825671580396526e-06, -1.4261829223683117e-09, 2.5443162032394223e-13, 16382.051115496746, -9.19892716405165], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[4.177331860342677, -0.0012986530515051672, 2.5984608392459963e-06, -9.710009093628354e-10, -9.263358309585801e-14, 545.4439677871569, -7.8361280056985745], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.407824912386021, -0.0015051356127564913, 2.6825671580396526e-06, -1.4261829223683117e-09, 2.5443162032394223e-13, 434.5392193389989, -9.19892716405165], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.685978627729595, 0.025296468804795018, -3.4398724583518516e-05, 2.4726462848270053e-08, -7.1681376112575634e-12, 35990.20721240954, -8.130952558650874], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.122123532985963, -0.004680413880020813, 8.377743678764652e-06, -4.483216274102132e-09, 8.058110283909199e-13, 33991.31094813005, -50.07405596097429], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.685978627729595, 0.025296468804795018, -3.4398724583518516e-05, 2.4726462848270053e-08, -7.1681376112575634e-12, 16343.973998021329, -8.130952558650874], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.122123532985963, -0.004680413880020813, 8.377743678764652e-06, -4.483216274102132e-09, 8.058110283909199e-13, 14345.077733741839, -50.07405596097429], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-3.1209839650654505, 0.03948489337397223, -5.467134560713659e-05, 3.872997294685073e-08, -1.0891107460331284e-11, 11641.153464683952, 11.198399654770991], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.50733559911769, -0.0062944615865850465, 1.1259999982182603e-05, -6.0234545814607654e-09, 1.0820098750351573e-12, 8719.129599344305, -51.2967294712286], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-3.1209839650654505, 0.03948489337397223, -5.467134560713659e-05, 3.872997294685073e-08, -1.0891107460331284e-11, 4243.710824638626, 11.198399654770991], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.50733559911769, -0.0062944615865850465, 1.1259999982182603e-05, -6.0234545814607654e-09, 1.0820098750351573e-12, 1321.6869592989788, -51.2967294712286], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.14003259781996247, 0.03586162976285301, -1.11021364991019e-05, -8.973999424710427e-09, 5.916364620439651e-12, 4714.51641935622, -0.9771971470803091], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[21.506545750084097, -0.021538701603008723, 3.84134172767583e-05, -2.049047834779493e-08, 3.67104278562163e-12, -1408.8967398356435, -113.46375175738402], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.14003259781996247, 0.03586162976285301, -1.11021364991019e-05, -8.973999424710427e-09, 5.916364620439651e-12, -6303.101720206838, -0.9771971470803091], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[21.506545750084097, -0.021538701603008723, 3.84134172767583e-05, -2.049047834779493e-08, 3.67104278562163e-12, -12426.5148793987, -113.46375175738402], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.5930036410580237, 0.03571236960277976, -2.8891917695947535e-05, 1.0353989429743649e-08, -6.877484692857649e-13, 22798.662435238835, 4.071108868409096], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.859740958863316, -0.012892229650732454, 2.2989923173715027e-05, -1.2260637510722244e-08, 2.1968922551084385e-12, 18430.999095757044, -80.0996968777047], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.5930036410580237, 0.03571236960277976, -2.8891917695947535e-05, 1.0353989429743649e-08, -6.877484692857649e-13, 11722.134931193179, 4.071108868409096], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.859740958863316, -0.012892229650732454, 2.2989923173715027e-05, -1.2260637510722244e-08, 2.1968922551084385e-12, 7354.47159171139, -80.0996968777047], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-1.0485328055132175, 0.028672112331914735, -3.4822695375238e-05, 2.2596349194893594e-08, -5.960530680138021e-12, 19060.913802576368, 2.5065656904453557], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.414361625368064, -0.006532492926442659, 1.1674964208927885e-05, -6.240271609019632e-09, 1.1201413670854261e-12, 16494.12293101877, -49.97073415880129], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-1.0485328055132175, 0.028672112331914735, -3.4822695375238e-05, 2.2596349194893594e-08, -5.960530680138021e-12, 7408.072988704966, 2.5065656904453557], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.414361625368064, -0.006532492926442659, 1.1674964208927885e-05, -6.240271609019632e-09, 1.1201413670854261e-12, 4841.282117147368, -49.97073415880129], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.3828187309797452, 0.031836903255905415, -4.013910077551464e-05, 2.761968717216655e-08, -7.788499012395533e-12, 26549.87455451591, 5.759655127568052], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.118039767476288, -0.0074059749629245735, 1.3261664190103652e-05, -7.105185250480473e-09, 1.2776281650071471e-12, 23738.19284711666, -51.83453946208235], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.3828187309797452, 0.031836903255905415, -4.013910077551464e-05, 2.761968717216655e-08, -7.788499012395533e-12, 15434.074140217788, 5.759655127568052], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.118039767476288, -0.0074059749629245735, 1.3261664190103652e-05, -7.105185250480473e-09, 1.2776281650071471e-12, 12622.392432818539, -51.83453946208235], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.7048343312416007, 0.028376201417515148, -3.7864509437051594e-05, 2.6544109758791067e-08, -7.541790109089064e-12, 47943.8927454966, -4.371824159907967], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.196869682854762, -0.004925420385461617, 8.881818762142402e-06, -4.805481378877049e-09, 8.710592807486574e-13, 45675.386802089975, -51.66537239982247], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.7048343312416007, 0.028376201417515148, -3.7864509437051594e-05, 2.6544109758791067e-08, -7.541790109089064e-12, 36808.45587696835, -4.371824159907967], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.196869682854762, -0.004925420385461617, 8.881818762142402e-06, -4.805481378877049e-09, 8.710592807486574e-13, 34539.94993356172, -51.66537239982247], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-1.236169616951722, 0.0391192964347373, -3.594452974308101e-05, 1.7078239755369327e-08, -3.0713001586413213e-12, 11355.677547885423, 3.5450552454458464], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.907361423361152, -0.013048576275606832, 2.3318786109779613e-05, -1.2471542891601062e-08, 2.239508305499705e-12, 6866.928214038797, -83.81982158180084], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-1.236169616951722, 0.0391192964347373, -3.594452974308101e-05, 1.7078239755369327e-08, -3.0713001586413213e-12, 279.1500438397686, 3.5450552454458464], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.907361423361152, -0.013048576275606832, 2.3318786109779613e-05, -1.2471542891601062e-08, 2.239508305499705e-12, -4209.599290006858, -83.81982158180084], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-1.0128277676926316, 0.039605453245976766, -2.4179579834566663e-05, 3.2356519006891704e-09, 1.993148701640024e-12, 8381.652433206516, 3.3418135904896475], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.5941142062787, -0.018498140954926762, 3.29579995577773e-05, -1.7553526856730535e-08, 3.1414002936479626e-12, 2748.292133192299, -102.82843075468661], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-1.0128277676926316, 0.039605453245976766, -2.4179579834566663e-05, 3.2356519006891704e-09, 1.993148701640024e-12, -2655.602162378872, 3.3418135904896475], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.5941142062787, -0.018498140954926762, 3.29579995577773e-05, -1.7553526856730535e-08, 3.1414002936479626e-12, -8288.96246239309, -102.82843075468661], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[0.2631703605638592, 0.02672958182700725, -2.8237311149280387e-05, 1.6164539099028483e-08, -3.69835412294961e-12, 30810.88729291626, -2.446254248524509], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.199486664560553, -0.008342041650362158, 1.4711414998931697e-05, -7.709954680296734e-09, 1.3627206815362359e-12, 28050.549162134375, -57.70149463482577], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[0.2631703605638592, 0.02672958182700725, -2.8237311149280387e-05, 1.6164539099028483e-08, -3.69835412294961e-12, 14922.284761241115, -2.446254248524509], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.199486664560553, -0.008342041650362158, 1.4711414998931697e-05, -7.709954680296734e-09, 1.3627206815362359e-12, 12161.94663045923, -57.70149463482577], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-1.2597947854333764, 0.042911061194315925, -6.112561275165806e-05, 4.481050517474996e-08, -1.3045467484040785e-11, 35251.33061496488, 3.5252823923395966], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.261909294145994, -0.006846950029475659, 1.2247928231585094e-05, -6.547805246035505e-09, 1.1756090977137418e-12, 32146.147441712375, -63.24393195054921], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-1.2597947854333764, 0.042911061194315925, -6.112561275165806e-05, 4.481050517474996e-08, -1.3045467484040785e-11, 24135.530200666755, 3.5252823923395966], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.261909294145994, -0.006846950029475659, 1.2247928231585094e-05, -6.547805246035505e-09, 1.1756090977137418e-12, 21030.347027414253, -63.24393195054921], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[1.600791364726406, 0.014704845247362895, -1.4669740619650143e-05, 6.819304873825679e-09, -1.1479810158032677e-12, -10898.73150121152, -0.766296623165708], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.295792299031667, -0.0025855513420097, 4.764106999098455e-06, -2.6619189543733584e-09, 4.947908487145042e-13, -12384.73176293381, -29.782781634319207], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[1.600791364726406, 0.014704845247362895, -1.4669740619650143e-05, 6.819304873825679e-09, -1.1479810158032677e-12, -10738.963933159283, -0.766296623165708], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.295792299031667, -0.0025855513420097, 4.764106999098455e-06, -2.6619189543733584e-09, 4.947908487145042e-13, -12224.964194881573, -29.782781634319207], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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
<<<<<<< HEAD
            NASAPolynomial(coeffs=[-0.6781890175202328, 0.03266563196550605, -3.482124141809595e-05, 1.9201333508215776e-08, -4.230282790729234e-12, -12090.58165056297, 1.4808105805832952], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.110986738337399, -0.007888949731124329, 1.419017817690404e-05, -7.661299725244604e-09, 1.3863367885039082e-12, -15347.27203058694, -63.26475767863039], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
=======
            NASAPolynomial(coeffs=[-0.6781890175202328, 0.03266563196550605, -3.482124141809595e-05, 1.9201333508215776e-08, -4.230282790729234e-12, -15421.26253254274, 1.4808105805832952], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.110986738337399, -0.007888949731124329, 1.419017817690404e-05, -7.661299725244604e-09, 1.3863367885039082e-12, -18677.95291256671, -63.26475767863039], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
>>>>>>> 5768489a (updated new workflow data)
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

