# Cycle 345: MCA rank-11 rank-eight circuit-shadow census (2026-08-15)

The first open rank-eight row is `K'=11`.  This cycle classifies its
codimension-one evaluation geometry exactly before attempting another
aggregate capacity inequality.

## Fixed circuit

Let `P=RS_{<11}` and let `V'<=P` have dimension ten.  If a fixed nine-set
`B` has evaluation rank eight, then

```text
ker(ev_B|V')=L_B RS_{<2}.
```

The functional cutting out `V'` therefore factors through `ev_B`.  Its
support is one fixed circuit `C_B subset B`, independent of every extension
pair.  Circuit size one is impossible in the actual component target: the
chart contains millions of distinct slopes, so a loop coordinate would
make its affine rich equation identically zero and contradict empty
residual global common support.  Thus `2<=c:=|C_B|<=9`.

For every `T=B union {x,y}`, the unique relation on the rank-ten
eleven-set has support `C_B`.  A nine-shadow has rank eight iff its omitted
pair is disjoint from the circuit.  Consequently it has

```text
C(11-c,2) rank-eight shadows,
55-C(11-c,2) rank-nine shadows,
c rank-ten bases.
```

The same functional factorization gives the structural containment

```text
L_(C_B) RS_{<11-c} <= V'.
```

Explicit finite-field hyperplanes realize all `c=2,...,9`; the eight-petal
fence realizes `c=9` with shadow census `1/54`.

## Route impact

No residual row closes.  The theorem gives the exact next split:

```text
c=9:   full-support circuit, 54 rank-nine shadows, eight-petal control;
c<=8:  additional rank-eight charts and locator-ideal dimension >=3.
```

The existing rank-nine cap cannot simply be summed over all neighboring
charts; that union bound is much too loose.  A useful continuation must keep
the owner label and extension overlap in the `(record,T,B')` incidence unit,
or derive a legitimate shortening/global-owner consequence from the larger
locator ideal.

```text
result:                PROVED exact K'=11 circuit-shadow census
DAG delta:             +1 PROVED node
critical status delta: none
rank-eleven boundary:  unchanged
delta-star movement:   none
compute:               GF(101) row-reduction replay and independent GF(103)
                       determinant replay under RAMguard; no Modal
next route action:     owner-labelled one-replacement coupling for c=9;
                       locator-ideal/extra-shadow coupling for c<=8
```
