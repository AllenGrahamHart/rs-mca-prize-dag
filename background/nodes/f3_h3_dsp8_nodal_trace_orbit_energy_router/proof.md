# Proof

Fix `c^3=1`. Permuting the three coordinates acts on `P_c`. Internal signed
distinctness implies ordinary distinctness, so this action is free. Hence
`P_c` is a disjoint union of six-element orbits, one for each underlying
unordered triple; in particular `6` divides `N_c`.

Two ordered presentations from the same orbit have the same root support.
They therefore cannot form a signed-disjoint DSP8 pair. If `M_c=N_c/6`, the
number of ordered presentation pairs that can remain on trace `3c` is at
most

```text
36M_c(M_c-1)=N_c(N_c-6).                                (1)
```

For every retained target, the proved cube-preimage envelope supplies the
quotient-line estimate

```text
R(t)<(51/16)n^(2/3).                                     (2)
```

The larger class coefficient is `17`. Summing `(1)` and `(2)` over the
singular traces gives

```text
10G_sing^0+17G_sing^A
 <17(51/16)n^(2/3)sum_c N_c(N_c-6),
```

which is `(NTE2)` because `17*51/16=867/16`.

Now assume `p=1 (mod 3)`. The cube-preimage subgroup `K` has order `3n`, and
`K/H` has order three. In the exact nodal parameterization, put

```text
A=theta H,       B=(1+theta)H.
```

The trace class is `cH=BA=theta(1+theta)H`. Thus the character sum in
`(NTE3)` is exactly the Fourier coefficient of the three eligible point
counts. If these counts are `N_0,N_1,N_2` and `omega^3=1`, then

```text
S=N_0+omega N_1+omega^2 N_2,
|S|^2=N_0^2+N_1^2+N_2^2-N_0N_1-N_0N_2-N_1N_2.           (3)
```

Since

```text
N^2=N_0^2+N_1^2+N_2^2+2(N_0N_1+N_0N_2+N_1N_2),
```

equation `(3)` gives `(NTE4)`. The eligible parameters are a subset of the
nonnode parameters in the cube-preimage envelope, so its strict point bound
gives `(NTE5)`. Notice that repeated-root nonnode points are harmless: they
are omitted from `P_c`, and no sixfold-orbit claim is made for them.

Multiplying `(NTE6)` by the coefficient in `(NTE2)` gives

```text
(867/16)(51066/1445)=76599/40,                            (4)
```

so `(NTE6)` is sufficient for the full uniform nodal allowance.

Under `(NTE6a)`, the nonnegative trace energy satisfies

```text
E_tr<=sum_c N_c^2<=N^2
    <=(3481/100)n^(4/3)
    <(51066/1445)n^(4/3),                              (5)
```

where the last comparison is exact because

```text
51066/1445-3481/100=15311/28900>0.
```

This proves the sparse gate. Also

```text
(51/16)3^(2/3)<(51/16)(2081/1000)=106131/16000,
```

using the cube bound from the proved cube-preimage envelope. Together with
`(NTE5)`, this proves `(NTE6b)`.

Finally, `(NTE7)` and `(NTE4)` imply

```text
E_tr <=(N^2+2(4N/5)^2)/3-6N
     <(19/25)N^2.                                        (6)
```

Use `(NTE5)` in `(NTE2)` and `(6)`. Since

```text
3^(1/3)<1443/1000
```

because `1443^3=3004685307>3000000000`, the coefficient is strictly below

```text
17(51/16)^3(19/25)3^(4/3)
 <17(51/16)^3(19/25)(4329/1000)
 =185481515817/102400000
 <1812.                                                  (7)
```

The difference from the live allowance is

```text
76599/40-185481515817/102400000
 =10611924183/102400000>103,
```

proving `(NTE8)` and the stated residual margin. QED.
