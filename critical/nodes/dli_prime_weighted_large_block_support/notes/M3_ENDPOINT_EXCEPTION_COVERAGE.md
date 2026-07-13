# M3: endpoint-exception coverage contract

- **status:** truth-apt route obligation posed; unproved
- **scope:** every official code row, not a density-one or deployer-selected set
- **nonclaim:** A1-PROD does not discharge this obligation

## Audit finding

The earlier route language suggested that the endpoint could consume “the
deployed `q` is not exceptional,” possibly in an engineering-hardness sense.
That is not a valid input to the prize theorem. The code, including its field,
is given; a proof cannot choose a typical prime or discard a sparse set of
admissible fields.

`A1_PROD_NORM_SIEVE.md` proves an unconditional count and density bound on
exceptional primes in a dyadic band. It does not identify each exceptional
prime and does not prove that the official row is outside the exceptional
set. The source also explicitly states that absence of low-weight vanishers
cannot be certified by exhaustive search at production scale. A list of
exhibited generators therefore proves neither completeness nor a residual
upper bound.

## Certificate soundness

For an official row `R`, an endpoint-exception certificate `pi_R` must contain:

1. the exact row key, field presentation, generated-field normalization, and
   primality/order certificates;
2. for every production level, a complete low-weight orbit ledger with a
   checkable completeness proof, not only exhibited representatives;
3. exact multiplier-shadow and lift de-duplication bounds;
4. an independently checkable residual near-peak upper certificate for every
   unlisted weight/frequency class;
5. the C2'' coset/bulk/accident ownership ledger, with the aggregate reserve
   charged once;
6. an exact rational final check against the binding endpoint `2^121`.

The soundness statement is

```text
VERIFY_ENDPOINT_EXC(R,pi_R)=ACCEPT  ==>  q^{-t+H} W_cen(R) <= 2^121.
```

An implementation may have several certificate types, but each type must
prove completeness of the mass it prices. “No explicit construction is
known,” “the row is likely nonexceptional,” and PPT/engineering hardness are
rejected certificate types.

Item 5 is not consistency-only: the ownership ledger's joint bridge must
resolve to the manifest's named C2''-instance, so assumption-only item-5
content is a REJECT (catch #163), and any reserve credit must be covered
exactly by the mass of buckets owned coset/accident (catch #165).

## Coverage obligation

The truth-apt route statement is

```text
for every official row R, there exists pi_R such that
VERIFY_ENDPOINT_EXC(R,pi_R)=ACCEPT.                         (ENDPOINT-EXC-COVERAGE)
```

Soundness without coverage is only a conditional checker. Density control
without individual coverage is only an average-over-fields theorem. Both are
insufficient for the full prize result.

## Current status

No repository asset proves `ENDPOINT-EXC-COVERAGE`. The strongest available
per-row artifacts certify exhibited generators and selected low-weight
windows, while their own source notes deny a complete production-scale absence
certificate. M3 is therefore posed but open.

This blocks M4 from being presented as an unconditional DLI assembly. M4 may
still prove the exact arithmetic implication from accepted C1', C2'', and
endpoint certificates, but it must expose coverage as an input and must fail
closed when that input is absent.

---

## M3 CORRECTED POSE (2026-07-13, appended per #104; the contract above
## remains the banked M4 interface — w6-C4 = catch #181, credit Codex)

### Interface correction

The pose above requires an accepted certificate to finish with
`q^(-t+H) W_cen(R)<=2^121` (item 6). Universal coverage by such
certificates is equivalent to B-WEAK itself and therefore CIRCULAR as a
decomposition target. The exact C1' theorem exposes a smaller interface:
once its finite primitive ledger is supplied, C1' controls the whole
level mean; no separate residual near-peak certificate is needed. The
100-bit baseline is an amber assembly, not an independent red predicate.

### Coverage obligation (the truth-apt successor)

For an official row `R` and level `L=1,...,34`, let

```text
W_cl(R,L) = sum_O 2 N_L 2^(-w(O)),
N_L       = 256L,
```

where the sum is over the complete set of reduced primitive signed-shift
orbits in the C1' window `L+1<=w(O)<=L+5`, after generated-field
normalization and first-owner de-duplication of multiplier shadows and
level lifts. The truth-apt M3 statement is

```text
for every official row R and every L=1,...,34,
W_cl(R,L) <= 1/32.                              (WCL-ZONE-COVERAGE)
```

This is the DAG node `dli_wcl_zone_coverage` (zero F-rounds; the
F-round rule applies before any promotion). A proof or certificate
family must pin the row and generated field, prove the primitive ledger
complete in the exact weight window, and prove ownership. A density
bound over primes, an engineering-hardness claim, or a list of merely
exhibited relations is not per-row coverage.

### Exact downstream assembly

Together with C1', WCL-ZONE gives

```text
r_L = q^L/2^(256L) < 1,
E_L <= 1 + 4r_L(1+W_cl) <= 41/8,
product_(L=1)^34 E_L <= (41/8)^34 < 2^100.
```

The final comparison is exactly `41^34<2^202`. This proves the amber
node `dli_marginal_baseline100_coverage`; C2'' then supplies the
independent 21-bit joint reserve. The corrected M3 contains no C1'
assertion, C2'' assertion, final endpoint check, residual certificate,
or reserve credit. No repository asset proves WCL-ZONE-COVERAGE on
every official level; A1-PROD proves only a density bound.

### CORRIGENDUM to the corrected pose (2026-07-13, wave-7 w7-C1/w7-C2,
### maintainer-ratified decision 4; per #155 the text above is
### annotated, not rewritten)

Two displays in the "M3 CORRECTED POSE" section above are superseded:

1. **Schedule (w7-C1, catch #205):** `N_L = 256L, L = 1,...,34`
   conflated level index with level dimension. The production tower of
   record is `t = 2^33`, `j = 0..33`,
   `ell_j = ceil(floor(t/2^j)/2)`, `N_j = 256*ell_j`, dims
   `(2^32,...,2,1,1)` summing to `t` (the banked skew-tower packet, S6,
   and C2''s `Sigma_j L_j = t` pin this; the linear reading sums to 595
   and contradicts it). The window and assembly formulas hold verbatim
   with `(R,j)` in place of `(R,L)` and `r_j = q^{ell_j}/2^{256 ell_j}`.
2. **Ledger (w7-C2, catch #206; maintainer ruling 4a):** the phrase
   "first-owner de-duplication of multiplier shadows and level lifts"
   is STRUCK — `W_cl` is the RAW primitive signed-shift ledger (no
   deletion; shadows/lifts classify but their primitive mass is priced
   at its own level and weight), matching the C1' pose of record and
   `dli_wcl_raw_ledger_interface_guardrail`. The wz2 dedup module
   remains an analogue-census bookkeeping device (ruling 4b).

Post-wave-7 state: WCL-ZONE is equivalent to six emptiness slots
(ell,w) = (1,5),(1,6),(2,5),(2,6),(2,7),(4,9) — see the wcl node's
official_terminal_attack.md.
