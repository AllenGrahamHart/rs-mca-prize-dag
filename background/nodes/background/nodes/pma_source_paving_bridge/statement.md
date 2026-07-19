# PMA source-to-paving bridge

- **status:** PROVED
- **consumer:** `pma_wide_residual`
- **upstream interface:** PR `#764`, all-pair augmented paving-basis charge

## Statement

Fix one maximal-sunflower PMA source instance, including its distinct nonzero
petal scalars. Let `T` be the disjoint union of the petals, `L=|T|`, let
`R_0` be the retained background agreement set, `r=|R_0|`, and let `d` be the
missed-core defect. The maximality convention gives `0<=r<=sigma`. The
auxiliary list consists of polynomials `W` with

```text
deg W <= d,
W|_(R_0)=0,
a(W):=#{x in T:W(x)=U_D(x)} >= d+1+sigma-r.
```

If `r>d`, this list is empty. If `r<=d`, put

```text
kappa=d-r+1,
L_R(X)=product_(z in R_0)(X-z),
V(x)=U_D(x)/L_R(x)  on T.
```

Then `W=L_R Q` gives a bijection with degree-`<kappa` polynomials satisfying

```text
a(Q):=#{x in T:Q(x)=V(x)} >= kappa+sigma.
```

For every such list,

```text
sum_Q binom(a(Q),kappa) <= binom(L,kappa),

#list <= floor(binom(L,kappa)/binom(kappa+sigma,kappa)).       (PMA-PB)
```

If the list is nonempty, hence `kappa+sigma<=L`, and `|F|>L`, adjoining any
locator `xi notin T` realizes the same objects as distinct retained pairs in
the weighted-RS chart of upstream PR `#764`:

```text
N_chart=L+1,
R_chart=L+1-kappa,
t=L-kappa-sigma,
gamma_Q=Q(xi).
```

The upstream transversality premise is automatic. Formula `(PMA-PB)` is the
sharper pinned-basis specialization obtained by charging only augmented bases
that contain `xi`.

## Scope

This theorem counts every PMA auxiliary polynomial, including repeated
`gamma_Q` values. It neither proves that `(PMA-PB)` is polynomial in the wide
regime nor identifies quotient owners. Those are precisely the remaining
consumer obligations.
