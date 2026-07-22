# L1 fixed-syndrome multiprefix source and route cut

- **status:** PROVED
- **closure:** proof plus independent exact replay
- **consumer:** `l1_mixed_petal_amplification` (evidence and route fence)
- **upstream:** `przchojecki/rs-mca` PR `#1041`, exact feature commit
  `752872ce98754a05f37540cd7780a89b86818222`

## Fixed multipartial source

Let `B` be a finite field, let `D subset B`, and suppose a monic degree-`c`
polynomial `phi` partitions `D` into complete `c`-point fibers indexed by
`Q`. Fix `h` partial-fiber labels, a set `P` of `r` points meeting each of
those fibers nontrivially but not completely, and integers `f,t` with

```text
0<K<=A<=|D|,  A=r+cf,       0<=t<=f,
r+c(f-t-1)<K                                      (MP1)
```

when `t<f`. Then one received word for `RS_B(D,K)` has at least

```text
ceil(binomial(|Q|-h,f)/|B|^t)                         (MP2)
```

distinct codewords at exact agreement `A`. Its complete radius-`|D|-A`
ball is boundary-only. When `t=f`, each full coefficient bucket is a
singleton and the same construction gives one exact-boundary codeword.

The source fixes the partial template `P`; it does not say that arbitrary
large frames share one template.

## Exact deployed specialization

Under upstream's printed Mersenne-31 complete-fold contract, the source
parameters are

```text
p=2^31-1,       |Q|=1024,       c=2048,
K=1048576,      h=3,             r=3959,
f=543,          t=32,            A=1116023,
```

the degree ceiling is `1048439=K-137` and `(MP2)` is exactly

```text
ceil(binomial(1021,543)/p^32)=1693898.                (MP3)
```

Thus a universal cap of 29 members in that `(u,v)=(1,1)` source profile is
false. Since the center and domain are base-field-valued, its complete ball
over the deployed extension field is still boundary-only and every
explaining codeword is base-field-valued. This is a source floor, not an
upper payment and not a prize-row closure.

## Multiprefix obstruction

There is an exact `F_17^*`, `(n,K,A)=(16,7,9)` received word with two
codewords whose agreement supports have the same fixed partial remainder
and whose error supports have the same fixed partial remainder, but whose
actual monic agreement-locator prefixes and error-locator prefixes are both
different. The replay prints

```text
agreement prefixes: (8,4), (8,8)
error prefixes:     (9,9), (9,5).                    (MP4)
```

A common codeword translation preserves every difference `Y-P`, hence every
pair `(L_S,H)` in

```text
Y-P=L_S H,       deg P<K,       H(x)!=0 on D\S.       (MP5)
```

It cannot identify the two actual locator prefixes in `(MP4)`. Consequently
an arbitrary-word face count has the form `sum_z N_Y(z)`. Bounding only
`max_z N_Y(z)` is insufficient unless a separate theorem coalesces or pays
the number of attained targets and preserves first-match ownership.

## Scope

This theorem validates the fixed-template source and refutes a literal
support-preserving common-prefix normalization. It does not rule out a
coarser target, a non-support-preserving adapter, or a collective attained-
image theorem. It proves no L1 upper bound, no carrier owner, no M31 row
closure, and no proximity-prize endpoint.
