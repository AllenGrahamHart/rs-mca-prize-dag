# L1 tangent double-root descent to a primitive shell

- **status:** PROVED
- **role:** convert each exact tangent owner to one lower-dimensional primitive shell
- **consumer:** `l1_mixed_petal_amplification`

## Setup

Use the exact-shell notation

```text
Omega=product_(x in H)(Z-x),       U-P=LQ,
deg P<k,       deg L=a,       deg Q=e,       w=a-k.
```

Fix a monic divisor `D|Omega` of degree `r` and consider the stratum

```text
gcd(L,Q)=D.                                             (TD1)
```

## Descent when `2r<=k`

Let `P_D` be the remainder of `U` modulo `D^2`, of degree below `2r`, and
put

```text
H'=H\roots(D),       Omega'=Omega/D,
W_D=(U-P_D)/D^2.                                      (TD2)
```

When `2r<=k`, every degree-below-`k` polynomial satisfying the tangent
conditions at `D` is uniquely

```text
P=P_D+D^2 R,       deg R<k'=k-2r.                     (TD3)
```

The convention at `k'=0` is the singleton zero codeword `R=0`.

There is a bijection between exact shell members satisfying `(TD1)` and
degree-below-`k'` codewords `R` such that:

1. `R` has exactly `a'=a-r` agreements with `W_D` on `H'`;
2. writing `W_D-R=L_0Q_0` for its complete agreement locator,
   `gcd(Q_0,Omega')=1`.

Under this bijection

```text
L=D L_0,       Q=D Q_0,
(n',k',a',e',w')=(n-r,k-2r,a-r,e-r,w+r).              (TD4)
```

Thus an exact tangent stratum descends in one step to a primitive exact
shell with larger surplus `w'` and smaller cofactor degree `e'`.

## Rigid range

If `2r>k`, the congruence `P=U mod D^2` has at most one solution with
`deg P<k`.  Hence the exact-`D` tangent stratum has size at most one.

## Scope

The punctured domain `H'` need not retain the original smooth subgroup
structure, and the theorem does not sum over the possible exact owners `D`.
It therefore does not close the tangent payment or justify applying a
smooth-domain Q theorem to the reduced shell.  It proves the exact recursive
object that a collective tangent theorem must count or absorb.
