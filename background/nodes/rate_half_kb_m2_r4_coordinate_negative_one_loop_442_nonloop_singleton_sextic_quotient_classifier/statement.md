# KoalaBear m2 r4 coordinate negative one-loop 442 nonloop-singleton sextic quotient classifier

- **status:** PROVED
- **scope:** the finite common-`K` orbit `[9,10,12,13]` after the degree-12
  gate
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_cubic_root_gate`
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_degree12_gate`
- **consumer:** `rate_half_band_closure`

Write the three factors of the degree-12 gate as

```text
G_-(b)=b^3-b^2-b-1,
G_+(b)=b^3+b^2+b-1,
S(b)=b^6-2b^5+7b^4-8b^3+7b^2-2b+1.             (KB41Q-1)
```

In every root-sign row, both cubic branches `G_-=0` and `G_+=0` force

```text
t^2+r^2=0,                                        (KB41Q-2)
```

which collides the singleton label `t^2` with the existing label `-r^2`.
Thus only the sextic branch `S(b)=0` remains.

After substituting the parent's rational reconstruction of `c`, the sextic
common ideal is zero-dimensional of rank six in every sign row.  Its
standard monomial basis is

```text
1, b, b^2, r, br, t.                              (KB41Q-3)
```

For the representative `(epsilon_1,epsilon_2)=(1,1)`, a reduced deployed-
field basis is

```text
b^2r+b^2+(i-1)br-(i+1)b+r+1,
b^3-(i+1)b^2+(i-1)br+(i+2)b+(i+1)(r+t)/2-i,
t^2-ir-(2i+1)t-(2i-1),
rt+i,
r^2+(i+2)r+t-(2i+1),
(i-1)b^2+b(r+t)-(i-1)b+(i-1).                    (KB41Q-4)
```

The multiplication determinant of the `c`-reconstruction denominator
`b(r^2+1)^2+r^4-6r^2+1` is `2^19` on `(KB41Q-3)`, in every sign row.
Hence the reconstruction is a unit in the quotient and no denominator
component is hidden.

This theorem reduces the orbit to four rank-six guarded quotient rows.  It
does not assert that every quotient root is admissible, impose outside
products or sums, classify another common orbit, close the coordinate
orientation or a row, or prove either Prize result.

## Falsifier

A guarded common packet on either cubic factor, failure of the rank-six
sextic basis in a sign row, or a zero reconstruction-denominator norm.
