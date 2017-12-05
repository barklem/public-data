+;---------------------------------------------------------------------
; This routine loads the synthetic profiles
;
PRO Loadprofile,filename,wlgrid,profile
openr,1,filename
s='' & nl=0
readf,1,s
nl=fix(s)
for i=1,nl do begin
  readf,1,s
endfor
readf,1,nwl,tmp
w=dblarr(2,nwl)
readf,1,w
close,1
wlgrid=dblarr(nwl)
profile=dblarr(nwl)
wlgrid=reform(w(0,*))
profile=reform(w(1,*))
end
