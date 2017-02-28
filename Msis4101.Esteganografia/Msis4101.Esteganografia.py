from mido import MidiFile, Message, MidiTrack

mid = MidiFile('song.mid')
mid_new = MidiFile()
mid_new.tracks.append(mid.tracks)

mystring = 'HOLAMUNDO'
letter_count = 0
b = mystring.encode('utf-8')

for i, track in enumerate(mid):    
    count_pc = 0
    if track.type == 'program_change':       
        letter = mystring[letter_count] 
        new_program = int.from_bytes(letter.encode('utf-8'), byteorder='big')
        new_program_l = new_program & 0x0f
        new_program_h = (new_program & 0xf0) >> 4
        track_new = MidiTrack()   
        mid_new.tracks.append(track_new)     
        mid_new.tracks.append(Message('program_change', program=128, time=0))
        mid_new.tracks.append(Message('program_change', program=new_program_h, time=0))
        print('Track {}: channel {}, program {}'.format(i, track.channel, hex(track.program)))    
        count_pc +1
    mid_new.tracks.append(track)

mid_new.save('song3_copy.mid')







        