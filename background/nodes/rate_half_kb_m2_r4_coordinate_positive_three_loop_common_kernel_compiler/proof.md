# Proof

The positive loop-ramification gate puts the three loops at both branch
values and at the single root of the nonzero linear form `B_1`.  These three
labels are distinct.  A projective quotient change preserving the branch
pair, followed if necessary by branch interchange, puts them at
`0,infinity,1`.  Therefore `B_1=beta(W-1)` with `beta!=0`.

The positive coefficient normal form is

```text
H(T,X)=A_2(W)T^2+A_0(W)+XT B_1(W),       W=X^2.   (1)
```

At a loop with target pair `{a,-a}`, the product is `-a^2` and the sum is
zero.  The positive Vieta product equation is

```text
A_0(W)-p A_2(W)=0.                                (2)
```

Applying `(2)` at `W=0,infinity,1` determines the constant, leading, and
middle coefficients of `A_0`.  Solving the middle coefficient gives
exactly `(KBP3K-2)`.

Now let `{u,v}` be either nonloop edge and set `p=uv`, `s=u+v`.  Substitute
`(KBP3K-2)` and `A_2=d_0+d_1W+d_2W^2` into `(2)` and collect the four
unknowns.  This is the first row in `(KBP3K-3)`.  The sum equation

```text
z B_1(z^2)+s A_2(z^2)=0                           (3)
```

is the second row.  Repeating these two rows for the two nonloop fibers
gives `M h=0`.  Every actual packet supplies the guarded vector `h`.
Conversely, `(KBP3K-2)` reconstructs the three loop rows, while the four
matrix rows reconstruct the two nonloop product/sum pairs; the nonvanishing
of `A_2` makes each quadratic have the prescribed two roots.  This proves
the exact kernel criterion.

For `(4,4,2)`, substitute loop representatives `(1,b,c)` and nonloop data

```text
(z,p,s)=(x,b,1+b),       (y,-b,1-b).              (4)
```

Direct determinant expansion gives

```text
det M=-xy(b-1)(b+1)(x-1)(x+1)(x-y)(x+y)
          (y-1)(y+1) R_442.                       (5)
```

For `(4,3,3)`, use `(x,b,1+b)` and `(y,c,1+c)`.  Then

```text
det M=xy(b+1)(c+1)(x-1)(x+1)(x-y)(x+y)
         (y-1)(y+1) R_433.                        (6)
```

Every factor outside `R_442,R_433` in `(5)--(6)` is a source branch/root,
source collision, or target collision guard in the displayed placement.
The exact symbolic checker constructs `(KBP3K-2)--(KBP3K-3)` independently
and verifies both polynomial identities by expansion. QED.
