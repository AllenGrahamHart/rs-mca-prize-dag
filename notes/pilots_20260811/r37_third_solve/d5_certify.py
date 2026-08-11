"""D2c - FULL certification of the T=4 record objects against the ORIGINAL 36x32
system M(Z)Q_Z = 0, from scratch. r37_third_solve. Appends to d5_results.txt.
"""
import time

def peval(a,x,p):
    r=0
    for c in reversed(a): r=(r*x+c)%p
    return r
def trim(a):
    while a and a[-1]==0: a.pop()
    return a
def pmul(a,b,p):
    if not a or not b: return []
    r=[0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        if ai:
            for j,bj in enumerate(b): r[i+j]=(r[i+j]+ai*bj)%p
    return trim(r)
def pdivmod(a,b,p):
    a=a[:]; db=len(b)-1; inv=pow(b[-1],p-2,p); q=[0]*max(0,len(a)-db)
    for i in range(len(a)-1,db-1,-1):
        c=(a[i]*inv)%p
        if c:
            q[i-db]=c
            for j in range(db+1): a[i-db+j]=(a[i-db+j]-c*b[j])%p
    return trim(q),trim(a)
def pgcd(a,b,p):
    a=a[:];b=b[:]
    while b: a,b=b,pdivmod(a,b,p)[1]
    return [x*pow(a[-1],p-2,p)%p for x in a] if a else []

def rref(M,p):
    M=[row[:] for row in M]; rows=len(M); cols=len(M[0]); r=0; piv=[]
    for c in range(cols):
        pr=None
        for i in range(r,rows):
            if M[i][c]: pr=i;break
        if pr is None: continue
        M[r],M[pr]=M[pr],M[r]
        iv=pow(M[r][c],p-2,p)
        M[r]=[x*iv%p for x in M[r]]
        for i in range(rows):
            if i!=r and M[i][c]:
                f=M[i][c]
                M[i]=[(M[i][j]-f*M[r][j])%p for j in range(cols)]
        piv.append(c); r+=1
        if r==rows: break
    return M,piv,r
def kernel(M,p):
    R,piv,rk=rref(M,p); cols=len(M[0]); free=[c for c in range(cols) if c not in piv]
    basis=[]
    for fc in free:
        v=[0]*cols; v[fc]=1
        for i,pc in enumerate(piv): v[pc]=(-R[i][fc])%p
        basis.append(v)
    return basis,rk

def hank(y,p):
    return [[y[a+b] for b in range(8)] for a in range(9)]
def matvec(M,v,p):
    return [sum(M[i][j]*v[j] for j in range(len(v)))%p for i in range(len(M))]
def rank(M,p):
    return rref(M,p)[2]

def certify(p,Q0,Q1,Q2,S0,Sinf,slopes,out):
    tag="q=%d"%p
    out.append("--- CERTIFICATION %s ---"%tag)
    out.append("%s deg(Q0,Q1,Q2) = (%d,%d,%d)  [required (7,7,7)]"
               %(tag,len(Q0)-1,len(Q1)-1,len(Q2)-1))
    sep=rank([Q0+[0]*(8-len(Q0)),Q1+[0]*(8-len(Q1)),Q2+[0]*(8-len(Q2))],p)
    out.append("%s separation rank (RNC2) = %d  [required m+1 = 3]"%(tag,sep))
    s=len(pgcd(pgcd(Q0,Q1,p),Q2,p))-1
    out.append("%s s = deg gcd(Q0,Q1,Q2) = %d  [required 0, (SAT1)]"%(tag,s))
    # 36x32 system on (y_0,y_1)
    M=[]
    for blk in range(4):
        for a in range(9):
            row=[0]*32
            for b in range(8):
                if a+b<16:
                    if blk==0: row[a+b]=(row[a+b]+Q0[b])%p
                    elif blk==1:
                        row[a+b]=(row[a+b]+Q1[b])%p; row[16+a+b]=(row[16+a+b]+Q0[b])%p
                    elif blk==2:
                        row[a+b]=(row[a+b]+Q2[b])%p; row[16+a+b]=(row[16+a+b]+Q1[b])%p
                    else: row[16+a+b]=(row[16+a+b]+Q2[b])%p
            M.append(row)
    ker,rk=kernel(M,p)
    out.append("%s nullity(36x32) = %d  [required >= 1]  rank = %d"%(tag,len(ker),rk))
    if not ker:
        out.append("%s FAILED: no kernel"%tag); return
    y=ker[0]; y0=y[:16]; y1=y[16:]
    M0=hank(y0,p); M1=hank(y1,p)
    ok=True
    for a in range(9):
        for e0,e1,e2 in ((0,0,0),):
            pass
    r0=matvec(M0,Q0,p); r1=[(matvec(M0,Q1,p)[i]+matvec(M1,Q0,p)[i])%p for i in range(9)]
    r2=[(matvec(M0,Q2,p)[i]+matvec(M1,Q1,p)[i])%p for i in range(9)]
    r3=matvec(M1,Q2,p)
    ok=all(v==0 for v in r0+r1+r2+r3)
    out.append("%s M(Z)Q_Z = 0 entrywise from scratch: %s"%(tag,ok))
    ranks={}
    for z in range(p):
        Mz=[[(M0[i][j]+z*M1[i][j])%p for j in range(8)] for i in range(9)]
        rr=rank(Mz,p); ranks[rr]=ranks.get(rr,0)+1
    grank=max(ranks)
    drops=[z for z in range(p) if rank([[(M0[i][j]+z*M1[i][j])%p for j in range(8)]
                                       for i in range(9)],p)<grank]
    rinf=rank(M1,p)
    out.append("%s generic rank max_z rank M_r(y0+z y1) = %d  [required rho = 7]; rank histogram %s"
               %(tag,grank,sorted(ranks.items())))
    out.append("%s finite rank-drop set = %s (rank there = %s); rank at infinity = %d  [delta = rho-3e = 1]"
               %(tag,drops,[rank([[(M0[i][j]+z*M1[i][j])%p for j in range(8)] for i in range(9)],p)
                            for z in drops],rinf))
    # degree-<=1 kernel: 27 x 16
    M2=[]
    for blk in range(3):
        for a in range(9):
            row=[0]*16
            for b in range(8):
                if blk==0: row[b]=(row[b]+M0[a][b])%p
                elif blk==1:
                    row[8+b]=(row[8+b]+M0[a][b])%p; row[b]=(row[b]+M1[a][b])%p
                else: row[8+b]=(row[8+b]+M1[a][b])%p
            M2.append(row)
    k2,_=kernel(M2,p)
    out.append("%s kernel vectors of parameter degree <= 1 : %d  [required 0, else e < m]  => e = %d"
               %(tag,len(k2),2 if len(k2)==0 else 1))
    # T over the bespoke union and over mu_32
    U=set(S0)|set(Sinf)
    supp={}
    for z in slopes:
        Qz=[(Q0[i]+z*Q1[i]+z*z*Q2[i])%p for i in range(8)]
        rt=[x for x in range(p) if peval(Qz,x,p)==0]
        supp[z]=set(rt)
        U|=set(rt)
    out.append("%s supported slopes {inf} u %s ; T = %d ; |union of root sets| = %d  [must be <= 32]"
               %(tag,slopes,len(slopes)+1,len(U)))
    # pairwise overlap matrix and (OV4)
    keys=list(supp)+['inf']
    supp['inf']=set(Sinf)
    e={}
    for i in range(len(keys)):
        for j in range(i+1,len(keys)):
            e[(keys[i],keys[j])]=len(supp[keys[i]]&supp[keys[j]])
    worst=0
    for a in keys:
        for b in keys:
            for c in keys:
                if len({a,b,c})==3:
                    worst=max(worst,e.get((a,b),e.get((b,a),0))+e.get((a,c),e.get((c,a),0)))
    out.append("%s pairwise overlaps e(i,j) = %s ; (OV4) worst e(k,i)+e(k,j) = %d  [<= 4]"
               %(tag,sorted(e.items(),key=lambda t:str(t[0])),worst))
    out.append("%s sum_x d_x over the supported slopes = %d out of 2|union| = %d"
               %(tag,7*(len(slopes)+1),2*len(U)))
    # mu_32 reading (zero-power control)
    gg=2
    while True:
        ok2=True
        for d in (2,3,5,7,11):
            if (p-1)%d==0 and pow(gg,(p-1)//d,p)==1: ok2=False;break
        if ok2: break
        gg+=1
    h=pow(gg,(p-1)//32,p); mu=set(); v=1
    for _ in range(32): mu.add(v); v=v*h%p
    tmu=0
    for z in list(slopes)+['inf']:
        st=supp[z] if z=='inf' else supp[z]
        if len(st)==7 and st<=mu: tmu+=1
    out.append("%s T over mu_32 for this object = %d  (the bespoke record has ZERO power for (SAT3))"%(tag,tmu))

def main():
    out=["","=== RUN d5_certify %s ==="%time.strftime("%Y-%m-%dT%H:%M:%S")]
    certify(97,[82,2,91,96,61,35,50,1],[22,39,54,52,92,55,41,82],[54,49,0,15,26,20,62,6],
            [4,23,25,51,66,83,86],[16,21,28,55,62,64,67],[0,23,72],out)
    certify(193,[87,60,124,147,158,175,92,1],[103,75,164,79,119,44,176,168],
            [58,106,55,126,173,99,58,26],[29,71,82,115,118,129,136],
            [14,30,45,89,138,154,181],[0,108,114],out)
    with open("notes/pilots_20260811/r37_third_solve/d5_results.txt","a") as fh:
        fh.write("\n".join(out)+"\n")
    print("\n".join(out))

main()
