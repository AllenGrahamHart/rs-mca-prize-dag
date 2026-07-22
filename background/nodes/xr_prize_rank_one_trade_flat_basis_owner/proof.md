# Proof

Write the active rows of the rank-one trade as

```text
lambda_i=alpha_i lambda,
```

and let `S=supp(lambda)`. Every active block contains `S`. Restrict the
selected-zero equation

```text
b+gamma_i q+w_i=0,       w_i in W,                    (1)
```

to `S` for two distinct active slopes. In the quotient `F^S/(W|S)`,

```text
[b]+gamma_i[q]=0,       [b]+gamma_l[q]=0.
```

Subtracting gives `[q]=0`, then `[b]=0`. This proves `(FO1)`.

Suppose first that `rk_W(S)=a`. Choose the lexicographically first basis
`T subset S`. Let `I_Tb,I_Tq` be the unique members of `W` matching `b,q` on
`T`. By `(FO1)`, some members of `W` match each received direction on all of
`S`; uniqueness on the basis says they are exactly the two interpolants.
Therefore

```text
a_T(x)=d_T(x)=0       for every x in S\T.             (2)
```

These are persistent coordinates of the affine basis pencil
`a_T+gamma d_T`. Every active block contains `T`, so at least `ell` selected
slopes use that basis.

Let `p_T` be the total number of persistent coordinates outside `T`. For a
selected slope whose block contains `T`, every one of its `m-a=h+u+v`
outside-basis zeros is either persistent or is a zero of a nonzero affine
coordinate function. Nonpersistent zero sets are disjoint across slopes.
Thus

```text
ell(m-a-p_T)<=N-a-p_T.                                (3)
```

Because at least two active slopes contain `T`, their intersection contains
`T` and all persistent coordinates. The pair cap gives

```text
p_T<=kappa-a=u+v.                                     (4)
```

The ratio in `(3)` is increasing in `p_T`, since

```text
(N-a-p)/(m-a-p)=1+(R-h-v)/(h+u+v-p).
```

Using `(4)` gives

```text
ell<=floor((N-a-(u+v))/(m-a-(u+v)))
    =floor((R-v)/h),
```

which is `(FO2)`.

Now suppose `j=rk_W(S)<a`. The closure `F=cl_W(S)` is a proper rank-`j`
flat. The flat-nullity theorem gives `|F|<=j+u`, proving `(FO3)`. The support
of a nonzero dual vector is dependent, so `|S|>=j+1`. Since `S subset F`,
`j+1<=j+u`, and hence `u>=1`.

Closure and the first-basis rule are deterministic, so the ownership is
canonical. If `u=0`, `(FO3)` would give `|F|<=j` while the dependent support
inside it has at least `j+1` points; that branch is empty. QED.
