# Unsafe spending-cell fiber-layout counterexample

- **status:** PROVED
- **role:** exact scope counterexample for the retired W3 consumer route

There is an admissible clean-rate planted-sunflower spending cell for which
the all-cell extension of the W3 inequality is false. Take

```text
q = 1705*2^120+1
  = 2266333732813281563300991037777987502081,
n = 8192,       k = 2048,       rho = 1/4,
B* = floor(q/2^128) = 6.
```

The field order `q` is prime by the Proth certificate

```text
3^((q-1)/2) = -1 mod q.
```

At `B*=6`, the first quotient-core count exceeding the budget is

```text
binom(7,2)=21>6,       binom(3,1)=3<=6.
```

Thus the spending cell has quotient order `N*=8`, petal size
`ell=n/N*=1024`, slack `sigma=ell-1=1023`, six petals, and one background
point.  There are six distinct printed plants.

Choose an order-`n` subgroup `H` of `F_q^*`, put `d=256`, and use distinct
fibers of `x -> x^d` to define the missed-core fiber `D`, a zero fiber, and
the six petal agreement fibers.  The proof constructs a degree-`k-1`
polynomial

```text
g(X)=L_(C\D)(X)(X^d-z_0)
```

which is not planted and has at least `3328` agreements with the planted
receiver, above the required `k+sigma=3071`.  Hence

```text
|List(U)| >= 6+1 = 7 > B*=6.
```

This is a prize-scope counterexample to applying the W3 upper inequality at
the unsafe spending cell. It is not a small-field window or a
large-background artifact. It does not refute W3's literal safe-side
quantifier.
