"""Independent w8 cross-check of the rate-half floor arithmetic (no v4 code reused)."""
from math import lgamma, log2, log
def log2C(n,m): return (lgamma(n+1)-lgamma(m+1)-lgamma(n-m+1))/log(2)
n=2**41; k=2**40; c=2**22; N=n//c; d=2048; s=2_978_146
m=N//2+d
sigma_star=8_592_912_738
assert k+d*c+s == k+sigma_star, (d*c+s, sigma_star)   # exact agreement = k+sigma*
lc=log2C(N-1,m)
# cyclic: count = C(N-1,m)/(N q^{d-1}); unsafe iff count > q/2^128 iff N q^d < 2^128 C
q_boundary=(128+lc-log2(N))/d
margin_at_cap=128+lc-log2(N)-d*256
# fixed tail: count = C(N-1,m)/q^d; unsafe iff q^{d+1} < 2^128 C
ft_boundary=(128+lc)/(d+1)
# qcore gap at cap: C(127,64) vs q/2^128 at q=2^256 -> trigger bits = 256-128 = 128
qcore_gap=128-log2C(127,64)
print(f"log2C={lc:.4f} q_boundary={q_boundary:.9f} margin={margin_at_cap:.6f} ft_boundary={ft_boundary:.10f} qcore_gap={qcore_gap:.4f}")
assert abs(q_boundary-256.036659972895)<1e-6
assert abs(margin_at_cap-75.079624489)<1e-4
assert abs(ft_boundary-255.9209759026302)<1e-6
assert q_boundary>256 and ft_boundary<256
print("W8_RATEHALF_CROSSCHECK_PASS")
