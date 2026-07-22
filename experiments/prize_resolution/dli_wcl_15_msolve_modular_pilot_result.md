# WCL `(1,5)` msolve modular pilot

## Decision

The fixed three-variable quotient endpoint was tested with a compiled F4
engine under the roadmap's five-minute self-authorization rule. The input was

```text
five equations in c0,c1,b over F_32003,
20,721,921 bytes,
sha256 c7b87cdf08b13210480aa6d6cad4a0774247328954c81757226277bca54f46cf.
```

The launcher regenerated `Y^256 mod G` with FLINT, reproduced all five pinned
content hashes and term counts, subtracted one from the constant remainder,
and only then invoked `msolve`. The engine accepted all five equations with
no invalid input. The launcher SHA-256 is
`549a835805d2c53420ae5ed52f49c6c70e9f8675d199a924e789654ba49b66d8`.

## Runs

The authoritative current-engine run was Modal app
`ap-i3qnWQSZ45Vr9x0QI1FHLk`:

```text
msolve              0.10.1
resources           8 physical cores, 32 GiB, one container
preparation         10.428 s
F4 cap              210 s
outcome             TIMEOUT, return code -15
output basis        none
unit_mod_32003      unknown
```

Its last complete retained trace row was

```text
178 20 515 1804 x 543871 20.17% 13 new 7 zero 15.38 | 15.25
```

The comparison app `ap-k2FBfUKS9IZb5wekKPXZfg` used `msolve 0.7.5` for
240 seconds on the same input. It also timed out without a basis, after a
similar sustained trace reaching the next `179` block. Neither run failed
from invalid syntax, immediate memory exhaustion, or a malformed polynomial.

All Modal apps are stopped. At the standard CPU and memory rates current at
the time of execution, the completed and diagnostic attempts together are
estimated below `$0.20`; this is an estimate rather than an account invoice.

## Verdict

This is useful implementation evidence but no mathematical result. It shows
that compiled F4 consumes the exact expanded endpoint and makes sustained
progress, while failing the pre-registered five-minute unit-result gate on
both the packaged and current msolve versions. No local extension, integer
reconstruction, or larger WCL slot is authorized.

The next external contributor should reuse the exact input hash and try a
different elimination implementation or ordering, preferably Magma/FGb or a
checkpointable msolve workflow. A complete handoff must return either a
modular unit basis with an independently replayable identity, or a compatible
modular point. A timeout remains `INCOMPLETE`.
