# Signal Flow and Track Formats

## Track Formats

The V-90 plug-ins are:

* **Mono-to-stereo:** insert on a mono track; the track becomes stereo after the plug-in.
* **Stereo-to-stereo:** insert on a stereo track, aux or bus.

## Mono Input, Stereo Output

Like the original unit, each program has a mono input and a stereo output. On a stereo track, the plug-in sums the left and right inputs to mono before the effect. The stereo image you hear comes from the effect: the reverb, the left and right delays, the panning and so on.

```
 Left  ─┐                                       ┌─ Left
        ├─ sum ─ INPUT ─┬─ effect ─┬─ BALANCE ──┤
 Right ─┘               └── dry ───┘            └─ Right
```

At BALANCE 0 % you hear the dry signal: the mono sum, after the INPUT knob. Use **BYPASS** to hear the original stereo input unchanged.

## BALANCE and Effect Returns

BALANCE mixes the dry and effect sound:

| Use | BALANCE |
|---|---|
| Effect return (aux or bus fed by sends) | 100 % |
| Insert on a track | To taste |

Some programs start with BALANCE below 100 % (Stereo Flange A at 50 %, Stereo Flange B at 75 %), as on the unit.

## Output Level

The plug-ins have no output level control. The output is at the original unit's 100 % output level.
