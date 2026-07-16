# Petal reserve rich-fiber reduction

- **status:** PROVED
- **role:** reserve-scale replacement for the collision-free PMA attack
- **consumer:** `petal_mixed_amplification`, `imgfib`

## Statement

Let a maximal sunflower source have core size `k-1`, petal size

```text
ell=sigma+1,
```

`M` full petals, and background size `b<ell`. Let `P` be a non-planted listed
codeword with at least `k+sigma=k+ell-1` agreements. Write `D` for its exact
missed-core set, `d=|D|`, and use the core-defect form

```text
P=Q+L_(C\D)W,       R=W/L_D,       deg W<=d.
```

Then `W` is nonzero. If `r` is the number of background agreements and `h`
the number of petal agreements, then

```text
r<=d,       h+r>=ell+d,       h>=ell.
```

Consequently some petal contains at least

```text
m_rich=ceil(ell/M)
```

agreements, all in one value fiber `R(y)=c_i`. In particular

```text
d>=m_rich.
```

If `R` is injective on all petal points, then `h<=M`; hence the entire
collision-free class is empty whenever `ell>M`.

At the asymptotic L1 lower cutoff

```text
ell>=C n/log_2 n
```

and any fixed constant-rate window, `ell>M` for sufficiently large `n`, and

```text
m_rich >= ceil(ell^2/(n-k+1))
       = Omega(n/log_2^2 n).
```

Thus the variable-defect collision-free family cannot falsify the actual
reserve-conditioned `imgfib` statement. Any reserve-scale counterexample in
this sunflower lane must instead produce a source-coupled rational-value
fiber of size `Omega(n/log^2 n)` inside one petal.

## Scope

This is a reduction, not a count of rich fibers. It does not prove that every
rich fiber is quotient-periodic or that all such fibers have polynomial total
multiplicity.
