# Proof

If a support-`c` circuit exists, deleting any point leaves an independent
`(c-1)`-set with at least the deleted point as a completion.  Thus `M_c=0`
is equivalent to an empty stratum, proving the last line of `(SC1)`.

Now assume `M_c=q-s>0`.  Choose an attaining independent deletion `A_0`,
let `Z_0` be all of its completions, and put `B=A_0 union Z_0`.  The
completion coordinates are distinct and

```text
|B|=(c-1)+(q-s)=q+c-1-s.                         (1)
```

For any independent `(c-1)`-set `A`, let

```text
H_A={f in V:f|_A=0}.
```

Evaluation on `A` is independent, so `dim H_A=11-c`.  Every `f in H_A`
vanishes on every circuit completion of `A`: the completion evaluation
functional lies in the span of the evaluations on `A`.  Hence `H_A`
vanishes on the complete carrier `U_A`.

Apply this to `A` and `A_0`.  Grassmann gives

```text
dim(H_A intersect H_(A_0)) >= 2(11-c)-10 = 12-2c.    (2)
```

This is positive for `2<=c<=5`.  The intersection vanishes on `U_A union
B`, so the common-root bound and `(1)` give

```text
|U_A setminus B|
 <= K-(12-2c)-|B|
 = s+c-1.                                             (3)
```

If `s=0`, the attaining completion labels span the full `q`-dimensional
annihilator.  Every support-`c` circuit label therefore has a representation
on `B`.  Comparing that representation with its minimal circuit support
uses at most

```text
|B|+c=q+2c-1<=q+9<K+1.
```

Vandermonde independence forces the circuit support into `B`, proving the
first line of `(SC1)`.

Suppose `0<s<q`.  A circuit with exactly `j` points outside `B` is exposed
by deleting each of those `j` points.  The remaining independent deletion
has `j-1` outside points, so `(3)` permits at most

```text
s+c-1-(j-1)=s+c-j
```

outside completions.  There are at most

```text
C(b,c-j) C(N,j-1)
```

such deletions.  Each circuit is counted exactly `j` times.  Multiplication,
division by `j`, integer flooring, and summation over `j=1..c`, together
with the inside stratum, prove `(SC1)`.  Each circuit extends to at most
`C(m-c,11-c)` selected eleven-sets.  QED.
