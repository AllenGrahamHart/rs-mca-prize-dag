# Heavy-ruling degree-24 partial-relative router

- **status:** PROVED
- **scope:** the actual order-32 packet emitted by the heavy Segre ruling
  branch on the official KoalaBear sextic row

Let `C` be the complete intersection of the 32 exact selected supports in
the degree-24 seed and put `c=|C|`. The seed proves `c<K-2`. Exact
cancellation leaves actual support-wise MCA-bad records in

```text
(n',K',m')=(n-c,K-c,m-c),       K'>=3,
```

with empty common selected support and slope-error degree in `24..31`.
For their residual exact supports `S_i'`, define

```text
chi'=sum_(x in D\C) min(2, |{i:x in S_i'}|).
```

Exactly one of these interfaces is available:

1. a pure-locator certificate;
2. a nontrivial scalar-locator rational certificate, with denominator
   roots retained and denominator degree at most `m-K=67472`; or
3. the residual two-cover bound

   ```text
   chi' >= 3(m-c)-(K-c)+3.
   ```

The first two certificates lift exactly to the original heavy-ruling
packet. They retain the same denominator, affine locator scalars, monic
support locators, first-owned slopes, and support labels. In the third
branch every coordinate of `C` contributes exactly two after lifting, so

```text
chi >= 3m-K+3 = 2299571.
```

## Nonclaim

No branch is paid here. In particular this node gives no whole-line owner,
spread or exception bound, local-core synchronization, adjacent safety, or
MCA closure.
