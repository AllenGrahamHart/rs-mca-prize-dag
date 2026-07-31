# Proof

Fix a root-sign row `(epsilon_1,epsilon_2)`.  Use the parent product equation
to substitute its guarded rational value of `c`.  Let `P(t)` be the
numerator of the remaining product minor and `Q(t)` the numerator of the
remaining q weld.  Both have degree at most two in `t`.

Form the direct Sylvester resultant

```text
R(r,b)=Res_t(P(t),Q(t)).                            (1)
```

No leading coefficient is inverted, so `(1)` includes every branch where
either quadratic drops degree.  Let

```text
C_(e1,e2)(r)=r^3+(2e1e2+e1*i)r^2
                   +(-1-2e2*i)r-e1*i
```

be the parent cubic.  Exact elimination gives the same identity in all four
sign rows:

```text
Res_r(C_(e1,e2)(r),R(r,b))
  =-2^56 b^24(b-1)^12(b+1)^12 G(b).               (2)
```

Every common solution has a shared `r` root of the two polynomials in the
left side, so `(2)` vanishes.  The factors `b`, `b-1`, and `b+1` are target
and product guards.  Therefore `G(b)=0`, proving `(KB41D-1)`.

The parent cubic has degree three, `G` has degree twelve, and `P` has degree
at most two in `t`, giving the stated raw bound of 72 triples per sign row.
The count is only an upper bound; repeated roots, failed guards, and failure
of the original equations can reduce it.

For nonemptiness of the retained gate, the parent's `F_41` witness has
`b=10`, and direct evaluation gives

```text
b^6-2b^5+7b^4-8b^3+7b^2-2b+1=0 mod 41.
```

Thus the degree-12 condition keeps the known guarded common packet. QED.
