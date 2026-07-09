#!/usr/bin/env python3
"""F2 campaign (Modal): the n = 256 DECIDER — canonical C(3) and the
family ledgered bound one octave up (q = 257, mu_256 = full group).

Measures, exhaustively over exponent pairs (gcd(u,v,256) = 1) and the
four sign members, sharded:
  (a) canonical member (+,+): max non-ledger fiber  [was 3 at all
      five scales; growth here would falsify the flat-C(3) target]
  (b) shifted members: max non-ledger fiber  [was 3 at n <= 64, 4 at
      n = 128 — growth to 5+ falsifies the bounded-family hypothesis;
      stabilization at 4 supports 'uniform 4 for shifted members']
Ledger per member: psi-values on {z : z^{u-v} = eps/del} (the proved
collapse-coset law).
"""
import modal
from math import gcd

app = modal.App("rs-mca-f2-n256")
image = modal.Image.debian_slim()

JOBS = [(7681, 512, i, 24) for i in range(24)]


@app.function(image=image, cpu=2, memory=1024, timeout=280)
def shard(job):
    q, n, si, ns = job
    def pf(x):
        out, d = [], 2
        while d * d <= x:
            while x % d == 0:
                out.append(d); x //= d
            d += 1
        if x > 1:
            out.append(x)
        return out
    g = next(c for c in range(2, q)
             if all(pow(c, (q - 1) // r, q) != 1 for r in set(pf(q - 1))))
    h = pow(g, (q - 1) // n, q)
    D = [pow(h, i, q) for i in range(n)]
    inv = [0] + [pow(a, q - 2, q) for a in range(1, q)]
    pw = {}
    pairs = [(u, v) for u in range(1, n) for v in range(u + 1, n)
             if gcd(gcd(u, v), n) == 1]
    mypairs = pairs[si::ns]
    worst_pp = 0
    worst_sh = 0
    wit_pp = wit_sh = None
    for (u, v) in mypairs:
        xu = [pow(x, u, q) for x in D]
        xv = [pow(x, v, q) for x in D]
        duv = (u - v) % (q - 1)
        for (e1, e2) in [(1, 1), (1, q - 1), (q - 1, 1), (q - 1, q - 1)]:
            ratio = e1 * inv[e2] % q
            ledger = set()
            for i in range(n):
                if pow(D[i], duv, q) == ratio:
                    num = (xu[i] - e1) % q
                    den = (xv[i] - e2) % q
                    ledger.add(num * inv[den] % q if den else 'inf')
            fibers = {}
            for i in range(n):
                num = (xu[i] - e1) % q
                den = (xv[i] - e2) % q
                if den == 0:
                    continue
                c = num * inv[den] % q
                if c == 0 or c in ledger:
                    continue
                fibers[c] = fibers.get(c, 0) + 1
            if fibers:
                mf = max(fibers.values())
                if e1 == 1 and e2 == 1:
                    if mf > worst_pp:
                        worst_pp = mf; wit_pp = (u, v)
                else:
                    if mf > worst_sh:
                        worst_sh = mf; wit_sh = (u, v, e1 == 1, e2 == 1)
    return {"q": q, "n": n, "shard": si, "pp": worst_pp,
            "pp_wit": wit_pp, "sh": worst_sh, "sh_wit": wit_sh}


@app.local_entrypoint()
def main():
    res = list(shard.map(JOBS, return_exceptions=True))
    fails = 0
    agg = {}
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:200])
            continue
        key = (r["q"], r["n"])
        cur = agg.setdefault(key, {"pp": 0, "ppw": None, "sh": 0, "shw": None})
        if r["pp"] > cur["pp"]:
            cur["pp"] = r["pp"]; cur["ppw"] = r["pp_wit"]
        if r["sh"] > cur["sh"]:
            cur["sh"] = r["sh"]; cur["shw"] = r["sh_wit"]
    if fails:
        raise SystemExit(f"F2_MDEP_FAIL ({fails})")
    for (q, n), v in sorted(agg.items()):
        m = (q - 1) // n
        print(f"(q={q}, n={n}, m={m}): canonical max = {v['pp']} "
              f"(wit {v['ppw']}); shifted max = {v['sh']} (wit {v['shw']})")
    print("F2_MDEP_FAMILY_PASS")
