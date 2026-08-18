# Global-atom pair-core owner floor

- **status:** PROVED
- **scope:** the global-atom branch of the quotient-only official KoalaBear
  residual

Let `H_p` be the complete pair core of a quadratic quotient type. Then

```text
|H_p|=m-2=1116046.
```

For the one global pole-simple atom `(Q,A,B)`, every `H_p` is disjoint from
the domain roots of `Q` and is contained in the atom owner set `G`. Distinct
pair cores intersect in at most `K-1=1048575` coordinates. Since at least
`q=520` quotient types occur, the second-moment union bound gives

```text
|G| >= |union_p H_p|
    >= ceil(q|H_p|^2/(|H_p|+(q-1)(K-1)))
     = 1187712.                                      (OF1)
```

This is `4191` coordinates beyond the first generic large-owner value
`2m-K+1=1183521`. It does not bound the number of atoms with an owner this
large or pay their images.

## Falsifier

A denominator root on one quotient pair core; a core coordinate outside the
atom owner; a distinct-type intersection above `K-1`; or an incorrect
second-moment floor.
