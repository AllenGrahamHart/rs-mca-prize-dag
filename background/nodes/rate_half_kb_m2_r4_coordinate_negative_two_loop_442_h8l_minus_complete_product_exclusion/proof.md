# Proof

The parent colored-`xi` theorem establishes the univariate descent
`(KB44D-1)` and deletes the two forced-`cD` cells.  It remains to treat the
other two canonical forced types in both signs.

If `sigma DE=1`, then `E=1/(sigma D)`.  With `a=cD` and `x=DF`, direct
substitution gives `(KB44D-2)`.  Its two unsigned entries and two complete
signed pairs place it in the scope of the signed-pair template theorem, so
matching indices `0,1,2` are impossible.

For each of the remaining six `F`-sign representatives, substitute the
three paired entries into `(KB44D-1)`, clear denominators, and use the
resultant chain `(KB44C-3)`.  Factor-by-factor norms against `P_4` are all
nonzero.  The primary verifier reconstructs them and obtains exactly the
prime-support unions `(KB44D-3)`.  This deletes both forced-`DE` cells.

If `DF=1`, then `F=1/D`.  Writing `a=cD,q=cE` gives

```text
sigma DE=sigma aq/c^2,       EF=q/a,
```

and hence `(KB44D-4)`.  This residual set has only one complete signed pair,
so all fifteen matchings are treated directly.

For indices outside `{6,7,8}`, the same primary resultant chain has no zero
factor norm; their complete prime-support unions are `(KB44D-5)`.  At
indices `6,7,8`, sharing the first pair equation makes the final eliminant
identically zero.  This is only a projection degeneracy.  Adjoining all
three cleared pair equations to `P_4` and computing in
`F_2130706433[a,q,b]` gives the unit ideal in all six sign-index cases.

As an independent audit, share the second pair equation instead of the
first when forming the two intermediate resultants.  This alternate chain
has a nonzero final eliminant and nonzero `P_4` factor norms for every one
of the 30 forced-`DF` sign-index cases, including `6,7,8`.  It also replays
all twelve forced-`DE` representatives.

The deployed prime has nonzero residue modulo every prime in
`(KB44D-3)--(KB44D-5)`.  Therefore neither forced type has a completion.
Combining these four cell deletions with the two colored-cell deletions
exhausts all `2 sigma x 3 xi` cells over the common row. QED.
