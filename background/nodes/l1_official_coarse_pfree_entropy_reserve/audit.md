# Audit - L1 official coarse p-free entropy reserve

1. The average is over all ambient p-free target vectors, including empty
   fibers; it is not normalized by the attained image.
2. The off-by-one `d_0=ell_0-1` is load-bearing: it gives 3,175 rather than
   3,174 layers before the first checkpoint.
3. The factor 15 comes from the smallest official rate `1/16`; no smaller
   rate is covered.
4. The 23-checkpoint cap and `q>n>=2^13` are both load-bearing in 28,276.
5. The theorem shows that coarse p-free flatness is not average-obstructed.
   It does not establish flatness or convert an image-normalized theorem.
6. The sharper per-condition calculation uses `f>=2`, the full canonical
   estimate for `d_0`, and all p-free conditions. It applies to a nonnegative
   integer extras residual after exact structured subtraction, not the full
   nonempty coarse fiber. Fifteen bits force extras emptiness; sixteen bits
   are not certified by the same coarse inequalities.
7. F2's printed `2^15` endpoint is numerically compatible but has the wrong
   target, map, structured subtraction, and owner for direct L1 consumption.
8. Positive-cofactor Pade graphs still require collective target control.
9. No computation or probabilistic evidence is load-bearing.
