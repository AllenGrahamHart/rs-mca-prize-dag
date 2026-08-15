# Proof

Use the stated zero convention on an empty circuit stratum.  Otherwise the
finite set of circuit deletions has an attaining deletion, and the universal
completion theorem gives `1<=M_c<=q`.  In either case `0<=M_c<=q`.  Hence
`s_c=q-M_c` is a unique integer in `0..q`; conversely every such defect
specifies the exact value `M_c=q-s_c`.  Taking the product for `c=4,5`
gives `(q+1)^2` disjoint exhaustive pairs.

The deletion count for source `c` is monotone under the completion ceiling,
so on exact defect `s_c` it may use

```text
floor(C(m,c-1) max_(0<=b<=q-s_c)
      b C(m-c+1-b,11-c) / c).                    (1)
```

When the cross-support carrier inequality is valid, its cap depends only on
the exact source defect and remains available.  Branch refinement always
intersects these caps with every parent cap, so no preceding resource is
lost.

If `s_4+s_5<q`, then both maxima are positive, so attaining independent
deletions exist.  Moreover `q>s_4+s_5`, exactly the hypothesis of the proved joint
support-four/support-five zero-carrier theorem.  Its external support-four
charge therefore applies.  If the inequality fails, no joint cap is used.

Finally let cap vectors `a,b` satisfy `a_c<=b_c` for every support and let
all weights be nonnegative.  For every further cap vector `u`,

```text
sum_c w_c min(a_c,u_c) <= sum_c w_c min(b_c,u_c).
```

Thus `a` can never maximize the premium while `b` is present.  Removing only
such dominated vectors preserves the exact maximum.  QED.
