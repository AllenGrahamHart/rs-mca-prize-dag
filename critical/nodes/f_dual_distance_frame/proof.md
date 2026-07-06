# f_dual_distance_frame proof

Let `P` be a flat of locators and let `ev_x : P -> F` be evaluation at the
domain point `x`. A subset `S` of domain points has dependent traces exactly
when the linear functionals `{ev_x : x in S}` are linearly dependent.

That dependence is a tuple of coefficients `(a_x)_{x in S}`, not all zero,
such that

```text
sum_{x in S} a_x ev_x = 0
```

as a functional on `P`. Equivalently, the vector supported on `S` with
coordinates `a_x` lies in the dual of the evaluation code of `P`, denoted
`P-perp`.

The low-weight cases are immediate:

- weight `1` means one trace is the zero functional, so every locator in `P`
  vanishes at that point, i.e. a common root/gcd branch;
- weight `2` means two traces are proportional, the twin case;
- general weight `w` is the general sparse-dual obstruction.

If the support is minimal, no coefficient on that support can be zero, since
otherwise a smaller support would carry the same dependence. Hence if a
locator vanishes on all but one point of a minimal support, the dependence
forces it to vanish on the last point as well. This is the stated closure
property.

Finally, if the dual distance of `P-perp` is greater than `r`, then no
dependent trace set of size at most `r` exists. Therefore every `r`-subset of
traces is in general position.
