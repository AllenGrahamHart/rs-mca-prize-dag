# Proof

The canonical factorization and centered outer values give

```text
Q=B^4+alpha B^2V^2+beta BV^3+gamma V^4
 =B^4+V^2K,
K=alpha B^2+beta BV+gamma V^2.                       (1)
```

Put `S=EV^2K`.  Since `EQ=1-z^N`,

```text
A:=EB^4=1-z^N-S.                                     (2)
```

Multiplying `T` by `B^3` shows

```text
TB^3=NA-zA'.                                         (3)
```

Substitution of `(2)` into `(3)` yields

```text
P=TB^3-N=zS'-NS.                                     (4)
```

Every term in the right side of `(4)` contains `V`, because `S` contains
`V^2`.  This proves `V|P`.  Pairwise coprimality of the canonical factors
implies `gcd(B,V)=1`.  If a nonconstant factor divided both `V` and `T`, then
`(EDG1)--(EDG2)` would make it divide the nonzero scalar `N`.  Thus
`gcd(V,TB)=1`, proving `(EDG2)`.

The secondary-differential dependency gives

```text
E'B+4EB'
 =-8Hc_0z^(2H-1)+8(H-1)E_4b_0z^(2H).                (5)
```

Since `N=8(H-1)`, substitution of `(5)` in `(EDG1)` proves `(EDG1')`.
The scalar eight is invertible, so `(EDG2)` is equivalently
`V|P_0^raw` with `gcd(V,T_0B)=1`.

Let `mathcal A=E^(-1/4)` be the normalized formal series.  The definition of
`B` and the primary double gap give

```text
mathcal A-B=z^(2H)D                                  (6)
```

for a formal series `D`: `B` ends in degree `2H-3`, while the next two
coefficients vanish.  Since `E mathcal A^4=1`, equation `(6)` implies

```text
A=EB^4=1+z^(2H)R                                    (7)
```

for a polynomial or formal series `R` through every degree occurring in
`A`.  Applying `(3)` and subtracting `N` gives

```text
P=z^(2H)((N-2H)R-zR'),                               (8)
```

which proves `(EDG3)`.  Since `P=8P_0^raw`, the same valuation holds for
`P_0^raw`.  Now `V=z^H C`, `C(0)=1`, and hence `gcd(C,z)=1`. Combining
`V|P_0^raw` with `(8)` proves `C|P_0`; the gcd assertion in `(EDG4)` follows
from `(EDG2)` and `(EDG1')`.

For minimum support, `(BSP5)` gives `deg J_supp=5H-11`.  The support
compiler bounds

```text
deg J_supp<=2+2deg C+(3H-7).
```

Together with `deg C<=H-3`, equality at `5H-11` forces
`deg C=H-3`, proving `(EDG5)`.

Reduce `(EDG1')` modulo `C`.  Equation `(EDG4)` gives

```text
T_0B^3=H-1 mod C.                                    (9)
```

Let `C_sharp` be the monic normalization of `C`.  Resultant multiplicativity,
the root-product formula for a monic first polynomial, and `(9)` yield

```text
Res(C_sharp,T_0)Res(C_sharp,B)^3
 =Res(C_sharp,H-1)=(H-1)^(deg C),                   (10)
```

which is `(EDG6)`.  The gcd statement makes both resultants nonzero.  Finally

```text
H-3=2^37-2=0 mod 3.
```

The right side of `(10)` is a cube, as is `Res(C_sharp,B)^3`; division
proves `(EDG7)`. QED.
