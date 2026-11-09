"""Render a silicon wafer study with a repeated lithography field."""
from pathlib import Path
import numpy as np
from PIL import Image,ImageDraw
W,H=1280,920
y,x=np.mgrid[0:H,0:W]
rng=np.random.default_rng(163)
light=np.exp(-((x-685)/740)**2-((y-425)/520)**2)
bg=np.stack([6+12*light,20+29*light,27+29*light],axis=-1)
grid=((x%66==0)|(y%66==0))[:,:,None]
bg=bg+grid*np.array([6,9,10])
def coords(dy):
    a=-.37
    dx=x-677; ddy=y-444-dy
    return (dx*np.cos(a)+ddy*np.sin(a))/602,(-dx*np.sin(a)+ddy*np.cos(a))/290
u,v=coords(0); r=np.hypot(u,v)
us,vs=coords(44)
shadow=np.exp(-((np.hypot(us,vs)/1.02)**12))*.43
bg*=1-shadow[:,:,None]
for z in range(10,0,-1):
    us,vs=coords(z)
    edge=(np.hypot(us,vs)<1)&(vs>-.986)
    bg[edge]=[41+z*2,72+z*3,74+z*3]
# Translate the physical surface into a rotated square grid.
a=.25
s=(u*np.cos(a)-v*np.sin(a)+1.4)*19
t=(u*np.sin(a)+v*np.cos(a)+1.3)*19
i,j=np.floor(s),np.floor(t); fx,fy=s%1,t%1
k=(.50+.25*u-.21*v+.17*np.sin(2.1*u+2.7*v)+.07*np.sin(6.5*u+2.4*v)).clip(0,1)
palette=np.array([[31,67,74],[50,110,118],[148,183,173],[90,132,157],[179,145,162],[229,178,127],[161,190,157],[103,178,180],[38,91,110]])
surface=np.stack([np.interp(k,np.linspace(0,1,len(palette)),palette[:,n]) for n in range(3)],axis=-1)
etch=((fx<.045)|(fy<.054)); border=((fx>.955)|(fy>.945))
wires=((fx>.12)&(fx<.58)&(fy>.12)&(fy<.85))*(((fy*25)%1<.42)*.32+.03)
banks=((fx>.61)&(fx<.90)&(fy>.09)&(fy<.9))*(((fx*16)%1<.34)*.28+.06)
circuit=(1-.57*etch+.23*border-wires-banks + .065*np.sin(i*24+j*31))
shine=(.1+.16*np.exp(-((u+v-.1)/.19)**2))
surface=surface*circuit[:,:,None]+shine[:,:,None]*np.array([59,72,70])
active=(r<1)&(v>-.986)
bg[active]=surface[active]
rim=(r<1)&(r>.995)&active
bg[rim]=np.clip(bg[rim]+65,0,255)
bg+=rng.normal(0,.9,(H,W,1))
im=Image.fromarray(np.uint8(bg.clip(0,255)))
d=ImageDraw.Draw(im)
for cx,cy in ((54,52),(1225,52),(54,866),(1225,866)):
    d.line((cx-9,cy,cx+9,cy),fill=(104,139,141),width=2)
    d.line((cx,cy-9,cx,cy+9),fill=(104,139,141),width=2)
im.save(Path(__file__).parent/'assets/wafer.webp','WEBP',quality=90)
