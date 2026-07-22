# Proof

The smooth-trace substar router proves that, on a fixed product fiber, the
graph of nodal edges on the `g` generic vertices has maximum degree at most
three. Restricting that graph to signed-disjoint distance-six edges can only
delete edges. The handshake lemma therefore gives

```text
D_nod(t)<=floor(3g/2).                              (1)
```

The disjoint-six multiplicity gate gives

```text
D_6(t)>=F_0(m)  if a=0,
D_6(t)>=F_A(m)  if a=1.                            (2)
```

Since `D_sm=D_6-D_nod`, equations `(1)` and `(2)` prove `(NSD2)` and
`(NSD3)`, including the harmless maximum with zero.

It remains to check where the lower bound in `(2)` is at least twice the
nodal cap. In the antipodal-free class, write first `m=2q`. Then

```text
F_0(m)-2nu_0(m)=2q^2-14q-6,
```

which is positive for `q>=8`. If `m=2q+1`, then

```text
F_0(m)-2nu_0(m)=2q^2-12q-11,
```

which is positive for `q>=7`. These are exactly the even and odd cases with
`m>=15`. Hence `D_6>=2D_nod`, and therefore
`D_sm=D_6-D_nod>=D_nod`.

In the antipodal class, `g=m-1`. For `m=2q` and `m=2q+1`, respectively,

```text
F_A(m)-2nu_A(m)=2q(q-8),
F_A(m)-2nu_A(m)=2q^2-14q-8.                        (3)
```

The first is nonnegative for `q>=8`, and the second is positive for `q>=8`.
Thus nodal edges are dominated by smooth edges whenever `m>=16`. This proves
`(NSD4)`.

For a retained target the rich-fiber ladder gives

```text
m>=7+ceil((P(t)-18)/2).                            (4)
```

Consequently `P>=33` implies `m>=15`, while `P>=35` implies `m>=16`.
Combining `(4)` with `(NSD4)` proves `(NSD5)`.

Finally multiply the two pointwise inequalities in `(NSD5)` by the
nonnegative quotient weight `R(t)` and sum in each target class. The targets
below the corresponding threshold are exactly the two terms `L_0,L_A` in
`(NSD6)`. This proves `(NSD7)`. QED.
