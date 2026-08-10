"""Escape test: replay the wave-10 arithmetic anchors (P1, P2, P10).

Stdlib only.  Run via tools/ramguard tiny -- python3 ...
"""
import math

OUT = []


def say(s):
    OUT.append(s)


n = 2 ** 41
k = 2 ** 40
R = n - k

# --- P1: r_Q / B_Q ------------------------------------------------------
s7 = math.isqrt(7 * k * k)
r_Q = 3 * k - s7 - 1
B_Q = r_Q + 1
say("k=%d  n=%d  R=%d" % (k, n, R))
say("floor(sqrt(7k^2)) = %d" % s7)
say("r_Q = 3k - floor(sqrt(7k^2)) - 1 = %d   [expect 389500552608]" % r_Q)
say("B_Q = r_Q+1 = %d   [expect 389500552609]" % B_Q)
say("PASS r_Q" if r_Q == 389500552608 else "FAIL r_Q")
say("PASS B_Q" if B_Q == 389500552609 else "FAIL B_Q")
say("7k^2 is a perfect square? %s" % (s7 * s7 == 7 * k * k))


def F(r):
    return r * r - n * (3 * r - (n - k))


say("F(B_Q-1) = %d  (>=0 ? %s)" % (F(B_Q - 1), F(B_Q - 1) >= 0))
say("F(B_Q)   = %d  (<0  ? %s)" % (F(B_Q), F(B_Q) < 0))
# quadratic hypothesis in the original form
say("(n-r)^2>=n(k+r) at r=B_Q-1 ? %s" % ((n - (B_Q - 1)) ** 2 >= n * (k + B_Q - 1)))
say("(n-r)^2>=n(k+r) at r=B_Q   ? %s" % ((n - B_Q) ** 2 >= n * (k + B_Q)))

endpoint = (B_Q + 1) * 2 ** 128
say("(B_Q+1)*2^128 = %d" % endpoint)
say("PASS endpoint" if endpoint ==
    132540169959144315698788704090115531231543332700160 else "FAIL endpoint")
say("log2(endpoint) ~ %.9f" % (math.log2(endpoint)))

# --- a_RH at three sample q below 2^167 ---------------------------------
say("")
say("--- a_RH(q) = n - floor(q/2^128) + 1 at three sample admissible q ---")
p_half = 132540169958804033333249306710494641010898987122689
for q in (2 ** 129 + 1, p_half, (2 ** 39 - 1) * 2 ** 128 + 12345):
    B = q // 2 ** 128
    say("q=%d  B=%d  a_RH=%d  (n-B+1);  covered by staircase? %s ; q<2^167? %s"
        % (q, B, n - B + 1, B <= B_Q, q < 2 ** 167))

# --- P2: the four printed prize rows ------------------------------------
say("")
say("--- P2: four printed prize rows ---")
rows = [
    ("1/2", 2 ** 41, 132540169958804033333249306710494641010898987122689, 389500552609),
    ("1/4", 2 ** 42, 411940680852499481698306614369841346700408394874881, 1210584858040),
    ("1/8", 2 ** 43, 979947269755402568812854322316630667196565607677953, 2879806199253),
    ("1/16", 2 ** 44, 2121285573237585848299875619011192262679065433997313, 6233898019554),
]


def proth(p):
    """p = u*2^s+1, u odd, u < 2^s; find a with a^((p-1)/2) = -1 mod p."""
    m = p - 1
    s = 0
    while m % 2 == 0:
        m //= 2
        s += 1
    if not (m % 2 == 1 and m < 2 ** s):
        return (False, None, s, m)
    for a in range(2, 200):
        if pow(a, (p - 1) // 2, p) == p - 1:
            return (True, a, s, m)
    return (False, None, s, m)


kk = 2 ** 40
for rate, N, p, Bp in rows:
    ok, a0, s_, u_ = proth(p)
    B = p // 2 ** 128
    say("rate %-4s N=2^%d  Proth(u=%d odd, s=%d, u<2^s=%s) witness a0=%s -> prime %s"
        % (rate, N.bit_length() - 1, u_, s_, u_ < 2 ** s_, a0, ok))
    say("      N | p-1 : %s ; p<2^256 : %s ; floor(p/2^128)=%d (printed %d) %s"
        % ((p - 1) % N == 0, p < 2 ** 256, B, Bp, "PASS" if B == Bp else "FAIL"))
    RR = N - kk
    Fnk = lambda r: r * r - N * (3 * r - RR)
    say("      F(B-1)=%d >=0 ? %s ;  F(B)=%d <0 ? %s"
        % (Fnk(B - 1), Fnk(B - 1) >= 0, Fnk(B), Fnk(B) < 0))

# --- bracket constants ---------------------------------------------------
say("")
say("--- bracket / floor constants ---")
say("k+2^34 = %d" % (k + 2 ** 34))
say("sigma_0 = d*c+c-1 with c=2^22,d=2048 : %d  [expect 8594128895]"
    % (2048 * 2 ** 22 + 2 ** 22 - 1))
say("v5 optimized c=2^33,d=1: dc+c-1 = %d ; k+that+1 = %d ; 2^34-1=%d"
    % (2 ** 33 + 2 ** 33 - 1, k + 2 ** 34, 2 ** 34 - 1))
say("sigma* = 8592912738 ; k+sigma*+1 <= k+sigma_0 ? %s"
    % (k + 8592912738 + 1 <= k + 8594128895))
say("3n/4 = %d ; k+2^34 = %d ; bracket width = %d ~ 2^%.3f"
    % (3 * n // 4, k + 2 ** 34, 3 * n // 4 - (k + 2 ** 34),
       math.log2(3 * n // 4 - (k + 2 ** 34))))

# --- P10: razor scale ----------------------------------------------------
say("")
say("--- P10: razor-slice budget scale ---")
for q in (2 ** 167, 2 ** 169, 2 ** 200, 2 ** 256):
    B = q // 2 ** 128
    say("q=2^%d : B=floor(q/2^128)=2^%d ; B<=n ? %s ; n-B+1 = %s"
        % (q.bit_length() - 1, B.bit_length() - 1, B <= n,
           (n - B + 1) if B <= n else "NEGATIVE (formula ill-posed)"))
say("residual budgets {2^39, 2^39+1} extend determined q from %d to %d"
    % ((2 ** 39) * 2 ** 128, (2 ** 39 + 2) * 2 ** 128))
say("relative q-extension = 2^128*2 / 2^167 = 2^%d" % (129 - 167))

print("\n".join(OUT))
