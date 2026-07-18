# Budget-three path witness on a power-of-two domain

- **status:** PROVED
- **closure:** exact finite certificate
- **consumer:** `rate_half_list_adjacent_crossing`

Let

```text
F=F_17,       D=F_17^*,       n=16,       k=8,       d=4.
```

There are four distinct degree-less-than-eight polynomials and one received
word whose four agreements are all exactly

```text
3d-1=11.
```

In ascending coefficient order, take

```text
f_0=(0),
f_1=(8,5,13,2,15,3,1,8),
f_2=(12,16,8,3,7,12,10,4),
f_3=(5,13,0,14,16,2,4,1),

u=(4,14,14,0,0,0,0,0,0,0,0,0,0,5,0,2),
```

where the entries of `u` are indexed by `D=(1,2,...,16)`. The exact
agreement supports realize the path-plus-singleton incidence type with

```text
T_0={1,2,3},       T_1={4,5,12},
T_2={7,8,13,15},   T_3={6,10,11},
E_02={9},          E_12={16},       S={14}.
```

Its `28 x 24` four-wise RS intersection matrix has rank `23`, and its
one-dimensional kernel contains the printed three codeword differences.

The corresponding path normal form has

```text
(q_01,q_02,q_03,q_12,q_13,q_23)
  =(8,4,1,13,10,15+14X).
```

Thus the path branch survives on a smooth power-of-two multiplicative domain
at `d=4`, even though its degree-`d` pencil has exactly three fully split
members. This refutes any exclusion based only on `d>=3`, power-of-two
smoothness, or the absence of a fourth pencil member.

This is not an official-row counterexample. It supplies no transport from
`n=16` to `n=2^41`, and the actual prize budget of the field `F_17` is not
three.
