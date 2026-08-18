# Cycle 515: endpoint direction saturation

## Result: PROVED global direction bank

At every full 218-owner coordinate, the plane endpoint theorem supplies at
least 210 distinct saturated projective directions. Counting their roots
against the degree cap `K'-1` gives, uniformly over `K'=4960..4982`,

```text
41746<=R<=47836.
```

Every represented direction has at least `K'-2609>=2351` residual roots.
Using the largest possible direction population in the capacity denominator
gives

```text
aggregate unused degree <=30203244,
aggregate saturation >=5750430/6589409>0.8726.
```

## Burn-down

```text
starting local pin:       f0a13cc6e
canonical prize pin:      0dd5b3244
upstream PR #1170 pin:    6186c7b1
DAG delta:                +1 PROVED direction-saturation node, +3 edges
critical status delta:    none
compute spend:            none
closed interface:         diffuse q=3170 plane directions
next action:              quotient-periodic classification or common-factor forcing
```

## Nonclaims

- aggregate saturation is not individual near-splitting;
- the direction bank is not classified or paid;
- the endpoint, rank eleven, and MCA remain open.
