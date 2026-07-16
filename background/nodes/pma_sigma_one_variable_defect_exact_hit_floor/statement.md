# PMA sigma-one variable-defect exact-hit floor

- **status:** PROVED
- **role:** superpolynomial sigma-one floor and reserve-scope guard
- **consumer:** `petal_mixed_amplification`, `imgfib`

## Finite theorem

Let `n` be a sufficiently large dyadic integer, put

```text
k=n/2,  K=k-1,  L=n-k,  M=L/2,
s_n=floor(n/(32 log_2 n)),
```

and let `F_q` contain a cyclic subgroup `H` of order `n`. Choose a maximal
sigma-one sunflower source with a balanced `(k-1)`-core, one background
point, paired remaining points, distinct nonzero labels, and base polynomial
`Q=1`, as in the defect-four obstruction.

For an integer `d` put

```text
a=d+2,
H_d=binom(L,2)+L+d+1.
```

Assume

```text
1 <= d <= M-2,
d <= k/2-s_n-3,
q>H_d,
q-1-a>2(M-a).
```

There is a choice of the source labels for which the number `N_d(U)` of
distinct codewords with exact core defect `d`, no background hit, exactly
`a` singleton petal hits, and total agreement `k+1` satisfies

```text
N_d(U) >= floor(
  binom(K,d) q^d(q-H_d)
  * 2^a binom(M,a)/(q-1)_a
  * (1-2(M-a)/(q-1-a))
).
```

Every counted codeword has trivial exact stabilizer, lies outside the growing
dyadic near-coset owner, and comes from a source outside the odd-lift owner.
It is mixed-petal and therefore belongs to the carried-layout Post class.

## Superpolynomial corollary

There is an infinite family of dyadic rate-half rows with generated field
size polynomial in `n` and sigma one for which `N_d(U)` is exponential in
`n`. More precisely, for sufficiently large dyadic `n`, take

```text
d=n/8,  a=n/8+2.
```

Linnik's theorem supplies a prime `p=-1 mod n` with `p<=n^A` for one absolute
constant `A` after enlarging the lower threshold. Put `q=p^2`. Then the
order-`n` subgroup of `F_q^*` generates `F_q`, all finite-theorem hypotheses
hold, and some source satisfies

```text
N_d(U) >= 3^(n/4)/(4q).
```

Consequently no fixed polynomial `n^B` bounds the sigma-one post-owner class
over all smooth rate-half rows with polynomial-size generated fields.

## Scope

This does not refute reserve-conditioned `imgfib`. Its asymptotic hypothesis
also requires `sigma>=C n/log n`; sigma one is deliberately outside that
scope. Finite adjacent-row work must use a row-specific exact ledger rather
than infer a uniform exponent-six or uniform sigma-one polynomial theorem.
