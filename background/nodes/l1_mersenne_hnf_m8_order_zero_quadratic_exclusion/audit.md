# Audit

## Scope and normalization

The duplicated color is used and therefore may be divided to one. The two
omitted normalized colors are distinct members of `mu_8\{1}`, giving exactly
`binom(7,2)=21` patterns. Choosing one primitive eighth root loses no pattern:
all eighth roots lie in the unique subgroup `mu_8`, and the enumeration uses
all nonzero exponents.

## Moment range

Only root power sums through degree six enter the three centered moments.
The identity `sum a_r^k=-s` is therefore used strictly inside its proved
range `k<=h=7`. No fourth-moment extrapolation occurs.

The verifiers check `C_2!=0` before forming the invariant. Since
`s notin F_p`, neither `s` nor `s+7` vanishes. Thus a nonzero color second
moment also forces `1-S!=0`; the ratio step loses no zero-center branch.

## Torsion and extension fields

The equation `b_7(s)^n=1` is only a necessary consequence of the product of
the seven locator roots. Coprimality with this necessary condition is enough
for exclusion. Computing the gcd over `F_p(mu_8)` excludes common roots in
its algebraic closure, so `s` need not belong to the quadratic color field.

The primary and audit implementations use different bases, different
quadratic relations, and different common-root tests. Neither enumerates
`F_(p^f)` or constructs the very large official fields.

## Nonclaims

The proof is row-exact and does not extrapolate from `m=8` to `m=16`. It
does not classify degree at least three or supply the inner Belyi lift.
