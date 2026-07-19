# F3 h=3 three-to-one characteristic-zero classification

Status: PROVED EXACT CHARACTERISTIC-ZERO COUNT AND SIGNED-COLLISION
LARGE-FIELD TRANSFER; OFFICIAL POLYNOMIAL-FIELD CORRIDOR REMAINS OPEN.

## Statement

Let `n=2^s`, `s>=3`, and let `mu_n` be the complex `n`th roots of unity.
The ordered relations

```text
(1-x)(1-y)(1-z)=1-w,
x,y,z,w in mu_n\{1},                              (CZ1)
```

are exactly the permutations of

```text
(x,y,z)=(q,-q,-q^2),       w=q^4,                 (CZ2)
```

where `q in mu_n` has order at least `8`.  Consequently

```text
N_3to1^C(mu_n)=3(n-4).                            (CZ3)
```

## The valuation pattern

Put `zeta=zeta_n` and write a nonzero exponent as `a=2^r A`, with
`A` odd.  In `Q(zeta)`, the unique prime above `2` satisfies

```text
v(1-zeta^a)=2^r.                                 (CZ4)
```

This follows from the standard factorization of `1-zeta^(2^r)` down
the quadratic cyclotomic tower; multiplication of the exponent by an odd
number is a Galois automorphism.

If `(CZ1)` has exponents `a,b,c,d`, equality of valuations says that a sum
of three powers of two is one power of two.  After permuting the inputs, the
only possibility is

```text
v_2(a)=v_2(b)=r,
v_2(c)=r+1,
v_2(d)=r+2.                                      (CZ5)
```

In particular `r<=s-3`.  Put `eta=zeta^(2^r)`, of order
`N=2^(s-r)>=8`, and write

```text
x=eta^A, y=eta^B, z=eta^(2C), w=eta^(4D),
A,B,C,D odd.                                     (CZ6)
```

## Two quadratic separations

Expand `(CZ1)`.  In the quadratic extension

```text
Q(eta)=Q(eta^2) direct_sum eta*Q(eta^2),
```

the odd-exponent part is

```text
-eta^A-eta^B+eta^(A+2C)+eta^(B+2C)
  =(eta^(2C)-1)(eta^A+eta^B).
```

It must vanish separately.  Since `eta^(2C)!=1`, this gives

```text
B=A+N/2 (mod N),                 y=-x.           (CZ7)
```

After substituting `(CZ7)`, equation `(CZ1)` becomes, with
`theta=eta^2` of order `M=N/2`,

```text
(1-theta^A)(1-theta^C)=1-theta^(2D).             (CZ8)
```

Separate odd and even powers once more in

```text
Q(theta)=Q(theta^2) direct_sum theta*Q(theta^2).
```

The odd part of `(CZ8)` gives `theta^A+theta^C=0`, and the even part
then gives

```text
C=A+M/2 (mod M),
D=A       (mod M/2).                             (CZ9)
```

Equations `(CZ7)` and `(CZ9)` are exactly

```text
y=-x,       z=-x^2,       w=x^4.
```

Conversely `(1-q)(1+q)(1+q^2)=1-q^4`, so every displayed relation is
valid.

There are `n-4` choices of `q` having order at least `8`.  The choices `q`
and `-q` give the same unordered input triple, and no other choice does.
Every triple has six orderings, proving `(CZ3)`.

## Distinct-input norm bound

Suppose now that `p=1 (mod n)` and `H=mu_n(F_p)`.  Lift a finite-field
relation to the same exponents over `Q(zeta_n)` and put

```text
alpha=(1-zeta^a)(1-zeta^b)(1-zeta^c)-(1-zeta^d).
```

After cancellation of the two constant terms, the eight signed roots are

```text
xy, xz, yz, w, -x, -y, -z, -xyz.                (CZ10)
```

Assume first that `x,y,z` are pairwise distinct.  The first three positive
products in `(CZ10)` are pairwise distinct, and `w` can duplicate at most
one of them.  Similarly `-x,-y,-z` are pairwise distinct and `-xyz` can
duplicate at most one of them.  No root can occur twice in both groups.  To
see this, after permuting suppose `-xyz=-x`, so `yz=1`.  If one of
`xy,xz,yz` also equals `-x`, then respectively `y=z=-1`, `z=y=-1`, or
`x=-1`; the first two contradict distinctness, while the last forces the
duplicating output `w=1`.  Thus every root in `(CZ10)` has multiplicity at
most `3`.

Put `m=n/2`.  For each antipodal pair `{zeta^r,-zeta^r}`, let `b_r` be the
difference of the two multiplicities in `(CZ10)`.  Then

```text
sum_r |b_r| <= 8,       |b_r| <= 3,
sum_r b_r^2 <= 3^2+3^2+2^2=22.                 (CZ11)
```

For the `m=phi(n)` odd Galois conjugates, antipodal folding followed by
Parseval gives exactly

```text
(1/m) sum_(j odd) |alpha(zeta -> zeta^j)|^2
  =sum_r b_r^2 <=22.                            (CZ12)
```

If the complex relation is false, `alpha` is a nonzero algebraic integer.
The finite relation puts `alpha` in a prime above `p`, hence
`p | Norm(alpha)`.  Applying arithmetic--geometric mean to `(CZ12)` yields

```text
0<|Norm(alpha)|<=22^(m/2)=22^(n/4).             (CZ13)
```

This is strictly sharper than the previous triangle-inequality bound
`8^(n/2)=64^(n/4)`.

## Signed-collision payment

The preceding bound can be sharpened by paying every equality among the
eight signed roots in `(CZ10)`.  The `binom(8,2)=28` pair labels collapse to
only `19` distinct algebraic loci.  The pairs not involving `w` give the
twelve conditions

```text
x=y, x=z, y=z,
x=-1, y=-1, z=-1,
x=-yz, y=-xz, z=-xy,
xy=1, xz=1, yz=1,                               (CZ14)
```

and the seven remaining loci are

```text
w=xy, w=xz, w=yz, w=-x, w=-y, w=-z, w=-xyz.    (CZ15)
```

Each locus in `(CZ14)` has at most `(n-1)^2` solutions, after which the main
relation uniquely forces `w`.

For six of the seven pairs involving `w`, choose an input variable not
appearing in the root paired with `w`.  The main relation is linear in that
variable with a nonzero coefficient of the form `(1-u)(1-v)`, so these loci
also have at most `(n-1)^2` records.  The remaining pair is `w=-xyz`.  On
this locus the relation becomes

```text
(x+y-xy)+z(1-x-y+2xy)=0.                       (CZ16)
```

Unless the coefficient of `z` vanishes, `(x,y)` forces at most one `z`.  If
both the coefficient and the constant in `(CZ16)` vanish, then

```text
xy=-1,       x+y=-1,
```

so `x,y` are the at most two ordered roots of `T^2+T-1`.  This exceptional
part contributes at most `2(n-1)` records.  Hence the complete signed-root
collision locus has size at most

```text
C_coll<=19(n-1)^2+2(n-1).                       (CZ17)
```

Off this locus the eight roots in `(CZ10)` are distinct.  Every antipodal
difference `b_r` is then in `{-1,0,1}`, and Parseval improves `(CZ12)` to

```text
sum_r b_r^2<=8,
0<|Norm(alpha)|<=8^(n/4)                        (CZ18)
```

whenever the complex obstruction is nonzero.  Thus collision-free finite
relations lift as soon as `p>8^(n/4)`.  Combining `(CZ3)`, `(CZ17)`, and
`(CZ18)` gives

```text
p>8^(n/4)
  => N_3to1((1-H)\{0})
       <=19(n-1)^2+2(n-1)+3(n-4)
       =19n^2-33n+5.                            (CZ19)
```

The right side satisfies the direct-floor `C36` inequality on every official
order.  Thus `(CZ19)` closes the entire h=3 stratum in this expanded
large-field branch.  It does not cover the hard official corridor beginning
at `p>=n^2`; `8^(n/4)` is still exponential in `n`.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_three_to_one_charzero_classification.py
```

Expected digest:

```text
H3_THREE_TO_ONE_CHARZERO_CLASSIFICATION_PASS rows=3 folded=22 collision_free=8 collision_loci=19
```
