# Exact rate-half Haboeck-Johnson safe bracket

- **status:** PROVED
- **closure:** theorem specialization and exact integer arithmetic
- **consumer:** `rate_half_band_crossing_location`

Fix the official maximal rate-half parameters

```text
n=2^41,   k=2^40,   B*=floor(q/2^128).
```

For every integer `m>=3`, define

```text
N_m=(2m+1)^14 n^7,
D=384^2 (k-1)^3,
Q_m=floor(sqrt(N_m/D)),                                (RHJ1)

a_m=min{a in Z: (2m a)^2 >= (2m+1)^2 n(k-1)}.         (RHJ2)
```

If `Q_m<=B*`, then the full support-wise MCA numerator is safe at `a_m`:

```text
B_mca(a_m)<=Q_m<=B*.                                   (RHJ3)
```

The printed theorem family has two exact, dual optimizer descriptions. For
an integer budget `B` for which the displayed set is nonempty, let

```text
m_B=max{m>=3: Q_m<=B}.
```

Then

```text
B_mca(a_(m_B))<=Q_(m_B)<=B,
a_(m_B)=min{a_m: m>=3 and Q_m<=B}.                     (RHJ7)
```

Conversely, for an integer support `s` for which the displayed set is
nonempty, let

```text
m_s=min{m>=3: a_m<=s}.
```

Then

```text
B_mca(s)<=Q_(m_s)=min{Q_m: m>=3 and a_m<=s}.           (RHJ8)
```

Thus `(RHJ7)` is the strongest safe agreement at a fixed budget, and
`(RHJ8)` is the smallest certified numerator at a fixed support, among all
members of the imported quadratic family.

The first member that strictly improves the existing `3n/4` safe endpoint
is `m=9`:

```text
Q_9=31838208335176550182206428283836,
a_9=1641330047987 < 3n/4=1649267441664.                (RHJ4)
```

Thus `(RHJ4)` applies whenever `q>=Q_9*2^128`, approximately
`log2(q)>=232.650530`.

Under the strict prize cap `q<2^256`, no `m>=96` is affordable. The strongest
possible theorem member is `m=95`:

```text
Q_95=330298791207625937408605578064099942258,
a_95=1563128173124,
n-a_95=635895082428.                                   (RHJ5)
```

The complete razor slice `q>2^255.9` receives at least the `m=94` bracket,
with

```text
Q_94=306835809425699384690368974701937497457,
a_94=1563215236073.                                    (RHJ6)
```

It upgrades to `(RHJ5)` exactly when `q>=Q_95*2^128`. Therefore the proved
crossing bracket becomes

```text
k+2^34 <= a_RH(q) <= a_94        below that threshold,
k+2^34 <= a_RH(q) <= a_95        at or above it,        (RHJ9)
```

throughout the razor slice.

## Scope

This is a safe-side bracket only. It neither identifies the exact crossing
nor proves that `a_m-1` is unsafe. It uses the proved quadratic Haboeck bound,
not the unproved BCHKS25 linear refinement. The two optimizer formulas exhaust
the printed quadratic family; a value below `(RHJ8)` at an intermediate
support would require a genuinely support-sensitive strengthening of the
source theorem.
