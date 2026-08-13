# Proof

## All exceptional coordinates are forced

Fix a transformed explanation `a_gamma` that owns the selected slope
`gamma` and has exact outside deficit `e`.  It agrees with the transformed
base word `r_0` on exactly

```text
A=m-e
```

coordinates outside `E`.  Ownership requires at least `m` total agreements.
There are only `e` coordinates in `E`, so equality is forced throughout:

```text
a_gamma(x)=r_0(x)+gamma q(x)    for every x in E.    (1)
```

Different selected slopes give different explanations in this layer,
because `q` is nonzero at every point of its support `E`.

## The affine codeword line

Suppose first that there are at least two terminal explanations, indexed by
distinct slopes `gamma` and `delta`.  Their normalized difference

```text
p=(a_gamma-a_delta)/(gamma-delta)
```

is a nonzero degree-`<K` codeword, and `(1)` gives `p|_E=q|_E`.
For any third terminal explanation `a_eta`, the codeword

```text
(a_eta-a_gamma)/(eta-gamma)
```

has the same restriction to `E`.  Since `|E|=e>=K`, evaluation on `E` is
injective for degree-`<K` polynomials.  Thus this codeword is `p`, and every
terminal explanation lies on the affine line

```text
a_eta=a_gamma+(eta-gamma)p.                          (2)
```

## Outside packing

Outside `E`, let `G` be the set of coordinates where `p=0` and one, hence
every, member of `(2)` agrees with `r_0`.  Write `g=|G|`.  Since `p` is a
nonzero degree-`<K` codeword,

```text
g<=K-1=c.                                            (3)
```

At every outside coordinate not in `G`, the equation

```text
a_gamma(x)+lambda p(x)=r_0(x)
```

has at most one line parameter `lambda`.  The outside agreement sets of
distinct terminal explanations are therefore disjoint after deleting their
common core `G`.  Each such set has size `A`, so if there are `L_e` terminal
explanations,

```text
L_e(A-g)<=n-g.
```

For `n>A`, the ratio `(n-g)/(A-g)` increases with `g`.  Apply `(3)` to get

```text
L_e<=floor((n-c)/(A-c)),
```

which is `(TL1)`.  If `L_e<=1`, the same conclusion is immediate because
the displayed ratio is at least one.

## Profile payment

For `h<e`, cumulative monotonicity gives

```text
N_h<=min_(h<=v<e) C_v=B_h.
```

The suffix minima are nondecreasing.  An exact-deficit-`h` explanation owns
at most `floor(e/h)` slopes, while a terminal explanation owns at most one.
Summation by parts on the prefix layers and `(TL1)` on the terminal layer
give `(TL2)`.

The primary verifier reconstructs every raw Johnson/mean-centered prefix
cap and all four endpoint/adjacent records with exact integers.  The
independent audit checks the terminal packing algebra, exercises a finite
affine-line model, and independently recompiles the official profiles.
