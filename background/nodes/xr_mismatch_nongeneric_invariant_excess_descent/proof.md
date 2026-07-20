# Proof

The update subtracts the same `d_j` from agreement and dimension, so

```text
A_(j+1)-K_(j+1)=A_j-K_j=h.
```

Because the next instance is live, `K_(j+1)>=1` and hence
`A_(j+1)=K_(j+1)+h>=h+1`. Independently, the next domain is the discrepancy
set of a pair jointly explained on at least `A_j` coordinates, so

```text
N_(j+1)<=N_j-A_j<=N_j-(h+1).
```

After `L` transitions,

```text
N_L<=n-L(h+1).
```

The final live instance has `N_L>=A_L>=h+1`. Therefore

```text
L(h+1)<=n-(h+1),
L<=floor(n/(h+1))-1.
```

For the clean candidates, `h=n/256+1` at rates `1/4,1/8` and
`h=n/512+1` at rate `1/16`. Substitution gives the six printed integer caps.
No field-size hypothesis enters this potential argument.
