# Official exact-slice rate-dependent near-tail bound

- **status:** `PROVED`
- **closure:** `proof`

## Statement

Let `N=2^41`, let `rho` be one of the four prize rates, let
`128<=L=log2(q)<256`, and let `t=t_XR` be the official exact-list corridor
depth. Write `A_b` for the number of `t`-null subsets of size `b`.

For

```text
rho       1/2   1/4   1/8   1/16
w_rho      15    14    13     12
```

the two near tails satisfy

```text
2 sum_{j=1}^{w_rho} A_{t+j} < 2^122.                 (NT)
```

Complementation identifies the factor two with the layers of sizes
`N-t-j`. Thus the rate-dependent strips consume less than half of the
`N^3=2^123` budget at every official exact-slice row.

## Attack surface

n/a (proved)

## Falsifier

n/a (proved)

> **Row-vocabulary note (2026-08-10, FLAG E adjudication).** This
> statement's row family "N = 2^41, K = rho*N" is Convention A:
> ADMISSIBLE BUT NOT MAXIMAL at rates < 1/2. Per the ABF26 page-5
> box, "maximal row" = the cap-saturating Convention B rows
> (k = 2^40, n = 2^40/rho). The claim here is unchanged — it is
> about the rows it defines (node-local-pin reading rule) — but any
> "maximal/official row" phrasing is read per
> notes/BAND_LANE_DEFINITIONS.md item 13. Rate 1/2 unaffected.
