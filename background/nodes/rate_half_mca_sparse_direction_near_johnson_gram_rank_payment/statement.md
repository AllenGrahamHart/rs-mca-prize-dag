# Sparse-direction near-Johnson Gram-rank payment

- **status:** PROVED
- **closure:** field-general post-Johnson list cap and exact adjacent strip
- **scope:** one shortened support-wise MCA-bad family after a codeword
  direction gauge

## Ordinary-list lemma

Let `S_1,...,S_L` be distinct `A`-subsets of an `n`-set with

```text
|S_i intersect S_j|<=c       (i!=j),       A>c.
```

In the near-Johnson regime put

```text
g=nc-A^2>=0,
G=(A-c)^2-cg.
```

If `G>0`, then

```text
L <= floor(n*A*(A-c)/G).                            (GR1)
```

## MCA payment

Use the notation of the punctured Johnson profile:

```text
N=R+K,       m=d+K,
r_1=b+q,     E=supp(q),     |E|=e<d.
```

Put `u=floor(e/2)`, `n=N-e`, and `c=K-1`.  Suppose the ordinary Johnson
denominator is positive at deficit `u`, and at deficit `e` put

```text
A=m-e,
g=nc-A^2>=0,
G=(A-c)^2-cg>0.
```

Define

```text
J_u=floor(n*(m-u-K+1)/((m-u)^2-nc)),
Q_e=floor(n*A*(A-c)/G).
```

Then the selected slope family satisfies

```text
|Z| <= (e-1)J_u+Q_e.                               (GR2)
```

Together with the preceding Johnson prefix, `(GR2)` expands the complete
certified low-support walls to

```text
KoalaBear K=14:   e<=64037,   j=R-e>=984539;
Mersenne K=6:     e<=65418,   j=R-e>=983158.
```

At the endpoints `(GR2)` equals

```text
198047217 <= 274980728111395087,
 16759641 <=          16777215.
```

At the next KoalaBear support `G=-36911`, so the lemma stops.  At the next
Mersenne support `G=247950` remains positive, but `(GR2)=18212004` exceeds
the official budget.

## Nonclaims

This does not pay either adjacent support, claim that `(GR1)` is sharp,
use the full-lift near-MDS structure, close a middle-support interval, or
close an official row.

## Falsifier

A legal equal-size set family exceeding `(GR1)`, a legal selected MCA
family exceeding `(GR2)`, or an incorrect official endpoint or adjacent
value.
