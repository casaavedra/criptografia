from mido import MidiFile, Message, MidiTrack

mid = MidiFile('song.mid')
mid_new = MidiFile()
mid_new.tracks = mid.tracks
mid_new.ticks_per_beat = mid.ticks_per_beat

mystring = 'HOLA'

letter_count = 0

for i, tracks in enumerate(mid_new.tracks): 
    j = 0   
    while j < len(tracks):
        track = tracks[j]
        j += 1
        if track.type == 'program_change':
            if letter_count < len(mystring):
                letter = mystring[letter_count]
                letter_byte = int.from_bytes(letter.encode('utf-8'), byteorder='big')     
                letter_l = letter_byte & 0x0f
                letter_h = (letter_byte & 0xf0) >> 4
                tracks.insert(j-1, Message('program_change', program=letter_l, time=0))
                tracks.insert(j, Message('program_change', program=letter_h, time=0))
                letter_count = letter_count +1
                j = j + 2

print('Mensaje insertado')
mid_new.save('song_encoded.mid')