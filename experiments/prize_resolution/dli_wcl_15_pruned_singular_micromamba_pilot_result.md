# WCL `(1,5)` minimal-image Singular pilot

## Scope

This is a route benchmark for the exact pruned straight-line presentation of
`dli_wcl_fixed_divisor_straight_line_lift`. It is not a WCL certificate and
changes no DAG status.

The Singular input has

```text
52 variables, 54 equations, maximum degree 3,
coefficient field F_32003,
degree-reverse-lexicographic order dp,
program sha256 201a1f596180e5383cc4364f970fcac445e0175ff1db64fe1d81ba9cad2db8e3.
```

The program hash is byte-identical to the cancelled Debian-image pilot. Thus
the image change does not change the mathematical system.

## Runs

The minimal Micromamba image installed the standalone conda-forge packages
`singular`, `libflint`, `ntl`, `gmp`, and their small dependencies. The
transaction downloaded 56 MB, the image built in 15.67 seconds, and Singular
started successfully.

The first function call, Modal app `ap-tqtBA7gmS9XY2n25STKrQK`, reached the
48-second algebra timeout. Its timeout reporter then failed because Python's
`TimeoutExpired` supplied byte strings despite text mode. The launcher now
decodes either byte or text tails before JSON serialization.

The corrected call, Modal app `ap-OkljVyyM1fPvNO3JEmhAnA`, used one CPU,
2 GiB, one container, no retries, and a 240-second algebra timeout. It
returned

```json
{
  "algebra_timeout": 240,
  "app": "dli-wcl-15-pruned-singular-micromamba-pilot",
  "equations": 54,
  "modulus": 32003,
  "program_sha256": "201a1f596180e5383cc4364f970fcac445e0175ff1db64fe1d81ba9cad2db8e3",
  "seconds": 240.00962194299998,
  "status": "TIMEOUT",
  "stderr_tail": "",
  "stdout_tail": "WCL15_STD_BEGIN\n",
  "unit_ideal_mod_p": null,
  "variables": 52
}
```

Commit `fac244f0` preserves that global-`dp` launcher. The follow-on source
replaced `std(I)` by Singular's exact
`eliminate(I, product_of_49_auxiliaries)`, retaining only the base variables
`(c0,c1,b)`. This is the precise three-variable intersection required by the
certificate endpoint, not a heuristic projection. Its program hash is
`5e0f18285a9e607c93721aade5540f659fb1cbf82f11e4b1ff208dce1eba5a81`.

Modal app `ap-wcQeDzPB9eNSB5q2VdaTMe` ran the elimination with the same one
CPU, 2 GiB, one-container, no-retry, 240-second envelope and returned

```json
{
  "algebra_timeout": 240,
  "app": "dli-wcl-15-pruned-singular-micromamba-pilot",
  "equations": 54,
  "method": "eliminate_49_auxiliaries",
  "modulus": 32003,
  "program_sha256": "5e0f18285a9e607c93721aade5540f659fb1cbf82f11e4b1ff208dce1eba5a81",
  "seconds": 240.008896514,
  "status": "TIMEOUT",
  "stderr_tail": "",
  "stdout_tail": "WCL15_ELIM_BEGIN\n",
  "unit_ideal_mod_p": null,
  "variables": 52
}
```

## Verdict

The former image-initialization blocker is resolved. Neither plain `std(I)`
with one global `dp` block nor Singular's exact 49-variable elimination meets
the roadmap's sub-five-minute self-auth rule, even at one modular prime.
Buying more time on either route is not the next action.

A contributor pilot should instead use an F4/F5-capable CAS, Magma/FGb, or a
custom stagewise quotient algorithm on the equivalent three-variable
remainder ideal while preserving quotient arithmetic. It should first
demonstrate a unit result at one nonexceptional prime inside five minutes,
then emit a checked characteristic-zero integer identity. A modular unit
basis alone does not close the slot.
