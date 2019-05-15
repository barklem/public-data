pro write_cross

read_farmcross, 'oxygen_finaltest_allautoplusL20.cross', a  ; read cross section data


;struct = { NZED: nz, NELC: nelc, NAST: ntarg, $
;           IL: ltarg, IG: starg, IP: ptarg, ENAT: (etarg - etarg[0])*2., $
;	   ETOT: sce1*Z^2., CROSS: xsn2, CFG: cfg, CFGI: cfgi }

; sce1 is scaled energy = E/(Z)^2
; xsn is in square bohr ; we change to cm^2
; etarg originally in au -> ryd, plus rezero to ground state



openw, 1,'oxygen_final_cross.dat

for j = 0, 18 do a.cross[*,j,j] = 0.d0  ; remove all elastic values

nume = n_elements(a.etot)

printf, 1, nume
for i = 0, nume-1 do begin
   printf, 1, a.etot[i]   ; ryd 
   printf, 1, transpose(a.cross[i,0:18,0:18]), format = '(19e10.3)'  ; only output spectroscopic states
endfor

close, 1

stop
end