# F3 h=3 char-zero classification (Codex overnight, 2026-07-08)

Status: PROVED for the char-zero classification; MACHINE-VERIFIED exact
against small cyclotomic rows and the banked norm-gate shapes by
`f3_h3_char0_classification.py`.

## Pre-registration

Stage: Terminal A, replacing the Conway-Jones enumeration route with a
direct unit-circle identity.

Hypothesis to falsify:

> If `X={x1,x2,x3}` and `Y={y1,y2,y3}` are distinct 3-subsets of roots
> of unity in characteristic zero with equal `e1` and equal `e2`, then
> both triples are zero-sum `mu_3` cosets. Equivalently, there are no
> exotic char-zero h=3 interior families at orders divisible by 5, 7, 9,
> or any other special order.

Failure criterion:

- an exact cyclotomic enumeration at some tested `n` finds a non-toral
  disjoint pair with `E1=E2=0`; or
- one of the banked finite-field norm-gate shapes has `E1=E2=0` in
  `Q(zeta_n)`, meaning it is a persistent char-zero family rather than a
  p-selected accident.

Success criterion:

- a proof explains why char-zero equality forces the toral `mu_3`
  classification for every order; and
- exact machine checks reproduce the toral counts and confirm that the
  banked interior finite-field shapes are char-zero nonzero but activate
  at their stated primes.

## Theorem

Let `X={x1,x2,x3}` and `Y={y1,y2,y3}` be 3-element subsets of roots of
unity in `C`. Assume

```text
x1 + x2 + x3 = y1 + y2 + y3
x1*x2 + x1*x3 + x2*x3 = y1*y2 + y1*y3 + y2*y3.
```

If `X != Y`, then

```text
x1 + x2 + x3 = y1 + y2 + y3 = 0,
```

and each of `X` and `Y` is a translate of the unique order-3 subgroup:

```text
X = a * {1, omega, omega^2},   Y = b * {1, omega, omega^2}
```

for roots of unity `a,b` and a primitive cube root `omega`. In a fixed
cyclic domain `mu_n`, such pairs exist exactly when `3 | n`; they are
the toral column, with unordered count `binom(n/3, 2)`.

## Proof

For any triple `X={x1,x2,x3}` of unit complex numbers, put

```text
s_X = x1 + x2 + x3,
p_X = x1*x2*x3,
e2_X = x1*x2 + x1*x3 + x2*x3.
```

Since every `xi` has absolute value one,

```text
e2_X = p_X * (conj(x1) + conj(x2) + conj(x3))
     = p_X * conj(s_X).
```

The same identity holds for `Y`. If `s_X=s_Y=s` and `e2_X=e2_Y`, then

```text
(p_X - p_Y) * conj(s) = 0.
```

If `s != 0`, then `p_X=p_Y`. The two monic cubic locators have the same
`e1`, same `e2`, and same product, hence the same coefficients and the
same root multiset. Therefore a distinct pair must have `s=0`.

It remains to classify zero-sum triples of unit complex numbers. Divide
by one element, so `1+u+v=0` with `|u|=|v|=1`. Then `|1+u|=1`, hence

```text
1 = |1+u|^2 = 2 + u + conj(u),
```

so `Re(u)=-1/2`. Thus `u` is a primitive cube root and `v=conj(u)`.
Undoing the scaling gives the claimed `mu_3` coset form. The count in
`mu_n` is then the number of unordered pairs of distinct cosets of the
unique subgroup of order three, namely `binom(n/3,2)`.

## Norm-gate corollary

For any ordered exponent shape `sigma=(A,B)` with `|A|=|B|=3`, define

```text
E1(sigma) = sum_{a in A} zeta_n^a - sum_{b in B} zeta_n^b,
E2(sigma) = sum_{a<a'} zeta_n^{a+a'} - sum_{b<b'} zeta_n^{b+b'}.
```

If `sigma` is not toral, then at least one of `E1,E2` is nonzero in
`Z[zeta_n]`. If the same shape is an h=3 trade after reduction modulo a
prime `p = 1 mod n`, then every nonzero obstruction among `E1,E2` has
norm divisible by `p`. Since each Galois conjugate of either obstruction
has complex absolute value at most `6`,

```text
|Norm(Ei)| <= 6^phi(n)
```

for every nonzero `Ei`. Hence each fixed non-toral shape can activate at
no more than

```text
floor(phi(n) * log(6) / (2 * log(n)))
```

rational primes `p >= n^2` for which a primitive `n`-th root exists.
This is a per-shape activation bound, not a pair-coprimality theorem
bounding the number of shapes activated at one prime.

## Replay

```text
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_char0_classification.py
```

Expected digest:

```text
CHAR0_CLASSIFICATION_PASS
```

