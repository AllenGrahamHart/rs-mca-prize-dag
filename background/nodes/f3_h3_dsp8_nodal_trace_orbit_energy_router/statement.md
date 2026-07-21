# DSP8 nodal trace-orbit energy router

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **dependencies:** `f3_h3_dsp8_nodal_trace_parameter_router`,
  `f3_h3_dsp8_nodal_cube_preimage_envelope`

For a singular trace `sigma=3c`, let `P_c` be the ordered curve-point
presentations

```text
(r,u,v),       ruv=1,       r+u+v=3c,
```

whose three roots are internally signed-distinct. Put `N_c=|P_c|` and

```text
N=sum_(c^3=1)N_c,       E_tr=sum_(c^3=1)N_c(N_c-6).       (NTE1)
```

Every underlying unordered triple has exactly six presentations. A retained
DSP8 pair is signed-disjoint, so its two presentations cannot come from the
same triple. Consequently

```text
10G_sing^0+17G_sing^A
  <(867/16)n^(2/3) E_tr.                                  (NTE2)
```

This replaces the class-blind square `sum_c N_c^2` by the exact cross-orbit
trace energy `E_tr`. Further signed collisions can only lower the count.

When `p=1 (mod 3)`, let `K={x:x^3 in H}`, choose a cubic character `chi` of
`K/H`, and write the nodal parameter of a point as `theta`. Define

```text
S=sum_(eligible theta) chi(theta(1+theta)).                (NTE3)
```

Then

```text
sum_c N_c^2=(N^2+2|S|^2)/3,
E_tr=(N^2+2|S|^2)/3-6N,                                  (NTE4)
N<(51/16)(3n)^(2/3).                                      (NTE5)
```

In particular, either of the following is a sufficient nodal payment:

```text
E_tr <=(51066/1445)n^(4/3),                               (NTE6)

|S|<=4N/5.                                                (NTE7)
```

There is also a distribution-free sparse gate:

```text
N<=(59/10)n^(2/3).                                        (NTE6a)
```

Indeed, `(NTE6a)` implies `(NTE6)`. Since `(NTE5)` has coefficient below
`106131/16000=6.6331875`, cubic trace balance is relevant only in the narrow
high-point interval

```text
(59/10)n^(2/3)<N<(106131/16000)n^(2/3).                   (NTE6b)
```

Under `(NTE7)`, the left side of `(NTE2)` is strictly below

```text
(185481515817/102400000)n^2 <1812n^2,                     (NTE8)
```

leaving more than `103n^2` of the uniform primitive allowance
`(76599/40)n^2` for smooth traces.

This node proves the orbit subtraction, Fourier identity, and sparse gate. It
does not prove `(NTE6)` outside `(NTE6a)`, prove `(NTE7)`, bound the smooth
traces, or close DSP8.
