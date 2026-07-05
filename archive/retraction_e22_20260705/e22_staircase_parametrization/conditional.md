# conditional: e22_staircase_parametrization

## Predicate nodes

- `e22_tail_coset_locator_algebra`
- `e22_agreement_coset_support_forcing`

## Claim

Conditional on the support-forcing predicate, every structured E22 challenger
has the advertised quotient-coset staircase parametrization.

## Proof

The open support-forcing predicate says that the mixed/full-petal agreement
equations force the relevant support to be a fixed tail `B` together with full
fibers of a quotient map `x -> x^M`, with `M > t`.

The proved algebra predicate then converts exactly such a support into the
locator form

```text
L_B(X) G(X^M).
```

Its top `t` coefficient invariance is also part of that algebra predicate, so
the resulting locators have the same codeword-side cancellation property used
by the X-4 quotient-coset staircase ledger. Thus the remaining work in this
node is precisely the support-forcing theorem; once it holds, the advertised
staircase parametrization follows.
