# C2 official-shape `t=2` CRT falsifier: report

## Verdict

The preregistered square-root falsifier did not fire at the first exact
`n/t=256` analogue:

```text
(n,t,q) = (512,2,7681),
J_prim < 1 < sqrt(2n)=32,
log2 J_prim = -9.5700325316325287361066757089202379707183e-74.
```

Thus the candidate has slightly more than five bits of slack on this row.
The near-zero logarithm is real, not floating cancellation: the analyzer
reconstructs the numerator and denominator exactly and checks that the
numerator is strictly smaller.

## Exact counts

```text
Z_0 = 227259606172895223931871329798529915863745504182648446230418158474213352436773778191377030361659036987692327140796443375499119317625629124310720768
C_1 = 15075132044957192478006898191470890229562554962327895331266773111833021696
Z_1 = 1745581035014008215020703684182508283749429217626922715495841875240432760066859390287966970207903063102464764768452812247622422348576523251005605760256
B_0 = 1745581035014008215020703684182508283749429217626922715495841875240432760066859390287966970207903063102464764768452812244988137327424369450113941136384
```

`Z_0-C_1` is positive and divisible by `512`, independently checking
primitive rotation-orbit ownership.

## Method and controls

Additive Fourier inversion computes each census modulo ten deterministic
60-bit primes. Quotienting dual pairs by
`(a,b)->(a*zeta,b*zeta^2)` leaves exactly `115246` character orbits per
target shard. Nine moduli already give a 541-bit CRT product, enough to
reconstruct every count below `2^512`; the tenth modulus is an independent
residue check.

The same executable reproduces the frozen `(32,2,97)` and `(32,2,5857)`
controls exactly. All 12 tasks returned in at most `6.989` seconds.

## Interpretation

This is the first exact row at the official aspect ratio, but it remains a
depth-one analogue. It gives no `t=2 -> t=2^33` transport and does not prove
the square-root candidate. The almost exact unit ratio suggests that more
`t=2` scale scans have low decision value; the live task is still an
analytic support-overlap-times-tail estimate at full depth.

## Replay

```text
tools/ramguard modal -- modal run notes/pilots_20260818/c2_official_shape_t2_crt/modal_run.py --output notes/pilots_20260818/c2_official_shape_t2_crt/results.json
tools/ramguard tiny -- python3 notes/pilots_20260818/c2_official_shape_t2_crt/analyze.py
tools/ramguard tiny -- python3 notes/pilots_20260818/c2_official_shape_t2_crt/analyze.py --tamper-selftest
```

Modal run: `ap-ofdfyMZFhdeIDNYzJZwyX8`. Frozen SHA-256 values:

```text
preregistration  2899039da6808dad323711326bb211801564f271de254ad0af96400ad67e7553
executed C++     0a19955b13f96c2a16d60c7f2e1d2eafd4b652d576ec301c7ccfe56dc2af4051
launcher         8f6b59137a838e353c3ce888b0779e7a58c3636bb8309b790cf76758dbd9ffcc
results          6fb1c4f8e8b660a2a97a8536d0b19939ad12a5167df706c03f1d8456d2674679
```

