# Proof

By the parity-profile reduction, the six light-light chords have distinct
non-diameter lengths and every nonzero autocorrelation magnitude is one or
two. Consider a non-diameter class containing exactly one heavy-heavy chord.
Its contribution of magnitude four cannot be reduced to `0,1,2` by no other
chord or by the at most one light-light chord in that class:

```text
|+-4|=4,             |+-4 +-1| in {3,5}.
```

Therefore that class contains a heavy-light chord. More generally, every
non-diameter heavy-heavy class either contains a heavy-light chord or contains
at least two heavy-heavy chords. If two heavy-heavy chords share a class but
there is no heavy-light chord, their signed magnitude-four products must
cancel; the optional unit chord then leaves magnitude zero or one. This
forces the two outer heavy coefficients to have opposite signs.

There is at most one heavy-heavy diameter. If there is none, the three
heavy-heavy lengths are either all distinct or exactly two are equal. They
cannot all be equal because `Z/128Z` has no element of order three. Equality
of two lengths is precisely a circular three-term progression on `H`. The
singleton third class must contain a heavy-light chord, proving templates 3
and 4.

Now suppose `H` contains an antipodal pair. The two remaining heavy-heavy
lengths are equal exactly when the third point is a quarter point. After
translation and reflection this is `H={0,32,64}`. The only possible
heavy-light diameter then uses the missing quarter point `96`. If its light
coefficient is `ell` and the heavy signs are `s_0,s_1,s_2`, the distance-32
coefficient is

```text
A_32=4 s_1(s_0+s_2)+2 ell(s_2-s_0).
```

It has absolute value four or eight for every sign choice, contradicting the
`(6,7)` profile. Hence `96` is absent. The same formula without its second
term, with at most one light-light contribution `u in {-1,0,1}`, is

```text
A_32=4 s_1(s_0+s_2)+u.
```

Its absolute value is at most two only when `s_2=-s_0`. This proves the
quarter template and gives `D_64=16`. If the third heavy point is not a
quarter point, the two non-diameter heavy-heavy lengths are distinct, so both
singleton classes contain heavy-light chords. This is template 2.

The diameter square masses and cross sums now follow from the parity-profile
ledger `C=-34+D_64/2`. QED.
