# Frontier after the moving-root slack cut

The first unresolved source size has two primitive local cells:

```text
GCD-TWIST:       H=L_C(X-g),       g outside the base field,
MOVING-COFACTOR: Pbar+eta Qbar=L_(F_eta)(a_eta X+b_eta),
                 with at least twenty potentially nonbase linear cofactors.
```

## Route fence

The existing rank-nine outlier and regular-locator contracts do not by
themselves exclude either cell.

1. A rich affine pencil contributes one affine direction. The eight outliers
   certify completion to affine rank nine, but their rank condition does not
   contain the common root `g` or the cofactor coefficients `(a_eta,b_eta)`.
2. The regular Hankel/locator equations are imposed separately on each exact
   witness support. They contain no cross-record identity linking an outlier
   locator to the rich-pencil gcd or moving cofactors.
3. Exact upstream controls realize rank-nine selectors satisfying the local
   regular equations, and separate exact controls realize both one-slack
   shapes. These controls are not deployed counterexamples, but they refute
   any proof using only the disjoint local interfaces.

Consequently the next valid reduction must add one of:

- a cross-record equation derived from selector minimality or completeness;
- execution of the deployed earlier-owner masks on the one-slack records;
- an injective first-match owner for nonbase linear twists; or
- a source-load theorem that pays every compatible completion.

A coefficient sweep over `g`, `(a_eta,b_eta)`, or arbitrary outlier vectors
does not decide any of those universal alternatives and is not a responsible
compute request.
