"""D1: exact size of the open residual, counted in (A,s,e) strata,
and the exact deficit of the counting layer in each.

Official row: N=2^41, R=2^40, m=2^37.
Strict budget B=2^39   : r=rho=4m-1, A=3, s=0, m   <= e <= floor(rho/3)
Half-dist  B=2^39+1    : r=4m ; A=3 (rho=4m-1, s=0, m+1<=e<=floor(rho/3))
                              ; A=1 (rho=4m, s in {0,1,2},
                                     m+1<=e<=floor((rho-s)/(1+s)))
"""
import math


def say(s=""):
    print(str(s), flush=True)


m = 2 ** 37
N, R = 2 ** 41, 2 ** 40
tot = 0
say("profile           rho            s  e-range                         "
    "#e        cap(e)-target at e_lo")

# strict A=3
rho = 4 * m - 1
lo, hi = m, rho // 3
cnt = hi - lo + 1
tot += cnt
target = rho + 1                                   # T <= r+1 = 4m
cap = 4 * lo + 1
say("strict A=3        %-14d %-2d [%d, %d]  %-9d cap=%d target=%d deficit=%d"
    % (rho, 0, lo, hi, cnt, cap, target, cap - target))

# half-distance A=3
lo2, hi2 = m + 1, rho // 3
cnt = hi2 - lo2 + 1
tot += cnt
target2 = rho + 2                                  # T <= r+1 = 4m+1
say("half-dist A=3     %-14d %-2d [%d, %d]  %-9d cap=%d target=%d deficit=%d"
    % (rho, 0, lo2, hi2, cnt, 4 * lo2 + 1, target2, 4 * lo2 + 1 - target2))

# half-distance A=1
rho1 = 4 * m
for s in (0, 1, 2):
    lo3 = m + 1
    hi3 = (rho1 - s) // (1 + s)
    cnt = hi3 - lo3 + 1
    tot += cnt
    d = rho1 - s
    Delta = d - (1 + s) * lo3
    Tmax = ((N - s) * lo3 + Delta) // d
    say("half-dist A=1     %-14d %-2d [%d, %d]  %-9d T_max=%d target=%d "
        "deficit=%d" % (rho1, s, lo3, hi3, cnt, Tmax, rho1 + 1,
                        Tmax - (rho1 + 1)))
say()
say("TOTAL open (A,s,e) strata = %d ~ 2^%.3f" % (tot, math.log2(tot)))
say("q-axis payoff of closing them: 2^167 -> 2^167 + 2^129 (relative 2^-38)")
say()
say("Deficit law at the strict A=3 face: cap-target = 4(e-m)+1, so the")
say("counting layer misses by ONE slope at e=m and by 4(e-m)+1 further out.")
say("At e=m every failure is forced onto the sharp face h=0, T=rho+2.")
say("=== END ===")
