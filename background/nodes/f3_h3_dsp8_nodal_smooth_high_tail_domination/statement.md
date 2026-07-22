# DSP8 nodal/smooth high-tail domination

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **dependencies:** `f3_h3_dsp8_smooth_trace_substar_router`,
  `f3_h3_dsp8_disjoint_six_multiplicity_gate`

Fix a retained product target `t` with `P(t)>=25`. Let `m` be the number of
its unordered squared-norm-at-most-three representations, let `a in {0,1}`
record whether the fiber contains an antipodal representation, and put
`g=m-a`. Split its signed-disjoint generic--generic distance-six edges into
nodal and smooth trace classes:

```text
D_6(t)=D_nod(t)+D_sm(t).
```

Define

```text
F_0(m)=ceil(m(m-4)/2)-2m-6,
F_A(m)=ceil(m(m-2)/2)-4(m-1)-8,
nu_0(m)=floor(3m/2),
nu_A(m)=floor(3(m-1)/2).                            (NSD1)
```

Then the antipodal-free class obeys

```text
D_nod(t)<=nu_0(m),
D_sm(t)>=max(0,F_0(m)-nu_0(m)),                     (NSD2)
```

and the antipodal class obeys

```text
D_nod(t)<=nu_A(m),
D_sm(t)>=max(0,F_A(m)-nu_A(m)).                     (NSD3)
```

In particular,

```text
D_nod(t)<=D_sm(t)   if a=0 and m>=15,
D_nod(t)<=D_sm(t)   if a=1 and m>=16.               (NSD4)
```

The rich-fiber ladder therefore gives the product-multiplicity version

```text
D_6(t)<=2D_sm(t)   if a=0 and P(t)>=33,
D_6(t)<=2D_sm(t)   if a=1 and P(t)>=35.             (NSD5)
```

For the quotient-weighted moments, put

```text
L_0=sum_(a=0,25<=P(t)<=32) D_6(t)R(t),
L_A=sum_(a=1,25<=P(t)<=34) D_6(t)R(t),
S_0=sum_(a=0,P(t)>=33) D_sm(t)R(t),
S_A=sum_(a=1,P(t)>=35) D_sm(t)R(t).                 (NSD6)
```

Then

```text
D_6,25^0<=L_0+2S_0,
D_6,25^A<=L_A+2S_A.                                (NSD7)
```

Thus the nodal trace locus is not an independent high-tail payment: above
the printed thresholds it can be charged one-for-one to smooth disjoint
edges at the same target and with the same quotient weight. This theorem
does not estimate the smooth moments or either bounded multiplicity band,
and it does not close DSP8.
