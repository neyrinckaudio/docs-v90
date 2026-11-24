# Troubleshooting

## The plug-in window shows only a message about missing files

The plug-ins share their panel graphics, which the installer puts in a common folder. If those files are missing, the window shows what is missing instead of the panel. Run the V-90 Complete installer again.

## The plug-in does not appear in my DAW

* Check that your DAW supports one of the installed formats: AAX (Pro Tools), AU (macOS), VST 3, or VST (Windows).
* Rescan plug-ins in your DAW, or restart it.
* Look under the manufacturer name **Neyrinck Audio**, or in the Reverb, Modulation, Delay and Pitch Shift categories.

## The licensing window appears every time

The plug-in cannot find a license. Make sure the iLok USB key holding the license is connected, or that the license is activated on this computer, using iLok License Manager. See [Activating the License](../getting-started/licensing.md).

## I hear no effect

* Check that **BYPASS** is off (its light is off).
* Check **BALANCE**: at 0 % you hear only the dry signal.
* Check the **INPUT** knob and the meter: at 0 there is no signal.
* Reverb & Gate and Delay Vibrato are triggered effects. Check TRG. LEVEL, or, with MIDI TRG. ON, that MIDI notes reach the plug-in. See [MIDI Control](../using/midi.md).

## My stereo track sounds mono at BALANCE 0 %

This is how the original unit works: the input is summed to mono. Use **BYPASS** to hear the original stereo input. See [Signal Flow and Track Formats](../using/signal-flow.md).

## Pitch Change does not follow my MIDI notes

* Only Pitch Change A and D follow MIDI notes.
* Check that **BASE KEY** is not OFF.
* Check that the MIDI track's output is set to the plug-in.

## My edits to a program came back after switching programs

That is by design: each memory keeps its own settings. To return a memory to its factory settings, press **RECALL** while it plays, without choosing another memory first. See [Memories and Recall](../using/memories.md).

## Contact Support

If you need further help, contact Neyrinck support through [neyrinck.com](https://neyrinck.com).
