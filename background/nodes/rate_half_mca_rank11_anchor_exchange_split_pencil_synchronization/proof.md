# Proof

## Global support choices

The parent chooses pair types `p_0,p_1,...,p_t`, with `1<=t<=4`, whose pair
cores intersect in the complete triple-owner core `J_3`. Fix these types and
three owned slopes from each `p_i`, `i>=1`.

Choose exactly 5524 of the anchor's owned slopes. For every record in this
fixed set, choose once and for all an exact size-`m` support containing the
anchor pair core. Make the analogous fixed choice for the selected secondary
records. This can be done record by record. Two records from one pair have
full agreement-set intersection equal to that pair core, so any two chosen
exact supports containing the core also intersect exactly in the core.

Every packet considered below contains at least three records from each
represented pair. Consequently its complete support intersection is always
`J_3`, independently of the anchor subset. Cancellation by `J_3` therefore
leaves the same residual anchor core `H_0`, the same integer

```text
e=m'-|H_0| in {1,...,11},
```

and a fixed exception locator `L_(E_gamma)` for every anchor slope `gamma`.

## One-swap packet star

The packet size allocated to the anchor is

```text
s=32-3t>=20.
```

Choose `A_0`, `alpha`, and the one-swap sets `A_eta` as in the statement.
Every resulting packet has exactly 32 distinct owned slopes, three from each
secondary pair, at least 20 from the anchor, the same recovered core, and an
off-line secondary record. Thus the pole-simple parent and the exact
partial-relative trichotomy apply to every packet.

If any packet has the high-complexity output, the first alternative holds.
Assume henceforth that all these packets have rational outputs. Apply the
exception split-pencil normal form to each packet. It gives a two-dimensional
polynomial subspace

```text
P_A=span(u_A,v_A)
```

containing `L_(E_gamma)` for every `gamma in A`. The affine locator scalar is
nonzero on every selected slope. Also `u_A,v_A` are coprime and have maximum
degree `e>=1`, so `P_A` is genuinely two-dimensional.

For every `eta notin A_0`, the sets `A_0` and `A_eta` share

```text
s-1>=19
```

anchor slopes. Choose any two of them. Their monic exception locators are
distinct because their nonempty root sets are disjoint. Distinct monic
polynomials are not scalar multiples, hence these two locators are linearly
independent. Both `P_(A_0)` and `P_(A_eta)` are two-dimensional and contain
them, so

```text
P_(A_eta)=P_(A_0).
```

The base pencil contains every base locator, and the `eta`-packet places the
new locator `L_(E_eta)` in that same pencil. Varying `eta` proves that the
single coprime base pencil contains all 5524 anchor locators. QED.

## Scope

Only the star of one-swap packets is used; no summation over packet
certificates occurs. The theorem synchronizes the rational output but does
not assert that the high-complexity alternative is paid or that the common
pencil belongs to any particular cyclic, dihedral, affine, or primitive
class.
