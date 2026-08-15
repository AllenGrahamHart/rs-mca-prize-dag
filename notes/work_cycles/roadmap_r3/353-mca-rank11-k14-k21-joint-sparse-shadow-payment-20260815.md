# Cycle 353: MCA rank-11 K'=14..21 joint sparse-shadow payment (2026-08-15)

Cycle 352 closed `K'=13` with a codimension-three completion dichotomy.
At `K'=14`, the direct four-completion generalization is valid, but adding
its complete recordwise sparse cap independently to the rank-nine shadow
capacity fails.  The missing accounting fact is that sparse circuits already
consume the same rank-nine marks.

## Cycle pins

```text
our start:       8fa0f03b2
canonical prize: 6ac775504a
upstream main:   93fba1be3f
open upstream:   #1170 at 8cf7c8f after the K'=13 export
```

## Dimension-parametric completion theorem

Let `V<=F[X]_<K'` have dimension ten and put `q=K'-10`.  For a
support-`c` circuit, delete one point to obtain an independent
`(c-1)`-set `A`.  The space

```text
H_A={f in V:f|_A=0}
```

has dimension `11-c`.  Generalized MDS permits at most `q` circuit
completions of `A`.

- If some `A` has `q` completions, their private coordinates make the
  labels a basis of the quotient.  Every support-at-most-five circuit then
  lies in one carrier of size at most `q+4`.
- Otherwise every `A` has at most `q-1` completions.  A rank-ten eleven-set
  cannot contain two labels, and deletion counting gives

```text
floor(C(m,c-1)/c
      * max_(0<=b<=q-1) b C(m-c+1-b,11-c)).
```

On `K'=14..21`, the maximum is at `b=q-1`.  Independent `GF(17)` models
realize the four-completion carrier and three-completion branches at
`K'=14`.

## Joint sparse/high shadow ledger

A support-`c` circuit creates exactly

```text
q_c=55-C(11-c,2)
```

rank-nine shadows.  The values for `c=2,3,4,5` are `19,27,34,40`, while
every `c>=6` circuit creates at least 45.  If `G` is the global rank-nine
mark capacity and `L_c` is a recordwise sparse cap vector, then

```text
I_full<=floor((G+R_actual sum_(c=2)^5(45-q_c)L_c)/45).
```

For alternative structural branches, maximize the weighted premium
recordwise.  This pays sparse circuits only the missing premiums
`26,18,11,5`; their ordinary rank-nine shadows remain charged inside `G`.

## Eight-row payment

For each `K'=14..21`, the payment retains:

1. every nonzero canonical-basis kernel corank;
2. every common-core offset `9<=j<K'`;
3. both structured and unstructured completion vectors; and
4. one shared rank-nine mark budget.

The exact demand-capacity gaps are

```text
K'=14: 21650768172043394032492459946400263590275020562192971022865376
K'=15: 18588028475285812265606143363906671348737995144736255147834120
K'=16: 15524989535492821727324938882048706164611583704587475891361669
K'=17: 12461651333490539307570308245171118440833885273861127661424680
K'=18:  9398013850103444858371174848818672822082629043827750046751608
K'=19:  6334077066154944217959550399858581606171131782792291719264278
K'=20:  3269840962466993657882795068981405767940223879562014346498774
K'=21:   205305519860193617784849691734671763401656917434567909452790
```

All record coefficients and unfloored endpoint crosses are positive, so the
contradictions persist above the residual-record floor.

## Exact method wall

The identical payment first fails at `K'=22`:

```text
capacity = 905885518366475292751564400874300832826807604203127204847344067
demand   = 903025989085629081334365478664955214394150391409598064684975031
excess   =   2859529280846211417198922209345618432657212793529140162369036
```

This is a numerical wall of the present ledger, not a counterexample to the
completion theorem.

```text
result:                PROVED K'=14..21 component-row closure
newly closed rows:     14..21
closed prefix:         10..21
remaining rank nine:  22..15528
new nodes:             3 PROVED
new premise:           none
compute:               exact local arithmetic and one small GF(17) audit
next route action:     recover the explicit K'=22 deficit by sharpening
                       sparse premiums, shadow weights, or kernel coupling
```
