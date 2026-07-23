# L1 Mersenne FRG saturation pilot result

- **Modal app:** `ap-0EK5ErTdMIAYixk0Leq78F`
- **case:** `(p,m,h)=(31,8,7)`
- **resources:** one CPU, 2 GiB, 120-second hard timeout
- **polynomial construction:** `0.067027` seconds
- **resultant construction:** `0.567595` seconds
- **coefficient system:** seven nonzero equations, maximum total degree `112`,
  constructed by `5.970123` seconds
- **saturation:** `INCOMPLETE`; SymPy's generic grevlex Groebner calculation
  hit the 120-second function timeout

No unit/nonunit result was returned, so this run supplies no mathematical
evidence about analogue or official emptiness. It establishes that forming
the exact Frobenius reciprocal system is cheap and that generic
three-variable SymPy saturation is the wrong backend. A follow-up contributor
run should use Singular, Magma, or a structure-aware two-variable elimination
and must emit an independently checkable unit certificate or complete
component decomposition. No retry is authorized on the current Modal account.
