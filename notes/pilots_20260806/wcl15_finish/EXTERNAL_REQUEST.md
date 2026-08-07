# External request: factor WCL `(1,5)` tail 191

**Status: RETIRED 2026-08-06.** Bounded official CADO-NFS app
`ap-gyFwY6AxmBrU0NioPlsJ5C` returned the complete split

```text
2618025003265620701077592958097921
*
247707694890502006805474333259382717013127180289.
```

Independent FLINT app `ap-hMfVc7KQMaSvmDtSO5a9kS` proves both factors prime,
checks the product, and gives `v_2(p-1)=9,12`. No external work remains for
this integer. The original request is retained below as custody history.

Factor the following 269-bit composite integer completely:

```text
648504938724625892617537595827566622528651020454874372151735040370465231483079169
```

This is tail index 191, affine-Galois class index 1,595,149, packed
representative key `6709553401856`, in the complete 2,296,920-class terminal
weight-five census.  It is the only unresolved norm after 193/194 hard tails
were completely factored.

## Required return

1. Complete prime factorization with exact exponents.
2. Exact product check against the displayed integer.
3. Checkable primality certificates (Pocklington, ECPP, or equivalent) for
   every factor; probable-prime labels alone are insufficient.
4. For every prime factor, its bit length and `v_2(p-1)`; flag factors below
   `2^256` with valuation at least 41.
5. Tool/version, wall time, peak RAM, command, and hashes of scripts and
   compact certificate files.

If an official-gate factor is found, return it immediately even before the
remaining cofactor is resolved; the project will reconstruct the finite-field
relation independently.  Otherwise the complete certified factorization pays
the last primary hard tail.

## Existing effort

- PARI/GP `factor` timed out at 300 seconds twice.
- FLINT factorization timed out at 300 seconds.
- Eight independent GMP-ECM workers at `B1=10^5,10^6,5*10^6` with fixed
  seeds each timed out at 300 seconds without a divisor.
- PARI independently reports that the integer is composite.

The exact no-factor packet is
`notes/pilots_20260806/wcl15_finish/tail191_ecm_result.json`, SHA-256
`11cbae528206806d411efe4e0deb9da59956335358d9afae6dd729780e1eae6f`.
A contributor should use a properly priced ECM continuation, QS, or NFS
workflow.  Do not run it on the WSL laptop.  No further Modal attempt is
authorized without a new estimate.
