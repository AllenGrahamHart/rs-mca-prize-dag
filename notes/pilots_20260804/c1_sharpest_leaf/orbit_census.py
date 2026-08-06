"""Control C-a / C-b: independent Burnside recomputation of the banked
affine-Galois class counts for reduced signed weight-w words at ell=1.

Banked (critical/nodes/dli_wcl_zone_coverage/weight5_orbit_route_fence.md:32-35):
    w=3:            11,054,080 words ->            254 classes
    w=4:         1,398,341,120 words ->         24,979 classes
    w=5:       140,952,784,896 words ->      2,296,920 classes
    w=6:    11,793,049,669,632 words ->    185,569,028 classes

Run: tools/ramguard local -- python3 notes/pilots_20260804/c1_sharpest_leaf/orbit_census.py
"""

import sys
from math import comb

M = 512
HALF = 256
WMAX = 6


def cycles_of(a, b):
    """Cycle id per point for x -> a*x+b mod 512, plus list of cycle lengths."""
    cid = [-1] * M
    lens = []
    reps = []
    nc = 0
    for start in range(M):
        if cid[start] != -1:
            continue
        x = start
        n = 0
        while cid[x] == -1:
            cid[x] = nc
            x = (a * x + b) % M
            n += 1
        lens.append(n)
        reps.append(start)
        nc += 1
    return cid, lens, reps


def fixed_counts(a, b):
    """Coefficients [z^0..z^WMAX] of prod over antipodal PAIRS of (1 + 2 z^len).

    Self-antipodal cycles are unusable by an antipodal-free subset.
    """
    cid, lens, reps = cycles_of(a, b)
    poly = [0] * (WMAX + 1)
    poly[0] = 1
    seen = [False] * len(lens)
    for c in range(len(lens)):
        if seen[c]:
            continue
        partner = cid[(reps[c] + HALF) % M]
        if partner == c:
            seen[c] = True          # self-antipodal: contributes factor 1
            continue
        seen[c] = True
        seen[partner] = True
        d = lens[c]
        if d > WMAX:
            continue                # (1 + 2 z^d) truncates to 1
        new = list(poly)
        for k in range(WMAX - d + 1):
            if poly[k]:
                new[k + d] += 2 * poly[k]
        poly = new
    return poly


def main():
    total = [0] * (WMAX + 1)
    ngroup = 0
    for a in range(1, M, 2):
        for b in range(M):
            ngroup += 1
            p = fixed_counts(a, b)
            for k in range(WMAX + 1):
                total[k] += p[k]

    print(f"affine group order = {ngroup}  (expected {HALF * M})")
    assert ngroup == HALF * M

    banked_words = {3: 11054080, 4: 1398341120, 5: 140952784896, 6: 11793049669632}
    banked_cls = {3: 254, 4: 24979, 5: 2296920, 6: 185569028}

    ok = True
    print()
    print(f"{'w':>2}  {'words (mine)':>20} {'words (banked)':>20}  {'cls (mine)':>12} {'cls (banked)':>13}  ok")
    for w in (3, 4, 5, 6):
        words = comb(HALF, w) * 2 ** (w - 1)      # modulo global sign
        assert total[w] % ngroup == 0, f"Burnside sum not divisible at w={w}"
        classes = total[w] // ngroup
        okw = (words == banked_words[w]) and (classes == banked_cls[w])
        ok &= okw
        print(f"{w:>2}  {words:>20,} {banked_words[w]:>20,}  {classes:>12,} {banked_cls[w]:>13,}  {okw}")

    print()
    print(f"CONTROL C-a/C-b: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
