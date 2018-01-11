J/A+A/vol/page   Inelastic Fe+H collision data                     (Barklem 2018)
================================================================================
Excitation and charge transfer in low-energy hydrogen atom collisions with 
neutral iron
P. S. Barklem
    <Astron. Astrophys. vol, page (2018)>
    =2018A&A...VVV.ppppB     (SIMBAD/NED BibCode)
================================================================================
Keywords: atomic data --- line: profiles

Description:
  The file states.dat lists the considered states.  The remaining files then
  provide the rate coefficients and "fluctuations". 

File Summary:
--------------------------------------------------------------------------------
  FileName   Lrecl  Records   Explanations
--------------------------------------------------------------------------------
ReadMe          80        .   This file
table1.txt     102      228   Input data for calculations; full table 1
states.dat      27      191   States and their energies
*_K.rates     2483      191   Rate coefficients from LCAO model
*_K.min       2483      191   Minimum rate coefficients from alternate models
                              (so-called "fluctuations")
*_K.max       2483      191   Maximum rate coefficients from alternate models
                              (so-called "fluctuations")
--------------------------------------------------------------------------------

Byte-by-byte Description of file: states.dat
--------------------------------------------------------------------------------
   Bytes Format Units           Label   Explanations
--------------------------------------------------------------------------------
   1- 3   I3    ---             index   index
   4- 15  A12   ---             label   term label
  16- 27  F12.3 cm-1            E       term energy in 1/cm         
--------------------------------------------------------------------------------

Byte-by-byte Description of file: table1.txt (1)
--------------------------------------------------------------------------------
   Bytes Format Units   Label   Explanations
--------------------------------------------------------------------------------
   1- 10  A10   ---     state   state label
  11- 17   I7   ---     L_A     electronic orbital angular momentum
  18- 24   I7   ---     2S_A+1  electronic spin multiplicity
  25- 31   I7   ---     n       principal quantum number for the active electron
  32- 38   I7   ---     l       orbital angular momentum quantum number for the
                                active electron
  39- 45   I7   cm-1    E_j^X   term energy in 1/cm  
  46- 52   I7   cm-1    E_lim   series limit energy in 1/cm  
  53- 59   I7   cm-1    E_j     asymptotic molecular energy in 1/cm   
  60- 66   I7   cm-1    N_eq    number of equivalent active electrons
  67- 77  A11   ---     Core    label for core
  78- 84   I7   ---     L_c     core electronic orbital angular momentum
  85- 91   I7   ---     2c_A+1  core electronic spin multiplicity
  92-102 F10.3  ---     G       coefficient of fractional parentage
--------------------------------------------------------------------------------
Note (1): The labels are given in the first record in text format

Byte-by-byte Description of file: *_K.rates, *_K.min and *_K.max
--------------------------------------------------------------------------------
   Bytes Format    Units  Label         Explanations
--------------------------------------------------------------------------------
  1-2483 191E13.3   cm+3/s  ratec       Rate coefficient (2)   
--------------------------------------------------------------------------------
Note (2): The files are in the form (row,column) = (final state, initial state), 
as defined by the labels in states.dat.
================================================================================
(End)          Paul Barklem [Uppsala University, Sweden]             11-Jan-2018
