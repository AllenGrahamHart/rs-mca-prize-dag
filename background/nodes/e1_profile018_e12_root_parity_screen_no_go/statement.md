# E1 profile-(0,18) energy-12 root/parity screen no-go

- **status:** PROVED
- **closure:** explicit positive autocorrelation witness
- **scope:** cofactor-514 necessary screens before coefficient realization

The 13-profile cofactor-`514` frontier is not emptied by combining energy,
local parity multiplicity, primitive-root divisibility modulo 257, and
positivity of the conjugate-square target.

Indeed, put

```text
D={1,2,...,11,15},
Y(X)=18+sum_(d in D)(X^d+X^(-d)).
```

Then:

1. `Y-18` has all-unit energy 12;
2. its parity polynomial has exact multiplicity two at `X=1`;
3. `s=148=3^59 mod 257` has order 256 and `Y(s)=0 mod 257`;
4. `Y(exp(i theta))>=4` for every real `theta`; and
5. its exact cubic relation index is `K=378`.

This is an autocorrelation-level witness only. It is not asserted to be the
autocorrelation of an 18-singleton integral polynomial, and it supplies no
official exact norm. Coefficient realization is therefore a genuinely
necessary next gate.
