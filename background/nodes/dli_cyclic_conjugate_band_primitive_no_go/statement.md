# DLI cyclic conjugate-band primitive no-go

- **status:** PROVED
- **closure:** exact tensor counterexample
- **consumer:** `dli_c2pp_joint_reserve`

Let `n=8r`, let `zeta` have exact order `n` in a finite field of
characteristic greater than eight, and draw `X in {0,1}^n` uniformly. Define

```text
F_2={2+8l:0<=l<r},       F_6={6+8l:0<=l<r}=-F_2 mod n,
E_2={the Fourier coefficients at every f in F_2 vanish},
E_6={the Fourier coefficients at every f in F_6 vanish}.
```

Then `E_2=E_6` and

```text
P(E_2)=P(E_6)=(36/256)^r.
```

After deleting the antipodally invariant words,

```text
P(Prim intersect E_2 intersect E_6)
  =(36^r-4^r)/256^r.
```

Consequently the primitive joint-to-product ratio is

```text
(64/9)^r (1-9^(-r)).                                    (CA1)
```

It equals `512/81>sqrt(16)` already at `r=1` and grows exponentially.

Thus dense cyclic phase rows, disjoint spectral bands, and antipodal
first-owner deletion do not imply any polynomial-loss product correlation
bound for arbitrary frequency sets. This does not falsify the DLI
square-root candidate: the two bands here are conjugate aliases, whereas the
official prefix lies in `1,...,t` with `t<n/2` and contains no pair `f,-f`.
The one-sided low-prefix geometry is load-bearing.
