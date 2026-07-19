# Proof

Choose exactly `a_0=3d-1` agreement coordinates for each of the four listed
codewords. The total incidence is

```text
sum_x m_x=4a_0=12d-4.                                  (1)
```

Two distinct degree-`<2d` polynomials agree at at most `2d-1` points. Double
counting pair intersections therefore gives

```text
sum_x binom(m_x,2)
 =sum_(i<j)|S_i intersect S_j|
 <=6(2d-1)=12d-6.                                     (2)
```

## Degree-count classification

Relative to incidence degree three at every one of the `4d` coordinates,
equation `(1)` and inequality `(2)` become

```text
3n_0+2n_1+n_2-n_4=4,                                  (3)
3n_0+3n_1+2n_2-3n_4>=6.                               (4)
```

Eliminating `n_4` gives

```text
3n_0+2n_1+n_2>=4,       6n_0+3n_1+n_2<=6.             (5)
```

Thus `n_0=0`. If `n_1=0`, then `n_2` is `4,5`, or `6`; if `n_1=1`, then
`n_2` is `2` or `3`; and if `n_1=2`, then `n_2=0`. These are the six raw
degree-count patterns, with `n_4` fixed by `(3)`.

Let `T` be the number of degree-three coordinates, let `t_i` count those
whose agreeing triple omits codeword `i`, let `s_i` count singleton
coordinates labeled `i`, and let `p_ij` count degree-two coordinates labeled
`{i,j}`. Put `p_i=sum_(j!=i)p_ij`. The four individual agreement equations
and six pair caps are

```text
T-t_i+s_i+p_i+n_4=3d-1,                               (6)
T-t_i-t_j+p_ij+n_4<=2d-1.                             (7)
```

For the raw pattern `(0,2,0,0)`, equations `(6)--(7)` reduce to
`s_i+s_j>=1` for every pair, while `sum_i s_i=2`. Two vertices have zero
singleton count, contradicting their pair inequality. Hence this pattern is
impossible.

For the other five patterns, substitute the possible singleton labels and
degree-two multigraphs into `(6)--(7)`. Up to a permutation of four vertices,
the surviving multigraphs are exactly those in the statement: two graphs
with four edges, followed by `K_4` minus one edge, `K_4`, a two-edge path
opposite the singleton, and a triangle opposite the singleton. This is six
types. The verifier exhausts the same finite nonnegative compositions and
checks the table independently of `d`.

## Intersection matrix

Subtract `f_0` from all codewords and from the received word. Write
`h_0=0` and `h_i=f_i-f_0` for `i=1,2,3`. At one coordinate, all codewords
whose index lies in `I_x={i:x in S_i}` have the same received value. If
`0 in I_x`, this says `h_i(x)=0` for every other `i in I_x`. If `0` is not
present, it says the values `h_i(x)`, `i in I_x`, are all equal. A spanning
tree gives exactly `|I_x|-1` independent displayed equations when
`I_x` is nonempty. Their coefficient rows define `M`.

A four-codeword witness therefore gives a vector in `ker M` for which
`0,h_1,h_2,h_3` are pairwise distinct. Conversely, such a vector defines a
received word by taking the common constrained value on every nonempty
`I_x` and an arbitrary value elsewhere. It lists all four polynomials on the
chosen supports. This proves the equivalence.

All viable patterns have `n_0=0`, so the raw row count is

```text
sum_x(m_x-1)=sum_x m_x-n=12d-4-4d=8d-4.
```

There are `3k=6d` coefficient columns. Full column rank excludes every
pairwise-distinct kernel vector and proves predecessor safety.

## Exact route fence

In `F_17`, take the order-eight domain

```text
D=(1,9,13,15,16,8,4,2)
```

and the four degree-less-than-four polynomials, in ascending coefficient
order,

```text
f_0=(0,0,0,0),
f_1=(11,2,8,7),
f_2=(8,5,13,2),
f_3=(15,13,15,13).
```

The received word

```text
u=(11,0,0,0,4,0,0,1)
```

has agreement exactly five with every `f_i`. Its coordinate incidences have
one singleton, two degree-two points, and five degree-three points, realizing
the `(0,1,2,0)` path type. The associated `12`-column matrix has rank `11`.
The focused verifier checks every evaluation, support, pair cap, matrix row,
and rank. Thus no argument using only `(1)--(2)` can prove the needed
official full-rank statement. QED.
