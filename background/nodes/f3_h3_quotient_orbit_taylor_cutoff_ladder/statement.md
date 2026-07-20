# H3 quotient-orbit Taylor cutoff ladder

- **status:** PROVED
- **closure:** proof
- **consumers:** `f3_h3_dsp8_correlation_bound`,
  `f3_h3_official_order_template_survivor`
- **dependencies:** `f3_h3_quotient_orbit_taylor_content_support_compiler`,
  `f3_h3_quotient_algebra_fitting_support_compiler`

For every canonical quotient block `q_O` and every `2<=c<n-1`, put

```text
F_c(T,X)=sum_(i=0)^c Pcal_n^[i](T)X^i,
C_O,c(X)=Res_T(q_O(T),F_c(T,X)),                       (TCL1)
```

and let `c_O,c` be the positive odd coefficient content of `C_O,c`. Then

```text
C_O,c!=0,       rad(c_O,c)=rad(s_O,c),                (TCL2)
```

where `s_O,c` is the exact orbitwise cutoff-`c` scalar annihilator. For every
odd prime `p`,

```text
p divides c_O,c
 iff some root t of q_O mod p has P(t)>=c+1.           (TCL3)
```

The prime supports form a descending cutoff ladder. If `2<=a<=b<n-1`, then

```text
rad(c_O,b) divides rad(c_O,a).                         (TCL4)
```

Consequently every cutoff `c<=35` is a complete candidate superset for the
cutoff-35 C36 endpoint. The coordinate-minimal exact pre-screen is `c=2`:
it keeps exactly quotient-supported triple product collisions, excludes the
different-root false positives admitted by the three scalar resultants, and
has

```text
deg_X(C_O,2)<=2 deg(q_O).
```

At `n=8192`, the cutoff-2 campaign has `24,534` independent blocks, maximum
auxiliary degree `8,192`, and total possible auxiliary degree `134,168,580`.
Exact row evaluation then removes genuine multiplicities `3<=P<=35`.

This theorem does not select an optimal cutoff, compare coefficient growth,
identify valuations, compute or factor any content, prove a resource bound,
bound the retained cutoff-35 moment, or close C36'.
