Adsorbate_thermo:

The Adsorbate_Thermo/O directory includes a sample input file for H2OX. The compute_NASA notebook generates cti entries for the species listed the in species_list.dat files. 
The current setup assumes that the species input files are in directories with the name of the respective surface adatom (specified at the bottom of the notebook with the "element" keyword).

TST_evaluation:

This includes example input files for surface reaction HCCH3* + * + * -> HCCH2** + H* (* denotes surface site).
The input files are located in TST_evaluation/Initial_State/C/ and TST_evaluation/Transition_State/C.
First, run the notebooks for the initial state and final state to obtain the harmonic approximation partition functions q vs T (the output .txt files - examples included in TST_evaluation/Initial_State/ and ST_evaluation/Transition_State/).
Then, run the Arrhenius_coefficients.ipynb notebook to obtain fitted Arrhenius coefficients based on the calculated TST rate constant k(T).
