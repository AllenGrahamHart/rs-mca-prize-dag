# KoalaBear m2 r4 positive 433-1b cell-0 complete exclusion

- **status:** PROVED
- **scope:** role cell `0` of the deployed positive route `433-1b -> O0a`
- **dependencies:** the positive `433-1b` common-minor compiler, product-rank-drop
  classifier and complete exclusion, signed `O0a` atlas, complete-fiber Vieta
  compiler, and order-two source-facet signature
- **consumer:** `rate_half_band_closure`

Cell `0` has singleton role `LA` and source deck pairs

```text
(AB,AC), (BC+,BC-).                               (KBP1BC0-1)
```

The product-rank-drop dependency excludes `rank(P)<=4`.  On the remaining
principal branch `rank(P)=5`, one of the six maximal product cofactors is
nonzero.  Localizing the six common-minor equations at each cofactor gives
24 exact chart rows: six charts and four source signs
`(epsilon_1,epsilon_2)`.

All twelve mixed-sign chart rows are unit ideals.  Every equal-sign row has
dimension one, basis size fourteen, and the same seven basis generators
that do not contain the localization variable.  Put

```text
p=2130706433, i=16711679, i^2=-1,
s=epsilon_1=epsilon_2, alpha_s=(1+s i)/2, x=t^2. (KBP1BC0-2)
```

The first, second, third, and sixth generators imply

```text
c^2+b^2=0,
(c-s i b)(r-b)=0,
c=s i b  ==>  b(br-1)=0,
xr+alpha_s x+alpha_s r^2+s i r=0.                (KBP1BC0-3)
```

The common guard has `b!=0`.  Hence every equal-sign common point lies on
one of exactly two necessary component families:

```text
A_s: c=s i b,  r=b^(-1),
     x b(1+alpha_s b)+alpha_s+s i b=0;

B_s: c=-s i b, r=b,
     x(b+alpha_s)+b(alpha_s b+s i)=0.             (KBP1BC0-4)
```

For each of the four pairs `(A_s,B_s)`, the exact compiler constructs the
unique common coefficient kernel and checks all ten common Vieta rows.
For each component, four target sign lanes, seven choices of outside record
at the missing mate, and fifteen perfect matchings of the residual six
records give

```text
2 components * 2 source signs * 4 target lanes * 7 * 15 = 1680 cases.
                                                               (KBP1BC0-5)
```

Each case imposes the component relation, missing-product equation, three
paired-product resultants, missing-mate squared-sum equation, and all source,
leading-support, and target-distinctness guards.  Exact sequential
saturation by the unique nonconstant guard factors gives the unit ideal in
all 1680 cases.  Thus the principal product-rank-five branch is empty in
cell `0`.  Together with the rank-drop dependency, the entire deployed
cell-0 route is empty.

This theorem does not exclude the principal branch in cells `1..14`, close
all of `433-1b -> O0a`, positive coordinate parity, K3, LIST, MCA, or either
Prize result.

## Falsifier

A missing chart/sign/component/target-lane/record/matching case, failure of
the factor implications in `(KBP1BC0-3)`, an invalid component kernel,
a nonunit saturated outside ideal, or a guard that deletes an admissible
packet.
