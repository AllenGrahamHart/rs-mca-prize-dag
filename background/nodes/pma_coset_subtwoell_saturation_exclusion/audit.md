# Audit - PMA constant-shift-pencil sub-two-ell saturation exclusion

## Hypothesis Audit

| hypothesis | use | failure mode if removed |
|---|---|---|
| `d<2ell` | gives the two-block decomposition | false at equality |
| `d>ell` | makes the common factor in the rank-three branch nonconstant | the strip is already root-paid in the intended consumer |
| `t>=3` | forces a constant value label from rank at most two | false for two petals |
| distinct `a_i` | supplies three distinct roots and pairwise-coprime locators | repeated petals are not distinct chart cells |
| `gcd(F,W)=1` | kills both the rank-three factor and constant-label branch | planted/common-factor pairs survive |
| locators `P-a_i` for one monic `P` | gives one common two-block row matrix | arbitrary petals remain open |

The argument is characteristic-free. A degree-two polynomial cannot have
three distinct roots over any field, including characteristics two and three.
Separability of each petal polynomial is not used.

## Sharp Counterexamples

### Two petals

Over `F_7`, take

```text
ell=2, d=3,
F=X^3-X^2-X+2,
W=2X^3-X^2-2X+2.
```

Then

```text
W-F=X(X^2-1),       W-2F=X^2-2,
gcd(F,W)=1.
```

Thus the statement is false with `t=2` inside the strict defect strip.

### Endpoint defect

For every `ell>=1`, over `F_7` take

```text
F=X^(2ell)+1,       W=X^ell.
```

At `a=(1,2,3)`, the values

```text
c_i=a_i/(a_i^2+1)=(4,6,1)
```

give `X^ell-a_i | W-c_iF`. The pair is coprime. Hence `d=2ell` cannot be
included.

### Saturation

For any three distinct labels and one scalar `c`, the pair `W=cF` satisfies
all petal congruences. Exact-defect saturation is what excludes this planted
common-factor branch.

## Consumer-Scope Audit

The theorem covers every constant-shift locator pencil `P-a_i`; the
upstream/local coset residue bridge supplies the special case `P=X^ell`.
The proved G1 atlas provides such coset charts for top-band contributors,
which are already paid. It does not assert that every surviving below-band
maximal-source layout has a common locator pencil. Therefore this node is a
proved scoped exclusion and an evidence edge to `petal_mixed_amplification`,
not a required supplier that promotes or globally narrows that target.

If a future source theorem maps the `M=4,t=3` residual into common
constant-shift locator pencils, this node removes its strict `ell<d<2ell`
portion. Root pinning already pays
`d<=ell`, and the top band pays `d>=2ell`, so that source bridge would remove
the whole `M=4,t=3` stratum.
