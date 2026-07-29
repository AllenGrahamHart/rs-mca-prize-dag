# E1 profile-(2,10) split-prime ideal router

- **status:** PROVED
- **closure:** local valuation census, residue-degree sieve, and ideal factorization
- **scope:** binding prize rate-`1/8` row, profile `(2,10,S=18)`

Let `alpha` be a profile-`(2,10,S=18)` collision at one fixed row prime `p`
and primitive quotient root `r`, and write

```text
|Norm(alpha)|=p m.
```

Then the exact cofactor list is

```text
{2,4,8,16,32,64,128,256,512,1024,514,1028,1538}.
```

For the ten pure powers of two, the normalized principal ideal is the fixed
row prime `P_r`. For `514=2*257` and `1028=4*257`, one additional prime
`Q_s` above `257` occurs; for `1538=2*769`, one additional prime `Q_s` above
`769` occurs. Both rational primes split completely, so each split cofactor
has `128` possible prime-ideal families.

Within every fixed cofactor and fixed extra prime ideal, all collisions form
at most one 256-vector negacyclic shift/sign orbit. Consequently

```text
T_210(p,r)<=10+3*128=394,
oriented profile-(2,10) vectors <=100864.
```

The corresponding coarse edge charge is at most

```text
61906644187645781406222007093836433195008.
```

This bound does not merge or exclude the `384` split-prime families. Their
occupancy is the remaining profile-specific problem.

