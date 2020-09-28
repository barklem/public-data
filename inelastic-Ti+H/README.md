**Archive:** Ti+H rate coefficients  

**Publication:**  
*Excitation and charge transfer in low-energy hydrogen atom collisions with neutral manganese and titanium*  
J. Grumer, P. S. Barklem A&A 637, A28 (2020)  
DOI: https://doi.org/10.1051/0004-6361/201937434

File               | Description
-------------------|--------------------------------------------------------------------------------------------------------
`table2.tex`       | LaTeX table with calculation input data
`table4.tex`       | LaTeX table with state labels and energies [cm-1]
`states.dat`       | ASCII file with state labels and energies [cm-1]
`rates/*_K.rates`  | Rate coefficients (**all**) [cm3/s]: **matrix form** (row, column) = (final, initial)
`rates/*_K.rat`    | Rate coefficients (**endothermic**) [cm3/s]: **list form** (by inital state into final states of higher energy)

States are defined (and ordered for the matrix form) according to the list in `states.dat` or `table4`.tex.  
The number in `table#.tex` correspond to the table numbering in the article.

Jon Grumer, April 2020
