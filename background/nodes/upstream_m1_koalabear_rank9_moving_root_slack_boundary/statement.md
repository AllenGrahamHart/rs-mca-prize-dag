# KoalaBear rank-nine moving-root slack boundary

- **status:** PROVED
- **closure:** proof under the printed record and C5-owner contracts
- **role:** finite rate-half support-wise MCA satellite
- **consumer:** `rate_half_band_closure` (evidence only)
- **upstream source:** `przchojecki/rs-mca` commit `951ad203`

Fix the KoalaBear row

```text
n=2097152,       k=1048576,       A=1116048,
j=n-A=981104,    t=A-k=67472.                          (MR1)
```

Consider one post-C5, post-source-rational, full-outside rank-two record with
source support `Sigma`, `s=|Sigma|`, polynomial pair `P,Q`, full monic gcd
`H`, and reduced pair

```text
P=H Pbar,       Q=H Qbar,       gcd(Pbar,Qbar)=1,
e=max(deg Pbar,deg Qbar).                              (MR2)
```

Let `W` be the moving carrier, `x=|W|-j`, and for each selected finite slope
`eta` let

```text
F_eta={z in W : a(z)+eta b(z)=0},
|F_eta|=x+delta_eta,       delta_eta>=0.               (MR3)
```

Assume the inherited record contracts:

1. the source vanishes on `W`, and no point of `F_eta` is a common root of
   `P,Q`;
2. the outside-source common-root set `C` has
   `c=|C|=A-x-s`, its locator `L_C` divides `H`, and
   `deg H+e<=k-1`;
3. the source-rational first-match owner leaves only
   `e>=ceil(s/2)`;
4. at least `J>=21` distinct finite slopes are selected; and
5. the proved C5 owner removes every positive-rank translated source pair
   whose two-coordinate span has a basis in the base field.

Then every selected member has the exact moving-root factorization

```text
Pbar+eta Qbar=L_(F_eta) A_eta,
deg A_eta<=e-x-delta_eta.                              (MR4)
```

Define

```text
h=deg H-c,       u=e-x,       ell=k-1-deg H-e,
r=s-t-1.                                                   (MR5)
```

These are nonnegative integers satisfying

```text
h+u+ell=r,       0<=delta_eta<=u.                     (MR6)
```

The boundary `r=0` is C5-owned. Consequently every surviving official
record obeys

```text
s>=67474,       e>=33737,       deg H<=1014838.       (MR7)
```

At the first unresolved source size `s=t+2`, the only slack triples are

```text
(h,u,ell)=(1,0,0), (0,1,0), (0,0,1).                 (MR8)
```

The last cell is C5-owned. In the first cell a surviving extra linear gcd
factor must be nonbase. In the second cell at most one selected member can
have `delta_eta=1`; at least twenty members have `delta_eta=0` and a linear
cofactor, and any two projectively base members are C5-owned.

This theorem is a record-level route cut, not a complete selector, upper
ledger, adjacent certificate, or KoalaBear threshold theorem.
