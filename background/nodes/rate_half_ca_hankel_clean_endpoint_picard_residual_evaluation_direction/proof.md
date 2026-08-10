# Proof

Push the fibre ideal sequence at `x_0`:

```text
0 -> O_P1(-m) --Q(-;x_0)--> O_P1 -> O_(C_x0) -> 0.                  (1)
```

Because `m>1`, its cohomology sequence is exactly `(PED2)`. Globally, this
is the fibre at `x_0` of the canonical quotient

```text
0 -> O -> pi_*O_C
  -> O(-rho) tensor H^1(O(-m)) -> 0.                                (2)
```

Now work in the discrete valuation ring `O_(C,P_*)`. The point is an
effective Cartier divisor of length one, so a local equation `u` generates
its maximal ideal. If `t=X-x_0` is the base parameter and the ramification
index is `e`, then

```text
t=c u^e,       c a unit.                                             (3)
```

The positive modification is locally generated over `O_C` by `u^(-1)`.
Multiplication by `t` identifies its direction in the fibre of `pi_*O_C`
with the class of

```text
c u^(e-1).                                                           (4)
```

Write the fibre polynomial locally as

```text
Q(z;x_0)=S(z)^e A_other(z),       A_other(S)!=0.
```

Then

```text
A_0=Q/S=S^(e-1)A_other,                                              (5)
```

so `(4)` is a nonzero scalar multiple of the class of `A_0`. This proves
the fibre-socle assertion, including the repeated-supported case.

It remains to identify the image under `(PED2)`. Pair the connecting class
of a fibre polynomial `f` with `p in H^0(O(m-2))` by the standard local
Grothendieck-residue form of Serre duality along the fibre divisor:

```text
<partial(f),p> = sum_(Q(r;x_0)=0) Res_r( f(z)p(z) dz / Q(z;x_0) ).  (6)
```

For `f=A_0`, cancellation in `(PED1)` gives

```text
A_0 p dz/Q = p dz/S.                                                  (7)
```

Among the local residues along `Q=0`, this has one simple pole, at `S`, and
its residue is a nonzero scalar times `p(S)`. Hence
`partial(A_0)=c_S ev_S` with `c_S!=0`, proving
`(PED4)--(PED5)`.

The trivial summand in `(2)` is the kernel of the connecting map. Since
`ev_S!=0` for `m>1`, the modification direction has a nonzero negative-block
component. The elementary-modification dichotomy therefore selects its
second splitting and gives `(PED6)`. QED.
