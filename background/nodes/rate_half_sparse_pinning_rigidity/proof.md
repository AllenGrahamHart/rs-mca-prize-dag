# Proof

Write `v_gamma=epsilon_1+gamma epsilon_2`. Each active coordinate contributes
at most one solution of `v_gamma(j)=0`, so there are at most `A<=e` tangent
slopes.

Let `(z,S)` be a failing witness, enlarged to the complete agreement locus of
`v_gamma` and `z`. Off `E`, the sparse word is zero, so the off-support weight
of `z` is at most the mismatch budget `r`. If no active coordinate were
matched on `S`, then on `S` the second sparse component would be zero and the
first would equal `z`; both restrictions would extend to codewords `0` and
`z`. The witness would extend mutually, a contradiction. Therefore some
active `j` is matched, and solving

```text
epsilon_1(j)+gamma epsilon_2(j)=z(j)
```

gives `(PR1)`. If the slope is non-tangent, `z` cannot be zero, because a
matched active coordinate would then be a tangent zero.

The nonzero degree-`<k` polynomial `z` vanishes at every off-support point
where its evaluation is zero. Since at most `r` off-support positions carry a
nonzero value and `|D\E|=n-e`, it has at least

```text
n-e-r=k+tau-e=a-e
```

such roots. Choose that many or more as `Z` and divide their distinct linear
factors from `z`. The remaining factor satisfies

```text
deg h<=k-1-|Z|<=k-1-(a-e)=e-tau-1,
```

which is `(PR2)`. If `e<=tau`, the bound is negative, so no nonzero `z`
exists. Every bad slope is then tangent.

For a non-tangent maximal witness, its mismatch set is the disjoint union of
the `A-T` unmatched active coordinates, the `u` unmatched inactive support
coordinates, and the `w_out` nonzero evaluations of `z` off `E`. This proves
the first inequality in `(PR3)`. Also `z` has at least

```text
n-e-w_out >= n-e-r+(A-T)+u
```

roots. Root counting for a nonzero degree-`<k` polynomial yields

```text
k-1>=n-e-r+(A-T)+u,
```

which rearranges to the second inequality in `(PR3)`. The last inequality
drops `u>=0`.

Finally, at rate one half, `m=2^40` and `tau>=1`, so
`r=m-tau<=2^40-1`. If `q>=2^168`, then
`floor(q/2^128)>=2^40`, proving `(PR4)`. QED.
