# `A=1` quadratic paired split-biform factor-degree trichotomy

- **status:** PROVED
- **closure:** content-free factorization and exact one-unit degree profiles
- **consumer:** `rate_half_band_crossing_location`

Retain the extremal paired split biform and the notation

```text
M=e-2,       N=p-3,       R=3p-3+d_A,
T=3e,       2p=3e-1,       d_A in {0,1}.           (FDT1)
```

Write its primitive factorization over `F(X)` as

```text
G(t,X)=c(X) product_(j=1)^s Q_j(t,X),
m_j=deg_t Q_j>0,       n_j=deg_X Q_j.              (FDT2)
```

Then the content is constant:

```text
c(X) in F^x,       sum_j m_j=M,       sum_j n_j=N. (FDT3)
```

Put `q=9-2d_A`, so `q` is `9` or `7`. Classify the factors by
their parameter degrees as follows:

```text
small odd:     m_j odd,       q m_j<3e;
large odd:     m_j odd,       q m_j>=3e;
ordinary even: m_j even,      q m_j<6e;
huge even:     m_j even,      q m_j>=6e.           (FDT4)
```

Every factor lies exactly on the incidence lower envelope:

```text
n_j=ceil(Rm_j/T).                                  (FDT5)
```

Moreover, exactly one of the following three profiles occurs:

```text
I.   one large odd, no small odd, no huge even;
II.  two large odd, one small odd, no huge even;
III. one huge even, one small odd, no large odd.   (FDT6)
```

Each profile may also contain any number of ordinary-even factors. In
particular, all odd and huge-even factors are accounted for by `(FDT6)`;
there is no unused `X`-degree slack.

For `d_A=0`, a large odd factor has `m_j>=e/3`, while a huge even factor
has `m_j>=2e/3`. For `d_A=1`, the corresponding thresholds are
`m_j>=3e/7` and `m_j>=6e/7`.

## Scope

The trichotomy does not exclude any of its three profiles and does not
prove that `G` is irreducible. It classifies only the factor bidegrees;
the factors retain the two-directional splitting proved by the preceding
macroscopic-factor theorem.
