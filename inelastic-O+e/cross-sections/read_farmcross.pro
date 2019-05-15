pro read_farmcross, filein, struct, elem=elem


if not keyword_set(elem) then elem = 'O'

name = string(replicate(32B,20))  ; 20 blanks
title = string(replicate(32B,80))  ; 80 blanks

nelc = 0l
nz = 0l
ntarg = 0l

openr, unit, filein, /GET_LUN

readf, unit, name, title, format = '(a20,a80)'
POINT_LUN, -1*unit, pos
readf, unit, nelc, nz, ntarg
POINT_LUN, unit, pos

etarg = dblarr(ntarg)
ltarg = lonarr(ntarg)
starg = lonarr(ntarg)

readf, unit, nelc, nz, ntarg, etarg, ltarg, starg

nxsn = 0l
nume1 = 0l

readf, unit, nxsn, nume1
sce1 = dblarr(nume1)
xsn = dblarr(nxsn,nume1)
readf, unit, sce1
readf, unit, xsn

FREE_LUN, unit 

; reformat xsn into a square array [energy, initial, final]
; note: forward xsects only available

xsn2 = dblarr(nume1, ntarg, ntarg)

it = -1
for iif = 0, ntarg-1 do begin
  for ii = 0, iif do begin
    it = it + 1
    xsn2[*,ii,iif] = xsn[it,*] * 2.80028e-17
  endfor
endfor

; no parity info, we have to supply it or know it
; default assumes oxygen

ptarg = ltarg * 0            
n = n_elements(ltarg)
ptt = [0,0,0,1,1,0,0,1,1,1,1,0,0,1,1,1,1,0,0]  ; oxygen
if elem eq 'Li' then ptt = [0,1,0,1,0,0,1,0,1]
nn = n_elements(ptt)
if n ge nn then begin
  ptarg[0:nn-1] = ptt  
endif else begin
  ptarg[0:n-1] = ptt[0:n-1]
endelse

; no config info
; default assumes oxygen
cfg = strarr(n)
cfgi = strarr(n)
cfs = ['2p$^4$','2p$^4$','2p$^4$','3s','3s','3p','3p','4s','4s','3d','3d', $
       '4p','4p','3s','3s','4d','4d','4f','4f']  ; latex
cfsi =['2p!e4!n','2p!e4!n','2p!e4!n','3s','3s','3p','3p','4s','4s','3d','3d', $
       '4p','4p','3s','3s','4d','4d','4f','4f']  ; idl
nn = n_elements(cfs)
if n ge nn then begin
  cfg[0:nn-1] = cfs  
  cfgi[0:nn-1] = cfsi  
endif else begin
  cfg[0:n-1] = cfs[0:n-1]
  cfgi[0:n-1] = cfsi[0:n-1]
endelse

Z = max([1,nz - nelc])

struct = { NZED: nz, NELC: nelc, NAST: ntarg, $
           IL: ltarg, IG: starg, IP: ptarg, ENAT: (etarg - etarg[0])*2., $
	   ETOT: sce1*Z^2., CROSS: xsn2, CFG: cfg, CFGI: cfgi }

; sce1 is scaled energy = E/(Z)^2
; xsn is in square bohr ; we change to cm^2
; etarg originally in au -> ryd, plus rezero to ground state

return
end 
