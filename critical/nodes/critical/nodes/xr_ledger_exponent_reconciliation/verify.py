#!/usr/bin/env python3
p = 101
def rank(M):
    M=[r[:] for r in M]; R=len(M); C=len(M[0]) if R else 0; r=0
    for c in range(C):
        piv=next((i for i in range(r,R) if M[i][c]%p),None)
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]; inv=pow(M[r][c],p-2,p)
        M[r]=[x*inv%p for x in M[r]]
        for i in range(R):
            if i!=r and M[i][c]%p:
                f=M[i][c]; M[i]=[(a-f*b)%p for a,b in zip(M[i],M[r])]
        r+=1
        if r==R: break
    return r
def basis(pts,sup,k,n):
    B=[]
    for j in range(k):
        w=[0]*n
        for i in sup: w[i]=pow(pts[i],j,p)
        B.append(w)
    for i in range(n):
        if i not in sup: w=[0]*n; w[i]=1; B.append(w)
    return B
ok=True
for (k,t) in [(4,3),(3,4),(5,2)]:
    for s in range(0,t+3):
        m=k+t; pts=list(range(1,m+s+1)); S=set(range(m)); T=set(range(s,s+m))
        n=len(S|T)
        B1=basis(pts,S,k,n); B2=basis(pts,T,k,n)
        d=rank(B1)+rank(B2)-rank(B1+B2)
        codim=n-d
        want=t+min(s,t)
        if codim!=want: print(f"FAIL k={k} t={t} s={s}: codim={codim} want={want}"); ok=False
print("ALL PASS: codim = t + min(s,t)" if ok else "FAILED")
