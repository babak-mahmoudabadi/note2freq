# note2freq

This program is C64 BASIC source code generator and imitates a simple form of QBaisc PLAY command. You should create a file as input that contains some commandstrings.  <br>

commandstring is a stringexpression that contains music commands that are:<br>

- On	Sets current octave (n = 0-9)
- A-G	Plays A, B, ..., G in current octave (+ = sharp, - = flat note)
- Lnn	Sets length of a note (L01 is whole note, L04 is quarter note, etc.) n = 01-99
- P		Pause  
- .		End of a music segment

for example: O3L12CDEDCDL05ECC. is a commandstring. <br>
After create input file, you should run following command for generate BASIC source code: 
python note2freq.py NoteFileName OutputFileName

refrences:
http://techlib.com/reference/musical_note_frequencies.htm