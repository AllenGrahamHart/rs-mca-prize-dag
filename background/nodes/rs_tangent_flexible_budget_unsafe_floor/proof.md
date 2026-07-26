# Proof

Choose `E subset D` with `|E|=e=n-a`. Start from any two codewords and subtract
them, so it is enough to construct error words. Let `g` be one on `E` and zero
off `E`. Let `f` be zero off `E` and injective on `E`; this is possible because
`e<=q`.

For each `x in E`, set `z_x=-f(x)` and

```text
S_x=(D\E) union {x}.
```

The word `f+z_x g` vanishes on `S_x`, so the zero codeword explains it there.
Moreover

```text
|S_x|=n-e+1=a+1>a.
```

Thus condition (i) of support-wise MCA badness holds at radius
`delta=1-a/n`.

No degree-`<k` polynomial can explain `g` on `S_x`. Such a polynomial would
vanish on the `a>k` points `D\E`, hence would be zero, but it would have to
equal `g(x)=1`. Therefore condition (ii) holds. The values `z_x` are distinct
because `f` is injective on `E`, giving at least `e` bad slopes on one line.

Finally, `e>B*=floor(q/2^t)` is equivalent to `e>=B*+1`, so

```text
e/q > (q/2^t)/q = 2^-t.
```

This is the tangent-floor argument of upstream `prop:floor`, independently
reconstructed at integer agreement.
