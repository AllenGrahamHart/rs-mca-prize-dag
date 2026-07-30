# Proof

Let `q_u:P1_Y->P1` and `q_v:P1_Z->P1` be the two degree-five reflection
quotients supplied by the dihedral reduction. Their common totally ramified
value has one point in each quotient coordinate; call these points `y_0`
and `z_0`. In the unique admissible degree-five pole profile, the outer map
after `q_u` and `q_v` has a simple pole at this value. Hence `y_0` and
`z_0` are among the six distinct order-five poles of `F`.

Let `C` be the normalization of the outer `(2,2)` component. Above
`Z=z_0`, both points of the degree-two projection `C->P1_Z` map under `Y`
to `y_0`: both have the same image in the full dihedral quotient, and
`q_u^(-1)` of that image is the singleton `y_0`. These are two distinct
points because the inertia at this branch value is the order-five rotation
group and contains neither reflection defining the projections. Thus,
set-theoretically and with total fiber degree two,

```text
Y^*[y_0]=Z^*[z_0] as reduced degree-two fibers on C. (KBM5-2)
```

The endpoint degree-two map `h` is unramified over every source pole. Write

```text
h^(-1)(z_0)={w_+,w_-},       h^(-1)(y_0)={t_+,t_-}.
```

Because `y_0,z_0` are poles of `F`, these four points belong to the complete
source set `{alpha_i}` (with the two pairs allowed to coincide).

The source reduction has a quadratic map `psi(X)=W` and the complete source
identity

```text
div(B)=psi^*(sum_i [alpha_i]).                       (KBM5-3)
```

Fix `w` in `{w_+,w_-}` and put `D_w=psi^*[w]`. This is an effective
degree-two divisor contained in `div(B)`. For every point `x` in `D_w`,
counted with multiplicity, the source component maps to the pullback of
`(KBM5-2)`, so every root of `H(T,x)` belongs to `{t_+,t_-}`. Complete-source
saturation gives two distinct source labels at every root of `B`: each
specialized row divisor has local order at most `ord_x(B)`, while their
total local order is `2 ord_x(B)`. Hence both available labels occur and

```text
H(T,x) is proportional to (T-t_+)(T-t_-).          (KBM5-4)
```

Complete-source saturation assigns `x` to the matching star vertex
`v={t_+,t_-}` with its multiplicity. Summing over `D_w` contributes weight
two to `v`. The divisors `D_(w_+)` and `D_(w_-)` are disjoint because they
are fibers over distinct source values, so their contributions add. Hence

```text
w_v >= deg(D_(w_+))+deg(D_(w_-))=4.                (KBM5-5)
```

But the proved quartic defect budget
`sum_v binom(w_v,2)<=3` implies `w_v<=3`. Equation `(KBM5-5)` is a
contradiction. Thus `n=5` is empty, leaving exactly `(KBM5-1)`. QED.
