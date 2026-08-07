# Audit - PMA full-petal band/root composition

## Scope and notation checks

1. `M` is the total number of petals in the fixed maximal source and in its
   carried G1 chart. `t` is the number touched by one codeword. They are not
   interchangeable.
2. The equality mutant `M=t` is false. The G1 clause-(P) proof and independent
   audit realize both `t=M-1` and `t=M` in the top band.
3. The top-band relation uses the same carried layout. No existential
   re-basing is allowed; that semantics is already refuted in the G1 packet.
4. Maximality `r<ell` is load-bearing. If `r=ell`, a top-band arithmetic shape
   can touch only `M-2` petals.
5. The `M<=3` close uses the proved non-planted fact `t>=2`. A planted
   one-petal anchor is outside this class.
6. Root pinning pays the below-band branch only at the L1 lower cutoff and
   under its existing source-multiplicity contract. No finite sigma-one
   polynomial conclusion is imported.
7. Partial petals have `u>0` and are untouched by this theorem.

## Adversarial controls

The verifier exhausts integer parameter shapes over multiple `ell`, `M`,
background, defect, and touched-petal values. It checks `(FPC1)` through
`(FPC6)` and includes three required-to-trip mutations:

- identify chart count with touched count;
- permit `r=ell` instead of the strict maximality inequality;
- drop the non-planted `t>=2` input in the `M=3` closure.

## Remaining attack

The full-petal part of the direct PMA residual is now restricted by `(FPC5)`
and `(FPC6)`. The mixed/partial-petal family and the unbounded off-band
root-excess family still require a natural-scale owner or a new aggregate
smooth-domain theorem.
