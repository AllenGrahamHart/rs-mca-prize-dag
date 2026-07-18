# Exact rate-half ordinary-list crossing at budgets one and two

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`

Let

```text
C=RS[F,D,k],       n=|D|=4d,       k=2d,
D=gamma H,         |H|=n,
L_1(a)=max_u #{c in C:agr(c,u)>=a}.
```

For either integer budget `B in {1,2}`, the exact adjacent ordinary-list
crossing is

```text
L_1(3n/4)<=B<L_1(3n/4-1).                         (LB12)
```

Consequently, on every official rate-half row satisfying

```text
B*=floor(|F|/2^128) in {1,2},
```

the certified map is

```text
a_L(C)=3n/4,       delta_L(C)=1-a_L(C)/n=1/4.      (LB13)
```

The unsafe witnesses are explicit. The `B=1` witness works for any set of
`n` distinct evaluation points. For `B=2`, choose a generator `zeta` of `H`,
put `i=zeta^d`, and partition `D` into the four fibers of
`y=(X/gamma)^d`. A three-codeword construction on these fibers attains the
predecessor.

The theorem makes no assertion for `B>=3` and no MCA/CA assertion.
