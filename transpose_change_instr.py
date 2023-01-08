from music21 import *
import sys
import mido
from mido import Message, MidiFile, MidiTrack

def midi_trans_instr(file_path, semitones, program_change):
    #convert midi or xml to stream
    piece = converter.parse(file_path)
    #loop through the parts
    for i in range(len(piece.parts)):
        #loop through the pitches
        for j in range(len(piece.parts[i].pitches)):
            p0 = piece.parts[i].pitches[j]
            p0.transpose(semitones, inPlace=True)

    mid = MidiFile(file_path)
    track = MidiTrack(mid)
    # change the instrument
    track.append(Message('program_change', program = program_change,
                     channel = 0))
    track.append(Message('program_change', program = program_change,
                     channel = 1))
    mid.save('new_sample.mid')

# fetching the arguments
arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]
  
# calling the function
midi_trans_instr(arg1, arg2, arg3)
