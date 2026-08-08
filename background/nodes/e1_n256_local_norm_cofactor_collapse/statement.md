# E1 N=256 local-norm cofactor collapse

- **status:** PROVED
- **closure:** proof plus local reciprocity

Let `zeta` be a primitive `256`-th root, let
`alpha=F(zeta)` have either first-band `N=256,s=5` profile, and
put

```text
R=|Norm_(Q(zeta)/Q)(alpha)|,
mu=v_2(R).
```

For every nonzero such norm,

```text
R/2^mu = 1 mod 256.                                    (1)
```

Suppose a pair-feasible row prime `p` divides `R`, and write
`R=p m`. The prime-field reduction gives `p=1 mod 256`. Therefore

```text
m/2^mu = 1 mod 256.                                   (2)
```

The exact cofactor bounds then collapse as follows:

- profile `(3,4,0)`: `1<=mu<=5`, `m<64`, and necessarily
  `m=2^mu`. Thus a collision norm is exactly `R=2^mu p`;
- profile `(4,2,0)`: `mu in {1,2,4,8,16}` and
  `m=2^mu(1+256t)<2^17`. There are exactly `419` resulting
  cofactor values.

On a prize-envelope row, the exact field floor sharpens the second line to

```text
m<=floor(18^64/(B_P 2^128))=2013.
```

There are then exactly eight possible `(4,2,0)` cofactors:

```text
mu=1:  2, 514, 1026, 1538;
mu=2:  4, 1028;
mu=4:  16;
mu=8:  256;
mu=16: none.
```

The global residue-degree rule removes `1026=2*3^3*19`: in a
`256`-th cyclotomic norm, every odd-prime exponent is divisible by that
prime's order modulo 256, whereas both `3` and `19` have order 64. Thus the
exact live prize list has seven values:

```text
{2, 514, 1538, 4, 1028, 16, 256}.
```

In particular, the square-mass-16 profile has only five possible cofactors,
not every integer below 64. This is a necessary norm shape, not a proof that
the odd norm part is prime or lies in a live interval.

## Round-24 catch (2026-08-08, CATCH-24C): this node's audit mis-filed a falsifying witness

audit.md:44-47 dismisses a 248-bit prime as "below 2^250 and
therefore harmless" — reading it only against the prize-interval
bar (p >= B_P*2^128 ~ 2^255.9). Against the ADMISSIBILITY bar
(p = 1 mod 256, p < 2^256) it is a folded-kernel WITNESS, one of
eight banked since July 2026 that already refuted the
family-uniform emptiness form at N' = 256. Filter bars must be
named per consumer. See the round-24 board event on
integer_code_distance_cert.
