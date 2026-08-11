# Proof

For `x in W`, the coordinate evaluation map `ev_x:V->F` is a nonzero
linear functional. Its kernel is one-dimensional, so it determines a unique
projective member `g` whose vector `z_g` vanishes at `x`. This proves that
the `F_g` partition `W` and that `supp(z_g)=W\F_g`. If `g_1!=g_2`, their
vectors span `V`; they cannot both vanish at a point of `W`. Therefore

```text
supp(z_(g_1)) union supp(z_(g_2))=W.                  (1)
```

Fix a supported slope `gamma` and `g!=gamma`. The representation vectors
for these distinct slopes have syndromes `y_0+gamma y_1` and
`y_0+g y_1`. Those syndromes form a basis of the original syndrome pencil,
so the vectors form a representation pair after an invertible basis change.
By the definition of the minimum joint support `a`,

```text
a<=|S_gamma union supp(z_g)|.
```

Since `|supp(z_g)|=a-n_g`, inclusion-exclusion gives

```text
|S_gamma intersect supp(z_g)|
 <=|S_gamma|+(a-n_g)-a
 =|S_gamma|-n_g,                                     (2)
```

which is `(TFC2)`.

Apply `(2)` to two distinct members `g_1,g_2`, neither equal to `gamma`.
Using `(1)` and the union bound inside `S_gamma`,

```text
|S_gamma intersect W|
 <=|S_gamma intersect supp(z_(g_1))|
   +|S_gamma intersect supp(z_(g_2))|
 <=2|S_gamma|-n_(g_1)-n_(g_2).                       (3)
```

Subtracting `(3)` from `|S_gamma|` proves the second inequality in `(TFC3)`.

Now suppose `g_1,g_2` are the two type-1 slopes. Type 1 means the correction
vector vanishes, so `S_(g_i)=supp(z_(g_i))`. Since every locator root set
has size at most `rho`,

```text
n_(g_i)=a-|S_(g_i)|>=a-rho=3m.                       (4)
```

Every type-2 `gamma` differs from both type-1 slopes. From `(TFC3)`, `(4)`,
and `|S_gamma|<=rho`,

```text
|S_gamma\W|>=6m-rho=2m+1,                            (5)
```

proving `(TFC4)` without a cleanliness assumption on `S_gamma`.

At `a=7m-1`, the outside root capacity is

```text
C=(N-a)m=(9m+1)m.                                    (6)
```

The two type-1 slopes contribute two, and `(5)` gives

```text
T<=2+floor(C/(2m+1)).                                 (7)
```

Write `m=4u`. Direct division gives

```text
C=144u^2+4u,
(8u+1)(18u-2)=144u^2+2u-2,
C-(8u+1)(18u-2)=2u+2<8u+1.                           (8)
```

Thus `floor(C/(2m+1))=18u-2=9m/2-2`, proving `(TFC5)`.
Its excess over `4m` is exactly `m/2`.

The exact-spend dependency proves that the same capacity ledger closes at

```text
p_req=9m/4+1.                                        (9)
```

The lower bound furnished by `(TFC3)` is
`n_(g_1)+n_(g_2)-|S_gamma|`, whose worst allowed value of
`|S_gamma|` is `rho`. It reaches `(9)` exactly when

```text
n_(g_1)+n_(g_2)>=rho+p_req=25m/4.                    (10)
```

The baseline `(4)` gives only `6m`, so the gap is `m/4`. Finally, if
`d_i=rho-|S_(g_i)|`, then `(4)` is an equality in the refined form
`n_(g_i)=3m+d_i`. Hence `(10)` is equivalent to `d_1+d_2>=m/4`, and the
remaining fibre mass is at most

```text
a-25m/4=3m/4-1.                                      (11)
```

This proves all stated claims. QED.
