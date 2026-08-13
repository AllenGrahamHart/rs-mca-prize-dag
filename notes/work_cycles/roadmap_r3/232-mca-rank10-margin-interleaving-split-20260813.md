# Cycle 232: MCA rank-10 margin/interleaving split (2026-08-13)

The support-local router left KoalaBear error rank ten with a direction-
exception-12 terminal.  Treating that terminal globally was too weak: it
asserted only that one low-margin support exists.  Instead split the whole
rank-ten family at a freely chosen margin threshold `T`.

The high-margin subfamily is paid by the proved support-local
transversality theorem.  For a low-margin slope, choose a direction codeword
with at most `T-1` exceptions.  The explanation and that direction form a
two-fold common-support pair at agreement `A=m-T+1`.  The ordinary
affine-span cap is sub-square-root in the official field, so the proved
interleaving collapse bounds the number of such pairs.  For each fixed
pair, pair noncontainment supplies an exception coordinate and the support
equation recovers the slope, giving multiplicity at most `n-A`.

Thus, for explanation rank `s`,

```text
|Z| <= 2w + max_(0<=r<=s) ST_r(T)
          + (n-m+T-1) floor(C(n-K+s,s)/C(w-T+1+s,s)).
```

At KoalaBear error rank ten, `s=9`.  The exact optimum of this formula is
`T=667`:

```text
high cap:  5143522968716559
low cap:  56727790457914040
near:                 134944
total:      61871313426765543
budget:    274980728111395087
slack:     213109414684629544
```

The first paying threshold is already `T=16`, giving a robustness check.
The same formula has minimum `1040506078215897711` at explanation rank ten,
so it does not pay error rank eleven.

```text
start:                   18a009bbf
canonical prize:         c8d48cd4b (no newer Fable commit)
upstream frontier:       #1163-#1166; #1166 @ af0e7c63b
result:                  NARROWED; one PROVED rank-10 payment
DAG delta:               +1 PROVED node, +6 edges
critical status delta:   none; replacement target remains TARGET
direct Koala frontier:   error ranks <=10 paid; rank >=11 remains
delta-star movement:     none
compute:                 exact constant-memory scans under RAMguard;
                         no Modal
next route action:       seek new structure for error rank >=11 and continue
                         the M31 full-lift boundary-layer route
export target:           coordinate as a proved successor packet on #1166
```
