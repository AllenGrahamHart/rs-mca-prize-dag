# O0b split cells 3 and 6 first basis-fed orbit exclusion

- **status:** PROVED
- **canonical case:** `(3,S0,-1,-1,-1,0,0)` in
  `(cell,lane,sigma_o,epsilon_1,epsilon_2,xi,pairing)` order

Adjoin this case's five outside equations to the proved 21-polynomial `--`
common basis. The initial ideal has dimension 3 and basis size 108. After
saturating `b,c,r,t,b-1`, the ideal remains nonunit; saturation by the next
guard `b+1` gives the unit ideal. Thus every algebraic solution has `b=-1`,
which violates the target-distinctness guard.

The two commuting quotient actions give exactly the four raw cases

```text
(3,S0,-1,-1,-1,0,0)   (3,S0,-1,-1,-1,0,4)
(6,S0,-1,-1, 1,1,7)   (6,S0,-1,-1, 1,1,11).
```

All four are empty on the guarded branch.

## Falsifier

A nonunit final ideal, an allowed point with `b=-1`, failed source custody,
or a quotient orbit other than the four printed tuples.
