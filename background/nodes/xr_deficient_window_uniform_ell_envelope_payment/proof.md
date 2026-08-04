# Proof

## Exact elementary-symmetric profile

The tuple count is the elementary symmetric function

```text
T_p(B)=e_p(m_1,...,m_v).                             (1)
```

Hold all parts except `a>=b` fixed and transfer one unit from `b` to `a`,
without exceeding `ell`. The only changing terms of `e_p` are those using
both parts, and their change is

```text
((a+1)(b-1)-ab)e_(p-2)(other parts)
 =(b-a-1)e_(p-2)(other parts)<=0.                   (2)
```

Repeated concentration produces the packed profile. Choosing either `p`
full parts or `p-1` full parts and the remainder gives exactly `(UE1)`.

## Comparison with ell=1

Use the common-ray cap on the full `s`-dimensional hull. The sequential
distinct-fiber lower bound, which is weaker than `(UE1)`, gives

```text
|Tau| <= (s+1) product_(j=0)^s(e-j)
                    /(2 product_(j=0)^s(r-j ell)).  (3)
```

Here

```text
e<=x-2ell-1,       r=h-x+ell.                       (4)
```

Compare `(3)` to the `ell=1` cap at

```text
y=x+(s-1)(ell-1).                                  (5)
```

Its numerator parameter is `e_1=y-3`, and

```text
e_1-(x-2ell-1)=(s+1)(ell-1)>=0.                    (6)
```

For each `0<=j<=s`, its denominator factor is `h-y+1-j`, while

```text
(r-j ell)-(h-y+1-j)=(s-j)(ell-1)>=0.               (7)
```

Thus every numerator factor in `(3)` is at most the corresponding `ell=1`
factor at `y`, and every denominator factor is at least the corresponding
one. The higher-`ell` cap at `x` is no larger than the proved `ell=1` cap at
`y`.

Insert the common-ray endpoints

```text
y<=8,500,560,263       for s=11,
y<=4,265,559,234       for s=10.
```

Expanding `(5)` gives `(UE2)`. At either endpoint the smallest reference
factor `h-y+1-s` is positive. Equation `(7)` then gives `r-s ell>0`, so the
tuple lower bound used in `(3)` is admissible. QED.

## Tuple-incidence no-go fence

Let `ell_0,r_0,d_0,e_0` be as in `(UE3)`. The defining floor gives

```text
7ell_0<=h-4.                                        (8)
```

Hence

```text
ell_0<=3d_0-2h-1,       e_0>=2r_0,                 (9)
```

and the verifier checks the remaining official depth inequalities exactly.
Thus these numbers and the packed three-fiber profile satisfy every numerical
hypothesis currently used by the tuple-incidence route.

For `p=2,3`, `(UE1)` gives

```text
T_2=ell_0^2+2ell_0,       T_3=ell_0^2.             (10)
```

For `p>=4` it gives zero. Use the common-ray owner constants `2` and `3` in
`(CRE2)`, take the permitted worst cases `N=n` and `e=e_0`, and evaluate the
resulting exact pair and triple caps. Their floors are the four integers in
the statement, all strictly above `B_0`. There is no higher-order incidence
to use. This proves the scoped no-go claim.

The calculation does not construct `P,Q`, a received pair, or a target
family realizing the packed profile. It proves only that the presently
banked numerical currencies cannot exclude or pay that profile. QED.
