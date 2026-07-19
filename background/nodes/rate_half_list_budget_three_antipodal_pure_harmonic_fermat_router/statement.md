# Budget-three antipodal pure harmonic-Fermat router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_pure_quartic_degree_rigidity`

Retain the maximal official pure-quartic stratum

```text
e_2=e_3=0,       d=2^39,       r=2^37-1,
deg V=r-1.                                               (HFR1)
```

Write the four deleted roots as `b_i=a_i^2`. The lifts `a_i` lie in the
order-`2d` subgroup, and distinctness of the `b_i` means
`a_i!=a_j` and `a_i!=-a_j` for `i!=j`.

After relabeling, the Möbius weld and `(HFR1)` force the harmonic equation

```text
cr(a_0,a_1;a_2,a_3)
 :=((a_0-a_2)(a_1-a_3))/((a_0-a_3)(a_1-a_2))=-1.      (HFR2)
```

Common scaling permits `a_0=1`. Put `x=a_1/a_0`, `y=a_2/a_0`, and
`w=a_3/a_0`. Then

```text
w=(2x-y(1+x))/(1+x-2y),                                (HFR3)
```

where the denominator is nonzero for distinct lifts. Thus the lift router is
the exact two-variable subgroup condition

```text
x^(2d)=y^(2d)=1,
((2x-y(1+x))/(1+x-2y))^(2d)=1,                         (HFR4)
```

with all four squares distinct.

The polynomial part has an equally exact normal form. Define

```text
E(z)=product_i(1-b_i z),       Q(z)=(1-z^d)/E(z).      (HFR5)
```

There are coprime polynomials `B,Z` such that

```text
Q=B^4+Z^4,
B(0)=1,       ord_0 Z=1,       deg B,deg Z<=r.         (HFR6)
```

Conversely, harmonic lifts satisfying `(HFR2)` together with a decomposition
`(HFR6)` reconstruct the pure-quartic antipodal pencil and its two locator
relations. Hence `(HFR2)--(HFR6)`, composed with the proved squarefreeness and
linear Wronskian residual, are an exact router for the pure boundary.

The harmonic condition is not an emptiness theorem: non-antipodal harmonic
quadruples occur in small finite two-power subgroups. The remaining task is to
exclude the matched Fermat decomposition at official scale.
