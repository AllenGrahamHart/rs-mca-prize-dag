# Budget-three residual transversal atlas

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`

Work in the canonical six-type split-pencil atlas, with `n=4d`. Together
with the path and cycle transversal theorems, every constant pencil printed
by that atlas has an exact large-scale member count.

## Dense two-graph branches

For the `K_4-e` and `K_4` types, put

```text
theta=A_1/A_0,
M_2=b_12/b_02,       M_3=b_13/b_03.
```

Then

```text
theta=infinity on T_0,       theta=0 on T_1,
theta=M_2     on T_2,        theta=M_3 on T_3.       (RTA1)
```

Both `M_2` and `M_3` are nonconstant injective Mobius maps. Moreover,

```text
M_3-M_2=b_01b_23/(b_02b_03).                         (RTA2)
```

The complement of the four large blocks has respectively six and eight
points. Hence any projective member of `<A_0,A_1>` other than `A_0,A_1` has
at most

```text
K_4-e: 1+1+6=8,       K_4: 1+1+8=10                (RTA3)
```

domain roots. The pencil therefore has exactly two fully domain-split
degree-`d-2` members for `d>=11` in the `K_4-e` type and for `d>=13` in the
`K_4` type.

Their deficit-free triangle pencils are also exact-three. In each such
degree-`d-1` pencil, the complementary large block is seen through a
nonconstant ratio of two products of distinct linear edge locators. A fiber
has at most two points. Charging every remaining exceptional point gives

| type | printed pencils | transversal roots | exceptional roots | residual cap | exact-three threshold |
|---|---:|---:|---:|---:|---:|
| `K_4-e` | 2 | 2 | 4 | 6 | `d>=8` |
| `K_4` | 4 | 2 | 5 | 7 | `d>=9` |

## Triangle-plus-singleton branch

Let `w` be the singleton point, `j` the full point, and let
`e_01,e_02,e_12` be the three distinct linear edge locators. The `013` and
`012` identities give the two representative constant pencils

```text
A_0, A_1, e_01 A_3                         (degree d-1),
e_12 A_0, e_02 A_1, e_01 A_2               (degree d). (RTA4)
```

On the complementary blocks their parameters are respectively

```text
A_1/A_0=b_12/b_02                 on T_2,
(e_02 A_1)/(e_12 A_0)=c e_02/e_12 on T_3,   c!=0.    (RTA5)
```

These are injective Mobius maps. Thus the first pencil has residual root cap
`1+4=5`, and the second has residual root cap `1+2=3`. Relabeling
`0,1,2` gives all three degree-`d-1` pencils. Consequently all four printed
pencils have exactly three fully domain-split members for `d>=7` (and the
degree-`d` pencil already does for `d>=4`).

## Pendant branch

The sole printed pencil is

```text
A_2,       e_12 A_0,       A_1                 (degree d-1). (RTA6)
```

On the complementary block `T_3`, its parameter is

```text
A_1/(e_12 A_0)=b_13/(b_03 e_12).                    (RTA7)
```

This rational function is nonconstant and every fiber has at most two
points. Indeed its numerator has degree at most two and is divisible by the
edge locator `e_13`, whereas its denominator is a nonzero scalar multiple of
`e_03e_12`; the three edge roots are distinct. The only unconsumed
exceptional points are the `03,13,23` edge points. Every further pencil
member therefore has at most `2+3=5` domain roots, and the pencil has exactly
three fully domain-split degree-`d-1` members for `d>=7`.

Combining this theorem with the prior path theorem proves that all thirteen
deficit-free pencils in the six-type atlas have exactly their three displayed
fully domain-split members at the official value `d=2^39`. Combining it with
the cycle theorem also gives an explicit two-fiber/two-graph or
three-fiber/low-degree-graph normal form for every incidence type. The
simultaneous coupling of those maps with the subgroup factorization remains
open; no incidence type or adjacent crossing is excluded here.
