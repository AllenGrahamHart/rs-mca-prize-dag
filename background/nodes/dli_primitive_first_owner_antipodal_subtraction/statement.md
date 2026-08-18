# Dyadic primitive first-owner subtraction

- **status:** PROVED

Let `n=2^s`, let `q` be odd with `n | q-1`, and let `T(n,t,b)` be the
number of `b`-subsets of the order-`n` evaluation subgroup whose first `t`
power sums vanish. Let `T_prim(n,t,b)` count only subsets with trivial
rotation stabilizer. Then

```text
T_prim(n,t,b) = T(n,t,b)                                      if b is odd,
T_prim(n,t,b) = T(n,t,b) - T(n/2,floor(t/2),b/2)              if b is even.
```

Consequently first-owner removal from any fixed-weight interval is one exact
subtraction, with no inclusion-exclusion remainder. For even `t`, the
full-cube normalized joint masses satisfy

```text
X_prim(n,t)
  = X(n,t) - (q^(t/2)/2^(n/2)) X(n/2,t/2).
```

At the official DLI row this is the exact primitive deletion that must be
inserted before applying the `C2''` joint reserve.
