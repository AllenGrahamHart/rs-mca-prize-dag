#!/usr/bin/env python3
"""Decode the h=3 interior families at 3 | q-1 rows (Modal): for every
nontoral trade orbit, test the AFFINE-LINE hypothesis Q = omega*P + s
(omega a primitive cube root in F_q, s in F_q) and its variants
(P self-related, mixed). Rows: (96, 9601), (128, 33409), (192, 37057)."""
import itertools
import json
import modal

app = modal.App("rs-mca-f3-h3decode")
image = modal.Image.debian_slim()

ROWS = [(96, 9601), (128, 33409), (192, 37057)]


@app.function(image=image, cpu=2, memory=3072, timeout=270)
def decode(rowspec):
    n, q = rowspec
    g = None
    for cand in range(2, q):
        x = pow(cand, (q - 1) // n, q)
        if x == 1:
            continue
        y, order = x, 1
        while y != 1:
            y = y * x % q
            order += 1
        if order == n:
            g = x
            break
    D = [pow(g, i, q) for i in range(n)]
    # primitive cube roots in F_q (3 | q-1 at these rows)
    omegas = []
    for cand in range(2, q):
        w = pow(cand, (q - 1) // 3, q)
        if w != 1 and w not in omegas:
            omegas.append(w)
        if len(omegas) == 2:
            break

    counts = {}
    for P in itertools.combinations(range(n), 3):
        r0, r1, r2 = D[P[0]], D[P[1]], D[P[2]]
        sig = ((r0 + r1 + r2) % q,
               (r0 * r1 + r0 * r2 + r1 * r2) % q)
        counts.setdefault(sig, []).append(P)

    step = n // 3 if n % 3 == 0 else None
    stats = {"total_nontoral": 0, "affine_line": 0, "self_line": 0,
             "other": 0}
    examples_other = []
    orbit_seen = set()
    orbit_stats = {"line_orbits": 0, "other_orbits": 0}
    for sig, mem in counts.items():
        if len(mem) < 2:
            continue
        for i in range(len(mem)):
            for j in range(i + 1, len(mem)):
                A, B = mem[i], mem[j]
                if set(A) & set(B):
                    continue
                if step and all(x % step == A[0] % step for x in A) and \
                        all(x % step == B[0] % step for x in B):
                    continue
                stats["total_nontoral"] += 1
                Av = sorted(D[a] for a in A)
                Bv = sorted(D[b] for b in B)
                tagged = None
                # affine-line: B = omega*A + s for some omega, s
                for w in omegas:
                    for a0 in Av:
                        for b0 in Bv:
                            s = (b0 - w * a0) % q
                            if sorted((w * a + s) % q for a in Av) == Bv:
                                tagged = "affine_line"
                            if tagged:
                                break
                        if tagged:
                            break
                    if tagged:
                        break
                if not tagged:
                    # self-line: A = omega*A + s (A on an omega-line orbit)
                    for w in omegas:
                        for a0 in Av:
                            s = (Av[0] - w * a0) % q
                            if sorted((w * a + s) % q for a in Av) == Av \
                                    and sorted((w * b + s) % q for b in Bv) == Bv:
                                tagged = "self_line"
                                break
                        if tagged:
                            break
                if tagged:
                    stats[tagged] += 1
                else:
                    stats["other"] += 1
                    if len(examples_other) < 3:
                        examples_other.append({"A": list(A), "B": list(B)})
                key = min(tuple(sorted(((a + s) % n for a in A + B)))
                          for s in range(n))
                if key not in orbit_seen:
                    orbit_seen.add(key)
                    orbit_stats["line_orbits" if tagged else "other_orbits"] += 1
    return {"n": n, "q": q, "stats": stats, "orbits": orbit_stats,
            "examples_other": examples_other}


@app.local_entrypoint()
def main():
    res = [r for r in decode.map(ROWS, return_exceptions=True)
           if isinstance(r, dict)]
    for r in res:
        print(f"({r['n']},{r['q']}): {r['stats']} orbits={r['orbits']}")
        for ex in r["examples_other"]:
            print("   other:", ex)
    with open("/tmp/f3_h3decode.json", "w") as f:
        json.dump(res, f, indent=1)
