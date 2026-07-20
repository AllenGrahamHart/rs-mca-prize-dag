# F3 h>=4 norm-gate aggregate count

- **status:** TARGET
- **consumer:** `f3_hge4_aggregate_budget`
- **binding claim:** NG-COUNT

## Row and width scope

At every official corridor row,

```text
n=2^s,                    13<=s<=41,
p prime,                  p==1 mod n,
p>=n^2,
H_max=min(k+t,floor(n/2)).
```

For each `4<=h<=H_max`, let `N_h^strip` count records in the direct-column
convention with all of the following properties:

1. the record is F-4-minimal in the x81 square-shift convention;
2. it is not a characteristic-zero full-fiber trade;
3. all `h-1` cleared x83 low obstructions vanish modulo the row prime and the
   recovered `lambda` is a nonzero square;
4. it survives the ordered quotient, dihedral, moment-trade, U2-boundary, and
   DLI/skew deletion columns.

The binding target is

```text
sum_(h=4)^H_max N_h^strip <=14n^3.                  (NG-COUNT)
```

An empty sum is zero. The count is on records in the x81/x83 anchoring and
deduplication convention, not on raw support pairs, moments, or unanchored
presentations.

## Strip-free sufficient target

Let `N_h^raw` count the same F-4-minimal, non-full-fiber x83 norm-gate records
before the five deletion columns. Deletion is monotone, so

```text
N_h^strip<=N_h^raw
```

at every width. Therefore

```text
sum_(h=4)^H_max N_h^raw<=14n^3                    (RAW-NG)
```

is a stronger sufficient theorem. RAW-NG is the preferred proof interface
because it does not require operational implementations of the U2-boundary
and DLI/skew deletions.

## Primitive shift-pair sufficient target

There is also a proved direct interface to the primitive part of the exact
shift-pair ledger. Let

```text
B_h=binom(n,h)(binom(n,h)-1)/p^(h-1)
```

and let `SP_h^prim` count ordered top shift pairs after the same
quotient-pullback/full-fiber deletion used by the quotient column. The proved
node `f3_hge4_primitive_shift_pair_aggregate_adapter` gives

```text
N_h^strip<=SP_h^prim
```

and proves that the uniform finite-track estimate

```text
SP_h^prim<=7000n max(1,B_h)                       (PSA3)
```

for every `4<=h<=H_max` implies NG-COUNT. This route does not require a width
cap or operational definitions of the other four deletions.

The scaling action gives an even more direct finite interface. Let
`O_h^prim` count scaling orbits of ordered primitive top shift pairs. The
proved `f3_hge4_primitive_shift_pair_orbit_aggregate_router` gives

```text
SP_h^prim=n O_h^prim
```

and therefore

```text
sum_(h=4)^H_max O_h^prim<=14n^2                  (OAR2)
```

is sufficient. This quadratic orbit census is the preferred exact-certifier
currency; `(PSA3)` remains a stronger per-width analytic route.

The proved near-square union router removes the left/right partition search.
For a `2h`-support `U`, let `D_U` be its monic locator. It is a valid
primitive union exactly when the unique monic degree-`h` square root at
infinity satisfies

```text
S_U^2-D_U=d_U^2 in F_p^*
```

and the two factors `S_U-d_U,S_U+d_U` reconstruct a primitive pair. If
`A_h^union` counts distinct valid primitive unions containing `1`, then

```text
A_h^union=hO_h^prim.
```

Thus `(OAR2)` is equivalently

```text
sum_(h=4)^H_max A_h^union/h<=14n^2.               (NSU4)
```

The stronger per-width route is equivalently
`A_h^union<=7000h max(1,B_h)`.

An anchored union generator has `binom(n-1,2h-1)` raw candidates, an exact
factor `binom(2h-1,h-1)` below the anchored ordered-pair generator.

The proved swap odd-moment router resolves the non-free union stabilizer
structurally. Swap-stabilized primitive unions are absent at even `h`. At odd
`h`, their two supports are `P,-P`, and they are exactly the antipodal-free
solutions of

```text
sum_(x in P)x^j=0,                 j=1,3,...,h-2,
```

subject to trivial common scaling stabilizer. If `A_h^swap` counts anchored
swap unions and `V_h^swap` their scaling orbits, then

```text
A_h^swap=hV_h^swap<=binom(n/2-1,h-1).
```

This is a generator reduction, not the required aggregate estimate: the
free-union class and the odd signed-moment fiber count remain open.

The proved half-order square descent removes the remaining sign search. Put
`N=n/2`, let `Y` select the `h` antipodal pairs, and set
`c_Y=prod_(y in Y)y`. The swap test is exactly

```text
(L_Y(Z)+c_Y)/Z=T_Y(Z)^2,
```

with trivial scaling stabilizer for `Y` in `mu_N`. This test deterministically
reconstructs the two sides, and its scaling-orbit count is exactly
`V_h^swap`. Thus an anchored swap generator checks only the
`binom(N-1,h-1)` supports containing `1`, with no `2^(h-1)` sign factor. It
still does not bound the number retained.

For every fixed `(N,h)`, the proved straight-line lift presents
`YT^2-c | Y^N-1` by an exact cubic repeated-squaring scheme. With
`m=log_2(N)`, `d=(h-1)/2`, `s_0=floor(log_2(h-1))`, and `k=m-s_0`, it has

```text
(d+1)+k(2h-1)-h variables,       k(2h-1) equations.
```

The scheme is empty in characteristic zero, so a checked nonzero integer
Nullstellensatz certificate restricts the possible characteristics in that
cell. No such certificate, uniform factor bound, or cross-cell sum is proved.

The proved non-full near-square lift extends this architecture to the
previously uncontrolled free-union class. For
`S=X^h+sum_(j=0)^(h-1)s_jX^j`, add

```text
sum_(j=1)^(h-1) z_j s_j=1
```

to the repeated-squaring presentation of `S^2-a^2 | X^n-1`. This captures
every non-full-fiber divisor before the primitive and strip deletions. With
`k=log_2(n)-floor(log_2(2h-1))`, the global selector has `k(4h-1)` variables
and `k(4h-1)+1` cubic-or-lower equations. An `h-1` chart cover reduces one
chart to `k(4h-1)-h+2` variables. Every fixed selector/chart ideal is empty
in characteristic zero and has an integer bad-characteristic endpoint.

The proved exact-ratio tower compiler removes duplication across ambient
orders. If `E_h^prim(m,p)` counts primitive ordered scaling orbits whose
ratio subgroup is exactly `mu_m`, then

```text
O_h^prim(n,p)=sum_(m|n, m>=2h) E_h^prim(m,p).
```

Since `sum_(m|n)m^2=(4n^2-1)/3`, the uniform level estimate

```text
sum_(h=4)^floor(m/2) E_h^prim(m,p)<=(21/2)m^2       (ERT4)
```

for every dyadic `m|n` implies `(OAR2)` strictly. In left-anchored currency
the same target is `sum_h C_h^prim(m,p)/h<=(21/2)m^2`. Each exact level has
an exact near-square implementation: impose the non-full selector, left
anchor `S(1)=a`, terminal remainder `V_r=1`, and exact-level selector
`V_(r-1)!=1`. This is a uniform decomposition and a sufficient target;
`(ERT4)` itself is not proved.

The proved `f3_hge4_nonfull_complement_third_gate` removes the near-full
widths uniformly. If a non-full pair at exact ratio level `m` has width `h`
and complement degree `c=m-2h`, differentiation produces a separator
`H=(d/m)XP'R`; comparing `H-1=PA` and `H+1=QB` forces `h<=c`. Since `m` is
dyadic, every retained pair satisfies `3h<m`. Therefore

```text
E_h^prim(m,p)=0                         whenever 3h>=m,
sum_(h=4)^floor((m-1)/3) E_h^prim(m,p)<=(21/2)m^2   (ERT4')
```

is the reduced exact-level target. The constant and geometric summation are
unchanged; this is an analytic deletion of the upper third, not an estimate
for the retained widths.

The proved `f3_hge4_complement_separator_defect_normal_form` makes the
retained near-third strip explicit. For

```text
H-1=PA,       H+1=QB,       G=B-A,       e=m-3h,
```

one has

```text
deg G=e,       lc(G)=-d^2h/m,
m(P+Q-PQG)=d^2 XP'R.                                (SDN4)
```

Thus the closest possible widths have a linear defect when `m=1 mod 3` and
a quadratic defect when `m=2 mod 3`. This is a necessary differential normal
form; it neither supplies split subgroup roots nor counts the systems.

The proved `f3_hge4_boundary_defect_trace_pin` removes the remaining free
separator coefficients at the two closest widths. If

```text
P=X^h+aX^(h-1)+bX^(h-2)+...,
```

then

```text
e=1: G=d^2(a-(h/m)X),
e=2: G=d^2((b-2a^2)+((m-1)/m)aX-(h/m)X^2).
```

The constant terms satisfy `P(0)+Q(0)=P(0)Q(0)G(0)`. In the dyadic `e=1`
case, scaling uniquely normalizes `P(0)=1`; with `x=Q(0) in mu_m\{1}`,

```text
d=x-1,       a=(1+x)/(x(x-1)^2).                    (BTP5)
```

This reduces the linear defect to one ratio trace parameter and pins every
quadratic defect coefficient. It does not exclude or count either boundary.

The proved `f3_hge4_linear_boundary_orbit_bound` first paid the `e=1`
width. For `m=3h+1`, reciprocal linearization gives

```text
U(y)=y^hP(1/y)=(1-3ay)^(-1/3) mod y^h.
```

After the unique normalization `P(0)=1`, each ratio
`x=Q(0)` determines `a`, `d`, and every coefficient of `P,Q`. The values
`x=1,-1` are impossible, so ordered scaling orbits inject into
`mu_m\{1,-1}` and

```text
E_h^prim(m,p)<=m-2.                                 (LBO2)
```

Every survivor also satisfies the degree-`m-1` endpoint equation

```text
h!x^h(x-1)^(2h)
 =2 product_(r=0)^(h-1)(3r+1)(1+x)^(h-1).           (LBO3)
```

This proves an initial `m-2` debit without computation. The endpoint equation
is not a converse.

The proved `f3_hge4_quadratic_boundary_orbit_bound` similarly gave an initial
payment for the `e=2` width. For `m=3h+2`, choose one of two square-class
normalizations
`P(0)=epsilon in {1,omega}`, put `x=Q(0)/P(0)` and

```text
c_2=b-2a^2=(1+x)/(epsilon^3x(x-1)^2).
```

Then

```text
F_(a,c_2)(y)=(1-3ay-3c_2y^2)^(-1/3)
```

forces `U(y)=y^hP(1/y)=F_(a,c_2)(y) mod y^h`, while the endpoint equations
are

```text
f_h=epsilon(1+x)/2,       f_(h+1)=0.
```

The second equation has degree exactly `h+1` in `a`, so

```text
E_h^prim(m,p)<=2(m-1)(h+1)=2(m^2-1)/3.             (QBO5)
```

These equations are necessary, not sufficient.

The proved `f3_hge4_near_third_belyi_necklace_bound` now supersedes both
boundary counts and handles part of the wider near-third strip. For every
`m=3h+e` with `0<e<h`, put

```text
N(c,e)=(1/c) sum_(r|gcd(c,e)) phi(r) binom(c/r,e/r).
```

Reciprocal linearization produces the tame central-star polynomial cover
`Phi=ZS^3`, `Phi-1=y^(h+e)T`. Its plane trees are binary necklaces, and

```text
E_h^prim(m,p)<=2N(h+e,e).                           (NTB4)
```

In particular, the sharp boundary debits are

```text
e=1: E_h^prim(m,p)<=2,
e=2: E_h^prim(m,p)<=h+2=(m+4)/3.
```

Before the dual-gap exclusion below, the same theorem supplied positive
payments for five additional exact-level cells:

```text
(m,h,e)       orbit debit       total debit at level
(32,9,5)            286                  298
(64,20,4)           892                  894
(128,41,5)        59598                59642
(256,84,4)        53020                53022
(1024,340,4)    3333532              3333534.       (NTB6)
```

The last column adds the sharp `e=1` or `e=2` boundary debit at the same
level. At this stage "paid" meant debited from `(ERT4')`; it was not a zero-cost deletion.
The bounds and arithmetic remain valid, but the next theorem supersedes all
of these positive debits except the first table row.

The proved `f3_hge4_near_third_dual_gap_exclusion` uses the cyclotomic
complement, not only the Belyi passport. With

```text
D=S^2-a^2y^(2h),       DW=1-y^m,       deg W=c=h+e,
```

the inverse `D^(-1)` has no coefficient above degree `c`. Below degree `2h`
this creates a dual gap in `Z^(2/3)`. If `h>=2e+1`, that gap contains `e`
consecutive coefficients; its order-`e` differential recurrence gives

```text
E_h^prim(m,p)=0       whenever h>=2e+1,
E_h^prim(m,p)=0       whenever 7h>=2m+1.           (DGE2)
```

Thus the reduced exact-level target is now

```text
sum_(h=4)^floor(2m/7) E_h^prim(m,p)<=(21/2)m^2.    (ERT4'')
```

This is a zero-cost analytic exclusion. It removes every `e=1,2` boundary
and the necklace cells at `m=64,128,256,1024`; none of those bounds is charged
to the level ledger. The cell `(m,h,e)=(32,9,5)` fails `h>=2e+1` and remains
paid by its necklace bound `286`. Consequently the strongest currently
consumed residual form is

```text
sum_(4<=h<=floor(2m/7), (m,h)!=(32,9)) E_h^prim(m,p)
    <=(21/2)m^2-286       if m=32,
sum_(h=4)^floor(2m/7) E_h^prim(m,p)
    <=(21/2)m^2           otherwise.                (ERT4''')
```

The necklace theorem still applies in the retained strip, but no additional
positive debit is currently consumed. The dual-gap theorem does not reach
the remaining `h<2e+1` near-third strip or any `e>=h` width.

## Posedness and falsifiers

The consumer names all five deletion predicates, but the current repository
has operational analogues for only three. This does not obstruct a RAW-NG
proof. It does mean that a purported counterexample to NG-COUNT must first
give positive definitions and an exact implementation of the U2-boundary and
DLI/skew deletions. An unstripped aggregate above `14n^3` is not by itself a
falsifier.

A valid falsifier is a complete official row or a proved transported slice
whose correctly stripped F-4-minimal norm-gate aggregate is greater than
`14n^3`. NG-ZERO is not claimed.

## Nonclaims

- Empirical zero on the banked cells is not a uniform theorem.
- No constant width cap is assumed; the proved exact-level cap is
  `floor(2m/7)`.
- The first-moment vacancy curve is evidence only.
- The primitive shift-pair estimate `(PSA3)` is not proved here.
- The primitive orbit aggregate `(OAR2)` is not proved here.
- The equivalent anchored near-square aggregate `(NSU4)` is not proved here.
- The odd signed-moment swap-fiber count is not proved here.
- The equivalent half-order perfect-square support count is not proved here.
- The fixed-cell integer certificates and their uniform summation are not
  proved here.
- No certificate family or count for the non-full selector schemes is proved.
- No exact-ratio level estimate `(ERT4)` is proved.
- No reduced exact-ratio level estimate `(ERT4')` is proved.
- No dual-gap-reduced exact-ratio estimate `(ERT4'')` or `(ERT4''')` is
  proved.
- The separator-defect normal form does not count its split solutions.
- The boundary trace pin alone does not exclude its linear or quadratic
  systems.
- The dual-gap exclusion makes no claim for `h<2e+1` or `e>=h`; the necklace
  payment does not settle that retained region.
- Reopening F-4 minimality changes the counted object and requires DAG
  surgery.
