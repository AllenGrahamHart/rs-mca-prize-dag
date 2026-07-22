# Claim contract - L1 official Newton cofactor-window router

## Inputs

- the official generated-field hypotheses, including `n>=2^13` and the
  strict field cap `p^f<2^256`;
- the canonical reserve threshold `a_0=k+ell_0-1`;
- a normalized received polynomial of degree `h`;
- one exact shell `a>=a_0` and one fixed error cofactor.

## Output

The characteristic satisfies `p>=3583` and `p-ell_0>=3174`. Whenever
`h-a_0<=p-ell_0`, the fixed-cofactor locator prefix has depth below `p` and
is exactly Newton-equivalent to a prescribed power-sum prefix.

## Falsifier

An official generated field with `p<3583`; a canonical cutoff with
`p-ell_0<3174`; or a shell in the declared window whose first `d` locator
coefficients and first `d` power sums are not bijective.

## Nonclaims

No max-fiber estimate, Pade-graph intersection bound, positive-cofactor
coalescing theorem, or implication from the special F2 Myerson target.
