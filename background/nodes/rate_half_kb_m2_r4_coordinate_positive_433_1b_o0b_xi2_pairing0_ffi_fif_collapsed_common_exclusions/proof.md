# Proof

The infinity-leading-collapse node proves that either chart forces

```text
k2 = k5 = 0.
```

These equations involve only the common variables `t,r,c,b`. Start with the
checked 21-element Gröbner basis of the common `epsilon=(-1,-1)` ideal,
which already represents the route-guard and rank-cofactor saturation of the
three common equations. Adjoining `k2,k5` and recomputing gives a
43-element dimension-zero basis of vector-space degree 65.

Because adjoining new equations can create boundary points in the closure,
all 16 printed route guards are saturated again in their printed order.
The exact transcript is

```text
guard 0: dim 0, size 34
guard 1: dim 0, size 34
guard 2: dim 0, size 34
guard 3: dim 0, size 32
guard 4: dim 0, size 22
guard 5: dim -1, size 1
```

Guard index 5 is `b+1`. Every later route-guard stage and the final
six-cofactor ideal saturation remain the unit ideal. Thus no admissible
common base point satisfies `k2=k5=0`.

Every admissible solution in either `FFI` or `FIF` would project to such
a base point, a contradiction. QED.
