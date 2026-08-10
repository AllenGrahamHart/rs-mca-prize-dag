# Proof

Set `rho=(k-1)/n`. The imported theorem gives, at integer parameter `m`,

```text
|E_m| <= ((m+1/2)^7 n^2)/(3 rho^(3/2)).                (1)
```

Squaring the positive right side and substituting `rho=(k-1)/n` gives

```text
((right side of (1)))^2
  = (2m+1)^14 n^7 / (384^2 (k-1)^3)
  = N_m/D.                                             (2)
```

Because `|E_m|` is an integer, `(1)--(2)` imply

```text
|E_m|<=floor(sqrt(N_m/D))=Q_m.                         (3)
```

The theorem's real agreement threshold is

```text
(1-gamma_m)n
  = (1+1/(2m))*sqrt((k-1)/n)*n
  = ((2m+1)/(2m))*sqrt(n(k-1)).                        (4)
```

An integer support meets `(4)` exactly when its size is at least the least
integer satisfying `(RHJ2)`, namely `a_m`. Equations `(3)--(4)` prove
`B_mca(a_m)<=Q_m`. If `Q_m<=B*=floor(q/2^128)`, this proves `(RHJ3)`.

The real quantity below the floor in `Q_m` is a positive constant times
`(2m+1)^7`. It is strictly increasing and unbounded in `m`, so `Q_m` is
nondecreasing and unbounded. The real threshold below the ceiling in `a_m`
is

```text
(1+1/(2m))*sqrt(n(k-1)),
```

which is decreasing in `m`; hence `a_m` is nonincreasing. It follows that
the largest affordable index `m_B` minimizes `a_m` over all affordable
members, proving `(RHJ7)`.

For fixed integer support `s`, support-wise MCA monotonicity gives

```text
B_mca(s)<=B_mca(a_m)<=Q_m whenever a_m<=s.             (5)
```

The least admissible index `m_s` minimizes the nondecreasing sequence `Q_m`
over this tail. Equation `(5)` therefore proves `(RHJ8)`. These are exact
optimizers within the printed theorem family; no support parameter remains
in the imported bound after the threshold condition is met.

The exact replay checks the floor and ceiling characterizations by their two
adjacent squared inequalities. It gives:

```text
a_8=1652128271987 > 3n/4,
a_9=1641330047987 < 3n/4,
```

so `m=9` is the first strict improvement. It also gives the exact values in
`(RHJ4)--(RHJ6)`, proves

```text
Q_95<=2^128-1<Q_96,
```

and verifies that `Q_m` is nondecreasing through the cap boundary. Hence
`m=95` is the largest member that can be affordable anywhere in the official
range `q<2^256`, and no official row can afford `m>=96`.

Finally, exact integer exponentiation proves

```text
(Q_94*2^128)^10 < 2^2559,
```

which is the assertion `Q_94*2^128<2^255.9`. Thus every row in the named
razor slice can use `m=94`; `m=95` applies precisely after its printed exact
threshold. Since a safe agreement is an upper bound on the first safe
agreement `a_RH(q)`, `(RHJ9)` follows. QED.
