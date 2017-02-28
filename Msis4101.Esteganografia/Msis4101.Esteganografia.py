from mido import MidiFile, Message

mid = MidiFile('song.mid')
mid_new = MidiFile()

mystring = 'HOLAMUNDO'
b = mystring.encode('utf-8')

for i, track in enumerate(mid):
    mid_new.tracks.append(track)
    count_pc = 0
    if track.type == 'program_change':
        new_program = bytes([b[count_pc]]) + bytes([track.program])
        int_new_program = int.from_bytes(new_program, byteorder='big')
        print('Track {}: {}, {}'.format(i, track.type, track.program))    
        print('Track {}: {}, {}'.format(i, track.type, int_new_program))
        track.program = int_new_program
        count_pc +1

mid.save('song3_copy.mid')


split_letters = []
for letter in b:
    hex_letter = hex(letter)
    hi_hex_letter = hex_letter & 0x0F
    split_letters.append(letter[:3])
    split_letters.append(letter[3:])


        