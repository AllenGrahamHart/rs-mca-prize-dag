import modal
app = modal.App("rs-mca-xr-eliminant-census")

@app.function(cpu=4.0, memory=8192, timeout=2400)
def census(grid, samples_per):
    import random
    random.seed(20260705)
    def inv(a,p): return pow(a%p,p-2,p)
    def rank(rows,p):
        rows=[r[:] for r in rows]; r=0; nc=len(rows[0]) if rows else 0
        for c in range(nc):
            piv=next((i for i in range(r,len(rows)) if rows[i][c]%p),None)
            if piv is None: continue
            rows[r],rows[piv]=rows[piv],rows[r]
            iv=inv(rows[r][c],p); rows[r]=[(x*iv)%p for x in rows[r]]
            for i in range(len(rows)):
                if i!=r and rows[i][c]%p:
                    cc=rows[i][c]; rows[i]=[(x-cc*y)%p for x,y in zip(rows[i],rows[r])]
            r+=1
            if r==len(rows): break
        return r
    def solve_square(A,b,p):
        aug=[row[:]+[rhs] for row,rhs in zip(A,b)]; n=len(A); r=0
        for c in range(n):
            piv=next((i for i in range(r,n) if aug[i][c]%p),None)
            if piv is None: return None
            aug[r],aug[piv]=aug[piv],aug[r]
            iv=inv(aug[r][c],p); aug[r]=[(x*iv)%p for x in aug[r]]
            for i in range(n):
                if i!=r and aug[i][c]%p:
                    cc=aug[i][c]; aug[i]=[(x-cc*y)%p for x,y in zip(aug[i],aug[r])]
            r+=1
        return [aug[i][n] for i in range(n)]
    def chart(domain,k,T,p):
        pivots=list(T[:k]); free=list(T[k:])
        Vp=[[pow(domain[x],d,p) for x in pivots] for d in range(k)]
        basis=[]
        for q in free:
            rhs=[(-pow(domain[q],d,p))%p for d in range(k)]
            pv=solve_square(Vp,rhs,p)
            if pv is None: return None
            w=[0]*len(domain)
            for x,val in zip(pivots,pv): w[x]=val
            w[q]=1; basis.append(w)
        return basis
    def normal_form(bases,slopes,union,p):
        rows=[]
        for coord in union:
            rows.append([lam[coord] for b in bases for lam in b])
        for coord in union:
            rows.append([(z*lam[coord])%p for z,b in zip(slopes,bases) for lam in b])
        return rows
    out=[]
    for (p,n,k,A) in grid:
        t=A-k; target=3*t
        domain=list(range(1,n+1))   # nonzero points, distinct mod p (n<p)
        cache={}
        def getchart(T):
            if T not in cache:
                b=chart(domain,k,T,p); cache[T]=b if (b is not None and len(b)==t) else None
            return cache[T]
        buckets={}
        pts=list(range(n)); got=0
        for _ in range(samples_per):
            triple=tuple(tuple(sorted(random.sample(pts,A))) for _ in range(3))
            sets=[set(T) for T in triple]
            pair_sum=len(sets[0]&sets[1])+len(sets[0]&sets[2])+len(sets[1]&sets[2])
            trip=len(sets[0]&sets[1]&sets[2])
            if pair_sum-trip>2*k: continue          # light filter
            bs=[getchart(T) for T in triple]
            if any(b is None for b in bs): continue
            slopes=tuple(random.sample(range(1,p),3))
            union=sorted(set().union(*sets))
            rk=rank(normal_form(bs,slopes,union,p),p)
            got+=1
            key=(pair_sum,trip,len(union))
            bk=buckets.setdefault(key,{"seen":0,"full":0,"maxrank":0})
            bk["seen"]+=1; bk["maxrank"]=max(bk["maxrank"],rk)
            if rk==target: bk["full"]+=1
        certified=sum(1 for v in buckets.values() if v["full"]>0)
        uncert=[{"profile":list(kk),"maxrank":v["maxrank"],"target":target,"seen":v["seen"]}
                for kk,v in buckets.items() if v["full"]==0]
        out.append({"row":[p,n,k,A],"t":t,"target_rank":target,"light_samples":got,
                    "light_profiles":len(buckets),"certified_nonvanishing":certified,
                    "uncertified":uncert})
    return out

@app.local_entrypoint()
def main():
    import json
    grid=[(101,12,2,4),(101,14,3,5),(101,16,3,6),(101,18,4,7),
          (103,20,4,8),(103,22,5,9),(107,24,5,10),(109,26,6,11)]
    res=census.remote(grid, 60000)
    print("XR_CENSUS_JSON_START")
    print(json.dumps(res))
    print("XR_CENSUS_JSON_END")
