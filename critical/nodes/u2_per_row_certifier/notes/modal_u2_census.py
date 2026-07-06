import modal
img = modal.Image.debian_slim(python_version="3.11").pip_install("sympy")
app = modal.App("rs-mca-u2cert")

@app.function(image=img, cpu=8.0, memory=24576, timeout=10800)
def moment_census(Nq, p, bmax, pbits=0):
    """u2 certifier: primitive t=3-null 0/1 blocks on mu_Nq mod p.
    A block B (subset of exponents) is t=3-null iff sum_{a in B} zeta^{ma}==0
    mod p for m=1,2,3. Primitive = no nontrivial rotational (a->a+j) or
    reflection (a->c-a) symmetry. MITM: split b into h1+h2, hash moment-sums.
    Returns per-b: #primitive t=3-null blocks (0 => CERTIFIED that b)."""
    import sympy, itertools, sys
    if pbits:
        q=(1<<pbits); q-=q%Nq; q+=1
        while not sympy.isprime(q): q+=Nq
        p=q
    def log(m): print(f"[Nq={Nq} p={p}] {m}", flush=True)
    g = sympy.primitive_root(p); zeta = pow(g, (p-1)//Nq, p)
    assert pow(zeta, Nq, p) == 1
    mom = [ (pow(zeta,a,p), pow(zeta,2*a,p), pow(zeta,3*a,p)) for a in range(Nq) ]
    def msum(S):
        s0=s1=s2=0
        for a in S: s0+=mom[a][0]; s1+=mom[a][1]; s2+=mom[a][2]
        return (s0%p, s1%p, s2%p)
    def is_primitive(B):
        Bs=frozenset(B)
        for j in range(1,Nq):
            if frozenset((a+j)%Nq for a in B)==Bs: return False   # rotation
        for c in range(Nq):
            if frozenset((c-a)%Nq for a in B)==Bs: return False   # reflection
        return True
    out={}
    for b in range(4, bmax+1):
        h1=b//2; h2=b-h1
        log(f"b={b}: MITM h1={h1} h2={h2} (C({Nq},{h1})={sympy.binomial(Nq,h1)})...")
        table={}
        for S1 in itertools.combinations(range(Nq), h1):
            table.setdefault(msum(S1), []).append(S1)
        prims=[]; total=0
        for S2 in itertools.combinations(range(Nq), h2):
            neg=tuple((-x)%p for x in msum(S2))
            for S1 in table.get(neg, ()):
                if not (set(S1)&set(S2)):
                    B=tuple(sorted(set(S1)|set(S2)))
                    if len(B)==b:
                        total+=1
                        if is_primitive(B):
                            prims.append(B)
                            if len(prims)<=3: pass
        # dedup primitive blocks (each counted multiple times via splits)
        uniq=set(prims)
        out[b]=dict(primitive_blocks=len(uniq),
                    example=sorted(min(uniq)) if uniq else None,
                    verdict="BLOCK FOUND" if uniq else "CERTIFIED")
        log(f"b={b}: {out[b]['verdict']} ({len(uniq)} primitive)")
    return dict(Nq=Nq, p=p, per_b=out)

@app.local_entrypoint()
def main():
    import json
    print("=== GATE (reproduce F2 census b=8) ===", flush=True)
    for p in (193, 257, 577, 641, 769):
        r = moment_census.remote(64, p, 8, 0)
        print("U2_GATE "+json.dumps({"p":p, "b8":r["per_b"].get(8)}), flush=True)
    print("=== CERTIFICATE (large primes, b up to 10) ===", flush=True)
    for pbits in (61, 128):
        r = moment_census.remote(64, 0, 10, pbits)
        print("U2_CERT "+json.dumps({"pbits":pbits, "p":r["p"], "per_b":r["per_b"]}), flush=True)
