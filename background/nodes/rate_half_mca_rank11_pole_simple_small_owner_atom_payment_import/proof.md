# Proof

Let

```text
P={x in D:Q(x)=0},       rho=|P|<=deg Q<=67472.
```

Pole-simplicity says each point of `P` occurs in at most one selected
support. Hence at most `rho` records have supports meeting `P`. Remove those
records and puncture `P` from the domain. Put `n_0=n-rho`. Every retained
support still has size `m`, and `Q` is nonzero on the punctured domain.

For a retained support, the atom equation and support agreement give

```text
(r_0-A/Q)+gamma_i(r_1-B/Q)=0
```

on that support. Outside the owner set `G`, this nonzero affine equation has
at most one slope solution. This is exactly upstream exclusive
rational-owner localization.

If `g<m`, each retained support uses at least `m-g` exclusive coordinates
outside `G`, so

```text
|I_nonpole|<=floor((n_0-g)/(m-g))<=n_0-m+1.
```

Restoring at most `rho` pole-touching records gives

```text
|I|<=rho+n_0-m+1=n-m+1=981105.
```

Now assume `m<=g<=2m-K`. At most `n_0-g` retained supports meet the
complement of `G`. The supports contained in `G` form a support-wise MCA-bad
instance for the punctured Reed--Solomon code `RS[F,G,K]` at agreement `m`.
Since

```text
2(g-m)<=g-K,
```

the half-distance pincer used in upstream `cor:small-owner` bounds those
contained slopes by `g`. Therefore

```text
|I|<=rho+(n_0-g)+g=rho+n_0=n=2097152.
```

The strict contrapositive gives `g>=2m-K+1`. Substituting the official values
gives

```text
2*1116048-1048576+1=1183521.
```

QED.
