10 goto 650

20 rem ## init sound ##
30 f0=55
40 d=4.101
50 s=54272
60 wf=32
70 ad=0
80 sr=240
90 tm=1200
100 ml=200:rem max notes
110 nc=20:rem note count
120 FOR sw=s to s+24:poke sw,0:next sw
130 POKE S+24,15
140 POKE S+2,0
150 POKE S+3,0
160 POKE S+5,ad
170 POKE S+6,sr
180 return

190 rem ## read music data ##
200 dim fh%(ml):dim fl%(ml):dim dr%(ml):dim m%(nc):m%(0)=0
210 l=0:o=0:j=0:p=0
220 read t$:rem print t$
230 if t$="end" then return
240 i=1
250 if i>len(t$) then 220
260 k=0
270 a$=mid$(t$,i,1)
280 n=asc(a$)-65
290 b$=mid$(t$,i+1,1)
300 bc$=mid$(t$,i+1,2)
310 if a$=" " or a$="," then i=i+1:goto 250
320 if a$="." then i=i+1:j=j+1:p=p+1:m%(p)=j:goto 250
330 if a$="l" then l=int(tm/val(bc$)):i=i+3:goto 250
340 if a$="o" then o=val(b$):i=i+2:goto 250
350 if a$="a" or a$="b" then k=1
360 if a$="b" or a$="c" then n=n+1
370 if a$="d" then n=n+2
380 if a$="e" or a$="f" then n=n+3
390 if a$="g" then n=n+4
400 if b$="+" or b$="#" then n=n+1:i=i+1
410 if b$="-" then n=n-1:i=i+1
420 n=n+(o+k)*12
430 if a$="p" then f=0:goto 450
440 f=int(f0*2^(n/12)*d)
450 fh%(j)=int(f/256):fl%(j)=int(f-256*fh%(j)):dr%(j)=l
460 j=j+1
470 i=i+1
480 goto 250

490 rem ## play music ##
500 i=m%(p)
510 poke s,fl%(i):poke s+1,fh%(i)
520 poke s+4,wf+1
530 for t=1 to dr%(i):next
540 poke s+4,wf
550 i=i+1
560 if dr%(i)<>0 then 510
570 return

580 data o3l12cdedcdl05ecc.
590 data o3l09bl16pbaapbpbpbaaapl09bl16pbaapb.
600 data o4l04pl09e-l16pe-d-d-pe-pe-pe-d-d-d-pl09e-l16pe-d-d-pe-.
610 data o4l04pl09g-l16pg-eepg-pg-pg-eeepl09g-l16pg-eepg-.
620 data o4l04pl09bl16pbaapg-pg-pg-eeepo3l09bl16pbaapb.
630 data o2l25efgefdc.
640 data end

650 print "init"
660 gosub 20:rem init sound
670 print "converting..."
680 gosub 190:rem read music data
690 print "playing..."
700 for p=0 to 5
710 gosub 490
720 next
