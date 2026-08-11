# Proof

The fixed-core-two branch is empty by the fixed-core pole-slack theorem.

For `s=1`, the same theorem excludes a profile whenever

```text
floor(p/3)+ell+2<e.                                   (1)
```

Since `p<=Delta=rho-1-2e`, every survivor obeys `(A1C2)`. At `ell=0`,

```text
floor(Delta/3)+2<e                                   (2)
```

throughout `e>=m+1`: already at the smallest degree,
`Delta=2m-3` and `floor(Delta/3)+2<m+1`, and the left side decreases while
the right side increases. Hence no core-one sharp profile survives.

For `s=0`, the four-contact theorem excludes `e=m+1,m+2` at every allowed
slack, in particular at `ell=0`. For

```text
m+3<=e<=rho/2-1,
```

the three-contact theorem uses `alpha=2` and `p<=Delta=rho-e`. Its sharp-cap
condition follows from

```text
floor((rho-e)/3)+3<e.                                 (3)
```

At `e=m+3`, the left side is `m+2`; thereafter it is nonincreasing while
`e` increases. For `rho/2<=e<=rho-1`, `alpha=1` and

```text
floor((rho-e)/2)+3<e,                                 (4)
```

which holds at `e=rho/2` for the official `m>3` and only strengthens. At
`e=rho`, `alpha=0`, `p=0`, and `3<rho`. Thus no core-free sharp profile
survives. QED.
