"""r34_pstar E1b: calibrate  codim{p* <= p} = 2R - 3p  in Gr(2,R).

Registered prediction (PREREG R0-c):
    dim{p* <= p} = 3p-4   inside  Gr(2,R) of dim 2R-4
    => frequency of {Ann(V)_p != 0} among uniform random pencils ~ q^{-(2R-3p)}
Falsifier: |measured -log_q(freq) - (2R-3p)| > 0.5 at cells where the
predicted codim is 1 or 2.
Stdlib only.  Run under tools/ramguard.
"""
import sys, random, math
from e1_census import rank_mod, stack

# name, q, n, k, r, [(p, N), ...]
JOBS = [
    ("W1_round33", 13, 11, 3, 6, [(5, 60000), (4, 300000)]),
    ("W2_round33", 11, 10, 2, 6, [(5, 60000), (4, 300000)]),
    ("S1_sep", 11, 11, 1, 8, [(6, 120000), (5, 400000)]),
    ("S2_sep", 13, 13, 1, 10, [(7, 300000)]),
    ("S3_sep", 17, 17, 1, 13, [(10, 120000)]),
    ("L1_lb1", 11, 7, 2, 3, [(3, 60000), (2, 300000)]),
]


def main():
    random.seed(777202608)
    out = open(sys.argv[1], "w")

    def emit(s):
        out.write(s + "\n")
        out.flush()
        print(s)

    emit("# r34_pstar E1b -- codim{p* <= p} calibration, prediction 2R-3p")
    emit("# cell  R  q   p   N        hits    freq        -log_q(freq)  "
         "pred=2R-3p  |diff|")
    for (name, q, n, k, r, plist) in JOBS:
        R = n - k
        for (p, N) in plist:
            hits = 0
            for _ in range(N):
                y0 = [random.randrange(q) for _ in range(R)]
                y1 = [random.randrange(q) for _ in range(R)]
                if rank_mod(stack(y0, y1, p, R, q), p + 1, q) < p + 1:
                    hits += 1
            pred = 2 * R - 3 * p
            if hits:
                freq = hits / N
                meas = -math.log(freq) / math.log(q)
                emit("%-11s %2d %2d  %2d  %8d %6d  %.3e   %8.3f      %3d"
                     "      %.3f"
                     % (name, R, q, p, N, hits, freq, meas, pred,
                        abs(meas - pred)))
            else:
                lo = -math.log(1.0 / N) / math.log(q)
                emit("%-11s %2d %2d  %2d  %8d %6d  0 hits -> -log_q(freq) > "
                     "%.3f ; pred=%d  (consistent=%s)"
                     % (name, R, q, p, N, hits, lo, pred, pred > lo - 0.5))
    out.close()


if __name__ == "__main__":
    main()
