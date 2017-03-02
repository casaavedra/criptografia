from mido import MidiFile, Message, MidiTrack

mid = MidiFile('song_encoded.mid')

count_pc = 0

for i, tracks in enumerate(mid.tracks): 
    j = 0   
    while j < len(tracks):
        if (tracks[j].type == 'program_change'):
            if (tracks[j+1] is not None) & (tracks[j+1].type == 'program_change'):
                if (tracks[j+2] is not None) & (tracks[j+2].type == 'program_change'):
                    letter_l = tracks[j].program
                    letter_h = tracks[j+1].program << 4
                    letter_byte = letter_h | letter_l
                    letter = bytes([letter_byte]).decode('utf-8')
                    print(letter)
                    count_pc +1
                    j = j + 2 
        j += 1
