# Proof

The fibers over `0,1,infinity` have the following ramification partitions:

```text
0:         3^h 1^e,
1:         c 1^(2h),
infinity:  m.                                             (1)
```

Their finite ramification contribution is

```text
2h+(c-1),
```

and infinity contributes `m-1`. Since `c=h+e` and `m=3h+e`, the total is
`2m-2`. Riemann--Hurwitz therefore leaves no further branch point. The cover
is tame because every ramification index is at most `m<p`.

We use the standard tame branch-cycle correspondence. In characteristic
zero it is the Riemann existence/dessin correspondence. In characteristic
`p>m`, the monodromy group is a subgroup of `S_m`, hence has order prime to
`p`; the prime-to-`p` tame specialization theorem identifies the same
branch-cycle classes. The relevant primary references are SGA 1, Expose XIII,
Corollaire 2.12, for tame specialization, and Shabat--Zvonkin, *Plane trees
and algebraic numbers*, Contemporary Mathematics 178 (1994), 233--275, for
the polynomial/plane-tree correspondence. Thus a labelled cover determines
one bicolored plane tree with the vertex degrees in `(1)`, and two covers
with the same tree differ by an affine source change. The unique point of
degree `c` above `1` is distinguished at zero, so that affine change is a
scaling.

It remains to count the trees. There is only one non-leaf white vertex: the
degree-`c` vertex over `1`. Every non-leaf black vertex has degree three. A
black degree-three vertex must meet the central white vertex; otherwise its
component contains only its two white leaves. It uses its two remaining
edges on those leaves. Every black degree-one vertex also meets the center.
Consequently the whole abstract tree is forced:

```text
central white vertex
  -- h black trivalent branches, each carrying two white leaves;
  -- e black leaves.
```

Only the cyclic ordering of these `c=h+e` incident objects remains. The
trivalent branches are indistinguishable from one another, as are the black
leaves. Hence an oriented plane tree is exactly a cyclic binary word of
length `c` with `e` leaf symbols.

Burnside's lemma for the cyclic rotation group gives

```text
# necklaces
 =(1/c) sum_(d|gcd(c,e)) phi(d) binom(c/d,e/d),
```

which is `(CSN1)`. Since the branch-cycle map is injective on cover classes,
this proves the bound. QED.
