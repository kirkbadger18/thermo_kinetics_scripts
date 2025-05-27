#!/usr/bin/env python
# encoding: utf-8


name = "SurfaceThermoPt111"
shortDesc = u"Surface adsorbates on Pt(111)"
longDesc = u"""
Surface species adsorbed on Pt(111). The thermochemistry of all adsorbates with up to 2 heavy atoms was calculated by Katrin Blondal at Brown University around 2018,
based on DFT calculations by Jelena Jelic at KIT. See https://doi.org/10.1021/acs.iecr.9b01464 for the details on the computational methods as well as the results.
This database was extended with DFT calculations for larger adsorbates by Bjarne Kreitz (Brown University).  
The computational methods for the extension are explained in detail in https://doi.org/10.1021/acscatal.2c03378. If you use this database in your work, please cite the publications mentioned above. 
Note: X indicates a bond to the surface. It is always on the left hand site of an atom that is bonded to the surface e.g. XCCH2 it means that C is bonded to the surface.
If the X is on the right hand side and at the end of a label, it means that this species is physisorbed. 
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
    label = "XH",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
       polynomials = [
            NASAPolynomial(coeffs=[
             -2.07570125, 0.0173580835, -2.60920784e-05, 1.89282268e-08,
             -5.38835643e-12, -3105.8617724107235, 8.15361518], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             2.72248139, -0.00106817206, 1.9865379e-06, -1.12048461e-09,
             2.09811636e-13, -4157.911142410723, -15.320747], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -2.481 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 3,
    label = "H2X",
    molecule =
"""
1 X  u0 p0 c0
2 H  u0 p0 c0 {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
    	polynomials = [
            NASAPolynomial(coeffs=[
             3.86406413, 0.000753456449, -1.65571442e-06, 1.55223217e-09,
             -4.4678226e-13, -2054.52717008486, -8.85806531], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             4.06879652, -0.000495806734, 6.59234335e-07, -1.72597715e-10,
             7.62965383e-15, -2065.9524700848597, -9.71917749], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -0.051 eV.

            The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 4,
    label = "H2OX",
    molecule =
"""
1 X  u0 p0 c0
2 O  u0 p2 c0 {3,S} {4,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             2.72971388, 0.00871051652, -1.29131826e-05, 1.07295e-08,
             -3.39433689e-12, -32577.161731862157, -6.04479516], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             5.8549628, -0.00328847412, 5.56990501e-06, -2.73008086e-09,
             4.55898028e-13, -33269.09633186215, -21.3518349], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.189 eV.

                The two lowest frequencies, 12.0 and 62.1 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 5,
    label = "XOH",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             0.689854677, 0.0115607144, -1.81720617e-05, 1.40194832e-08,
             -4.13411839e-12, -18941.233822425897, 2.12906671], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             3.95940025, -0.00165986909, 2.83126775e-06, -1.40393759e-09,
             2.37010808e-13, -19619.968122425897, -13.6888773], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2.

                Updated by Matt and Kirk --> DFT binding energy: -1.763 eV
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 6,
    label = "HOOHX",
    molecule =
"""
1 X  u0 p0 c0
2 O  u0 p2 c0 {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             2.96560716, 0.0133978369, -1.34293557e-05, 7.12175948e-09,
             -1.41063029e-12, -25607.588033902848, -6.15466087], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             8.63537655, -0.00464148419, 8.09255957e-06, -4.16762137e-09,
             7.26386983e-13, -27036.72683390285, -34.8128042], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.285 eV.

                The two lowest frequencies, 12.0 and 47.7 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 7,
    label = "XOXO",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 O  u0 p2 c0 {1,S} {4,S}
4 O  u0 p2 c0 {2,S} {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             0.967032554, 0.0201073426, -3.43087565e-05, 2.75767553e-08,
             -8.53056861e-12, -12895.454696330484, -5.63546035], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             5.80193269, -0.000729910156, 1.37020436e-06, -7.76162799e-10,
             1.45741297e-13, -13851.747896330484, -28.7540997], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.232 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 8,
    label = "XOOH",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             2.72534279, 0.0142651752, -2.21410322e-05, 1.71597713e-08,
             -5.14814406e-12, -15274.233013319516, -5.88006622], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             6.85340011, -0.00206281219, 3.57770248e-06, -1.82187965e-09,
             3.14702407e-13, -16158.364713319514, -25.9655505], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -1.205 eV.

                The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 9,
    label = "XO",
    molecule =
"""
1 X  u0 p0 c0 {2,D}
2 O  u0 p2 c0 {1,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -0.294475701, 0.0144162624, -2.61322704e-05, 2.19005957e-08,
             -6.9801942e-12, -15287.427955192037, -0.199445623], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             2.90244691, -0.000338584457, 6.43372619e-07, -3.6632666e-10,
             6.90093884e-14, -15875.251655192038, -15.2559728], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -4.101 eV.
    """,
    metal="Pt",
    facet="111",
)

#entry(
#    index = 10,
#    label = "XONH2",
#    molecule =
#"""
#1 X  u0 p0 c0 {3,S}
#2 N  u0 p1 c0 {3,S} {4,S} {5,S}
#3 O  u0 p2 c0 {1,S} {2,S}
#4 H  u0 p0 c0 {2,S}
#5 H  u0 p0 c0 {2,S}
#""",
#    thermo = NASA(
#        polynomials = [
#            NASAPolynomial(coeffs=[2.40658689E+00, 1.61838708E-02, -1.58074626E-05, 8.48925729E-09, -1.83038307E-12, -8.83680682E+03, -7.56970401E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
#            NASAPolynomial(coeffs=[9.42636683E+00, -5.74378741E-03, 1.01435819E-05, -5.32742710E-09, 9.43135142E-13, -1.06436383E+04, -4.31963080E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
#        ],
#        Tmin = (298.0, 'K'),
#        Tmax = (2000.0, 'K'),
#    ),
#    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
#            Based on DFT calculations by Jelena Jelic at KIT.
#            DFT binding energy: -0.698 eV.
#            Linear scaling parameters: ref_adatom_O = -3.586 eV, psi = 1.09537 eV, gamma_O(X) = 0.500.""",
#    metal = "Pt",
#    facet = "111",
#)

entry(
    index = 11,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             1.63812716, 0.011236545, 3.66483568e-06, -1.11206508e-08,
             4.85717369e-12, -18698.914298960564, -2.01845704], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             10.2529575, -0.00948030603, 1.6901234e-05, -9.01198807e-09,
             1.61413339e-12, -21246.009498960564, -47.3210723], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -1.800 eV.

                The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 12,
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
            NASAPolynomial(coeffs=[
             1.56327589, 0.0142661984, -1.29739542e-05, 7.2687839e-09,
             -1.69074657e-12, -13165.84814929925, -4.45259196], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             8.41707953, -0.00711106769, 1.2402771e-05, -6.38806523e-09,
             1.11283978e-12, -14936.43214929925, -39.2567003], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.723 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 13,
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
            NASAPolynomial(coeffs=[
             -1.87792693, 0.0283563105, -4.27751406e-05, 3.27407761e-08,
             -9.75815262e-12, -1994.2466598462447, 6.32923187], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             6.66921838, -0.00466299714, 8.16399248e-06, -4.22273875e-09,
             7.38391582e-13, -3869.8792598462446, -35.4655795], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.888 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 14,
    label = "XNH",
    molecule =
"""
1 X  u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -2.75570044, 0.0293126058, -4.84378942e-05, 3.84469118e-08,
             -1.17238091e-11, 1096.9492367653297, 10.09653], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             4.82838736, -0.00245958668, 4.34675415e-06, -2.27530633e-09,
             4.01865349e-13, -440.5054692346703, -26.3699701], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -3.283 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 15,
    label = "XN",
    molecule =
"""
1 X  u0 p0 c0 {2,T}
2 N  u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             -1.04344143, 0.0172369169, -3.0686977e-05, 2.53882536e-08,
             -8.01509647e-12, 6467.761476449115, 3.05464056], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             2.87102348, -0.000459581662, 8.69500195e-07, -4.94327131e-10,
             9.30407113e-14, 5731.7378564491155, -15.4667725], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -4.259 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 16,
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
            NASAPolynomial(coeffs=[
             1.37992771, 0.0177510484, -1.20850096e-05, 2.53914859e-09,
             6.810061e-13, -14539.809535909944, -0.282754632], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             10.2493987, -0.00793851746, 1.39420012e-05, -7.26519181e-09,
             1.27843053e-12, -16908.567635909945, -45.7560718], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.716 eV.

            The two lowest frequencies, 21.4 and 69.7 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 17,
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
            NASAPolynomial(coeffs=[
             1.29355054, 0.0125511912, -1.30542429e-05, 7.66161218e-09,
             -1.92155255e-12, -6690.269890637305, -0.238965324], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             6.51681954, -0.00383955255, 6.87833355e-06, -3.68900437e-09,
             6.63962241e-13, -8041.8080106373045, -26.7584137], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.217 eV.

            The two lowest frequencies, 38.5 and 75.1 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 18,
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
            NASAPolynomial(coeffs=[
             -0.0100447037, 0.027915973, -3.70081058e-05, 2.57029157e-08,
             -7.11788328e-12, -9437.854855154848, -1.48390407], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.46433421, -0.00561460668, 9.92457916e-06, -5.21537158e-09,
             9.23919834e-13, -11669.961055154849, -48.5707128], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.279 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 19,
    label = "XNO",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 O  u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             1.86197814, 0.0122677128, -1.77317719e-05, 1.31553757e-08,
             -3.94011021e-12, -11825.430361429946, -9.28967905], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             5.6032557, -0.00139401495, 2.57360975e-06, -1.43631389e-09,
             2.66647908e-13, -12697.733761429947, -27.8122649], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.494 eV.
""",
    metal = "Pt",
    facet = "111",
)

#entry(
#    index = 20,
#    label = "XNXO",
#    molecule =
#"""
#1 X  u0 p0 c0 {3,D}
#2 X  u0 p0 c0 {4,S}
#3 N  u0 p1 c0 {1,D} {4,S}
#4 O  u0 p2 c0 {2,S} {3,S}
#""",
#    thermo = NASA(
#        polynomials = [
#            NASAPolynomial(coeffs=[2.01597450E+00, 1.16417245E-02, -1.66451395E-05, #1.22700017E-08, -3.66343934E-12, -1.45871732E+04, -9.85062942E+00], Tmin=(298.0, 'K'), #Tmax=(1000.0, 'K')),
#            NASAPolynomial(coeffs=[5.60950909E+00, -1.37182073E-03, 2.53200598E-06, #-1.41282013E-09, 2.62247587E-13, -1.54307490E+04, -2.76693956E+01], Tmin=(1000.0, 'K'), #Tmax=(2000.0, 'K')),
#        ],
#        Tmin = (298.0,'K'),
#        Tmax = (2000.0,'K'),
#    ),
#    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics #(file: ThermoPt111.py).
#            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations #were performed with Quantum Espresso
#            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 #supercell (1/9ML coverage)
#            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). #The following settings were applied:
#            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-#vanderbilt', mixing_mode='local-TF',
#            fmax=2.5e-2.
#""",
#    metal = "Pt",
#    facet = "111",
#)



entry(
    index = 21,
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
            NASAPolynomial(coeffs=[
             0.607392748, 0.0241134778, -3.62264027e-05, 2.70975905e-08,
             -7.93438333e-12, -8629.85630662427, -4.17347143], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             7.64464251, -0.00292010795, 5.16967957e-06, -2.71890373e-09,
             4.82364682e-13, -10178.233306624268, -38.6148816], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -3.172 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 22,
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
            NASAPolynomial(coeffs=[
             0.880903991, 0.0183200664, -5.85331987e-06, -4.76198976e-09,
             3.30072549e-12, -1581.5602288431628, 1.69887512], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             11.8627109, -0.0112030919, 1.97216353e-05, -1.03149694e-08,
             1.82010147e-12, -4642.4032688431635, -55.2039293], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.082 eV.

            The two lowest frequencies, 12.0 and 78.7 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

#entry(
#    index = 23,
#    label = "NHNHX",
#    molecule =
#"""
#1 X  u0 p0 c0
#2 N  u0 p1 c0 {3,D} {4,S}
#3 N  u0 p1 c0 {2,D} {5,S}
#4 H  u0 p0 c0 {2,S}
#5 H  u0 p0 c0 {3,S}
#""",
#    thermo = NASA(
#        polynomials = [
#            NASAPolynomial(coeffs=[6.28467971E-01, 2.12301596E-02, -2.12507892E-05, #1.09499539E-08, -2.14994342E-12, 9.47120803E+03, -3.87189726E+00], Tmin=(298.0, 'K'), #Tmax=(1000.0, 'K')),
#            NASAPolynomial(coeffs=[9.39084917E+00, -6.21655586E-03, 1.10453064E-05, #-5.85660437E-09, 1.04485360E-12, 7.22949955E+03, -4.82981277E+01], Tmin=(1000.0, 'K'), #Tmax=(2000.0, 'K')),
#        ],
#        Tmin = (298.0,'K'),
#        Tmax = (2000.0,'K'),
#    ),
#    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics #(file: ThermoPt111.py).
#            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations #were performed with Quantum Espresso
#            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 #supercell (1/9ML coverage)
#            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). #The following settings were applied:
#            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-#vanderbilt', mixing_mode='local-TF',
#            fmax=2.5e-2.
#""",
#    metal = "Pt",
#    facet = "111",
#)


entry(
    index = 24,
    label = "NNX",
    molecule =
"""
1 X  u0 p0 c0 
2 N  u0 p1 c0 {3,T}
3 N  u0 p1 c0 {2,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             4.17733216, -0.00129865405, 2.59846229e-06, -9.71001677e-10,
             -9.2633758e-14, -4585.750858477321, -7.83612949], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             4.40782454, -0.0015051351, 2.68256663e-06, -1.42618269e-09,
             2.54431581e-13, -4696.655308477321, -9.19892489], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.110 eV.

            The two lowest frequencies, 12.0 and 9.9 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 25,
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
            NASAPolynomial(coeffs=[
             0.263164123, 0.0267296024, -2.82373411e-05, 1.61645549e-08,
             -3.69835405e-12, 7590.1250262548, -2.44622365], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             11.1994872, -0.00834204243, 1.47114158e-05, -7.70995505e-09,
             1.36272074e-12, 4829.7845762548, -57.7014996], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.214 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 26,
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
            NASAPolynomial(coeffs=[
             1.13128416, 0.01840288, -2.42779025e-05, 1.72243668e-08,
             -4.97078538e-12, 12111.511997525155, -5.77950056], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             7.49413519, -0.00379724488, 6.797286e-06, -3.63818104e-09,
             6.53847754e-13, 10581.037557525155, -37.5219634], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.964 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 27,
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
            NASAPolynomial(coeffs=[
             0.556437046, 0.0248819034, -3.18839077e-05, 2.19076353e-08,
             -6.06237354e-12, 7225.48496552709, -4.09637251], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.38092848, -0.0057193651, 1.00978887e-05, -5.29677042e-09,
             9.37012803e-13, 5108.91978552709, -48.1251409], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -2.006 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 28,
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
            NASAPolynomial(coeffs=[
             0.812245466, 0.0224081867, -2.56054345e-05, 1.57371471e-08,
             -3.91354553e-12, 11466.851539647565, -4.91399191], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.42091871, -0.00590851754, 1.04678917e-05, -5.52324839e-09,
             9.8155471e-13, 9328.167159647564, -48.2375354], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.776 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 29,
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
            NASAPolynomial(coeffs=[
             0.252827172, 0.0219608531, -2.99508053e-05, 2.13584065e-08,
             -6.12574428e-12, 9641.219661592993, -2.72256992], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             7.47925936, -0.0038018983, 6.80669434e-06, -3.64354947e-09,
             6.55031279e-13, 7937.997181592993, -38.618202], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.201 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 30,
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
            NASAPolynomial(coeffs=[
             0.587222135, 0.0218842706, -9.0921218e-06, -3.20129649e-09,
             2.93456143e-12, -3626.9617993055767, -3.09771386], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             13.0834738, -0.0119829848, 2.13029335e-05, -1.13098079e-08,
             2.01902125e-12, -7111.034979305576, -67.8173122], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.773 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 31,
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
            NASAPolynomial(coeffs=[
             0.687362498, 0.0213234859, -2.33604236e-05, 1.4597562e-08,
             -3.85095498e-12, 4320.943669190958, -4.10743889], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.37461488, -0.00660654156, 1.17973587e-05, -6.29736292e-09,
             1.12896272e-12, 2107.191929190958, -48.0457206], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.566 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 32,
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
            NASAPolynomial(coeffs=[
             0.498737658, 0.0205752033, -1.26878072e-05, 2.05802186e-09,
             8.0524938e-13, -3494.506813781617, -3.11635206], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             11.2229107, -0.00961282244, 1.71594913e-05, -9.16352374e-09,
             1.64334916e-12, -6436.0000237816175, -58.4009481], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -2.963 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 33,
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
            NASAPolynomial(coeffs=[
             1.60078793, 0.0147048566, -1.46697571e-05, 6.81931357e-09,
             -1.14798228e-12, -22708.40753376162, -0.76627979], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             7.29579, -0.00258554813, 4.76410371e-06, -2.66191748e-09,
             4.94790605e-13, -24194.40763376162, -29.7827689], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.050 eV.

            The two lowest frequencies, 31.4 and 43.4 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 34,
    label = "XC",
    molecule =
"""
1 X  u0 p0 c0 {2,Q}
2 C  u0 p0 c0 {1,Q}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -1.94350915, 0.0197767398, -3.36336641e-05, 2.69027201e-08,
             -8.27959229e-12, 6299.836927375625, 7.17469909], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             2.81347137, -0.000693951702, 1.30307929e-06, -7.38700347e-10,
             1.38795827e-13, 5359.298547375625, -15.5738286], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -7.665 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 35,
    label = "XCXC",
    molecule =
"""
1 X  u0  p0 c0 {3,D}
2 X  u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,D} {4,D}
4 C  u0  p0 c0 {2,D} {3,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             0.257614736, 0.0193811681, -2.99692178e-05, 2.27772298e-08,
             -6.82679954e-12, 23785.54030386604, -2.70419665], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             5.60814537, -0.00142377339, 2.64198198e-06, -1.48289867e-09,
             2.76540004e-13, 22611.444603866043, -28.8541367], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -6.388 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 36,
    label = "XCCH2",
    molecule =
"""
1 X  u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 C  u0  p0 c0 {2,D} {4,S} {5,S}
4 H  u0  p0 c0 {3,S}
5 H  u0  p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             0.353720415, 0.0273804858, -3.86126272e-05, 2.92701452e-08,
             -8.86074894e-12, 12110.32937379429, -2.85681996], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.50738185, -0.0059652088, 1.06150068e-05, -5.63034056e-09,
             1.00413592e-12, 9972.44837379429, -48.1889215], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.610 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 37,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             0.498832282, 0.0220312098, -1.63022134e-05, 5.40142239e-09,
             -2.95003605e-13, -11870.574977900125, -0.341231804], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             11.3080922, -0.00936315902, 1.67090264e-05, -8.9184054e-09,
             1.59869331e-12, -14785.179577900124, -55.8203537], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -6.087 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 38,
    label = "XCH",
    molecule =
"""
1 X  u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -2.66805027, 0.0290693485, -4.82653552e-05, 3.87589256e-08,
             -1.19749384e-11, -3239.5602592323257, 9.72941427], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             4.90429859, -0.00263865042, 4.71729273e-06, -2.51267002e-09,
             4.49659283e-13, -4785.8129692323255, -26.7107945], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -4.820 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 39,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -3.12098801, 0.0394849074, -5.4671378e-05, 3.87299954e-08,
             -1.08911005e-11, 123.54599665196753, 11.1984198], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.50734934, -0.00629448074, 1.12600196e-05, -6.02346339e-09,
             1.08201133e-12, -2798.4875343480326, -51.2968133], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -1.907 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 40,
    label = "CHCHX",
    molecule =
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,T} {4,S}
3 C  u0 p0 c0 {2,T} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             0.472394638, 0.0277615066, -4.4882533e-05, 3.68137777e-08,
             -1.16132416e-11, 19453.606197095556, 2.41179267], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             8.5322849, -0.0049378126, 8.6408175e-06, -4.46203746e-09,
             7.78651886e-13, 17742.833697095557, -36.6656813], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.160 eV.

                The two lowest frequencies, 12.0 and 90.3 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 41,
    label = "XCH2",
    molecule =
"""
1 X  u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -2.23006757, 0.0292222928, -4.33154923e-05, 3.31428193e-08,
             -9.96471308e-12, -170.2483509940434, 8.30173205], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             6.83459954, -0.00514926339, 9.15491022e-06, -4.84917377e-09,
             8.63766547e-13, -2206.969204994043, -36.2215373], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -4.305 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 42,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -2.6719234, 0.0380645196, -3.8243629e-05, 2.04023322e-08,
             -4.28929114e-12, -8202.93532173625, 10.5040932], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             13.228995, -0.0118706595, 2.11521655e-05, -1.1264162e-08,
             2.0156694e-12, -12279.230801736248, -70.1190196], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.927 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 43,
    label = "XCH3",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -0.044454906, 0.0194367665, -1.91028733e-05, 1.11269371e-08,
             -2.73735895e-12, -6065.066751372315, -0.173375969], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             8.65704524, -0.00790307778, 1.40100438e-05, -7.40016074e-09,
             1.31516592e-12, -8313.014301372315, -44.3352558], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -1.721 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 44,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             2.21371476, 0.0122146805, 1.90686655e-05, -2.86454335e-08,
             1.10578994e-11, -15844.252926975574, -3.32732546], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             15.8691357, -0.0176783249, 3.14415254e-05, -1.67061667e-08,
             2.98335715e-12, -20047.366026975575, -75.9101763], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.192 eV.

                The two lowest frequencies, 12.0 and 77.2 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 45,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             4.85496247, -0.00554134984, 3.01198105e-05, -2.99225917e-08,
             1.00502514e-11, -12136.836535261617, -9.25620913], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.54139378, -0.0104025134, 1.837774e-05, -9.6676513e-09,
             1.71211379e-12, -13874.770135261617, -35.5638434], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.125 eV.

                The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 46,
    label = "XCN",
    molecule =
"""
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,T}
3 N  u0  p1 c0 {2,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             3.76715019, 0.00417953363, -5.16460774e-06, 4.28173958e-09,
             -1.53270699e-12, 7568.127978148837, -16.4486651], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             5.52234227, -0.00148724278, 2.71154695e-06, -1.48804637e-09,
             2.72508607e-13, 7102.342578148837, -25.3724453], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -3.283 eV.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 47,
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
            NASAPolynomial(coeffs=[
             2.05736559, 0.0187855246, -2.93807183e-05, 2.35018796e-08,
             -7.34023377e-12, -1479.9220414896874, -10.4215334], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             7.60952099, -0.00298591387, 5.27829656e-06, -2.7673937e-09,
             4.89307754e-13, -2697.9531414896874, -37.5334941], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.691 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 48,
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
            NASAPolynomial(coeffs=[
             1.58467103, 0.021387566, -2.66801735e-05, 1.80859993e-08,
             -4.95468285e-12, -9555.590621042857, -8.56646952], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.40654432, -0.00539963874, 9.4909414e-06, -4.94450145e-09,
             8.7003446e-13, -11448.218121042857, -47.6757545], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: 13.415 eV.
""",
    metal = "Pt",
    facet = "111",
)





entry(
    index = 49,
    label = "XCO",
    molecule =
"""
1 X  u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 O  u0  p2 c0 {2,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             1.42895, 0.0140374509, -2.2117892e-05, 1.78659581e-08,
             -5.71478802e-12, -34657.94213327415, -7.78265517], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             5.48656312, -0.00168118543, 3.0903031e-06, -1.71186643e-09,
             3.15864598e-13, -35570.643233274146, -27.6788365], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -1.415 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 50,
    label = "XCOH",
    molecule =
"""
1 X  u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             0.281392618, 0.0236060988, -3.32958929e-05, 2.35937581e-08,
             -6.59988036e-12, -30796.947827481705, -2.84937962], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             7.57277703, -0.00316578469, 5.61811938e-06, -2.96831946e-09,
             5.2868399e-13, -32458.921327481705, -38.8297167], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -4.708 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 51,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -4.49841757, 0.0474505397, -6.33178372e-05, 4.41445511e-08,
             -1.23100766e-11, -2865.6002845487246, 16.9502146], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             11.4364336, -0.00900409564, 1.60927814e-05, -8.59946878e-09,
             1.54310894e-12, -6627.972104548725, -62.2564682], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -3.339 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 52,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             0.118934574, 0.0254180961, -9.60812964e-06, -4.29518553e-09,
             3.46436421e-12, -10700.018818931054, -0.738059313], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             15.0607717, -0.014857635, 2.64630769e-05, -1.40881129e-08,
             2.51997894e-12, -14890.617018931054, -78.2120803], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.301 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 53,
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
            NASAPolynomial(coeffs=[
             0.339064957, 0.01798479, -8.0099974e-06, -2.61848735e-09,
             2.58905539e-12, 4341.318158232632, 4.13906217], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             10.2640967, -0.00902467036, 1.60300783e-05, -8.50179159e-09,
             1.51671257e-12, 1592.952685232632, -47.2020184], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.229 eV.

            The two lowest frequencies, 57.5 and 70.1 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)



entry(
    index = 54,
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
            NASAPolynomial(coeffs=[
             -0.455692456, 0.026371171, -2.11931532e-05, 8.24654743e-09,
             -8.51058332e-13, -8857.482837234114, 6.94077695], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             12.0910212, -0.0110330507, 1.94844078e-05, -1.0237439e-08,
             1.81287504e-12, -12173.062737234113, -57.1680638], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.957 eV.

            The two lowest frequencies, 12.0 and 76.8 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)





entry(
    index = 55,
    label = "CH2OX",
    molecule =
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 O  u0 p2 c0 {2,D}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             4.152111, -0.000548713399, 1.6858931e-05, -1.83357871e-08,
             6.29630397e-12, -21514.97802178987, -11.442038], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             8.40512532, -0.00690216938, 1.2352155e-05, -6.6236299e-09,
             1.19136449e-12, -22996.05702178987, -34.8417937], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.161 eV.

                The two lowest frequencies, 12.0 and 51.8 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 56,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -0.373829188, 0.0233977003, -1.95735792e-05, 7.62721113e-09,
             -7.42114703e-13, -29130.69770812689, 6.57911397], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             10.3141499, -0.00856871933, 1.51855306e-05, -8.02279311e-09,
             1.42722033e-12, -31943.20280812689, -47.9896307], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.347 eV.

                The two lowest frequencies, 25.3 and 72.1 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 57,
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
            NASAPolynomial(coeffs=[
             -1.0485395, 0.0286721344, -3.48227275e-05, 2.25963662e-08,
             -5.96053451e-12, 4005.811895465142, 2.50659852], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.41435444, -0.0065324829, 1.16749539e-05, -6.24026701e-09,
             1.12014061e-12, 1439.0227464651418, -49.9706934], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.601 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 58,
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
            NASAPolynomial(coeffs=[
             -3.09328989, 0.0405476013, -5.06187173e-05, 3.33841016e-08,
             -8.8507376e-12, -483.4123880397601, 11.0445208], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             11.3403886, -0.00885658573, 1.57672358e-05, -8.37951354e-09,
             1.49743294e-12, -3972.37873803976, -61.1144252], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.721 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 59,
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
            NASAPolynomial(coeffs=[
             0.928890847, 0.0163186384, 6.61270744e-06, -1.79028395e-08,
             7.84820353e-12, -14329.901520407999, 1.69399491], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             13.7744179, -0.014595527, 2.58477964e-05, -1.36465988e-08,
             2.42551222e-12, -18109.564020408, -65.8062154], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.926 eV.

            The two lowest frequencies, 12.0 and 96.0 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 60,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             3.05737703, 0.0128624334, 4.84927639e-06, -1.35997111e-08,
             5.96900307e-12, -31221.71989659225, -12.4359019], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             13.1134924, -0.0114087964, 2.0203011e-05, -1.06647877e-08,
             1.89545946e-12, -34179.15409659225, -65.2666455], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.304 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 61,
    label = "XCHXC",
    molecule =
"""
1 X  u0  p0 c0 {3,S}
2 X  u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,S} {4,D} {5,S}
4 C  u0  p0 c0 {2,D} {3,D}
5 H  u0  p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -0.590352229, 0.028202941, -4.31920779e-05, 3.32067162e-08,
             -1.00161719e-11, 13784.101233923386, 0.224767212], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             7.59299131, -0.00351002045, 6.29100233e-06, -3.36852902e-09,
             6.05610928e-13, 11982.333033923387, -39.7960433], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -4.559 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 62,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -0.308859296, 0.0283916975, -3.01517554e-05, 1.77197656e-08,
             -4.2759303e-12, 2487.5203511243785, 1.02855689], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             11.3486298, -0.00890556058, 1.58461696e-05, -8.4175655e-09,
             1.50324475e-12, -475.4836388756212, -57.9325796], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.860 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 63,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -1.02964656, 0.0305643757, -2.57333903e-05, 1.12938139e-08,
             -1.82181353e-12, -5709.374571702699, 2.66178101], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             13.2389405, -0.0120662335, 2.15309174e-05, -1.14893042e-08,
             2.05901892e-12, -9497.813241702699, -70.2795064], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -3.834 eV.
    """,
    metal="Pt",
    facet="111",
)

#entry(
#    index = 64,
#    label = "HCNX",
#    molecule =
#"""
#1 X  u0  p0 c0
#2 C  u0  p0 c0 {3,T} {4,S}
#3 N  u0  p1 c0 {2,T}
#4 H  u0  p0 c0 {2,S}
#""",
#    thermo = NASA(
#        polynomials = [
#            NASAPolynomial(coeffs=[2.53721411E+00, 1.54381672E-02, -2.30464671E-05, 1.84850825E-08, -5.85209659E-12, 8.88848734E+03, -1.05654655E+01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
#            NASAPolynomial(coeffs=[7.54725616E+00, -3.42528202E-03, 6.08981805E-06, -3.22389145E-09, 5.73999322E-13, 7.74009913E+03, -3.52485026E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
#        ],
#        Tmin = (298.0,'K'),
#        Tmax = (2000.0,'K'),
#    ),
#    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
#            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
#            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
#            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
#            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
#            fmax=2.5e-2.
#""",
#    metal = "Pt",
#    facet = "111",
#)



entry(
    index = 65,
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
            NASAPolynomial(coeffs=[
             0.153325541, 0.0231297046, -3.28959339e-05, 2.44114282e-08,
             -7.24366068e-12, 4789.195408971899, -1.78965726], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             7.53708641, -0.00385776053, 6.93478093e-06, -3.73304473e-09,
             6.73801673e-13, 3074.887918971899, -38.3206373], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.614 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 66,
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
            NASAPolynomial(coeffs=[
             -0.296223695, 0.021861836, -2.3841642e-05, 1.40957825e-08,
             -3.38822779e-12, 1049.8003863641493, 6.2072095], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             8.41293505, -0.0062344343, 1.10893362e-05, -5.88758257e-09,
             1.05127072e-12, -1146.9410196358508, -37.7714995], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -2.162 eV.

            The two lowest frequencies, 35.5 and 72.6 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 67,
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
            NASAPolynomial(coeffs=[
             -1.03436292, 0.0295489149, -3.73889895e-05, 2.50542947e-08,
             -6.77330492e-12, -1686.5566080838116, 2.75698701], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.38499077, -0.00627016703, 1.11635116e-05, -5.93188307e-09,
             1.06009992e-12, -4200.672908083811, -49.3041524], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -2.435 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 68,
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
            NASAPolynomial(coeffs=[
             -0.519320374, 0.0237344198, -2.12915681e-05, 9.94556369e-09,
             -1.70053514e-12, -6796.9841689658215, 7.35349309], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             10.1456333, -0.00875176973, 1.54803755e-05, -8.15209375e-09,
             1.44641454e-12, -9581.133158965822, -46.9713639], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -2.723 eV.

            The two lowest frequencies, 24.5 and 55.1 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 69,
    label = "XCHO",
    molecule =
"""
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 O  u0  p2 c0 {2,D}
4 H  u0  p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             1.33925015, 0.0156187879, -1.78706053e-05, 1.16103367e-08,
             -3.20827392e-12, -27995.55483223874, -4.27823196], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             7.47250182, -0.00425652358, 7.67240272e-06, -4.1509429e-09,
             7.52057428e-13, -29557.233132238744, -35.2777491], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.573 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 70,
    label = "XCHXO",
    molecule =
"""
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 O  u0 p2 c0 {2,S} {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             0.873097043, 0.0193259085, -2.43372823e-05, 1.61326691e-08,
             -4.3452672e-12, -24142.481660004076, -2.94044233], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             7.63455521, -0.00373566071, 6.72665116e-06, -3.63437732e-09,
             6.57956785e-13, -25786.682960004076, -36.7791287], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.275 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 71,
    label = "XCHOH",
    molecule =
"""
1 X  u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -0.500706212, 0.0203875126, -1.83412371e-05, 8.05213048e-09,
             -1.17601762e-12, -26177.64178938842, 7.4226431], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             8.40355286, -0.00656451064, 1.17183592e-05, -6.25846821e-09,
             1.12274887e-12, -28507.85828938842, -37.9680665], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.949 eV.

                The two lowest frequencies, 12.0 and 58.4 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 72,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             0.336104022, 0.0226483369, -2.39239155e-05, 1.37256579e-08,
             -3.24031427e-12, -20662.74254874488, -1.88215814], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.52489548, -0.0065073405, 1.16586275e-05, -6.25680688e-09,
             1.12649338e-12, -23012.28834874488, -48.4225553], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.213 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 73,
    label = "XCOOH",
    molecule =
"""
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,S} {4,S}
4 H u0 p0 c0 {3,S}
5 X u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             0.359051461, 0.0250172545, -3.09587526e-05, 2.00287012e-08,
             -5.26520494e-12, -57904.434325465256, 3.52735255], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.16264817, -0.00470146235, 8.43555601e-06, -4.53366378e-09,
             8.17971447e-13, -60056.152925465256, -40.5975157], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.570 eV.

                The two lowest frequencies, 36.7 and 64.6 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 74,
    label = "CO2X",
    molecule =
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
4 X u0 p0 c0
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             2.00959799, 0.0133597565, -1.62303912e-05, 1.10029585e-08,
             -3.14484723e-12, -53249.621377532785, -2.58903014], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             6.98298591, -0.00309871776, 5.62883251e-06, -3.07847525e-09,
             5.62449215e-13, -54501.28087753279, -27.6481272], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298, 'K'),
        Tmax=(2000, 'K'),
    ),
    longDesc=u"""Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied: kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2.DFT binding energy: -0.062 eV. The two lowest frequencies, 10.8 and 12.0 cm-1, where replaced by the 2D gas model. The heat of formation of CO2 was corrected by +0.41 eV since the BEEF-vdW functional overestimates the binding energy (see SI of DOI:10.1039/c0ee00071j)""",
    metal="Pt",
    facet="111",
)

entry(
    index = 75,
    label = "HC(O)XO",
    molecule =
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,S} {5,S}
3 C u0 p0 c0 {1,D} {2,S} {4,S}
4 H u0 p0 c0 {3,S}
5 X u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             2.6545242, 0.0153991982, -1.01838393e-05, 1.7530405e-09,
             5.79614481e-13, -45985.990159400855, -11.0811323], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             10.1836282, -0.00548155633, 9.9350472e-06, -5.42476495e-09,
             9.90183951e-13, -48068.67495940086, -49.9790695], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -1.902 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 76,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             0.389187265, 0.0292112653, -3.68630528e-05, 2.57772068e-08,
             -7.38835035e-12, -22763.290593262624, 3.25846272], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             11.0991553, -0.00740804127, 1.32480136e-05, -7.08463685e-09,
             1.27176536e-12, -25383.85639326262, -50.3706835], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.619 eV.

                The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 77,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             1.23038408, 0.0213641887, -1.09879577e-05, -4.0854811e-10,
             1.72792683e-12, -36226.94317640585, 0.412454379], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             12.8961233, -0.0106029491, 1.89557851e-05, -1.0145896e-08,
             1.82293047e-12, -39475.02487640585, -59.9543192], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.551 eV.

                The two lowest frequencies, 23.8 and 88.9 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 78,
    label = "XCHCO",
    molecule =
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
5 X u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             0.0425530093, 0.0279328122, -3.9427743e-05, 2.93799156e-08,
             -8.78679074e-12, -16310.112233265743, 4.03639097], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.11773004, -0.00500204545, 8.99633603e-06, -4.84653933e-09,
             8.75265787e-13, -18435.017733265744, -40.9365888], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.511 eV.

                The two lowest frequencies, 38.0 and 95.1 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 79,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -1.25479749, 0.0376847805, -3.93538492e-05, 2.16708327e-08,
             -4.77858725e-12, -3533.546152512003, 4.10178815], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             13.9365153, -0.0103605118, 1.85207758e-05, -9.90839299e-09,
             1.77999302e-12, -7410.664052512004, -72.8413395], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -5.430 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 80,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -0.593007302, 0.0357123823, -2.8891947e-05, 1.03540097e-08,
             -6.87748469e-13, 5820.4669967899845, 4.07112708], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             15.8597409, -0.0128922295, 2.2989923e-05, -1.22606374e-08,
             2.19689224e-12, 1452.8016867899846, -80.0996985], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -3.359 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 81,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             0.193063496, 0.0288384322, -1.13116346e-05, -5.04671551e-09,
             4.14390397e-12, -3382.302263866197, 4.76068688], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             16.7774942, -0.0157411973, 2.80704427e-05, -1.49721483e-08,
             2.68245819e-12, -8030.630003866197, -81.2380722], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.944 eV.

                The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 82,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -1.01283183, 0.0396054673, -2.41796124e-05, 3.23567437e-09,
             1.99314176e-12, -10644.12855612444, 3.3418338], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             19.5941002, -0.0184981215, 3.29579796e-05, -1.75535179e-08,
             3.14139881e-12, -16277.483556124442, -102.828351], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.713 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 83,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -0.578976324, 0.0371915827, -1.22898025e-05, -8.77177071e-09,
             6.04039735e-12, -14594.75888014975, 1.4727787], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             21.5363954, -0.0215932574, 3.8529924e-05, -2.05691913e-08,
             3.68755975e-12, -20837.696780149752, -113.399138], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.333 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 84,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             2.15856144, 0.0248539972, 1.53525973e-05, -3.25302366e-08,
             1.35067652e-11, -20834.674359054934, -8.74139325], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             23.2832355, -0.0245407014, 4.37313468e-05, -2.33036993e-08,
             4.17150293e-12, -27161.164159054933, -120.201845], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.241 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 85,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -2.72979307, 0.0477487399, -4.5782706e-05, 2.34519012e-08,
             -4.78486001e-12, -9692.423017329204, 9.23470861], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             17.8566754, -0.0157310158, 2.81077398e-05, -1.50276611e-08,
             2.69754383e-12, -15045.752377329203, -95.4811248], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -3.195 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 86,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -0.140036274, 0.0358616425, -1.11021659e-05, -8.97397908e-09,
             5.91635074e-12, -15367.209369673039, -0.977178836], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             21.5065179, -0.0215386628, 3.84133775e-05, -2.04904605e-08,
             3.67103983e-12, -21490.60956967304, -113.46359], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.157 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 87,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -3.02780964, 0.048682792, -4.64697726e-05, 2.28751861e-08,
             -4.238776e-12, -8408.215080963375, 11.5070732], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             17.77877, -0.0155322169, 2.76898539e-05, -1.47575432e-08,
             2.64275606e-12, -13795.289890963373, -94.2606313], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.196 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 88,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             0.260792367, 0.0296600289, -3.7462411e-05, 2.3585704e-08,
             -5.9791512e-12, -62276.715586923485, 4.32145289], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             10.0467898, -0.00351638045, 6.49177075e-06, -3.63351445e-09,
             6.7629741e-13, -64652.187386923484, -44.6692931], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298, 'K'),
        Tmax=(2000, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). 
        		Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso 
        		using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) 
        		following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
        		kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
        		fmax=2.5e-2. DFT binding energy: -3.027 eV. 
        		The two lowest frequencies, 89.5 and 92.5 cm-1, where replaced by the 2D gas model. 
        		The heat of formation of CO3 was corrected by +0.41 eV since the BEEF-vdW functional overestimates the binding energy (see SI of DOI:10.1039/c0ee00071j)""",
    metal="Pt",
    facet="111",
)

entry(
    index = 89,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             1.01328212, 0.0326276222, -3.70609785e-05, 2.09604143e-08,
             -4.66693351e-12, -76224.68859178782, -4.75360743], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             12.8523534, -0.00570824836, 1.02858082e-05, -5.56715984e-09,
             1.01065309e-12, -79181.71069178783, -64.4494097], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298, 'K'),
        Tmax=(2000, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -2.365 eV. The heat of formation of HCO3 was corrected by +0.41 eV since the BEEF-vdW functional overestimates the binding energy (see SI of DOI:10.1039/c0ee00071j)""",
    metal="Pt",
    facet="111",
)

entry(
    index = 90,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             2.35698005, 0.016581795, -8.93246966e-06, -5.9659096e-10,
             1.65711542e-12, -54904.478534088754, -0.543199062], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             11.0477913, -0.0072427437, 1.29091018e-05, -6.88021503e-09,
             1.2328955e-12, -57307.79423408875, -45.4728471], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.216 eV.

                The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 91,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             3.3768885, 0.017168295, 1.0226307e-05, -2.31122378e-08,
             9.75945366e-12, -55824.93917959884, -7.59071433], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             17.3815092, -0.0148389347, 2.65610657e-05, -1.42501123e-08,
             2.56517842e-12, -60047.540979598845, -81.6468299], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.318 eV.

                The two lowest frequencies, 62.9 and 75.5 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 92,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             1.68079896, 0.0312126215, -8.078934e-06, -1.08377033e-08,
             6.48220713e-12, -47333.49549013445, -5.80786049], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             20.4132198, -0.0173601838, 3.10764492e-05, -1.66713256e-08,
             3.00083064e-12, -52676.62719013445, -103.396841], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -1.997 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 93,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             0.369923804, 0.0286585416, -2.78936419e-05, 1.36526428e-08,
             -2.53912516e-12, -35667.37576106521, -0.370031423], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             12.2233961, -0.00774165833, 1.3941835e-05, -7.54192659e-09,
             1.36669487e-12, -38748.42876106521, -60.6800543], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -3.554 eV.
    """,
    metal="Pt",
    facet="111",
)


entry(
    index = 94,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             0.461067651, 0.0253309271, -2.95243491e-06, -1.26602001e-08,
             6.61140934e-12, -26460.353239023156, 3.45861454], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             16.7501781, -0.0161554398, 2.88603109e-05, -1.54358268e-08,
             2.77154673e-12, -31148.649639023155, -81.5974052], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -1.905 eV.

                The two lowest frequencies, 12.0 and 92.3 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 95,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -0.382821995, 0.0318369145, -4.01391269e-05, 2.76197052e-08,
             -7.78850595e-12, 11180.160029827546, 5.75967137], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             11.1180258, -0.00740595551, 1.32616442e-05, -7.1051763e-09,
             1.27762668e-12, 8368.484099827547, -51.834459], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -3.773 eV.

                The two lowest frequencies, 12.0 and 99.7 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 96,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -2.27103445, 0.0427539019, -5.61652527e-05, 3.84419292e-08,
             -1.06004164e-11, 12376.277829602079, 6.93062665], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             12.1290474, -0.00757219828, 1.36015955e-05, -7.32089312e-09,
             1.3215761e-12, 8939.937059602078, -64.8251627], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -3.648 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 97,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -0.407836856, 0.0338179738, -1.82365043e-05, -2.17799277e-10,
             2.78237156e-12, -16160.149244213531, 3.03397088], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             17.6952935, -0.0161873878, 2.89121382e-05, -1.5456086e-08,
             2.77424705e-12, -21165.616344213533, -90.5055229], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -6.099 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 98,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -0.414367704, 0.0297866357, -2.42611023e-05, 8.22145796e-09,
             -2.81785012e-13, -30201.656800254572, 7.21907667], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             13.0250135, -0.00979365971, 1.74609646e-05, -9.31041024e-09,
             1.66893053e-12, -33765.42190025458, -61.5413406], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -5.950 eV.

                The two lowest frequencies, 12.0 and 51.0 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 99,
    label = "XCCHO",
    molecule =
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {5,T}
4 H u0 p0 c0 {2,S}
5 X u0 p0 c0 {3,T}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -0.154881082, 0.0246650429, -2.7882926e-05, 1.67435167e-08,
             -4.17255119e-12, -24353.93849896448, 5.36194261], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.17648225, -0.00539008423, 9.76740931e-06, -5.32718475e-09,
             9.7157878e-13, -26719.000598964478, -41.7960043], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -5.377 eV.

                The two lowest frequencies, 20.1 and 76.7 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 100,
    label = "XCCO",
    molecule =
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,D}
3 C u0 p0 c0 {1,D} {2,D}
4 X u0 p0 c0 {2,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             0.482296413, 0.0258715605, -3.9360387e-05, 3.04629746e-08,
             -9.3653349e-12, -20354.255889347944, -3.57376015], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             8.07081859, -0.00300851572, 5.51539311e-06, -3.04805549e-09,
             5.61469009e-13, -22068.936589347944, -40.8625858], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -5.276 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 101,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             0.317980384, 0.0337808273, -1.47996341e-05, -3.8491422e-09,
             3.93637206e-12, -37816.33198731191, 3.57199396], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             19.3377955, -0.0174343755, 3.11976589e-05, -1.67226574e-08,
             3.00798191e-12, -43156.91988731191, -95.0724091], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.348 eV.

                The two lowest frequencies, 12.0 and 63.5 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 102,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             2.44141648, 0.0201418511, 1.00444529e-05, -2.46324618e-08,
             1.06436492e-11, -33116.42403989183, -2.16253584], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             18.5992615, -0.0179442101, 3.18809278e-05, -1.6915779e-08,
             3.01870761e-12, -37914.245839891824, -87.2751435], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.023 eV.

                The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 103,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -0.0938075627, 0.0325418587, -1.95081006e-05, 1.90337747e-09,
             2.01784423e-12, -35632.37301588977, 5.47743439], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             16.8236097, -0.015032595, 2.67326715e-05, -1.41983594e-08,
             2.53584549e-12, -40254.320115889765, -81.6921311], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.332 eV.

                The two lowest frequencies, 12.0 and 96.1 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 104,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -0.264775456, 0.0303517808, -2.04737999e-05, 4.47036782e-09,
             8.49809806e-13, -35238.58244751335, 6.53319807], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             14.8988986, -0.0128910736, 2.29998891e-05, -1.22748249e-08,
             2.20049375e-12, -39355.89754751335, -71.4636815], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.952 eV.

                The two lowest frequencies, 12.0 and 58.0 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 105,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -1.47420628, 0.0421450105, -5.01975896e-05, 3.19228373e-08,
             -8.2499077e-12, 8070.8284103984115, 6.36468208], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             14.1133329, -0.00985218182, 1.76095803e-05, -9.41496495e-09,
             1.69037771e-12, 4225.888840398412, -71.9224209], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.423 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 106,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             -1.60792265, 0.0365072698, -1.7302833e-05, -2.63268524e-09,
             3.77289172e-12, -8307.893412617064, 11.71797], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             18.6868441, -0.0188617963, 3.36944612e-05, -1.8017049e-08,
             3.23426057e-12, -13963.408062617065, -93.3401144], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -3.649 eV.

                The two lowest frequencies, 12.0 and 74.1 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 107,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             0.403765346, 0.0343477499, -1.58933907e-05, -2.43971983e-09,
             3.40954348e-12, -9838.556041488062, -2.81376113], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             19.7785534, -0.0185076861, 3.30425254e-05, -1.76515167e-08,
             3.16607226e-12, -15245.954741488064, -103.131111], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -3.420 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 108,
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[
             2.76865237, 0.015420904, 5.76787174e-06, -1.58270365e-08,
             6.75180571e-12, -31455.023169815806, -5.05938429], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             14.8477497, -0.0133581956, 2.38689301e-05, -1.27693401e-08,
             2.29305318e-12, -35050.93036981581, -68.6748062], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.259 eV.

                The two lowest frequencies, 30.5 and 72.0 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 109,
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
            NASAPolynomial(coeffs=[
             1.30720584, 0.0165960781, -1.65593895e-06, -8.53643563e-09,
             4.49817961e-12, -1361.9319538407394, 1.00987103], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             12.1842322, -0.0115021314, 2.03950515e-05, -1.07880418e-08,
             1.91997845e-12, -4461.64195284074, -55.6581654], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -0.216 eV.

            The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 110,
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
            NASAPolynomial(coeffs=[
             -2.34433622, 0.0452667542, -3.3447686e-05, 1.03612371e-08,
             -1.30499778e-13, -14437.922968649871, 8.41335045], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             19.6554137, -0.0186218831, 3.3226555e-05, -1.7733432e-08,
             3.17881568e-12, -20356.29706864987, -104.466461], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -1.046 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 111,
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
            NASAPolynomial(coeffs=[
             0.346550846, 0.0332090432, -3.22987737e-05, 1.775211e-08,
             -4.03378719e-12, 9666.391545741819, 3.58666724], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             14.9403509, -0.0122710198, 2.18143728e-05, -1.15729874e-08,
             2.06442673e-12, 5886.539115741817, -70.5497634], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -0.277 eV.

            The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 112,
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
            NASAPolynomial(coeffs=[
             1.89699352, 0.0313653839, -3.45366352e-05, 1.9380379e-08,
             -4.25074559e-12, -82681.60449432017, -0.682208145], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             13.8341567, -0.00712667706, 1.26390399e-05, -6.68179574e-09,
             1.19065178e-12, -85670.69809432018, -60.9099445], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -0.348 eV.

            The two lowest frequencies, 12.0 and 37.3 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 113,
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
            NASAPolynomial(coeffs=[
             -4.02635101, 0.0503308424, -5.38588531e-05, 3.03407703e-08,
             -6.84918788e-12, -2335.267937832245, 15.7737894], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             15.8963681, -0.0132662345, 2.37473427e-05, -1.27307691e-08,
             2.29051345e-12, -7388.2359678322455, -84.9812453], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -4.341 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 114,
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
            NASAPolynomial(coeffs=[
             -4.80891778, 0.0537146126, -6.67782051e-05, 4.3278281e-08,
             -1.1302341e-11, 6230.5213351429675, 17.8493803], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             14.0662167, -0.0104801296, 1.88192337e-05, -1.0130724e-08,
             1.82883288e-12, 1646.294795142967, -76.6191987], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -4.292 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 115,
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
            NASAPolynomial(coeffs=[
             -3.40514908, 0.0477243064, -6.43560316e-05, 4.44980067e-08,
             -1.22960184e-11, 9773.212627781575, 11.8363424], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             12.1348559, -0.00752689921, 1.35205213e-05, -7.2771888e-09,
             1.31382482e-12, 6121.789677781575, -65.3413425], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -3.402 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 116,
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
            NASAPolynomial(coeffs=[
             -3.87649194, 0.0504109402, -4.03708786e-05, 1.47882509e-08,
             -1.23971666e-12, -10638.873547284817, 15.7499252], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             19.66012, -0.0189254315, 3.38211492e-05, -1.80931479e-08,
             3.24941421e-12, -16915.45194728482, -104.756688], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -3.283 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 117,
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
            NASAPolynomial(coeffs=[
             -3.48448515, 0.0496119073, -4.6542023e-05, 2.23779541e-08,
             -4.0310949e-12, 884.3767869093269, 13.7505559], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             17.8868252, -0.0158385251, 2.83251785e-05, -1.51673166e-08,
             2.72609641e-12, -4682.571773090674, -95.0346021], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -5.146 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 118,
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
            NASAPolynomial(coeffs=[
             -1.79815684, 0.0326996376, -4.25662573e-05, 2.91542676e-08,
             -8.0358567e-12, -2794.328047886155, 5.84807669], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.43023108, -0.00645957592, 1.15448998e-05, -6.16905671e-09,
             1.10713611e-12, -5477.929057886155, -50.1225511], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -3.916 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 119,
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
            NASAPolynomial(coeffs=[
             -0.528083316, 0.0285783353, -2.22349304e-05, 7.78829612e-09,
             -5.93358696e-13, -26695.132040989974, 7.51944172], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             12.9781551, -0.010727812, 1.92368201e-05, -1.0341454e-08,
             1.86454984e-12, -30331.357740989974, -61.7793029], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -1.976 eV.

            The two lowest frequencies, 58.8 and 75.3 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 120,
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
            NASAPolynomial(coeffs=[
             -1.94518379, 0.0395654165, -3.03930791e-05, 9.7928988e-09,
             -1.95808647e-13, -31614.59716764829, 13.1064835], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             16.7847482, -0.0152226559, 2.70968887e-05, -1.44118191e-08,
             2.57708191e-12, -36617.21426764829, -82.857198], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -2.488 eV.

            The two lowest frequencies, 12.0 and 93.4 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 121,
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
            NASAPolynomial(coeffs=[
             -2.37007233, 0.0452879213, -5.44419673e-05, 3.43225741e-08,
             -8.71185762e-12, -28759.524706991357, 8.3369218], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             14.0545368, -0.00976944446, 1.74383432e-05, -9.30556763e-09,
             1.66873012e-12, -32784.63660699136, -74.0554815], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -3.361 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 122,
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
            NASAPolynomial(coeffs=[
             -0.300416383, 0.0361961687, -4.28843203e-05, 2.71417157e-08,
             -6.93485547e-12, -22908.89568494904, 5.48365659], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             13.1911025, -0.00886429182, 1.57291273e-05, -8.31877139e-09,
             1.48112563e-12, -26226.07468494904, -62.2425505], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -2.837 eV.

            The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 123,
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
            NASAPolynomial(coeffs=[
             -1.37761371, 0.0372565997, -5.30168625e-05, 3.85555128e-08,
             -1.11934628e-11, -27404.86633058119, 3.96229085], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             10.1988493, -0.00511717278, 9.26394034e-06, -5.03840097e-09,
             9.16957643e-13, -30078.31633058119, -53.268012], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -3.460 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 124,
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
            NASAPolynomial(coeffs=[
             3.37271709, 0.0119486098, 2.71504465e-05, -3.88526285e-08,
             1.49405852e-11, -32497.147585274695, -7.75895151], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             18.5166607, -0.0190746655, 3.40122343e-05, -1.81459402e-08,
             3.25144074e-12, -37255.5592852747, -88.7571696], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -0.362 eV.

            The two lowest frequencies, 12.0 and 67.3 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 125,
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
            NASAPolynomial(coeffs=[
             -4.5418411, 0.0516072922, -6.99489368e-05, 4.85158534e-08,
             -1.34564929e-11, 12748.474790360158, 16.5180273], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             12.1430416, -0.00783417928, 1.4122672e-05, -7.64053459e-09,
             1.38487512e-12, 8831.281690360158, -66.3229379], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -5.613 eV.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 126,
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
            NASAPolynomial(coeffs=[
             -4.92854074, 0.0553472012, -7.06461759e-05, 4.67854057e-08,
             -1.2437669e-11, 2628.0255173976234, 18.2810138], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             14.083457, -0.0102652951, 1.84117274e-05, -9.89306924e-09,
             1.78340127e-12, -1938.2871026023768, -76.6281115], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -6.285 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 127,
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
            NASAPolynomial(coeffs=[
             -3.24543107, 0.0457407291, -5.20679215e-05, 3.10116074e-08,
             -7.43118067e-12, 4264.620344863533, 14.2275299], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             13.9737231, -0.0105202964, 1.88516802e-05, -1.0120419e-08,
             1.82311527e-12, -31.740959736466788, -72.5198475], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -6.189 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 128,
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
            NASAPolynomial(coeffs=[
             -2.57393128, 0.0477399245, -4.59807447e-05, 2.35135768e-08,
             -4.7455026e-12, -8762.895854156146, 9.44154348], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             17.9080385, -0.0155492702, 2.77729619e-05, -1.48415413e-08,
             2.66313378e-12, -14077.784884156146, -94.6976696], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -3.399 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 129,
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
            NASAPolynomial(coeffs=[
             -2.33599764, 0.0409549542, -3.30896797e-05, 1.23408962e-08,
             -1.07948372e-12, -4212.221410501172, 14.8603663], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             16.7497477, -0.0155450741, 2.76946971e-05, -1.47478624e-08,
             2.63918113e-12, -9280.954810501173, -82.7715317], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -1.775 eV.

            The two lowest frequencies, 12.0 and 74.2 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 130,
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
            NASAPolynomial(coeffs=[
             -0.29935428, 0.03629506, -3.94436193e-05, 2.30734162e-08,
             -5.50516577e-12, -16275.5866739101, -0.524288186], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             14.0890656, -0.00990516134, 1.76961471e-05, -9.4570079e-09,
             1.69729334e-12, -19918.370573910102, -73.2427736], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -1.133 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 131,
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
            NASAPolynomial(coeffs=[
             -4.00241403, 0.0522189088, -5.89122044e-05, 3.51035783e-08,
             -8.41934161e-12, -2579.9758790475876, 15.0822089], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             15.9486678, -0.0128837296, 2.30283272e-05, -1.23167595e-08,
             2.21202132e-12, -7564.437099047587, -85.4536705], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -4.131 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 132,
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
            NASAPolynomial(coeffs=[
             0.897583218, 0.0246743148, -3.70136199e-05, 2.82073318e-08,
             -8.56860763e-12, -20001.391486851982, -4.67313316], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             8.1781755, -0.00274871719, 5.05296264e-06, -2.80344383e-09,
             5.18025206e-13, -21657.294586851982, -40.5106752], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -5.210 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 133,
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
            NASAPolynomial(coeffs=[
             1.49804316, 0.0287614176, -2.6886222e-05, 1.52783281e-08,
             -3.78230086e-12, 11186.694944759352, -1.11521746], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             14.8327083, -0.0123703052, 2.19686449e-05, -1.16339578e-08,
             2.07217584e-12, 7690.111764759353, -69.0163887], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -0.310 eV.

            The two lowest frequencies, 51.8 and 63.4 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 134,
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
            NASAPolynomial(coeffs=[
             -1.25979918, 0.0429110764, -6.1125648e-05, 4.48105295e-08,
             -1.30454814e-11, 19947.88060756566, 3.5253043], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             12.2618815, -0.00684691121, 1.22478884e-05, -6.54778739e-09,
             1.17560614e-12, 16842.71010756566, -63.24377], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -3.349 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 135,
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
            NASAPolynomial(coeffs=[
             -4.33834725, 0.0549356355, -8.04348255e-05, 5.94297575e-08,
             -1.73391856e-11, 8402.830084536161, 15.1752797], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             12.2196206, -0.00722560903, 1.29807408e-05, -6.9811981e-09,
             1.25948043e-12, 4669.968124536161, -66.26233], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -4.271 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 136,
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
            NASAPolynomial(coeffs=[
             0.170293757, 0.0268182339, -2.11880127e-05, 8.20992815e-09,
             -1.02776468e-12, 2726.614073092521, 3.50629321], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             12.9502839, -0.0105538555, 1.88909383e-05, -1.01262169e-08,
             1.82152861e-12, -712.8040939074791, -62.0424122], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -4.747 eV.

            The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 137,
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
            NASAPolynomial(coeffs=[
             -2.72746229, 0.049119337, -5.72165653e-05, 3.62071595e-08,
             -9.37581263e-12, 227.06143963891748, 9.21506685], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             15.9653882, -0.0126651294, 2.2613298e-05, -1.20712119e-08,
             2.16431136e-12, -4421.942283361082, -84.8332759], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -1.220 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 138,
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
            NASAPolynomial(coeffs=[
             -1.15893067, 0.0370424993, -3.12332418e-05, 1.29953202e-08,
             -1.80175319e-12, -8878.936581647638, 2.95909204], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             15.8046677, -0.013393455, 2.39475392e-05, -1.28180432e-08,
             2.3031851e-12, -13385.79827164764, -83.7975104], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -4.100 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 139,
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
            NASAPolynomial(coeffs=[
             -4.32569037, 0.0522761881, -6.52481961e-05, 4.25489345e-08,
             -1.11793769e-11, 256.747120409451, 15.7860707], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             14.0354949, -0.0103288659, 1.85144208e-05, -9.93982041e-09,
             1.7906297e-12, -4194.596111590548, -76.0710085], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -5.141 eV.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 140,
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
            NASAPolynomial(coeffs=[
             -1.23617363, 0.0391193103, -3.59445619e-05, 1.7078262e-08,
             -3.07130016e-12, -6657.468089669765, 3.54507519], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             15.9073613, -0.0130485761, 2.33187859e-05, -1.24715428e-08,
             2.2395083e-12, -11146.219609669764, -83.8198234], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -1.915 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 141,
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
            NASAPolynomial(coeffs=[
             2.35949301, 0.026577909, 4.85435584e-06, -2.33007362e-08,
             1.08024076e-11, -57589.88616333766, -2.72908301], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             21.2488755, -0.0193209268, 3.44158139e-05, -1.83320271e-08,
             3.28169374e-12, -63121.704563337655, -101.870265], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -0.459 eV.

            The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 142,
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
            NASAPolynomial(coeffs=[
             -3.96827051, 0.0482122603, -7.02038671e-05, 5.07019364e-08,
             -1.44599541e-11, 15083.704214216144, 14.0625208], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             10.25616, -0.00501053573, 9.09120689e-06, -4.95996444e-09,
             9.05238271e-13, 11881.417114216143, -55.9084362], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -5.202 eV.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 143,
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
            NASAPolynomial(coeffs=[
             0.704831422, 0.0283762115, -3.78645327e-05, 2.65441259e-08,
             -7.54179011e-12, 33456.5662885376, -4.37180969], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             10.1968696, -0.00492542027, 8.88181864e-06, -4.80548132e-09,
             8.71059272e-13, 31188.058788537604, -51.6653737], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -3.793 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 144,
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
            NASAPolynomial(coeffs=[
             -0.98488242, 0.0360148185, -5.06524253e-05, 3.62843216e-08,
             -1.03804604e-11, 21417.818625120937, 1.66468647], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             10.2578284, -0.00486514372, 8.79773214e-06, -4.77770413e-09,
             8.68659255e-13, 18814.052225120937, -53.9672632], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -4.749 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 145,
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
            NASAPolynomial(coeffs=[
             -1.25342098, 0.0327302187, -3.75493266e-05, 2.32114742e-08,
             -5.93083221e-12, -19398.738313185037, 9.92661471], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             11.1794819, -0.00779813608, 1.40437569e-05, -7.59182897e-09,
             1.37483935e-12, -22525.466813185038, -52.7836731], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -3.420 eV.

            The two lowest frequencies, 12.0 and 98.6 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 146,
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
            NASAPolynomial(coeffs=[
             -0.678192366, 0.0326656436, -3.48212682e-05, 1.9201352e-08,
             -4.23029667e-12, -23112.88073320696, 1.48082726], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             12.1109589, -0.00788891095, 1.41901384e-05, -7.66128189e-09,
             1.38633384e-12, -26369.557933206957, -63.2645953], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -3.816 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 147,
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
            NASAPolynomial(coeffs=[
             1.92629641, 0.0239209948, -1.1102911e-05, -3.27472177e-09,
             3.46492626e-12, -55807.23745779836, -0.762359459], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             14.9097254, -0.0114976893, 2.03256816e-05, -1.07026073e-08,
             1.89947433e-12, -59387.460157798356, -67.8769969], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -0.341 eV.

            The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 148,
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
            NASAPolynomial(coeffs=[
             1.0741251, 0.0229655848, -1.22605664e-05, -1.24601909e-09,
             2.54035334e-12, -44874.490527417496, 1.02956006], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             13.0486159, -0.00984841705, 1.75672095e-05, -9.37554784e-09,
             1.68161712e-12, -48180.443027417496, -60.8626514], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -1.593 eV.

            The two lowest frequencies, 42.0 and 64.2 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 149,
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
            NASAPolynomial(coeffs=[
             -4.87253669, 0.0556211271, -6.41174541e-05, 3.90946699e-08,
             -9.64986424e-12, 5631.821107436793, 18.4285138], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             16.0332585, -0.0130870619, 2.34592896e-05, -1.25997206e-08,
             2.27017641e-12, 427.4620054367928, -86.812333], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -1.808 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 150,
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
            NASAPolynomial(coeffs=[
             0.957932995, 0.0341777137, 2.82673229e-06, -2.45769826e-08,
             1.15600862e-11, -4305.257569443249, 2.11035371], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             24.884372, -0.025217765, 4.49134428e-05, -2.39131219e-08,
             4.27855482e-12, -11272.519589443249, -123.216412], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.848 eV.

            The two lowest frequencies, 37.8 and 59.8 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)



entry(
    index = 151,
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
            NASAPolynomial(coeffs=[
             2.23075265, 0.0177836646, -5.8815493e-06, -3.71240588e-09,
             2.53490284e-12, 29584.48931856441, -3.17521175], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             12.9257481, -0.0105258288, 1.88140143e-05, -1.00666038e-08,
             1.80803508e-12, 26546.30904856441, -58.7921287], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.119 eV.
        
            The two lowest frequencies, 60.4 and 70.3 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 152,
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
            NASAPolynomial(coeffs=[
             1.90915977, 0.0215348213, -9.82326705e-06, -2.19028204e-09,
             2.46328999e-12, 26652.414836104395, -8.92747457], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             13.8638716, -0.0107277422, 1.91868566e-05, -1.02769215e-08,
             1.8476574e-12, 23303.729896104396, -70.900742], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.397 eV.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 153,
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
            NASAPolynomial(coeffs=[
             3.99716674, 0.0250963574, 1.32739888e-05, -3.22924772e-08,
             1.39061436e-11, -12256.105959991846, -7.7220488], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             23.931485, -0.0209159552, 3.73740583e-05, -2.00021409e-08,
             3.59373223e-12, -18227.726159991846, -112.979839], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.458 eV.

            The two lowest frequencies, 41.9 and 44.8 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 154,
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
            NASAPolynomial(coeffs=[
             1.76341767, 0.0219464568, -2.10331786e-05, 1.0462359e-08,
             -2.00841774e-12, -7843.2317454665845, -2.25653938], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             11.1105347, -0.00680546425, 1.20935402e-05, -6.41229006e-09,
             1.1443165e-12, -10268.512495466584, -49.7988752], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.687 eV.

            The two lowest frequencies, 18.7 and 56.2 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)




entry(
    index = 155,
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
            NASAPolynomial(coeffs=[
             1.0356492, 0.0240376349, -3.10715372e-05, 2.12746585e-08,
             -5.93634517e-12, -25023.363479484797, 0.842342326], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.32089542, -0.00452469969, 8.14668857e-06, -4.39895298e-09,
             7.96128873e-13, -27028.2762794848, -40.5621373], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.461 eV.

            The two lowest frequencies, 29.7 and 57.2 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 156,
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
            NASAPolynomial(coeffs=[
             0.942334653, 0.0249348823, -2.7919441e-05, 1.57195859e-08,
             -3.49022547e-12, -6380.326075685715, -4.56590148], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             10.1702298, -0.00483260136, 8.68920587e-06, -4.68832118e-09,
             8.48623192e-13, -8693.154655685714, -51.1288594], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.563 eV.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 157,
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
            NASAPolynomial(coeffs=[
             0.932902353, 0.0255944058, -2.99292308e-05, 1.79225102e-08,
             -4.3129042e-12, -227.52602298038255, -4.32356506], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             10.1899092, -0.00483727621, 8.70454352e-06, -4.70078536e-09,
             8.51292268e-13, -2523.6319829803824, -50.9038584], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.021 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 158,
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
            NASAPolynomial(coeffs=[
             1.84587368, 0.0298470479, -1.62880846e-05, -5.16049916e-10,
             2.71070666e-12, -8726.57206232521, -2.26198847], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             17.5641376, -0.013464318, 2.39991758e-05, -1.27908081e-08,
             2.29130643e-12, -13065.670282325209, -83.4757372], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.591 eV.

            The two lowest frequencies, 26.2 and 53.1 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 159,
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
            NASAPolynomial(coeffs=[
             0.993524997, 0.0191880996, -2.42925189e-05, 1.54780612e-08,
             -3.9995105e-12, -21653.903954719863, 0.798257555], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             7.35498572, -0.00236271293, 4.361156e-06, -2.43964123e-09,
             4.53868801e-13, -23202.43365471986, -31.0619586], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.025 eV.

            The two lowest frequencies, 63.4 and 94.1 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 160,
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
            NASAPolynomial(coeffs=[
             0.550023151, 0.0306842134, -3.99225227e-05, 2.52783205e-08,
             -6.33311112e-12, -23128.6609996746, 3.79685931], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             10.2421752, -0.00291226023, 5.39200871e-06, -3.0311934e-09,
             5.66192922e-13, -25429.9023996746, -44.5032687], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.349 eV.

            The two lowest frequencies, 71.1 and 71.3 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 161,
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
            NASAPolynomial(coeffs=[
             1.49859414, 0.0323552017, -2.1571888e-05, 4.16724299e-09,
             1.18921539e-12, -7293.127200475746, -1.21982137], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             17.6025118, -0.0133532482, 2.37989451e-05, -1.26809102e-08,
             2.27106788e-12, -11670.763060475747, -84.0931219], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.529 eV.

            The two lowest frequencies, 43.3 and 91.3 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 162,
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
            NASAPolynomial(coeffs=[
             1.38602505, 0.0166417938, -1.69194435e-05, 9.53014507e-09,
             -2.17925678e-12, -6758.756863406493, -0.717727031], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             8.44372099, -0.00568404051, 1.00351868e-05, -5.26778604e-09,
             9.32182352e-13, -8561.217433406491, -36.4672604], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: 392.535 eV.

            The two lowest frequencies, 32.9 and 61.9 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 163,
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
            NASAPolynomial(coeffs=[
             -0.26696303, 0.0256587171, -3.67461104e-05, 2.65256975e-08,
             -7.56688462e-12, -4104.038743327682, -0.599888085], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             7.58972292, -0.00344279656, 6.15410498e-06, -3.28642966e-09,
             5.89854827e-13, -5888.355763327681, -39.3223551], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.123 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 164,
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
            NASAPolynomial(coeffs=[
             1.33477884, 0.024001935, -2.56561855e-05, 1.48677005e-08,
             -3.52970084e-12, -35900.25166599109, -0.658172135], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             10.9970911, -0.00679595586, 1.20456893e-05, -6.35963045e-09,
             1.13133387e-12, -38356.28426599109, -49.5455886], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -2.139 eV.

            The two lowest frequencies, 37.0 and 61.0 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 165,
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
            NASAPolynomial(coeffs=[
             1.9695853, 0.0205229019, -1.16212974e-05, 6.21594217e-10,
             1.3989955e-12, -34250.64815047985, -2.35482681], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             12.8660725, -0.00980041411, 1.74045626e-05, -9.22325085e-09,
             1.64480939e-12, -37248.71545047985, -58.5945462], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.441 eV.

            The two lowest frequencies, 29.8 and 83.1 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 166,
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
            NASAPolynomial(coeffs=[
             2.54964727, 0.018460045, -2.42001249e-05, 1.73475076e-08,
             -5.0418246e-12, -25675.236377311456, -4.24775497], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.09915251, -0.00440019391, 7.81455043e-06, -4.13467387e-09,
             7.36415159e-13, -27251.283177311456, -36.9210659], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.238 eV.

            The two lowest frequencies, 26.0 and 32.2 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 167,
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
            NASAPolynomial(coeffs=[
             1.90934123, 0.0151098629, -2.03599314e-05, 1.49754141e-08,
             -4.53949205e-12, -19226.885423807027, -3.1891881], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             7.07963202, -0.00288358254, 5.25788665e-06, -2.88822698e-09,
             5.29485705e-13, -20487.61142380703, -29.0324525], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -2.032 eV.

            The two lowest frequencies, 79.6 and 79.6 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 168,
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
            NASAPolynomial(coeffs=[
             1.26262337, 0.0239707044, -3.57807164e-05, 2.69417574e-08,
             -8.08701023e-12, -18121.344310318535, -6.66075441], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             8.29013669, -0.00244795486, 4.51250001e-06, -2.51311053e-09,
             4.65787206e-13, -19717.442610318532, -41.2529556], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.865 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 169,
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
            NASAPolynomial(coeffs=[
             -0.910143692, 0.0364340487, -4.22975839e-05, 2.64150988e-08,
             -6.69559547e-12, -38566.41116723985, 8.34636517], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             12.9170344, -0.00926657106, 1.64164339e-05, -8.66024411e-09,
             1.53917134e-12, -41992.736267239845, -61.1916973], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -2.711 eV.

            The two lowest frequencies, 36.0 and 69.6 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 170,
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
            NASAPolynomial(coeffs=[
             0.444259551, 0.035143406, -3.82519408e-05, 2.31954956e-08,
             -5.75459819e-12, -16469.506286606484, 1.98278452], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             14.7451421, -0.0111329696, 1.95851124e-05, -1.02216976e-08,
             1.80103482e-12, -20068.047086606482, -70.1962072], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -2.451 eV.

            The two lowest frequencies, 12.7 and 85.0 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 171,
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
            NASAPolynomial(coeffs=[
             -0.253593131, 0.0331664368, -4.26353538e-05, 2.8610013e-08,
             -7.69395658e-12, -25282.128818855766, 5.80810638], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             11.171428, -0.00647195732, 1.14856356e-05, -6.07312525e-09,
             1.08156521e-12, -28012.602518855765, -51.1680784], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -2.354 eV.

            The two lowest frequencies, 15.1 and 62.2 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 172,
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
            NASAPolynomial(coeffs=[
             3.38877769, 0.0148507117, -1.80530123e-05, 1.27003048e-08,
             -3.71603096e-12, -13119.216929811379, -8.57157309], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.15463312, -0.00449876944, 8.01467389e-06, -4.2613033e-09,
             7.61516664e-13, -14554.668029811379, -37.5505709], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.450 eV.

            The two lowest frequencies, 46.1 and 61.5 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 173,
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
            NASAPolynomial(coeffs=[
             -0.0596034019, 0.0349356173, -4.39856077e-05, 2.87275485e-08,
             -7.52218426e-12, -30897.91801762719, -0.905182754], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             12.0728775, -0.00664305447, 1.17919653e-05, -6.23770047e-09,
             1.11168262e-12, -33819.0485176272, -61.52689], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -2.862 eV.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 174,
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
            NASAPolynomial(coeffs=[
             1.28038311, 0.0261463906, -3.32047308e-05, 2.1735497e-08,
             -5.73948875e-12, -19994.43113943153, -6.26697041], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             10.2004371, -0.00438798391, 7.85384852e-06, -4.20515081e-09,
             7.56900202e-13, -22147.60683943153, -50.8566505], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.035 eV.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 175,
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
            NASAPolynomial(coeffs=[
             1.13821321, 0.0282308741, -3.84375643e-05, 2.68682199e-08,
             -7.51932891e-12, -19354.15448304365, -5.62233584], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             10.261952, -0.00431697326, 7.73409668e-06, -4.14491544e-09,
             7.46254072e-13, -21494.35598304365, -50.9135576], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: 0.280 eV.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 176,
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
            NASAPolynomial(coeffs=[
             0.732881822, 0.0322634231, -3.77959035e-05, 2.39865566e-08,
             -6.16155738e-12, -4696.842155610184, 1.35885516], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             13.000137, -0.0085570909, 1.50757986e-05, -7.88551105e-09,
             1.39206697e-12, -7720.448975610184, -60.2600619], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -2.374 eV.

            The two lowest frequencies, 37.4 and 56.0 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 177,
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
            NASAPolynomial(coeffs=[
             0.846156622, 0.0305167786, -4.18817275e-05, 3.03845873e-08,
             -8.77242029e-12, 4411.514764764546, 1.70061405], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             11.0715759, -0.00635951594, 1.12239817e-05, -5.88249981e-09,
             1.03983295e-12, 2026.6608527645458, -48.9746741], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.405 eV.

            The two lowest frequencies, 24.2 and 51.1 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 178,
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
            NASAPolynomial(coeffs=[
             -1.7583011, 0.0420264164, -5.60075709e-05, 3.82518529e-08,
             -1.04094164e-11, 2017.6155546592354, 5.85343299], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             12.0774744, -0.00693996003, 1.23652357e-05, -6.57652822e-09,
             1.17675905e-12, -1236.0471053407646, -62.8944956], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.627 eV.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 179,
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
            NASAPolynomial(coeffs=[
             -0.140583135, 0.0339593004, -4.87797333e-05, 3.54552666e-08,
             -1.02284292e-11, 10491.702147874246, -0.98566238], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             10.2447852, -0.00442304397, 7.94052752e-06, -4.26592023e-09,
             7.69472791e-13, 8121.4686678742455, -52.2121115], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.462 eV.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 180,
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
            NASAPolynomial(coeffs=[
             0.824292443, 0.0260175022, -3.76424613e-05, 2.85388931e-08,
             -8.61619109e-12, 10978.84684534906, 0.771836536], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             9.10136599, -0.00456807185, 8.15499965e-06, -4.34420901e-09,
             7.779506e-13, 9070.687205349062, -40.1048198], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.459 eV.

            The two lowest frequencies, 54.1 and 75.0 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 181,
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
            NASAPolynomial(coeffs=[
             0.308794263, 0.0232270733, -3.55698494e-05, 2.77535744e-08,
             -8.5854622e-12, 16343.102154074131, 2.81137857], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             7.11559913, -0.00280516951, 5.13269765e-06, -2.82900391e-09,
             5.20007112e-13, 14809.453754074131, -30.6095689], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -2.145 eV.

            The two lowest frequencies, 88.1 and 88.1 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 182,
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
            NASAPolynomial(coeffs=[
             0.569719655, 0.0268881696, -2.50562761e-05, 1.14633679e-08,
             -1.86725635e-12, -30115.151614848273, -3.35425312], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             11.97405, -0.007721484, 1.38176784e-05, -7.40522422e-09,
             1.33270445e-12, -33095.48421484827, -61.4703595], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -2.676 eV.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 183,
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
            NASAPolynomial(coeffs=[
             -1.46588822, 0.0403267261, -5.16776687e-05, 3.37840088e-08,
             -8.78536827e-12, 7597.709411190753, 4.13713622], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             12.1581859, -0.00688771672, 1.22864756e-05, -6.54894795e-09,
             1.17381288e-12, 4350.878231190753, -63.7877393], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.126 eV.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 184,
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
            NASAPolynomial(coeffs=[
             1.67175843, 0.0241961042, -3.02241262e-05, 1.98954137e-08,
             -5.34017969e-12, -26830.046491412915, -7.69026459], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             10.1803718, -0.00463831947, 8.31985413e-06, -4.4687505e-09,
             8.05814447e-13, -28907.599291412913, -50.3183604], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.349 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 185,
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
            NASAPolynomial(coeffs=[
             1.68597603, 0.0252964778, -3.43987454e-05, 2.47264772e-08,
             -7.16814108e-12, 11114.442344299458, -8.13093966], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             10.1221165, -0.00468040411, 8.37773366e-06, -4.48321178e-09,
             8.05810286e-13, 9115.548434299457, -50.0740161], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -1.454 eV.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 186,
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
            NASAPolynomial(coeffs=[
             2.22982508, 0.0285706262, -1.49633224e-05, -5.17615158e-10,
             2.38101552e-12, -8239.810834770431, -3.88140044], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             17.6621705, -0.0137670445, 2.46103337e-05, -1.31714514e-08,
             2.36652085e-12, -12528.181654770431, -83.7118545], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.582 eV.

            The two lowest frequencies, 12.0 and 57.8 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 187,
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
            NASAPolynomial(coeffs=[
             2.36068306, 0.0141657352, -1.89200306e-05, 1.38011347e-08,
             -4.17869558e-12, -2037.9883122881213, -5.69573544], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             7.21381437, -0.00256957555, 4.70490156e-06, -2.59884578e-09,
             4.78532133e-13, -3229.8920622881215, -29.994781], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -3.125 eV.

            The two lowest frequencies, 67.9 and 67.9 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 188,
    label = "XNN",
    molecule =
"""
1 X  u0  p0  c0  {2,D}
2 N  u0  p0  c+1  {1,D}, {3,D}
3 N  u0  p2  c-1  {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[
             2.86330453, 0.0044727379, -7.65788825e-06, 7.56655132e-09,
             -2.82403094e-12, -3451.405740958081, -7.40114657], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             4.41139674, -0.00160318406, 2.88800786e-06, -1.55632395e-09,
             2.80777974e-13, -3817.0786409580815, -15.0272586], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.090 eV.

            The two lowest frequencies, 56.8 and 56.8 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 189,
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
            NASAPolynomial(coeffs=[
             2.92356214, 0.0106821592, -1.25081953e-05, 8.48134994e-09,
             -2.47957557e-12, -5864.240322364489, -2.17670553], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             7.08621605, -0.00280516119, 5.09896037e-06, -2.79091167e-09,
             5.10196893e-13, -6932.175002364489, -23.23758], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: -0.287 eV.

            The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 190,
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
            NASAPolynomial(coeffs=[
             2.36621691, 0.0190207407, -2.6531518e-05, 1.90189564e-08,
             -5.52564938e-12, 236.14436131737966, -10.6646849], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             8.33416082, -0.00232001212, 4.27361295e-06, -2.38022238e-09,
             4.41207352e-13, -1173.3767786826206, -40.3102482], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: 0.092 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 191,
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
            NASAPolynomial(coeffs=[
             1.33103899, 0.0241467477, -3.50637586e-05, 2.52901973e-08,
             -7.2690326e-12, 5468.8807518346475, -6.60866925], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
             8.42068601, -0.00211968435, 3.92392411e-06, -2.19955314e-09,
             4.09820147e-13, 3853.2225718346476, -41.5660882], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Kirk Badger at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=1e-3. DFT binding energy: 0.583 eV.
""",
    metal = "Pt",
    facet = "111",
)

