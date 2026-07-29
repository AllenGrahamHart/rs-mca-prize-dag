# Proof

Fix `r` and `R` as in the statement. If `R` divides `J_j`, then

```text
J_j=R P_j
```

for a monic polynomial `P_j` of degree `r`. Hence every corresponding
neighbor lies in the affine flat

```text
a_0 + R F[X]_(<=r).                                  (1)
```

The direction space in `(1)` has dimension `r+1`: multiplication by the
nonzero polynomial `R` is injective, and all products have degree at most
`(t-r)+r=t=k-1`, so they are codeword directions of the residual
`RS[F,Omega,k]` code.

Apply `(AS1)` from `upstream_gfv4_affine_span_list_compiler` to this affine
flat, the same received table, and agreement threshold `m=k+w`. It contains
at most

```text
floor(C(N-k+r+1,r+1)/C(w+r+1,r+1))                  (2)
```

listed codewords. The anchor belongs to the flat and is counted in `(2)`.
Deleting it proves `(CS1)`.

For `r=0`, `(2)` is

```text
floor(1048577/67448)=15,
```

so `B_0=14`. For `r=1`, the unfloored ratio is

```text
(1048578*1048577)/(67449*67448).
```

The exact integer comparison

```text
241*67449*67448
 <= 1048578*1048577
 < 242*67449*67448
```

gives a flat cap `241`, hence `B_1=240`. This proves `(CS2)`.

Finally, each squarefree degree-`t` direction locator `J_j` has exactly
`C(t,r)` monic degree-`t-r` divisors. Count incidences `(j,R)` with
`R|J_j`. There are `d C(t,r)` incidences, while `(CS1)` puts at most `B_r`
neighbors over any fixed `R`. This proves `(CS3)`. Substituting
`d=215793`, `t=4980`, and `B_1=240` gives `(CS4)`. QED.
