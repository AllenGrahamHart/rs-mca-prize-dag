# Budget-three antipodal intermediate Hensel certifier

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_fourth_root_gap_reduction`

Work on the maximal official intermediate floor

```text
e_2=0,       e_3!=0,
s=2^37,      d=4s,       r=s-1,
h=(s+1)/3,  v=2h-2.                                     (IHC1)
```

Retain `E,A,B,Q,R` from the fourth-root reduction:

```text
A=E^(-1/4),       B=sum_(m=0)^r [z^m]A z^m,
Q=(1-z^d)/E,      R=Q-B^4.                              (IHC2)
```

The primary intermediate gap gives `ord_0 R=3h`. Define

```text
Rbar=z^(-3h)R,       theta=Rbar(0),
H=Rbar/(theta B),    C_*=H^(1/3),       C_*(0)=1.       (IHC3)
```

Then `theta!=0`. Put

```text
Delta=[z^(h-1)] C_*^2/B,
kappa=[z^(2h-1)] C_*.                                  (IHC4)
```

For each scalar `u`, there is a unique normalized formal series `C_u` solving

```text
H=C_u^3(1+u z^h C_u/B),       C_u(0)=1.                (IHC5)
```

It satisfies the exact first-block expansion

```text
C_u=C_*-(u/3)z^h C_*^2/B mod z^(2h).                  (IHC6)
```

Every valid intermediate floor-boundary solution has `u=phi/theta`, where
`phi` is its scaled centered fourth outer coefficient, and its degree bound
forces

```text
3 kappa-u Delta=0.                                     (IHC7)
```

Consequently:

```text
Delta!=0              ==> u=3kappa/Delta is unique;
Delta=0, kappa!=0     ==> the intermediate boundary is impossible;
Delta=0, kappa=0      ==> this terminal gate leaves one scalar u. (IHC8)
```

For every surviving `u`, the complete certifier requires that `C_u` be a
polynomial of degree at most `2h-2`, that the multiplied identity `(IHC5)`
hold exactly, and that

```text
W^4+theta W+theta u=product_i(W+w_i)                   (IHC9)
```

split into four distinct centered parameters fractionally-linearly matched
to square-root lifts `a_i^2=b_i` of the deleted roots. These conditions are
also sufficient to reconstruct the intermediate antipodal pencil.

Common subgroup scaling preserves the three cases in `(IHC8)`, so one deleted
root may again be normalized to one. This theorem gives a unique candidate on
the nondegenerate branch and a precise one-parameter degenerate branch; it
does not prove that every candidate rejects.
