# Pair-noncontained proper-subspace occupancy compiler

- **status:** PROVED
- **scope:** field-general Reed-Solomon MCA slope families
- **repair:** replaces the false final `w` basis-extension factor by the
  exact certified factor `L=max(1,e-(N-m))`

Let `C=RS[F,D,K]` have length `N`.  Let

```text
r_gamma=r_0+gamma r_1,       m>K,       w=m-K,
```

and let `Z` be a finite set of distinct slopes.  Suppose that for every
`gamma in Z` there is an explanation `c_gamma` in one affine codeword space
of dimension `q`, where `1<=q<=K`, with agreement at least `m`.  Suppose
also that the maximal agreement support of every selected pair is
same-support pair-noncontained.

Put

```text
e=min_(b in C) wt(r_1-b),       t=N-m,
L=max(1,e-t).
```

Then

```text
|Z| <= floor(max(A_q,B_q)/L),                         (PSO)

A_q = N^(q+1)_falling /
      (m (w+1)^(q-1)_rising),

B_q = (N-K+q)^(q+1)_falling /
      ((w+1)^q_rising).
```

The maximum is a maximum of rational numbers before the final floor.

At the first residual dimensions this pays every KoalaBear affine rank
`q<=9` and the Mersenne-31 rank `q=1`, independently of direction support.
The exact higher-rank support walls are in the contract.

This theorem does not restore the rejected ordered-basis denominator: its
last factor is at most `w`, and can be exactly one.
