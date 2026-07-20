# Audit

1. The square-class transversal has two elements because
   `gcd(h,m)=2`. Treating the normalization as unique would undercount.
2. The two normalized representatives arising from the kernel `{1,-1}` may
   duplicate one orbit. Counting all candidate triples is still a valid upper
   bound; no division by two is used.
3. Both endpoint equations are necessary. The orbit bound uses only the
   nonzero degree of `f_(h+1)`; the `f_h` equation and all root checks can
   only remove candidates.
4. The coefficient of `a^(h+1)` is nonzero because every factor `3r+1` and
   `(h+1)!` is nonzero in the stated characteristic.
5. The scope `h>2` excludes the exact `m=8,h=2` fixture, where the earlier
   top-coefficient derivation receives low-degree constant-shift terms.
6. This is one width per exact level. It supplies no estimate for defects
   `e>=4` and does not close the HGE4 aggregate.
7. The upper bound is an analytic debit against the level allowance. A
   retained-width certificate must subtract it; treating the boundary as a
   zero contribution would double-spend `(ERT4')`.
