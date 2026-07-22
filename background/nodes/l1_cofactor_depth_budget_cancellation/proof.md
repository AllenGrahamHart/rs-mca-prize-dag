# Proof - L1 cofactor-depth budget cancellation

## 1. Cofactor union

For `0<=e<k`, fixed-cofactor transport gives depth `d=w+e` and places every
exact-shell locator belonging to one fixed cofactor in one depth-`d` locator
fiber.  The leading coefficient of the degree-`e` cofactor is fixed and its
remaining `e` coefficients are arbitrary, so there are exactly `q^e`
possible cofactors.  Exactness can only delete locators.  Taking the maximum
full-divisor fiber and summing proves `(CD1)`.

## 2. Ambient and image normalization

Substituting `(CD2)` into `(CD1)` gives

```text
q^e K_amb binom(n,a)/q^(w+e)
  = K_amb binom(n,a)/q^w,
```

which is `(CD3)`.

Likewise, substituting `(CD4)` into `(CD1)` and multiplying and dividing by
`q^d` gives

```text
q^e K_img binom(n,a)/L_(a,d)
  = K_img (q^d/L_(a,d)) binom(n,a)/q^w.
```

This is `(CD5)`.  In particular, a full-image certificate
`L_(a,d)>=q^d/K_fill` changes the right side to at most
`K_img K_fill binom(n,a)/q^w`.  Without that certificate, the attained-image
normalization retains the collapse factor exactly.

## 3. Integer rounding

Put `x=binom(n,a)/q^w`.  Since `d=w+e`,

```text
q^e ceil(binomial(n,a)/q^d)
  = q^e ceil(x/q^e)
  < x+q^e.
```

Multiplication by `K` proves `(CD6)`.  This also shows why an ambient real-
mean cancellation can cease to be useful as soon as the deeper mean is below
one: every nonempty fiber still costs one integer object.

## 4. Finite-row diagnosis

Grande Finale v3 gives

```text
q_KB  = 2^31-2^24+1,     B*_KB  = 274980728111395087,
q_M31 = 2^31-1,           B*_M31 = 16777215,
```

and the four printed ceilings in the statement.  If `M=ceil(x)`, then
`x<=M` and `x>M-1`.  For both KoalaBear rows, `M-1>q_KB` but
`M<q_KB^2`, proving that the first subunit deeper mean is at `e=2`.  For both
Mersenne-31 rows, `M<q_M31`, so it is at `e=1`.

Direct integer comparison gives `q_KB<B*_KB<q_KB^2` and
`B*_M31<q_M31`, proving the route-fence column.  These comparisons concern
the sufficiency of the raw `q^e` union estimate only; they assert neither
that all cofactor targets are occupied nor that a large exact shell exists.
