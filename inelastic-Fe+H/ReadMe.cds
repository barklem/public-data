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

Byte-by-byte Description of file: *_K.rates, *_K.min and *_K.max
--------------------------------------------------------------------------------
   Bytes Format    Units  Label         Explanations
--------------------------------------------------------------------------------
  1-2483 191E13.3   cm+3/s  ratec       Rate coefficient (1)   
--------------------------------------------------------------------------------
Note (1): The files are in the form (row,column) = (final state, initial state), 
as defined by the labels in states.dat.
================================================================================
(End)          Paul Barklem [Uppsala University, Sweden]             11-Jan-2018
