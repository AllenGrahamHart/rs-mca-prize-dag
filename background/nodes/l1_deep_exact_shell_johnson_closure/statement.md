# L1 deep exact-shell Johnson closure

- **status:** PROVED
- **role:** pay every exact shell above the balanced-lattice band
- **consumer:** `l1_mixed_petal_amplification`

## Johnson list bound

Let `H` be any `n`-point evaluation set and let `RS[F,H,k]` have `k<n`.
For any received word `U` and agreement threshold `m` satisfying

```text
m^2>n(k-1),                                           (DJ1)
```

the number `L_>=m(U)` of degree-below-`k` codewords agreeing with `U` on at
least `m` coordinates satisfies

```text
L_>=m(U)
 <= floor(n(m-k+1)/(m^2-n(k-1))).                    (DJ2)
```

## Complete deep-tail payment

Put

```text
m_J=floor((n+k-1)/2)+1.                              (DJ3)
```

Then `2m_J>n+k-1`, hence `(DJ1)` holds, and

```text
L_>=m_J(U)<=n^2.                                     (DJ4)
```

Every exact shell with `2m>n+k-1` is contained in this one list.  Therefore
the **total number of codewords across all deep exact shells** is at most
`n^2`; there is no extra factor for the number of shell levels.

For the full prize box, `k<=2^40` and rate at least `1/16` give
`n<=2^44`, so this universal contribution is at most `2^88`, independently
of the field size.  This is a polynomial L1 payment, not a claim that the
coarse bound fits every finite adjacent-row budget by itself.

## Scope

The theorem is a coarse polynomial payment, not the exact finite Johnson
anchor for a particular budget.  It does not count the complementary band
`2m<=n+k-1`, where the balanced split-pencil census remains open.
