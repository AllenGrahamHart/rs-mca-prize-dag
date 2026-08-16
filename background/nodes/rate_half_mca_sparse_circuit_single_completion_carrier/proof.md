# Proof

Independence of the `c-1` evaluation functionals in `A` gives

```text
dim W_A=10-(c-1)=11-c.
```

By definition, a completion point `x` makes `A union {x}` dependent. Thus
the evaluation functional at `x` lies in the span of those at `A`. Every
polynomial in `W_A` vanishes on `A`, so it also vanishes at every such `x`.
Hence `W_A` vanishes on `D_A=A union X_A`.

Completion points are domain points outside the deletion, and the exact
maximum counts distinct points. Therefore `A` and `X_A` are disjoint and

```text
|D_A|=(c-1)+M_c=M_c+c-1.
```

The pair is fixed once the attaining deletion is chosen, so it satisfies the
fixed-before-target quantifier of the collision theorems. QED.
