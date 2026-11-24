import json,sys
from PIL import Image,ImageDraw,ImageFont
import os
V=os.environ.get('V90_SRC','/Users/pneyrinck/Code/ncontrol_symph_1_0/internal/N-Control/V90')+'/'
R=V+'Common/Resources/'
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','docs','images')+'/'
S=2
def img(n): return Image.open(R+n).convert('RGBA')
def render(plugin,bg,mem,l1,l2,active='parameter',meter=4,input_=80,out=None,recall=False,bypass=False):
    lay={c['id']:c for c in json.load(open(V+plugin+'/layout.json'))['children']}
    im=img(bg)
    W,H=im.size
    # knob
    sp=img('input_sprite.png'); fw=sp.size[0]//101
    fr=sp.crop((fw*input_,0,fw*input_+fw,sp.size[1]))
    c=lay['Input']; fr=fr.resize((c['w']*S,c['h']*S),Image.LANCZOS); im.alpha_composite(fr,(c['x']*S,c['y']*S))
    d=ImageDraw.Draw(im)
    # meter
    c=lay['Meter']; x,y,w,h=[v*S for v in (c['x'],c['y'],c['w'],c['h'])]
    d.rectangle((x,y,x+w-1,y+h-1),fill='#1a1a1a')
    b=[x+2*S,y+2*S,x+w-2*S,y+h-2*S]; gap=2*S; bh=((b[3]-b[1])-gap*7)/8; bot=b[3]
    for i in range(8):
        col='#1c1c1f' if i>=meter else ('#FF8C00' if i>=5 else '#2b900b')
        d.rectangle((b[0],bot-bh,b[2]-1,bot-1),fill=col); bot-=bh+gap
    # 7seg
    if '7seg' in lay and mem is not None:
        c=lay['7seg']; s=f'{mem:2d}'
        for k,ch in enumerate(s):
            g=img('SegOff.png' if ch==' ' else f'Seg{ch}.png')
            im.alpha_composite(g,(c['x']*S+k*68,c['y']*S))
    # LCD
    font=ImageFont.truetype(R+'lcddot_tr.ttf',round(23*S*46/26))
    for key,text,colr in [('BLCD1','▮'*16,'#2c3321'),('BLCD2','▮'*16,'#2c3321'),('LCD1',l1,'#2b900b'),('LCD2',l2,'#2b900b')]:
        c=lay[key]; d.text((c['x']*S,c['y']*S),text,font=font,fill=colr)
    # buttons
    btn={'Parameter':'parameterOn' if active=='parameter' else 'parameterOff','Balance':'balanceOn' if active=='balance' else 'balanceOff',
         'Bypass':'bypassOn' if bypass else 'bypassOff','Up':'up','Down':'down','MemoryUp':'up','MemoryDown':'down','Recall':'recallOn' if recall else 'recallOff'}
    for k,n in btn.items():
        if k not in lay: continue
        g=img(n+'.png'); g=g.resize((g.size[0]*S,g.size[1]*S),Image.LANCZOS)
        im.alpha_composite(g,(lay[k]['x']*S,lay[k]['y']*S))
    im=im.convert('RGB').resize((W//2*1,H//2*1),Image.LANCZOS) if False else im.convert('RGB')
    im.save(OUT+out,optimize=True)
render('Symphonic','symphonic_bgd.png',None,'   SYMPHONIC',' MOD. FRQ= 0.7 Hz',out='symphonic.png')
render('Reverbs','spx90wide_bgd.png',1,'  REV 1  HALL   ',' REV TIME= 2.6s ',out='reverbs.png')
render('Reflections','spx90wide_bgd.png',5,'  EARLY REF. 1  ','  TYPE =  HALL  ',out='reflections.png')
render('Modulations','spx90wide_bgd.png',9,'STEREO FLANGE A ','MOD. FRQ= 2.5 Hz',out='modulations.png')
render('PitchChange','spx90wide_bgd.png',23,' PITCH CHANGE C ',' L PITCH=  + 0  ',out='pitchchange.png')
render('Reverbs','spx90wide_bgd.png',4,'  REV 4  PLATE  ',' REV TIME= 2.6s ',out='memory-select.png',recall=True)
