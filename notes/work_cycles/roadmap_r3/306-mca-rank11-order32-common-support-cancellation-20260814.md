# Cycle 306: MCA rank-11 order-32 common-support cancellation (2026-08-14)

Cycle 305 emits `32` actual low-margin records whose exact support
intersection `C` has size

```text
c<K-4922.
```

The new proved node
`rate_half_mca_rank11_order32_common_support_cancellation` removes that
intersection without changing record semantics. Since `c<K`, interpolate the
two received columns on `C` by degree-below-`K` polynomials `A,B`. For every
record, the common-support locator `L_C` divides

```text
h_i-A-gamma_i B.
```

On `D\C`, divide the received differences pointwise by `L_C` and divide the
explanation polynomial exactly. This produces records in

```text
RS[F,D\C,K-c]
```

at agreement `m-c`. A residual simultaneous pair explanation would lift to
one on the complete original support, so support-wise MCA-badness is
preserved. Taking `C` to be the complete support intersection makes the
residual intersection empty.

The two governing differences are invariant:

```text
(n-c)-(K-c)=1048576,
(m-c)-(K-c)=67472.
```

Hence the critical order remains exactly

```text
floor(2*1048576/67472)+1=32,
```

and `K-c>=4923`.

The audit also identifies the exact nonuniformity that prevents a silent
application of Grande Finale v4. On the residual common-support-free row,
the slope-degree incidence floor is

```text
r_min(K')=ceil(32(K'+67472)/(K'+1048576)).
```

It is `3` at `K'=4923` and reaches the deployed value `18` only at
`K'>=1044446`, equivalently when the canceled support has size at most
`4130`. The punctured-domain classifier must therefore handle genuine
degree `3..17` residuals or exploit the inherited rank-eleven pair
structure. Reusing the deployed degree-18 statement would be invalid.

Focused verification:

```text
RATE_HALF_MCA_RANK11_ORDER32_COMMON_SUPPORT_CANCELLATION_PASS
  Kmin=4923 order=32 toy=6 controls=7/7
RATE_HALF_MCA_RANK11_ORDER32_COMMON_SUPPORT_CANCELLATION_AUDIT_PASS
  Kmin=4923 toy=6 controls=5/5
DAG_MANIFEST_PASS nodes=2444 edges=7260 bytes=5557874 mutations=3/3
RUN_ALL_VERIFIERS total=2 failures=0
```

No Modal computation was used.

```text
start:                   277f52660
DAG delta:               +1 PROVED cancellation node, +1 requirement edge,
                         +1 evidence edge
critical status delta:   none
upstream terminal delta: common-support semantics and critical order closed;
                         punctured-domain degree-3..17 classification exposed
delta-star movement:     none
compute:                 exact local arithmetic and GF(17) control only
next route action:       attack the inherited low-slope-degree residual using
                         the ten-dimensional pair-component span before
                         attempting a fully puncture-uniform v4 theorem
```
