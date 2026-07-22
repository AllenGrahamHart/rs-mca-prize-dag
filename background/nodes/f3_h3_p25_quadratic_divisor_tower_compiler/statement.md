# H3 P25 quadratic divisor-tower compiler

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_dsp8_correlation_bound` (evidence/router)
- **dependencies:** `f3_h3_global_resultant_compression`,
  `f3_h3_shifted_product_sidon`

Let `n=2^s`, let `p=1 mod n`, and put `q=25`. A nonidentity target with
`P(t)>=q` exists if and only if the following quadratic divisor-tower system
has a geometric solution in characteristic `p`.

Choose a monic polynomial `Q(X)` of degree `q`, a residue `Z(X)` of degree
below `q`, a scalar `T`, and inverse selectors `tau,eta`. Impose

```text
XZ=1 mod Q,       T tau=1,       (T-1)eta=1.       (QDT1)
```

In `F_p[X]/(Q)`, start

```text
A_0=1-X,       B_0=(X-T)Z,                        (QDT2)
```

and introduce degree-below-`q` residues satisfying

```text
A_(j+1)=A_j^2 mod Q,
B_(j+1)=B_j^2 mod Q,       0<=j<s,
A_s=B_s=1.                                         (QDT3)
```

Every congruence is encoded coefficientwise as `left-right=Q times L` with
the unique quotient of the allowed degree. All equations have total degree
at most two over `Z`.

With internal residues and all quotient polynomials retained, the system has
exactly

```text
(4s+1)q+5-2s =98s+30 variables,
(4s+2)q+4-2s =98s+54 equations.                    (QDT4)
```

Thus the official band `13<=s<=41` uses at most `4,048` variables and
`4,072` quadratic equations, independent of the exponential value of `n`.
The equations are empty in characteristic zero by shifted-product
Sidonicity. Consequently any checked nonzero integer Nullstellensatz
certificate for one `s` gives a complete finite outer set of possible
characteristics for nonidentity `P>=25` at that order.

This is a complete bounded-degree presentation, not a claim that Groebner,
resultant, SAT, or Nullstellensatz computation on four thousand variables is
cheap. No run is authorized without a smaller measured pilot, a certificate
checker, and a hard resource ceiling.
