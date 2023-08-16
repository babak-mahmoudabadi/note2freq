# note2freq for Commodore 64 - v1.0
# by Babak Mahmoudabadi

import sys

f0=55
d=4.101
tm=1200
l=0
o=0

def getFrequency(notestr):
    result=[]
    i=0
    while i < len(notestr):
        k = 0
        a = notestr[i]
        n = ord(a.lower())-97
        b = ""
        if i + 1 < len(notestr):
            b=notestr[i+1]
        bc = ""
        if i+1 < len(notestr)-1:
            bc=notestr[i+1:i+1+2]
        if a == "\r" or a == "\n": 
            i=i+1
            continue
        if a == " " or a == ",": 
            i=i+1
            continue
        if a == ".": 
            result.append((0, 0, 0))
            i=i+1
            continue
        if a == "l":
            l=int(tm/int(bc))
            i=i+3
            continue
        if a == "o":
            o=int(b)
            i=i+2
            continue
        if a == "a" or a == "b":
            k=1
        if a == "b" or a == "c":
            n=n+1
        if a == "d":
            n=n+2
        if a == "e" or a == "f":
            n=n+3
        if a == "g":
            n=n+4
        if b == "+" or b == "#":
            n=n+1
            i=i+1
        if b == "-":
            n=n-1
            i=i+1
        
        n=n+(o+k)*12
        
        if a == "p": 
            f=0
        else:
            f=int(f0*(2**(n/12))*d)
        
        fh=int(f/256)
        fl=int(f-256*fh)
        dr=l
        result.append((fh, fl, dr))
        i=i+1

    return result

def generateCode(data):
    rowno=10
    programLines=[
    "{0} rem ## this code was generated by note2freq.py ##\n",
    "{0} goto 290\n",
    "{0} rem ## init sid ## \n",
    "{0} s=54272 \n",
    "{0} wf=32 \n",
    "{0} FOR sw=s to s+24:poke sw,0:next sw \n",
    "{0} POKE S+24,15 \n",
    "{0} POKE S+2,0 \n",
    "{0} POKE S+3,0 \n",
    "{0} POKE S+5,0:rem ad \n",
    "{0} POKE S+6,240:rem sr \n",
    ]
 
    lines=[]
    for line in programLines:
        lines.append (line.format(rowno))
        rowno += 10
    
    lastrowno=rowno
    rowno=1000
    dataLines=[]
    noteCount=0
    temp=""
    comma=""
    for notestring in data:
        for note in notestring:
            if (noteCount%3)==0:
                temp="{} data ".format(rowno)
                comma=""
            else:
                comma=","
            temp=temp+"{}{},{},{}".format(comma, note[0], note[1], note[2])
            if (noteCount%3)==2:
                temp=temp+"\n"
                dataLines.append (temp)
            noteCount+=1
            rowno += 10
    if temp != "":
        dataLines.append (temp)
    rowno=lastrowno

    programLines=[

    "{0} dim fh%({1}):dim fl%({1}):dim dr%({1}):dim p%({2})\n",
    "{0} j=2 \n",
    "{0} for i=1 to {1} \n",
    "{0} read fh%(i), fl%(i), dr%(i)\n",
    "{0} if dr%(i)=0 and i<>{1} then p%(j)=i+1:j=j+1 \n",
    "{0} next \n",
    "{0} return \n",
    "{0} rem ## play seqment (j) ## \n",
    "{0} i=p%(j) \n",
    "{0} poke s,fl%(i):poke s+1,fh%(i) \n",
    "{0} poke s+4,wf+1 \n",
    "{0} for t=1 to dr%(i):next \n",
    "{0} poke s+4,wf \n",
    "{0} i=i+1 \n",
    "{0} if dr%(i)<>0 then 210 \n",
    "{0} return \n",
    "{0} rem ## program start ## \n",
    "{0} gosub 30:rem init sid \n",
    "{0} for j=1 to {2} \n",
    "{0} gosub 200:rem play seqment (j)\n",
    "{0} next \n",
    "{0} end \n",
    ]
  
    for line in programLines:
        lines.append (line.format(rowno,noteCount, len(data)))
        rowno += 10

    lines.extend(dataLines)

    return lines

def main():
    if len(sys.argv) < 3:
        print ("Invalid arguments!")
        print ("usage: python note2freq.py NoteFileName OutputFileName")
        exit()

    NoteFileName = sys.argv[1]
    OutputFileName = sys.argv[2]

    data=[]
    fr = open(NoteFileName, "r")
    for row in fr:
        data.append(getFrequency(row))
    fr.close()

    lines=generateCode(data)
    fw = open(OutputFileName, "w")
    for line in lines:
        fw.write (line)
    fw.close()

def test():
    rowno=10
    row=getFrequency("o3l12cdedcdl05ecc")
    for item in row:
        print ("{} data {},{},{}\n".format(rowno, item[0], item[1], item[2]))
        rowno = rowno + 10

main()