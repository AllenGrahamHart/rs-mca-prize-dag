#!/usr/bin/env python3
"""h=4 structured-tail follow-up (Modal): (a) extend the n=64 q-ladder past
n^2 (does nontoral stay 0?); (b) extract dilation-orbit representatives of
the structured tail at q = 2113 and 3137 (counts 128, 96 = multiples of 32,
exceeding Poisson mean 21 / 6.5 by 6-15x) and test their algebraic shape
(rotation/reflection relations, gap patterns, signature form)."""
import itertools
import json
import modal

app = modal.App("rs-mca-f3-h4tail")
image = modal.Image.debian_slim()

EXTEND_QS = [5441, 6337, 8929, 12289, 15361]     # all = 1 mod 64, > 64^2
INSPECT_QS = [2113, 3137]


def _domain(q, n):
    for c in range(2, q):
        x = pow(c, (q - 1) // n, q)
        if x == 1:
            continue
        y, order = x, 1
        while y != 1:
            y = y * x % q
            order += 1
        if order == n:
            return [pow(x, i, q) for i in range(n)]


def _census(q, n, h, want_members=False):
    D = _domain(q, n)
    counts = {}
    for P in itertools.combinations(range(n), h):
        cf = [1] + [0] * (h - 1)
        for a in P:
            r = D[a]
            for j in range(h - 1, 0, -1):
                cf[j] = (cf[j] - r * cf[j - 1]) % q
        sig = tuple(cf[1:])
        counts[sig] = counts.get(sig, 0) + 1
    colliding = {s for s, k in counts.items() if k >= 2}
    members = {}
    if colliding:
        for P in itertools.combinations(range(n), h):
            cf = [1] + [0] * (h - 1)
            for a in P:
                r = D[a]
                for j in range(h - 1, 0, -1):
                    cf[j] = (cf[j] - r * cf[j - 1]) % q
            sig = tuple(cf[1:])
            if sig in colliding:
                members.setdefault(sig, []).append(P)
    return members


@app.function(image=image, cpu=2, memory=3072, timeout=240)
def extend(q):
    n, h = 64, 4
    members = _census(q, n, h)
    step = n // h
    T = toral = 0
    for mem in members.values():
        for i in range(len(mem)):
            for j in range(i + 1, len(mem)):
                A, B = mem[i], mem[j]
                if set(A) & set(B):
                    continue
                T += 1
                if all(x % step == A[0] % step for x in A) and \
                   all(x % step == B[0] % step for x in B):
                    toral += 1
    return {"q": q, "nontoral": T - toral, "toral": toral}


@app.function(image=image, cpu=2, memory=3072, timeout=240)
def inspect(q):
    n, h = 64, 4
    members = _census(q, n, h)
    step = n // h
    orbits = {}
    for mem in members.values():
        for i in range(len(mem)):
            for j in range(i + 1, len(mem)):
                A, B = mem[i], mem[j]
                if set(A) & set(B):
                    continue
                if all(x % step == A[0] % step for x in A) and \
                   all(x % step == B[0] % step for x in B):
                    continue
                key = min(tuple(sorted(((a + s) % n for a in A + B)))
                          for s in range(n))
                if key not in orbits:
                    rot = any(sorted((a + s) % n for a in A) == list(B)
                              for s in range(n))
                    refl = any(sorted((s - a) % n for a in A) == list(B)
                               for s in range(n))
                    gapsA = sorted((A[k + 1] - A[k]) % n for k in range(3))
                    gapsB = sorted((B[k + 1] - B[k]) % n for k in range(3))
                    # stabilizer size of the pair under rotation
                    stab = sum(1 for s in range(n)
                               if sorted(((a + s) % n) for a in A + B)
                               == sorted(A + B))
                    orbits[key] = {"A": list(A), "B": list(B), "rot": rot,
                                   "refl": refl, "gapsA": gapsA,
                                   "gapsB": gapsB, "stab": stab}
    return {"q": q, "n_orbits": len(orbits),
            "orbits": list(orbits.values())[:6]}


@app.local_entrypoint()
def main():
    ext = [r for r in extend.map(EXTEND_QS, return_exceptions=True)
           if isinstance(r, dict)]
    ins = [r for r in inspect.map(INSPECT_QS, return_exceptions=True)
           if isinstance(r, dict)]
    print("=== extension past n^2 = 4096 ===")
    for r in sorted(ext, key=lambda r: r['q']):
        print(f"  q={r['q']}: nontoral={r['nontoral']} toral={r['toral']}")
    print("\n=== structured tail orbits ===")
    for r in ins:
        print(f"  q={r['q']}: {r['n_orbits']} orbits")
        for o in r["orbits"]:
            print(f"    A={o['A']} B={o['B']} rot={o['rot']} refl={o['refl']} "
                  f"gapsA={o['gapsA']} gapsB={o['gapsB']} stab={o['stab']}")
    with open("/tmp/f3_h4tail.json", "w") as f:
        json.dump({"extend": ext, "inspect": ins}, f, indent=1)
