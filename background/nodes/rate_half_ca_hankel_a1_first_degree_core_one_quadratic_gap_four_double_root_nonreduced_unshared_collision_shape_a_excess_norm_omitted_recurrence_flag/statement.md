# `A=1` collision shape-A excess-norm omitted-recurrence flag

- **status:** PROVED
- **closure:** every fiber degree drop is an initial omitted-recurrence zero run
- **consumer:** `rate_half_band_crossing_location`

Retain shape A and put

```text
R=|U_0|=3p-2,       d=2p-1=3e-2,
n=p-3=(3e-7)/2,     R-d-2=n.                       (ORF1)
```

Write the source moments and locator as

```text
h_j(t)=sum_(x in U_0)omega_x(t)x^j,
Q(t,X)=sum_(i=0)^d q_i(t)X^i,                      (ORF2)
```

and define every omitted recurrence defect by

```text
R_j(t)=sum_(i=0)^d q_i(t)h_(i+j)(t).               (ORF3)
```

For an off-line supported slope `delta`, let

```text
q_delta=n-deg_X G(delta,X).                        (ORF4)
```

Then, for every `0<=r<n`,

```text
q_delta>=r+1
 iff R_(d+1)(delta)=...=R_(d+1+r)(delta)=0.        (ORF5)
```

Thus `q_delta` is exactly the length of the initial zero run in the omitted
recurrence sequence.

Let `H_off(t)` be the squarefree polynomial cutting out all `3e` off-line
supported slopes, and put

```text
C_r=gcd(H_off,R_(d+1),...,R_(d+1+r))       (monic).
                                                               (ORF6)
```

The complete degree-drop and excess-norm ledgers are

```text
sum_delta q_delta=sum_(r=0)^(n-1)deg C_r,
deg T=e-sum_(r=0)^(n-1)deg C_r.                   (ORF7)
```

In particular, the first degree-drop locus is the off-line root set of the
first omitted recurrence defect

```text
R_(d+1)=Lambda(t)[X^n]G(t,X).                      (ORF8)
```

## Scope

This identifies the source invariant controlling `T`; it does not bound the
nested gcd degrees. A shape-A exclusion now needs a source/Hankel theorem
showing that the flag in `(ORF6)` is incompatible with the scalar weld,
collision jets, or the exact excess sum.
