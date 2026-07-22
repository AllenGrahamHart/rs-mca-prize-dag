# XR low-core terminal shift-pair fiber bound

- **status:** PROVED
- **consumer:** `xr_lowcore_spread_heart`

Let `mathcal F` be a family of distinct `a`-subsets of an `N`-set, where

```text
a=K+h,       H=h+1,
|S intersect T|<=K-1=a-H       for distinct S,T in mathcal F.       (TS1)
```

For disjoint ordered sets `X,Y` of common size `t`, define the oriented
shift fiber

```text
R_(X,Y)={I subset Omega\(X union Y):
         |I|=a-t, X union I in mathcal F, Y union I in mathcal F},
r_(X,Y)=|R_(X,Y)|.                                                (TS2)
```

Every nonempty nonzero fiber has

```text
H<=t<=N-a.                                                        (TS3)
```

If a fiber contains two residuals, the corresponding two family members
both contain `X`. Hence their intersection contains `t` coordinates, so

```text
r_(X,Y)>=2 implies t<=K-1.                                       (TS3a)
```

In particular, every shift fiber with `t>=K` has multiplicity at most one.

Moreover, `R_(X,Y)` is a constant-weight code of length `N-2t`, weight
`a-t`, and minimum Hamming distance at least `2H`. Consequently,

```text
r_(X,Y)<=floor(4H/(4H-N+2t))       if N-2t<4H,                    (TS4)
r_(X,Y)<=2(N-2t)=8H                if N-2t=4H.                    (TS5)
```

Write `M=|mathcal F|` and use difference energy

```text
E(mathcal F)=#{(S,T,U,V): 1_S-1_T=1_U-1_V}
            =sum_(X,Y) r_(X,Y)^2.                                (TS6)
```

If `E_term` is the contribution from nonzero fibers satisfying
`N-2t<=4H`, then

```text
E_term<=8H M(M-1).                                                (TS7)
```

The stronger wide-shift contribution obeys

```text
E_wide=sum_(t>=K) r_(X,Y)^2<=M(M-1).                              (TS7a)
```

In particular, if `N,H<=n` and `M>8n^3`, then

```text
E_term<M^3/n^2.                                                   (TS8)
```

Thus every P-B counterexample has analytically paid all shift widths at
least `K`, including the entire terminal-width interval at the six official
rows. Any unresolved repeated-difference concentration lies in

```text
H<=t<=K-1.                                                        (TS9)
```

At the six clean-rate roots, the terminal interval is:

| row | `H` | `K` | first terminal `t` | maximum `t=N-a` |
|---|---:|---:|---:|---:|
| RowC `1/4` | 6 | 256 | 500 | 763 |
| RowC `1/8` | 6 | 128 | 500 | 891 |
| RowC `1/16` | 4 | 64 | 504 | 957 |
| prize `1/4` | 8,589,934,594 | 549,755,813,888 | 1,082,331,758,588 | 1,640,677,507,071 |
| prize `1/8` | 8,589,934,594 | 274,877,906,944 | 1,082,331,758,588 | 1,915,555,414,015 |
| prize `1/16` | 4,294,967,298 | 137,438,953,472 | 1,090,921,693,180 | 2,057,289,334,783 |

This theorem does not bound the range `(TS9)` and does not prove the P-B
slope count.

Terminology guard: the fiber in `(TS2)` is a repeated oriented difference of
Boolean support indicators. It contributes to additive fourth energy. It is
not the local primitive locator shift-pair degree called SPI in CAP25 v13.2;
no bound on that local degree is claimed here.

For the P-B application, `mathcal F` is genuinely a family of distinct
supports. If two distinct slopes had the same selected exact-`A` agreement
support, the two selected codewords could be linearly recombined into a
codeword pair jointly explaining `(u,v)` on that support. This contradicts
the globally generic P-B hypothesis.
