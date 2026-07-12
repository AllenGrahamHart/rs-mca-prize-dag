# Residual-free top-band petal charts are Johnson-safe

- **status:** PROVED
- **consumer:** `petal_k4_primitive_bound`

Let a sunflower auxiliary chart have petal size `ell>=1`, petal count `m>=2`,
degree bound `d`, no retained residual (`r=0`), and the pinned top-band
condition

```text
d >= ell(m-2).
```

Its petal domain has size `|T|=m ell` and its auxiliary agreement is
`a=ell+d`.  Then

```text
a^2-d|T| >= ell^2 > 0.
```

Consequently the exact Johnson-slice theorem gives

```text
|ImgFib_U^(<=d)(a;T)|
  <= floor(|T|(a-d)/(a^2-d|T|))
  <= m.
```

Thus K4 holds on every residual-free chart in the pinned top band with the
strong exponent `b4=1`.  The sub-Johnson portion of K4 is confined to charts
with a nonempty retained residual (or to a future chart dictionary that does
not satisfy the pinned P1 parameters).
