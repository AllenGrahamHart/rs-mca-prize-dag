# Rank-eleven low-span residual payment

- **status:** PROVED
- **row:** KoalaBear MCA, post-near affine error rank eleven
- **source interface:** the anchored row-space partition of upstream PR `#1173`

Use cutoff `tau=1549`, rich-flat threshold `h=42451`, and write

```text
A=m-tau=1114499,  c=2A-n=131846,  n-A=982653.
```

Partition the selected low-margin pair types relative to one actual anchor as
in PR `#1173`. Let `U_e` be the rank-one or rank-two row space of the
coefficient-matrix difference from the anchor. Call `U_e` nontransverse when
a proper flat of `U_e^perp` contains at least `h+1=42452` labelled
anchor-good evaluation columns, and put

```text
V_nt = sum of all represented nontransverse U_e.
```

Then every unsafe line satisfies

```text
dim(V_nt) >= 7.                                             (LS1)
```

More quantitatively, before merging there are at least `134181` represented
nontransverse row spaces. After canonical promotion and merging as in the
rich-flat residual compiler, there are at least `8406` distinct dimension-two
or dimension-three rich containers, each vanishing on at least `42452`
actual coordinates.

Indeed, if `dim(V_nt)<=6`, all nontransverse pair types lie in one two-fold
affine correction container of direction dimension at most six. The ordinary
affine-span list theorem and sub-square interleaving collapse cap the complete
nontransverse contribution by

```text
R_6=(n-A) floor(C(n-K+6,6)/C(A-K+6,6))
   =15909196289385.
```

Adding `R_6` to the complete transverse envelope gives

```text
274963410460662890 <= B*=274980728111395087,
```

with slack `17317650732197`. Thus an unsafe line cannot have
`dim(V_nt)<=6`, proving `(LS1)`.

The adjacent threshold `h=42452` makes this same declared envelope exceed
`B*` by `1804196591101`. This is an exact adjacent failure of the payment
formula, not an assertion that an unsafe line exists there.

## Nonclaims

This node does not pay rank eleven: it replaces the rich-flat terminal by the
strictly narrower rank-at-least-seven collective-span terminal. It does not
assert that the promoted containers share one locator, factor, chronology
owner, or first-match cell.
