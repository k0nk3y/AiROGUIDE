"""XP-egyensuly szimulator: a pilotatipusok mennyi repulesi ora alatt erik el a legmagasabb rangot (200 000 XP). Futtatas: python3 tools/xp_sim.py [wt]"""
import importlib.util, math, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec=importlib.util.spec_from_file_location('a',os.path.join(ROOT,'app.py'));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
WT=m.WT_TRO
SKIP=("conditions","altitude","special","hidden")
FEAT_ALL=sum(t['xp'] for t in m.PR_TRO if t['cat'] in SKIP)     # 1810
def sat(h,mx,tau): return mx*(1-math.exp(-h/tau))
# archetype: kt (avg ground speed incl. climb), fl_h (avg flight hours), ld_per_fl, uniq functions, star quality, feats share, wt dict function
A={}
A["WT kis gép (Cessna, 6 kontinens, gyűjtögető)"]=dict(kt=100,fl_h=2.5,ldf=1.0,cc=lambda h:sat(h,170,420),ap=lambda h:sat(h,700,900),po=lambda h:sat(h,30000,700),tr=lambda h:min(h*0.04,45),ac=lambda h:min(2+h/250,6),q=4.5,n5f=0.2,feat=0.6,
    wt=lambda h:{"legs":h/2.5,"tours":h/240.0,"dirs":({"E","W"} if h>=480 else {"E"}),"conts":(6 if h>=240 else 3 if h>=100 else 1),"oneac":int(h>=240),"detour":int(h>=60),"pole":int(h>=150)})
A["WT kis gép, rövid szakaszokkal (1,5 óra)"]=dict(kt=95,fl_h=1.5,ldf=1.0,cc=lambda h:sat(h,170,420),ap=lambda h:sat(h,900,1100),po=lambda h:sat(h,30000,700),tr=lambda h:min(h*0.04,45),ac=lambda h:min(2+h/250,6),q=4.5,n5f=0.2,feat=0.6,
    wt=lambda h:{"legs":h/1.5,"tours":h/240.0,"dirs":({"E","W"} if h>=480 else {"E"}),"conts":(6 if h>=240 else 3 if h>=100 else 1),"oneac":int(h>=240),"detour":int(h>=60),"pole":int(h>=150)})
A["Utasszállító-szimulátor (4 órás járatok, nagy gép)"]=dict(kt=430,fl_h=4.0,ldf=1.0,cc=lambda h:sat(h,110,500),ap=lambda h:sat(h,260,500),po=lambda h:sat(h,2500,500),tr=lambda h:0,ac=lambda h:min(3+h/150,12),q=5,n5f=0.3,feat=0.5,wt=None)
A["Utasszállító-szimulátor, hosszú járatok (7 óra)"]=dict(kt=470,fl_h=7.0,ldf=1.0,cc=lambda h:sat(h,100,500),ap=lambda h:sat(h,240,500),po=lambda h:sat(h,2000,500),tr=lambda h:0,ac=lambda h:min(3+h/150,10),q=5,n5f=0.3,feat=0.5,wt=None)
A["Látványpilóta (túrák + POI, 1 órás körök)"]=dict(kt=105,fl_h=1.0,ldf=1.2,cc=lambda h:sat(h,90,500),ap=lambda h:sat(h,260,500),po=lambda h:sat(h,45000,800),tr=lambda h:min(h*0.12,250),ac=lambda h:min(4+h/80,30),q=5,n5f=0.3,feat=0.8,wt=None)
A["Vegyes (kis gép + időnként turbó/jet)"]=dict(kt=170,fl_h=2.0,ldf=1.1,cc=lambda h:sat(h,130,450),ap=lambda h:sat(h,500,700),po=lambda h:sat(h,25000,700),tr=lambda h:min(h*0.05,80),ac=lambda h:min(4+h/100,25),q=4.5,n5f=0.2,feat=0.7,
    wt=None)

def stats(a,h):
    nfl=h/a['fl_h']; nld=nfl*a['ldf']
    C={"fl":[],"nfl":nfl,"nm":h*a['kt']*0.93,"sec":h*3600.0,"ld":[{"vs":200}]*int(nld),"ldx":[{}]*int(nld),
       "stars":[3]*int(nld),"n5":nld*a['n5f'],"apts":set(range(int(a['ap'](h)))),"acs":set(range(int(a['ac'](h)))),
       "cc":set(range(int(a['cc'](h)))),"cont":set(range(min(6,int(1+a['cc'](h)/12)))),"pois":a['po'](h),"tours":a['tr'](h),"ad":{}}
    if a['wt']: C["wt"]=a['wt'](h)
    return C,nld
def xp(a,h,wt_on):
    C,nld=stats(a,h)
    tx={}
    got=set()
    for t in m.PR_TRO:
        if t['cat'] in SKIP: continue
        try:
            if t['fn'](C): tx[t['cat']]=tx.get(t['cat'],0)+t['xp']; got.add(t['id'])
        except Exception as e: pass
    wtx=0
    if wt_on and C.get("wt"):
        for w in WT:
            if w[7](C): wtx+=w[1]
    qd=nld*a['q']
    time=h*100; dist=C['nm']*m.PR_XP_NM; land=int(nld)*m.PR_XP_LD+qd; sights=C['pois']*0.5; stamps=len(C['cc'])*25; tours=C['tours']*25
    feat=a['feat']*FEAT_ALL
    parts={"idő":time,"táv":dist,"landolás":land,"látnivaló":sights,"pecsét":stamps,"túra":tours,"trófea":sum(tx.values()),"feats":feat,"WT-trófea":wtx}
    return sum(parts.values()),parts,C
if __name__=="__main__":
    wt_on=len(sys.argv)>1 and sys.argv[1]=="wt"
    ranks=[r[0] for r in m.PR_RANKS]
    for n,a in A.items():
        row=[]
        for h in (100,250,500,750,1000,1200,1500):
            row.append("%d h:%6d"%(h,xp(a,h,wt_on)[0]))
        # hours to 200000
        h=100
        while h<5000 and xp(a,h,wt_on)[0]<200000: h+=10
        print("%-52s"%n[:52]," | ".join(row)," => 200k XP: %d h"%h)
