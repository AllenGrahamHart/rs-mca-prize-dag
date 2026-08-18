# Proof

For every residual class counted at `x_1`, extend its selected `11217` roots
to a fixed `37736`-coordinate subset of its full residual zero set, retaining
`x_1`. Double count the remaining `37735` coordinates with class slope mass
as weight. The ambient anchor-good universe has size at most `1116048`, so
some distinct `x_2` is shared by classes of total mass at least

```text
M_2=ceil(37735 M_1/1116047)=10266384562185.
```

Within this subfamily, double count the `37734` selected roots other than
`x_1,x_2`. Some distinct `x_3` is shared by mass at least

```text
M_3=ceil(37734 M_2/1116046)=347110921118.
```

Every residual space in the final subfamily lies in

```text
B_T=ker(ev_{x_1},ev_{x_2},ev_{x_3}:B -> F^3).
```

Suppose the displayed evaluation map had rank three. Then `dim B_T=2`, and
all corresponding correction pairs would lie in `P B_T`, of dimension at
most four. The chronology-safe affine-subspace payment bounds their complete
first-owned slope contribution by

```text
R_4=63397365764.
```

But `M_3=347110921118>R_4`, a contradiction. Hence the evaluation rank is at
most two, proving `(TR2)`. QED.
