# WCL `(1,5)` FLINT quotient endpoint

## Scope

`dli_wcl_15_flint_quotient_contributor.py` computes the five coefficients of

```text
Y^256 - 1 mod G,
G=Y(Y^2+c1 Y+c0)^2-(bY+1)^2,
```

over `F_32003`. It represents each coefficient as a python-flint
`nmod_mpoly` in `(c0,c1,b)`, squares the degree-below-five remainder, and
reduces descending powers by the monic divisor. It does not compute a
Groebner basis.

## Conformance

With python-flint `0.9.0` and FLINT `3.6.0`, the total term counts at
exponents `2,4,...,128` were

```text
1, 1, 32, 240, 1881, 14831, 117644.
```

This exactly matches the independent native Singular checkpoint. The final
exponent-256 squaring took `3.7290703449980356` seconds and produced

```text
coefficient terms: 183162, 191699, 189670, 186887, 185330
total terms:        936748
```

The five content hashes are

```text
735baaf4c765bff2da760560913dcbd11fcc51ea63c6a2bec7f44012d07f5c06
43ebc8299aae2b3341bfbd80d2b64a07e652e73b128f1ab7d116eac85710f737
c79d7ba146912df590481d1e3499e16103cb9b83edeec418c950f7c3c95caa9c
3e49b3a1355076a893c0283316fdea45feda7309b995307a0d32614d703ec856
0bd441cbfeeb88815458883143021c2ce8b6ed0b767951959e7af5974aeb7e03
```

A second run loaded the five exponent-128 gzip TSV checkpoints, performed
only the final squaring, and reproduced all five hashes. The compact JSON
record pins the exponent-128 hashes as well. Hashes cover uncompressed TSV
content, so gzip metadata is irrelevant.

## Reproduction

The guarded smoke test is

```text
tools/ramguard local -- VENV/bin/python \
  experiments/prize_resolution/dli_wcl_15_flint_quotient_contributor.py
```

For the full resumable endpoint, first use `--max-step 7 --emit-dir DIR`,
then use `--resume-stage7 DIR --max-step 8 --emit-dir OUT`. The emitted
coefficient dumps are disposable multi-megabyte artifacts and should not be
committed.

## Verdict

The quotient expansion is no longer a compute request. CR-004 now begins
with the five hash-pinned polynomials above: use an F4/F5-capable engine to
seek a modular unit basis, independently replay its identity, and proceed to
integer reconstruction only if that pilot succeeds under a declared resource
cap.

This computation proves no WCL emptiness statement and changes no DAG status.
