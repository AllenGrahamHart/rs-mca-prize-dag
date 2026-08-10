# Sharp rate-half FPC5 six-value rational-map descriptor

- **status:** PROVED
- **consumer:** `l1_fpc5_ratehalf_m4_t2_payment`

Fix one official sharp rate-half `M=4,t=2` source, one touched pair, and one
exact contributor. Write `P_1,P_2` for the touched petals, `P_3,P_4` for
the untouched petals, `B` for the background, and `C` for the source core.
Let `L_i` be the petal locators and use the guarded cofactors

```text
U_1=L_1A_1,       U_2=L_2A_2,       deg A_i<=ell-3,
F=(U_1-U_2)/(c_2-c_1),
W=(c_2U_1-c_1U_2)/(c_2-c_1).                         (SV1)
```

Then `U_1,U_2` are coprime, the rational function

```text
phi=U_1/U_2                                             (SV2)
```

has degree exactly `d=2ell-3`, and the contributor injects into the class
of such rational maps satisfying

```text
P_1 subset phi^(-1)(0),
P_2 subset phi^(-1)(infinity),
D=Z(F)=phi^(-1)(1),             |D|=2ell-3,
B subset phi^(-1)(c_1/c_2),     |B|=ell-3,             (SV3)
P_u intersect phi^(-1)(alpha_u)=empty,  u=3,4,
alpha_u=(c_1-c_u)/(c_2-c_u).                           (SV4)
```

The six marked values

```text
0, infinity, 1, c_1/c_2, alpha_3, alpha_4              (SV5)
```

are pairwise distinct. The `1`-fiber is complete, reduced, and lies in the
core. The background condition fixes `ell-3` distinct points in a second
fiber, while exact untouched-petal nonagreement excludes two further fibers
on two disjoint `ell`-point blocks.

At this sharp endpoint the source blocks exhaust the official domain:

```text
|C|+|B|+sum_i |P_i|
 =(5ell-5)+(ell-3)+4ell
 =10ell-8=n.                                           (SV6)
```

Thus this is a full-domain marked rational-map problem, not an arbitrary
split flat with untyped coordinates.

## Scope

The descriptor does not bound the number of such maps. The zero, pole, and
`c_1/c_2` fibers may contain additional points away from the displayed
source blocks, and no reciprocal, dihedral, or quotient classification is
asserted. Its purpose is to expose the exact fiber data available to an
incidence, value-set, or rational-map argument.
