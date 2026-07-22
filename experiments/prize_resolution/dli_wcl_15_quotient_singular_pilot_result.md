# WCL `(1,5)` native quotient Singular pilot

## Scope

This benchmark consumes the proved three-variable divisor endpoint directly:

```text
G(Y)=Y(Y^2+c1 Y+c0)^2-(bY+1)^2.
```

Over `F_32003`, it computes `Y^256 mod G` by eight native Singular
reductions in the block ring

```text
F_32003[Y,c0,c1,b],       ordering (lp(1),dp(3)).
```

It then extracts the five coefficients of `Y^256-1 mod G` and is designed to
compute a standard basis only in their three-variable ideal. This is exactly
equivalent to the direct remainder endpoint. A modular unit result would
still be route evidence rather than the required characteristic-zero integer
certificate.

## Run

The program hash is

```text
c6aa3dccca9d16934ddc1a7c5aa30a895c6189f6b513a867187dc7eff298f236.
```

Modal app `ap-CbRAXvnzzd9oUxuxtqRe3F` used one CPU, 2 GiB, one container, no
retries, and a 240-second algebra timeout. It returned

```json
{
  "algebra_timeout": 240,
  "app": "dli-wcl-15-quotient-singular-pilot",
  "method": "native_quotient_then_three_variable_std",
  "modulus": 32003,
  "program_sha256": "c6aa3dccca9d16934ddc1a7c5aa30a895c6189f6b513a867187dc7eff298f236",
  "seconds": 240.006409012,
  "status": "TIMEOUT",
  "stderr_tail": "",
  "stdout_tail": "WCL15_QSTEP\n1\n1\nWCL15_QSTEP\n2\n1\nWCL15_QSTEP\n3\n32\nWCL15_QSTEP\n4\n240\nWCL15_QSTEP\n5\n1881\nWCL15_QSTEP\n6\n14831\nWCL15_QSTEP\n7\n117644\n",
  "unit_ideal_mod_p": null
}
```

The printed term counts are the total terms in the degree-below-five
remainder after exponents `2,4,8,16,32,64,128`. Singular did not finish the
eighth squaring to exponent `256`; coefficient extraction and the
three-variable standard basis never started.

## Verdict

This localized the bottleneck more precisely than either 52-variable lift
run. Do not buy a longer Singular run. The successor FLINT computation in
`dli_wcl_15_flint_quotient_result.md` reproduced all seven counts, completed
the final sparse squaring in `3.7290703449980356` seconds, and emitted five
hash-pinned base-variable coefficient polynomials. The expansion task is
therefore retired. The next contributor endpoint is their three-variable
modular unit basis in an F4/F5-capable engine; the independent straight-line
presentation remains the conformance oracle.

This benchmark proves no WCL emptiness statement and changes no DAG status.
