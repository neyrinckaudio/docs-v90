# Release Notes

## Version 1.1.0.4

* **AAX DSP** for V-90 Reverbs, V-90 Pitch Change and V-90 Modulations, as for V-90 Symphonic: on Pro Tools HDX systems they can run on the DSP. Each needs one DSP chip at 96 kHz.
* On DSP, Reverbs takes a parameter change 4 samples later than AAX Native does, and a Memory change is silent for about 0.2 ms; Pitch Change's Memory change is silent for about 33 ms.
* Memory, Reflections' Type, Modulations' Direction and Pitch Change's Base Key are now discrete parameters, and MIDI Trigger and Bypass are on/off switches, so hosts show them as lists or switches and never ramp them.
* A Memory now starts from its current settings when it was changed while another Memory played or while bypassed.

**Known issues**

* V-90 Reflections is AAX Native only (no AAX DSP).
* AU automation recorded with earlier versions on the parameters that are now discrete may play back rescaled.
* VST automation in sessions saved with 1.1.0.2 may not match its parameters, which have changed.

## Version 1.1.0.3

**New plug-ins in addition to V-90 Symphonic**

* **V-90 Reverbs**: Rev 1 Hall, Rev 2 Room, Rev 3 Vocal, Rev 4 Plate and Reverb & Gate.
* **V-90 Reflections**: Early Ref. 1, Early Ref. 2, Gate Reverb and Reverse Gate.
* **V-90 Pitch Change**: Pitch Change A, B, C and D. Pitch Change A and D follow MIDI notes (BASE KEY).
* **V-90 Modulations**: Delay L,R, Stereo Echo, Stereo Flange A and B, Chorus A and B, Stereo Phasing, Tremolo, Auto Pan and Delay Vibrato. Delay Vibrato can be triggered by MIDI notes.

The V-90 Complete installer installs all five, as AAX, AU and VST 3 on macOS and AAX, VST and VST 3 on Windows.

**Changes since 1.1.0.2**

* Reverbs, Reflections, Pitch Change and Modulations no longer have an Out Level parameter; it is fixed at 100 %, as in Symphonic.
* Their parameters start with Memory, Input and Balance and end with Bypass, and are named in title case ("Room Size").
* They are listed in more specific host categories: Reverb, Pitch Shift, and Modulation and Delay.
* Smaller plug-ins.

## Version 1.1.0.1

* Every V-90 plug-in now shares one version number.
* New plug-ins: V-90 Reverbs, V-90 Pitch Change and V-90 Modulations.

## V-90 Symphonic 1.0.2.3

* Smaller download: the plug-ins are about a third of their previous size.
* Fixed a short fade-in when playback or rendering starts.
* Improved AAX compatibility: the AAX Native and AudioSuite plug-ins no longer declare DSP-only settings.

## V-90 Symphonic 1.0.2

* Fixed a short fade-in when playback or rendering starts.

## V-90 Symphonic 1.0.1

* Fixed AAX DSP loading on Mac.
