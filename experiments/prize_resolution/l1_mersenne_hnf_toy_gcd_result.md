# L1 Mersenne HNF toy gcd result

- **Modal app:** `ap-gT0DyToHmnD911PEFFilTd`
- **case:** `(m,h,p,n)=(8,7,31,256)`
- **worker time:** `2.805886` seconds on one CPU with a 1-GiB limit
- **exact common gcd:** `s-1` in `F_31[s]`
- **prime-field part:** `s-1`
- **outside-prime-field quotient:** `1`

Thus the order-zero hypergeometric normal form has no non-prime-field
cyclotomic survivor on this analogue. The sole common root `s=1` is exactly
the prime-field chamber already excluded by the rational-derivative theorem.
This is calibration and evidence for the Frobenius/gcd route, not an
official-row exclusion. The full remote payload, including every remainder
coefficient, is pinned by SHA-256 in the JSON certificate and independently
recomputed by `check_l1_mersenne_hnf_toy_gcd.py`.

The first app `ap-zbyPpAZamkVE3AlXYQJzov` failed before producing a
mathematical output because of a SymPy coefficient-domain coercion error.
