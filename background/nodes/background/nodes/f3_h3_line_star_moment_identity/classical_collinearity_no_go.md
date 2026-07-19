# Classical collinearity direct-embedding fence

Write the six subgroup variables of the non-swap incidence as

```text
x =1-a,          x'=1-lambda*a,
y =1-b,          y'=1-b/lambda,
z =1-c,          w =1-a*b*c.
```

The classical shifted-subgroup collinear-triple count uses one equation

```text
(u1-v1)(u2-w2)=(u1-w1)(u2-v2).
```

The exact symbolic search in
`experiments/prize_resolution/h3_collinearity_embedding_search.py` tested all
`6!=720` assignments of `(x,x',y,y',z,w)` to
`(u1,v1,w1,u2,v2,w2)`. Over the rational function field in independent
`a,b,c,lambda`, no assignment made the collinearity determinant vanish
identically.

Modal app `ap-Za2G7lUzGrsf5V3XDVHy2B` returned

```text
H3_COLLINEARITY_EMBEDDING_SEARCH assignments=720 hits=0
MODAL_RUN exit=0 peak_rss=56MB
```

Therefore the Macourt--Shkredov--Shparlinski classical collinear-triple bound
cannot be applied to `S_ns` by merely relabelling its six subgroup variables.
A rational incidence map or a new directed correlation estimate could still
work; this is a complete fence only for direct coordinate permutations.
