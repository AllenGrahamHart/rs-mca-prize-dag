# Proof certificate

## 1. Finite completeness router

Write a reduced signed weight-five polynomial as

```text
P(X) = sum_{i=1}^5 s_i X^{e_i},
s_i in {+1,-1}, 0 <= e_i < 256,
```

where the `e_i` are distinct.  Encode `-X^e` by the full exponent `e+256`
in `Z/512`.  A reduced polynomial is therefore a five-set of order-512
roots with no antipodal pair, modulo translation by 256 (global sign).
Translation and odd dilation act by

```text
S -> aS+b,  a odd mod 512.
```

They preserve reducedness, exact-order evaluation, vanishing, and the
absolute cyclotomic norm.

The proved node `dli_wcl_weight4_ambient_exclusion` supplies a complete
normalized section of the reduced weight-four affine orbits.  Given any
reduced five-set, delete one term and move the resulting four-set to that
section.  Its fifth term is not equal or antipodal to a retained term, so it
appears among the generator's complete legal-extension loop.  The generator
then canonicalizes under every translation and odd dilation.  Thus every
reduced weight-five orbit is represented.  Exact de-duplication gives

```text
2,296,920 affine-Galois classes,
representative SHA-256
9ac0ca650e704a13514180fe2d8bcea94943c771f125b3942888a6aba8c87f00.
```

This extension argument proves surjectivity; canonical keys make distinct
output rows disjoint.  It does not infer completeness merely from the
observed class count.

## 2. Norm obstruction

For a representative polynomial define

```text
N(P) = |Res(X^256+1, P(X))|.
```

This integer is nonzero.  Indeed, a zero would be a characteristic-zero sum
of five `512`th roots.  Splitting a vanishing sum into its even and odd
exponents recursively shows that every zero sum of `2^m`th roots with
coefficients `+1` partitions into antipodal pairs.  An odd five-set cannot
partition in this way, and reducedness excludes an antipodal sub-pair.

Now let `q` be official, so `q<2^256` and `2^41 | q-1`.  In particular an
order-512 root `zeta` lies in `F_q`.  If `P(zeta)=0`, then one linear factor
of `X^256+1` over `F_q` is shared with `P`, hence

```text
q | Res(X^256+1,P) = +/- N(P).                       (1)
```

Moving `P` to its affine-Galois representative only multiplies its value by
a nonzero root and replaces `zeta` by an odd power, so (1) applies to one of
the finite representatives above.

## 3. Complete factor ledger

The primary run evaluates every representative with the recursive exact
resultant identity obtained by repeatedly writing

```text
f(X)=f_0(X^2)+X f_1(X^2)
```

and pairing `alpha,-alpha`.  It produces `35,890` contiguous 64-row batches.
Exactly `2,296,726` rows factor within the easy stage and `194` distinct rows
enter the hard-tail manifest.

The independent replay does not reuse the recursive norm algorithm.  It
computes direct FLINT resultants, proves every easy factor prime with
`fmpz_is_prime`, trial-divides each exact norm by its stored factors, and
reconstructs the primary candidate and factor digests.  FLINT documents
`fmpz_is_prime` as a proof attempt with APRCL fallback, rather than a probable
prime predicate.  The replay covers all `35,890` batches and `2,296,920`
rows, performs `6,177,403` primality checks, reconstructs `6,528,119` factor
records, and leaves exactly the declared `194` tails.  It has no missing or
duplicate batch.  Its custody digest is

```text
975220600606e8f9fac4de09d7d350121ea04ea3de23b9e492fb0651b331e033.
```

An independent content-pinned tail checker certifies `193` of those rows:
400 factor occurrences, 399 distinct proved primes, exact products, maximum
`v_2(p-1)=17`, and no official-gate factor.  The sole residual norm was tail
191,

```text
648504938724625892617537595827566622528651020454874372151735040370465231483079169.
```

A pinned official CADO-NFS image factors it as

```text
2618025003265620701077592958097921
*
247707694890502006805474333259382717013127180289.
```

A separate FLINT certificate proves both factors prime, multiplies them back
to the exact norm, and computes bit lengths `112,158` and depths `9,12`.

Across the easy ledger, the 193-tail packet, and tail 191, the maximum depth
is therefore

```text
max_p v_2(p-1) = max(30,17,12) = 30 < 41.
```

Equation (1) says an official vanisher would contribute an official prime
factor to this exhaustive ledger.  None exists.  Hence the `(1,5)` slot is
empty at every official row.

## 4. Reproduction and custody

The compact checker is:

```text
tools/ramguard tiny -- python3 \
  critical/nodes/dli_wcl_slot_1_5_emptiness/verify.py --tamper-selftest
```

The load-bearing remote replays are
`notes/pilots_20260806/wcl15_finish/full_batch_replay_modal.py`,
`tail_independent_cert_modal.py`, and `tail191_factor_cert_modal.py`.  Their
preregistrations record all app IDs, source hashes, resource ceilings,
partial semantics, and operational-null CADO packaging attempts.
