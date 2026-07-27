# Proof: averaged locator-to-slope conversion

For every nonnegative integer `x`,

```text
1_(x>0) >= x-x(x-1)/2.
```

Apply this pointwise to `x=X_z(A)` and sum over the `q` finite slopes:

```text
Y(A) >= N(A)-(1/2)sum_z X_z(A)(X_z(A)-1).
```

Take expectations. The exact theorem `averaged_xr` says that the ordered
second factorial moment is the same value `C_t(A)` for every fixed `z`.
Therefore

```text
E[Y(A)] >= E[N(A)]-(q/2)C_t(A).
```

If the right side is greater than `B-1`, then `E[Y(A)]>B-1`. Since `Y(A)` is
integer-valued, not every pair can have `Y(A)<=B-1`; hence one pair has
`Y(A)>=B`. No independence between different slopes is used.

The exact first moment may either be summed directly from the fixed-slope
probability in `averaged_xr` or supplied by `fm1`:

```text
E[N(A)]=|A|(1-q^(-t))q^(1-t).
```

Paid-family ownership and field transfer are payload hypotheses, not steps in
this conversion.
