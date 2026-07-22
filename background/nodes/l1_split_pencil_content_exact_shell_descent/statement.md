# L1 split-pencil content is exact-shell excess

- **status:** PROVED
- **role:** replace the complete-agreement guard in every interpolation-module
  split pencil by a basis-invariant coefficient-content test
- **consumer:** `l1_mixed_petal_amplification`

## Statement

Let `H subset F` contain `n` distinct points and put

```text
Omega=prod_(x in H)(X-x).
```

For a received word `U:H->F`, let

```text
M_U={(W,N) in F[X]^2:N(x)=W(x)U(x) for every x in H},
```

and fix any `F[X]`-basis `g_1,g_2` of `M_U`.  Suppose

```text
(W,N)=A g_1+B g_2,       W|Omega,       deg W=omega=n-m,
W monic,                 N=Wc,          deg c<k.       (CD1)
```

The zero coefficient pair is excluded.  Define the monic coefficient
content and its degree by

```text
G=gcd(A,B),        r=deg G.                         (CD2)
```

Then:

1. the ideal `(A,B)` and hence `G` are independent of the chosen module
   basis;
2. `G|W`, so `G` is a squarefree locator on `H`;
3. the complete agreement set is exactly

   ```text
   Agr_H(U,c)=(H\Z_H(W)) disjoint_union Z_H(G);       (CD3)
   ```

   in particular `agr_H(U,c)=m+r`;
4. the level-`m` member is exact if and only if `gcd(A,B)=1`; and
5. division by `G` gives the unique primitive representative

   ```text
   (W/G,N/G)=(A/G)g_1+(B/G)g_2                      (CD4)
   ```

   for the same codeword at its true exact shell `m+r`.

Consequently, coefficient content gives a canonical first-match partition of
the raw level-`m` split-pencil census.  A codeword with `a` agreements occurs
through its `binom(a,m)` support choices, every such coefficient pair has
content degree `a-m`, and all of them descend to the one coprime coefficient
pair at level `a`.  Thus the guarded interior BC numerator is precisely the
primitive coefficient-pair split-pencil census; higher-shell ray
multiplicity is not a separate owner/coalescing obligation.

## Scope

The theorem does not bound the number of coprime split-pencil pairs, prove
row-sharp Q or BC flatness, transport a nonconstant boundary multiplier, or
fit a finite prize numerator.  It identifies and removes the exact-shell
overcount before those estimates are attempted.
