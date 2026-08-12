# Near-rational line BC-guard rejection

- **status:** PROVED
- **closure:** explicit shifted-lattice vector
- **scope:** the `67472` displayed bad slopes in the deployed KoalaBear
  counterexample of upstream `#1160`

## Statement

Every displayed bad slope in the `#1160` near-rational counterexample is
rejected by the necessary balanced-profile guard in the cycle-19 candidate
`P_BC` certificate contract.

For the slope `gamma_i`, the word `U_i=u+gamma_i v` is nonzero exactly on
`E\{e_i}`, a set of size `w-1=67471`.  Its support locator `W_i`, together
with numerator zero, is a nonzero vector `(W_i,0)` in the received-word
lattice and has effective shifted degree `67471`.  Hence the lattice minimum
is at most `67471`, whereas the candidate BC contract requires it to be at
least `67472`.  No displayed bad slope can satisfy that contract.

## Consequence

The mandatory `#1160` hostile regression passes at guard level: the repaired
near-rational line cannot leak into candidate BC through its balanced-profile
test.  This removes one cheap falsifier of the shared SEM-QBC/WLCS substrate.

## Nonclaims

The candidate `P_BC` relation is still not a fully executable, source-proved
equivalent of the frozen BC owner.  This result proves neither that relation's
soundness or coverage nor the guarded `K` adapter, Q exclusion, endpoint
realization, selector totality, a slope payment, or an MCA row.

## Falsifier

A displayed `#1160` slope whose word does not have support `E\{e_i}`, failure
of `(W_i,0)` to lie in its received-word lattice, or a candidate certificate
that can pass while its minimum shifted degree is below `67472`.
