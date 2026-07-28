# Audit

Date: 2026-07-27.

## External theorem pin

The load-bearing external input is the local reciprocity law and its explicit
cyclotomic specialization:

- Kiran S. Kedlaya, *Notes on class field theory*, Theorem 4.1.2 and
  Example 4.1.4,
  https://kskedlaya.org/cft/sec_localrecip.html .

The theorem identifies the norm group with the reciprocity kernel; the
example states that on `Q_p` units the cyclotomic component is
`a -> a^-1`. At conductor 256 its kernel is exactly
`1+256 Z_2`.

## Falsification replay

Modal run `ap-1mAvRBXG3IhB77PeHwGRiO` computed 513 exact FLINT
resultants across both profiles, including the full-conductor variance-36
witness. Every odd norm part was one modulo 256; no counterexample was found.
The run completed in 0.177 seconds of container work. It is not load-bearing.

The local verifier checks all cofactor ranges and mutation-controls the
congruence filter. No broad support or norm census is claimed.

The prize-specific refinement is exact integer arithmetic:
`floor(18^64/(B_P 2^128))=2013`. Intersecting this with the existing local
valuation classes leaves eight cofactors. It does not alter the RowC atlas.

The independent integer sieve factors each odd cofactor and checks every
prime exponent modulo `ord_256(r)`. It removes only 1026; 257 and 769 are
prime and split completely.

Follow-up run `ap-LBruvVXqSS0uA8jYvFIgZV` computed the exact odd
part of the full-conductor variance-36 witness:

```text
356858204980334759596299368487390019197885759833937347520976391876156177921.
```

FLINT certifies that this 248-bit integer is prime. It is below `2^250`
and therefore harmless, but it falsifies the proposed shortcut "every signed
template has composite odd norm part." The remaining route is a sharp norm
size bound, not universal factorization.

Run `ap-5UMA1KDXGUrjeQ0nEKyugT` additionally replayed exact central
moments `(M_2,...,M_6)=(36,24,2398,2720,196728)`. Its sampled
conjugate-square range was approximately `[5.378,26.862]`. These values
are route diagnostics only.
