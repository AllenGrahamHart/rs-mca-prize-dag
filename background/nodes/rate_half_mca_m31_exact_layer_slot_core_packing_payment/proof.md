# Proof

## Exact-layer core bound

In this support range the parent ceiling satisfies `H>=m`, so there is no
separate cross-layer top slot.  Every slot in the recursive bank belongs to
one exact layer `h>b`.

Write a selected parameterized line as `c_gamma=a+gamma*b`.  At an inside
coordinate outside its common core, the equation

```text
r_0+gamma*r_1=a+gamma*b
```

holds for at most one parameter.  A core coordinate belongs to every one of
the `lambda` agreement sets.  Since every slot member has at least `h`
inside agreements, incidence counting in the fixed `e`-coordinate support
gives

```text
lambda*h <= e+(lambda-1)u.
```

Therefore

```text
u>=ceil((lambda*h-e)/(lambda-1)).                  (EL1)
```

This is an inside-core lower bound directly; it does not spend the outside
zero allowance `c`.

## Three-line payments

Retain absorption cutoff `65450` and complementary actual-core cap
`G_e=e+9-65450` from the parent dichotomy.  If any selected line exceeds
that cap, the weighted-prefix absorption branch pays the original family by
at most `5161243`.  Otherwise use the capped lower-aware convex charge.

The following legal cutoff table gives the same forced threshold for each of
the first three residual selections:

```text
e                 b       lambda    EL1 lower u
130226             65516   14        60540
130227             65516    5        49340
130228             65517   13        60126
130229             65517    4        43948
130230             65518   11        59048
130231             65518    4        43949
130232             65519    9        57431
130233,130234      65520    7        54736
130235,130236      65521    4        43951
```

For three distinct selected lines, pairwise inside-core intersections are
at most `c=5`.  The smallest packing lower bound in the table is therefore

```text
3*43948-C(3,2)*5=131829>130229,
```

and the two endpoint rows give `131838>130236`.  Exact replay checks every
row individually and proves all eleven supports.

## Adjacent wall

At `e=130237`, cutoff `b=65521` is legal but its first-layer denominator is
only 64 above zero.  The bank has

```text
prefix=15893203, groups=1933560, base=13961576.
```

It forces threshold two, and `(EL1)` gives only

```text
u=2*65522-130237=807.
```

The first-order packing expression `s*807-C(s,2)*5` has maximum 65529,
below `e`.  Under complementary cap 64796, after 7583 such lower bounds the
capped convex envelope has

```text
core budget=143903917,
charge=882245,
target=15894970,
next threshold=1.
```

No further actual line is forced.  This is a method wall, not an unsafe
certificate.
