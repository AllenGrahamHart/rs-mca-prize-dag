# KoalaBear Q6 u2 complete-source conic exclusion

- **status:** PROVED
- **scope:** KoalaBear MCA row at agreement `1116048`
- **upstream:** PR `#1128`, head `ad109774f7d9bc320e7e0c046ba83471f39d5cd9`
- **consumer:** `rate_half_band_closure`

In the proved KoalaBear equality-wall source reduction, let `H(T,X)` be an
actual irreducible `Q=6,s=6,u=2` outgoing component in the conic-image
branch. Let `alpha_1,...,alpha_12` be the distinct source labels, put

```text
q_i(X)=H(alpha_i,X),
```

and let `B` be the complete source form of degree `24`. The endpoint producer
gives nonzero quartics `q_i|B`, and the conic quotient makes every
`div(q_i)` invariant under its involution `iota`. Then

```text
sum_(i=1)^12 div(q_i)=2 div(B).                       (KBC-1)
```

Consequently `div(B)` is `iota`-invariant, and every `iota`-fixed root of
`B` has even multiplicity. These two facts exclude all three retained
reduced conic profiles: reciprocal, `D_4`, and `D_5`. Together with the
previously proved ramified-common exclusions, every actual
`Q=6,s=6,u=2` conic-image component is impossible.

This closes one structural branch only. It supplies no distinct-slope count,
owner, `U_Q`, `U_BC`, `U_new`, cap `68`, adjacent certificate, or KoalaBear
row payment. Ledger movement is zero.

## Falsifier

An actual component for which a source row does not divide `B`, equality
`(KBC-1)` fails, or one of the exact reciprocal/`D_4`/`D_5` orbit ledgers is
compatible.
