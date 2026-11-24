# MIDI Control

Some V-90 programs respond to MIDI notes, as on the original unit:

| Program | Plug-in | What MIDI notes do | Turn it on with |
|---|---|---|---|
| Pitch Change A | V-90 Pitch Change | Set the pitch | BASE KEY (not OFF) |
| Pitch Change D | V-90 Pitch Change | Set the pitch | BASE KEY (not OFF) |
| Reverb & Gate | V-90 Reverbs | Open the gate | MIDI TRG. = ON |
| Delay Vibrato | V-90 Modulations | Start the vibrato | MIDI TRG. = ON (the default) |

## Playing the Pitch from a Keyboard

In Pitch Change A and D, a MIDI note sets **PITCH** to the note's distance in semitones from **BASE KEY**. With BASE KEY at C3 (the default), C3 plays the original pitch, G3 plays a fifth up and C2 an octave down. The pitch is limited to ±12 semitones.

Set BASE KEY to **OFF** to ignore MIDI notes.

The PITCH value the note sets shows on the LCD and in your DAW, so you can record it as automation.

!!! note
    BASE KEY C3 is MIDI note 60 (middle C).

## Triggering with MIDI

Reverb & Gate's gate and Delay Vibrato's vibrato are normally triggered by the input level (TRG. LEVEL). With **MIDI TRG.** set to **ON**, a MIDI note-on triggers them instead, at the exact time of the note. Use this to trigger the effect in time with the music, independently of the audio.

## Sending MIDI to the Plug-In

How you route MIDI to an effect plug-in depends on your DAW.

=== "Pro Tools"

    1. Create a MIDI track.
    2. Set the MIDI track's output to the V-90 plug-in (it is listed by the plug-in's name and insert).
    3. Record or draw the notes on the MIDI track.

=== "Other DAWs"

    Route a MIDI track's output to the V-90 plug-in, if your DAW supports MIDI input to effect plug-ins. See your DAW's documentation for sending MIDI to an audio effect.

AAX DSP: MIDI control on AAX DSP is new in version 1.1.0.4.
