# Proof

Put `q=K'-10`.  Exactify supports two through five.  For each nonempty
support-two/support-three pair with `M_3<=M_2`, the carrier-position theorem
leaves two fixed-union cases.  If `s_2+s_3<q`, neither case can satisfy the
common-root bound, so that exact pair is impossible.  At `K'=71` this
removes 961 pairs.  Every other pair remains explicit.

Pairs with `M_3=M_2+1` retain their position provenance until support four
is chosen.  If also `M_4=M_2+1`, replace the formerly uncharged leaf by all
six `T23/A23/T24/A24/N34/N34A` alternatives.  Otherwise retain the old
cross-support caps.  This prevents vector deduplication from discarding an
unpriced geometry case.

For supports four and five retain every exact defect pair and the joint
support-four external charge whenever `s_4+s_5<q`.  Retain all 120
support-six through support-nine terminal/fallback choices.  Duplicate cap
vectors may be identified, and a componentwise dominated vector discarded,
because every deficit weight is nonnegative and every later operation takes
componentwise minima.

For each surviving leaf, compute

```text
P=sum_(d=2)^9 C(11-d,2) cap_d.
```

Combine it with the unchanged rank-nine marks `G`, kernel capacity, and
residual record floor `R` as

```text
Cap_full=floor((G+R P)/55).
```

At `K'=71`, the exact maximum is the branch printed in the statement.  It
lies below the safe premium ceiling by

```text
23776122440930417094576446937038395558574009,
```

and the final integral comparison gives `(P71)`.  The old unsafe
one-step branch `s2=32,s3=s4=s5=31` is paid in all six geometry cases; its
largest residual premium is the `N34` case and is already below the new
maximizer.

At `K'=72`, the exact maximizer has
`s2=33,s3=s4=s5=31`; here `M_3=M_2+2`, outside the one-step trichotomy.
The same exhaustive replay gives `(W72)`.  This is a method wall, not a
counterexample.  QED.
