# Claim contract - L1 tangent double-root descent

## Inputs

- the exact-shell factorization and complement gcd guard;
- the exact tangent owner `D=gcd(L,Q)`;
- the fixed-owner equivalence `D^2|U-P`.

## Outputs

- affine parameterization `P=P_D+D^2R` when `2 deg(D)<=k`;
- a bijection from the exact-`D` tangent stratum to a primitive exact shell
  on `H\roots(D)`;
- parameter transform `(n,k,a,e,w)->(n-r,k-2r,a-r,e-r,w+r)`;
- multiplicity at most one when `2r>k`.

## Consumer rule

Apply the descent once using the exact gcd.  The reduced shell is primitive,
so it must not be recursively charged to another tangent owner.  Retain the
punctured domain and do not silently invoke subgroup-specific flatness there.

## Nonclaims

No sum over `D`, preservation of smoothness, row-sharp reduced-shell bound,
quotient absorption, or closure of `l1_mixed_petal_amplification` is proved.

## Falsifier

A failure of the affine parameterization, an outside-`D` agreement mismatch,
a reduced primitive member whose lift has another tangent/complement root,
an exact-`D` member omitted or duplicated by the map, an incorrect parameter
transform, or two rigid-range codewords for one `D`.
