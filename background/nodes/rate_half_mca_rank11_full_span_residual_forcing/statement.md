# Rank-eleven full-span residual forcing

- **status:** PROVED
- **row:** KoalaBear MCA, post-near affine error rank eleven
- **source interface:** anchored row-space partition of upstream PR `#1173`

Select cutoff `tau=1679` and rich-flat threshold `h=38384`. Let `C'` be the
post-gauge correction space, with `dim(C')<=10`, and let `V_nt` be the span of
all represented nontransverse rank-one/rank-two row spaces. Then every unsafe
line satisfies

```text
dim(C')=dim(V_nt)=10.                                     (FS1)
```

Indeed, if `dim(V_nt)<=9`, all nontransverse pair types lie in one two-fold
affine correction container of dimension at most nine. The exact transverse
envelope is `209812758437679617`, and ordinary affine-span plus sub-square
interleaving charges the complete nontransverse union by

```text
R_9=(n-A) floor(C(n-K+9,9)/C(A-K+9,9))
   =65157026870188671.
```

The total is

```text
274969785307868288 <= B*=274980728111395087,
```

with slack `10942803526799`. Since `V_nt<=C'` and `dim(C')<=10`, unsafety
forces `(FS1)`.

Every unsafe survivor also has at least

```text
65167969673715471 nontransverse slopes,
262093370 represented row spaces,
16384884 distinct promoted dimension-two/three rich containers,
38385 common actual zero coordinates per container.
```

The adjacent threshold `h=38385` exceeds budget by `2062328934603`. No
dimension-ten version of this one-container formula pays: its global best is
`tau=872,h=0`, still over budget by `773076621594690156`.

## Nonclaim

Full collective span is not equidistribution, general position, or a
first-match owner. This theorem does not pay rank eleven; it isolates the
unique ambient-rank case that any unsafe survivor must realize.
