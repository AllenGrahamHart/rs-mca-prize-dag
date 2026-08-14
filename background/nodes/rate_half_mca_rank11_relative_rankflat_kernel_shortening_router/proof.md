# Proof

Let `W` be the absorbing correction space, `dim W=s`, and let `T` be an
`s+1` coordinate tuple on which evaluation has rank `r<s`. Put

```text
U=ker(ev_T),       u=dim U=s-r.
```
Every word of `U` vanishes at every coordinate in `T`.

Consider an irreducible positive-dimensional component of the common zero
set of the coordinate equations indexed by `T`. If its projection to the
slope line is one point, it contributes one finite slope. Assume the
projection is nonconstant. It is then dense in the slope line.

In this case `r>=1`. If `r=0`, every correction word vanishes on `T`, so
the coordinate equations there reduce to `E_x(Z)=0`. Empty residual common
support makes every `E_x` a nonzero polynomial; their common slope set is
finite and cannot support a nonconstant projection. Hence, on the present
component,

```text
1<=u=s-r<=s-1<=9.
```

Choose a complement `W_0` to `U` in `W`. Evaluation embeds `W_0` into
`F^T` with rank `r`; choose `r` coordinates `B subset T` on which it is an
isomorphism onto its image. Solving the equations on `B` gives a unique
polynomial complement curve

```text
P_0(Z)=sum_j P_(0,j)Z^j in W_0 tensor F[Z]_(<=31).
```

Compatibility with the remaining equations in `T` holds identically on the
slope-dominating component. Every solution on the component is

```text
P(Z)=P_0(Z)+Q(Z),       Q(Z) in U.
```

The correction space absorbs every `H_j`, `j>=2`. Decompose

```text
H_j=H_(0,j)+H_(U,j),       H_(0,j) in W_0, H_(U,j) in U.
```

On `B`, the coefficient equation for `j>=2` forces
`P_(0,j)=-H_(0,j)`. Therefore every high coefficient of `H+P_0` lies in
`U`. Define the affine codeword owner from the low coefficients,

```text
L(X,Z)=(H_0+P_(0,0))+Z(H_1+P_(0,1)).
```

For `x in T`, all high `U`-coefficients vanish and the component equations
say that `L(x,Z)` equals the residual received line identically in `Z`.
Translate the received line and all explanations by this codeword pair.
Translation preserves slopes, agreement supports, and support-wise
pair-noncontainment.

After translation, every component explanation is `U`-valued and both
received columns vanish on `T`. Let `L_T` be the monic locator of `T`.
Every correction codeword is divisible by `L_T`. Since `U` is nonzero, the
RS root bound also gives `|T|<=K'-1`, so the shortened dimension is positive.
Delete `T` and divide by `L_T`. The common-core cancellation adapter
preserves actual bad witnesses and produces

```text
(n'',K'',m'')=(n'-|T|,K'-|T|,m'-|T|),
```

with unchanged `R=n''-K''` and `d=m''-K''`. Division is injective on `U`,
so the descended explanation space has dimension exactly `u` (or a smaller
dimension if the selected component uses only a subspace).

Since `u<=9`, the proved global-core rank-drop theorem pays the complete
component: ranks at most eight by support-local transversality and rank nine
by the uniform `T=667` margin/interleaving split. This proves the component
route.

The proof treats one irreducible component. It supplies no bound on the
number of distinct flats, complement curves, or affine owners, so no
aggregate sum is claimed.
