# Integral heavy-owner split-pencil cap

- **status:** PROVED
- **scope:** clean dominant lines in the weighted split-pencil theorem

Use the hypotheses and notation of the common-core-offset split-pencil
theorem.  Put

```text
a=floor(P/2)+1,       b=P-1,
C0=C(P,2)+rP,         phi(s)=C0/(P-s)-s.
```

For light mass `ell` and `t` globally heavy owners, maximize

```text
ell * sum_(i=1)^t phi(s_i)                         (IH)
```

over integers `a<=s_i<=b` and `sum_i s_i<=S-ell`.  Since `phi` is
increasing and convex, its maximum has as many weights `b` as possible,
at most one intermediate weight, and every other weight `a`.  Let
`C_clean^int` be the floor of the finite maximum of `(IH)` over
`0<=ell<=S` and `1<=t<=floor((S-ell)/a)`.

Then the clean dominant-line charge is at most `C_clean^int`.  Therefore
the complete split-pencil capacity is at most

```text
C_clean^int
+ floor((floor(P^2/4)+rP) C(S,2)/floor(P^2/4))
+ C(h,2)(C(P-1,2)+rP),

h=floor(S/a).
```

For every `K'=22` core offset `9<=j<=21`, the exact maximum has eight
owners of weight `P-1`.  The largest complete chart cap is

```text
9269974099565290
```

at `j=21`.

## Falsifier

A clean-line family above `(IH)`; failure of the convex extreme-weight
reduction; a larger exact `K'=22` core-offset cap; or a missed integral
one-variable maximum.
