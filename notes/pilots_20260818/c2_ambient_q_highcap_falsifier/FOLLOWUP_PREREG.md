# High-cap Haar follow-up: preregistration

The complete first pass is now frozen in `results.json` (Modal run
`ap-cyl68HXbcxGroGwKLkgEzV`): 189/189 primes returned, and 56 have a
nonempty primitive zero fiber. Thus the stronger ambient candidate
`K_amb<=sqrt(2n)` is falsified.

Before computing any Haar marginals, register the exact follow-up. For every
one of the same 189 rows, compute independently

```text
Z_1 = #{(A,B) : sum_i (1_A(i)+1_B(i)) zeta^(2i)=0},
B_0 = #{(A,B) : sum_i (1_A(i)-1_B(i)) zeta^i=0},
J_prim = (Z_0-C_1) 2^32/(Z_1 B_0).
```

The scalar subset histograms give `Z_1=sum_s h_even(s)h_even(-s)` and
`B_0=sum_s h_odd(s)^2`. The registered gate is the exact integer comparison

```text
(Z_0-C_1)2^32 > 8 Z_1 B_0.                              (J-FIRE)
```

because `sqrt(2n)=8` at `n=32`.

- If any row fires, the scale-free conjecture `J_prim<=sqrt(2n)` is
  falsified. This does not by itself falsify official `HAAR-21`.
- If no row fires, the ambient failure is absorbed by the exact marginal
  denominator on this complete high-cap analogue. This is evidence only.
- Missing rows or incomplete shards give `INCOMPLETE`.

