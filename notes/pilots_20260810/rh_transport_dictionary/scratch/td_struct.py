"""td_struct.py -- dump the agreement sets of one explicit word, and run a
restricted top-degree scan (d1 = n-1, ratio = 1) to test a candidate law.

Usage:
  tools/ramguard local -- python3 <this> sets n q sigma d1 d2 c
  tools/ramguard local -- python3 <this> scan n q sigma out
"""
import json
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from td_core import mu, qcore_count  # noqa: E402
from td_scan import flist  # noqa: E402


def agreement_sets(n, q, k, a, xs, Y):
    out = []
    from itertools import combinations
    for A in combinations(range(n), a):
        L = [1]
        for i in A:
            x = xs[i]
            new = [0] * (len(L) + 1)
            for j, c in enumerate(L):
                new[j + 1] = (new[j + 1] + c) % q
                new[j] = (new[j] - x * c) % q
            L = new
        r = Y[:]
        for i in range(len(r) - 1, a - 1, -1):
            c = r[i]
            if c:
                r[i] = 0
                for j in range(a):
                    r[i - a + j] = (r[i - a + j] - c * L[j]) % q
        if all(v == 0 for v in r[k:a]):
            out.append(A)
    return out


def main():
    mode = sys.argv[1]
    n, q, sigma = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    k = n // 2
    a = k + sigma
    xs = mu(n, q)
    if mode == "sets":
        d1, d2, c = int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7])
        Y = [0] * n
        Y[d1] = 1
        Y[d2] = c
        S = agreement_sets(n, q, k, a, xs, Y)
        M = 4 if n % 4 == 0 else 2
        print(json.dumps({
            "n": n, "q": q, "sigma": sigma, "a": a, "word_degrees": [d1, d2],
            "ratio": c, "count": len(S),
            "sets": [list(A) for A in S],
            "coset_pattern_mod_%d" % (n // M): [
                sorted([i % (n // M) for i in A]) for A in S],
            "qcore": qcore_count(n, k, sigma)[0],
        }, indent=1))
    else:
        out = sys.argv[5]
        res = {"n": n, "q": q, "sigma": sigma, "a": a,
               "qcore": qcore_count(n, k, sigma)[0], "words": []}
        for d2 in range(k, n - 1):
            Y = [0] * n
            Y[n - 1] = 1
            Y[d2] = 1
            fl, fs, prof, deg = flist(n, q, k, a, xs, Y)
            rec = {"degrees": [n - 1, d2], "F_LIST": fl, "F_SUBSET": fs,
                   "profile": prof, "slack": deg - a}
            res["words"].append(rec)
            print(json.dumps(rec), flush=True)
            with open(out, "w") as fh:
                json.dump(res, fh, indent=1)


if __name__ == "__main__":
    main()
