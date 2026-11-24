import json,re,os
V=os.environ.get('V90_SRC','/Users/pneyrinck/Code/ncontrol_symph_1_0/internal/N-Control/V90')+'/'
import os
HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(HERE,'..','docs','plugins')+'/'
TPL=os.path.join(HERE,'templates')+'/'
cat=json.load(open(os.environ.get('SPX90_CATALOG',V+'../../../modules/spx90/lib/generated/programs.json')))
tables={p['id']:p for p in cat['params']}
def val(line):
    v=line.split('=',1)[1].strip()
    v=v.replace('\x7f-','←-').replace('-~','-→').replace('\x7f~','↔').replace('←-R','← R').replace('L-→','L →')
    v=re.sub(r'\s+',' ',v)
    v=v.replace('+ ','+').replace('- ','-') if re.match(r'^[+-] ',v) else v
    return v.replace('THRU','Thru').replace('OFF','Off').replace('ON','On').replace('HALL','Hall').replace('RANDOM','Random').replace('REVERSE','Reverse').replace('PLATE','Plate')
def dirtext(v):
    return {'L-→R':'L → R','L←-R':'L ← R','L↔R':'L ↔ R'}.get(v.replace(' ',''),v)
DESC={
 'balance':'Mix of dry and effect sound. 0 % is dry only, 100 % is effect only. Use 100 % when the plug-in is on an effect return.',
 'revTime':'Reverb time: how long the reverb takes to decay by 60 dB.',
 'high':'High-frequency reverb time, as a ratio of REV TIME. Lower values make the highs die away sooner, for a darker, more natural decay.',
 'delay500':'Initial delay before the reverb starts.',
 'hpf':'High-pass filter on the effect sound. THRU is off.',
 'lpf':'Low-pass filter on the effect sound. THRU is off.',
 'trgLevel':'Input level that triggers the effect. Lower values trigger on quieter signals.',
 'hold':'How long the gate stays open after it is triggered.',
 'release':'How long the gate takes to close after HOLD.',
 'midiTrg':'When ON, a MIDI note-on triggers the effect instead of the input level.',
 'type':'Reflection pattern: HALL, RANDOM, REVERSE or PLATE.',
 'roomSize':'Spacing of the reflections. Larger values sound like a larger space and spread the reflections over a longer time.',
 'liveness':'Decay of the reflections: 0 is a dead room (the reflections die away), 10 a live room (they stay strong).',
 'delay4000':'Initial delay before the reflections start.',
 'lchDly5000':'Left channel delay time.','rchDly5000':'Right channel delay time.',
 'lchDly2500':'Left channel delay time.','rchDly2500':'Right channel delay time.',
 'lchFb':'Left channel feedback: the number of repeats. Negative values invert the polarity of the feedback.',
 'rchFb':'Right channel feedback: the number of repeats. Negative values invert the polarity of the feedback.',
 'modFrq':'Modulation speed.',
 'modDepth':'Modulation depth.',
 'modDly1000':'Base delay that the modulation sweeps around.',
 'modDly80':'Base delay that the modulation sweeps around.',
 'fbGain':'Feedback: how much of the effect is fed back into it. Higher values give a more pronounced, resonant effect.',
 'dmDepth':'Delay modulation depth: how far the pitch of the chorus voices wanders.',
 'amDepth':'Amplitude modulation depth: how much the level of the chorus voices varies.',
 'panSpeed':'Speed of the panning.',
 'direction3':'Direction of the panning: L → R, L ← R, or L ↔ R (back and forth).',
 'depth':'Width of the panning.',
 'vibDly':'Time from the trigger to the start of the vibrato.',
 'vibRise':'Time the vibrato takes to reach full depth.',
 'vibFrq':'Vibrato speed.',
 'vibDepth':'Vibrato depth.',
 'pitch':'Pitch shift in semitones, ±1 octave.','fine':'Fine pitch shift, in cents (1/100 semitone).',
 'pitch1':'Voice 1 pitch shift in semitones.','fine1':'Voice 1 fine pitch shift, in cents.','dly1':'Voice 1 delay.',
 'pitch2':'Voice 2 pitch shift in semitones.','fine2':'Voice 2 fine pitch shift, in cents.','dly2':'Voice 2 delay.',
 'lPitch':'Left channel pitch shift in semitones.','lFine':'Left channel fine pitch shift, in cents.','lDly':'Left channel delay.',
 'rPitch':'Right channel pitch shift in semitones.','rFine':'Right channel fine pitch shift, in cents.','rDly':'Right channel delay.',
 'baseKey':'The MIDI note that plays the pitch unshifted. A MIDI note sets PITCH to its distance from BASE KEY. OFF ignores MIDI notes. See [MIDI Control](../using/midi.md).',
}
def table(plug,f,num):
    src=open(V+plug+'/Source/'+f+'.cpp').read()
    pdefs=re.findall(r'\{ "(\w+)", "([^"]+)", "([^"]+)", (\d+), spx90::programs::(\w+), (\w+), (\w+) \}',src)
    for t in re.finditer(r'\{ (\d+), "([^"]+)", (\d+), (\d+),\s*\{([^}]*)\},\s*\{([^}]*)\},\s*\{([^}]*)\} \}',src):
        if int(t.group(1))!=num: continue
        order=[x.strip() for x in t.group(5).split(',')]
        tabs=[x.strip().replace('spx90::programs::','') for x in t.group(6).split(',')]
        defs=[int(x) for x in t.group(7).split(',')]
        rows=['| Parameter (LCD) | Host name | Range | Default | Description |','|---|---|---|---|---|']
        for o,tb in zip(order,tabs):
            pi=[i for i,p in enumerate(pdefs) if p[0].lower()==o.lower() or p[4]==o or p[0]==o.lower().replace('ertype','type')][0]
            T=tables[tb]; L=T['lines']
            lo,hi=val(L[0]),val(L[-1])
            if tb in ('type',): rng='Hall, Random, Reverse, Plate'
            elif tb=='direction3': rng='L → R, L ← R, L ↔ R'
            elif tb=='midiTrg': rng='Off, On'
            elif tb=='baseKey': rng='Off, C1 – C6'
            else: rng=f'{lo} – {hi}'
            dv=val(L[defs[pi]])
            if tb=='direction3': dv='L → R'
            if tb=='baseKey': dv=dv.replace(' ','')
            name=T['name'].strip()
            desc=OVR.get((plug,tb),DESC.get(tb,''))
            rng=units(rng); dv=units(dv)
            rows.append(f'| **{name}** | {pdefs[pi][1]} | {rng} | {dv} | {desc} |')
        return '\n'.join(rows)
    raise Exception(num)
OVR={('PitchChange','delay4000'):'Delay of the shifted voice.',
 ('Modulations','high'):'High-frequency damping of the repeats: lower values make each repeat darker. 1.0 is no damping.'}
def units(v): return re.sub(r'(\d)(ms|kHz|Hz|s)\b',r'\1 \2',v)
P={}
P['reverbs']=('Reverbs','ReverbTypes')
P['reflections']=('Reflections','ReflectionTypes')
P['modulations']=('Modulations','ModulationTypes')
P['pitch-change']=('PitchChange','PitchTypes')
import sys

def sub(m):
    key,num=m.group(1),int(m.group(2)); plug,f=P[key]; return table(plug,f,num)
for fn in ['reverbs','reflections','modulations','pitch-change']:
    s=open(TPL+fn+'.md.in').read()
    s=re.sub(r'\{\{table (\S+) (\d+)\}\}',sub,s)
    open(OUT+fn+'.md','w').write(s)
print('ok')
