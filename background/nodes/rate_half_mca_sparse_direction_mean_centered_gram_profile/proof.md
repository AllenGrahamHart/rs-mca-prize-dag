# Proof

## Mean-centered Gram lemma

Let `B` be the `L` by `n` incidence matrix and put

```text
P=I_n-(1/n)J_n,       H=B P B^T.
```

Then `H` is positive semidefinite and

```text
rank(H)<=n-1.                                         (1)
```

Set `p=A^2/n`.  The diagonal entries of `H` are `A-p`; an off-diagonal
entry is

```text
x_ij=|S_i intersect S_j|-p in [-p,c-p].
```

On this interval, convexity puts the square below its endpoint chord:

```text
x_ij^2 <= (c-2p)x_ij+p(c-p).                         (2)
```

The condition `2A^2>=nc` says `c-2p<=0`.  Since `H` is positive
semidefinite,

```text
1^T H 1 >=0,
2 sum_(i<j) x_ij >= -L(A-p).                         (3)
```

Multiply `(3)` by the nonpositive chord slope and combine with `(2)`.  With
`C=p(c-p)=A^2 g/n^2`, this gives

```text
tr(H^2) <= C L^2 + A(A-c)L.                         (4)
```

Also `tr(H)=L(A-p)`.  The PSD trace-rank inequality and `(1)` imply

```text
L^2(A-p)^2 <= (n-1)(C L^2+A(A-c)L).
```

After cancellation,

```text
L((A-p)^2-(n-1)C) <= (n-1)A(A-c).
```

But

```text
(A-p)^2-(n-1)C = A^2 T/n^2.
```

The assumption `T>0` therefore proves `(MC1)`.

## Deficit profile

For transformed explanations, let `N_h` be the number with outside deficit
at most `h`.  The punctured ordinary Johnson argument gives `N_h<=C_h` in
the positive-Johnson case.  In the other case, choose exactly `A_h=m-h`
outside agreement coordinates for each explanation and apply `(MC1)`;
distinct degree-`<K` explanations have pairwise agreement at most `K-1=c`.
Thus `N_h<=C_h` in every printed case.

Moreover, for every `v>=h`,

```text
N_h<=N_v<=C_v.
```

Hence `N_h<=B_h=min_(v>=h)C_v`.  The suffix minima `B_h` are
nondecreasing.  An exact-deficit-`h` explanation owns at most
`floor(e/h)` slopes, and these weights are nonincreasing.  Saturating the
cumulative caps, or summation by parts, gives

```text
|Z| <= sum_h (B_h-B_(h-1))*floor(e/h),
```

which is `(MC2)`.

The primary verifier scans all 46 newly paid official supports with the
full exact profile.  The independent checker reconstructs the rational
mean-centered identities and tests the chord and trace inequalities on
finite block systems.
