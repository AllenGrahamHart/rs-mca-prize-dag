# Proof

By `petal_retained_zero_effective_degree`, every actual chart image factors
uniquely as

```text
G=L_R Q,    deg Q<=d-r=:d_eff.
```

On a fully touched petal `T_i`, agreement with the chart word says

```text
Q(x)L_R(x)=c_i L_D(x)    for every x in T_i.
```

Since the petals are disjoint from `D` and `R`, this prescribes one fixed
residue class for `Q` modulo the monic petal locator `L_i`.

Let `I` be the touched-petal set. Full-petal listedness gives

```text
|I| ell >= a = ell+d_eff > d_eff.
```

The petal locators are pairwise coprime, so the Chinese remainder theorem
combines the fixed residues for `i in I` into one residue modulo
`prod_(i in I)L_i`, whose degree is `|I|ell>d_eff`. At most one polynomial of
degree at most `d_eff` has that residue. Hence two listed chart images with the
same touched set have the same `Q`, then the same `G`, proving injectivity.

Every touched set has size at least `ceil(a/ell)`, so counting the possible
sets gives the displayed binomial tail. Filtering for aperiodic exact support
can only decrease this count.
