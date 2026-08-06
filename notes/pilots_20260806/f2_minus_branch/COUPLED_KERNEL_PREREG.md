# F2 minus-branch coupled-kernel preregistration

## Claims under test

1. For every odd residue `p=3 mod 4`,
   `ord_(2^a)(p)=2^max(1,a-v_2(p+1))`.
2. In the official top-window range, the Frobenius closure of the first `R`
   odd roots has cardinality `hR` with no collisions.
3. The generic weighted collision identity and pointwise rank floor hold on
   complete finite matrices.
4. The two new PROVED nodes and the repaired F2 target have the printed DAG
   statuses and edges.

## Falsifiers

- any order-law mismatch in the exhaustive surrogate sweep;
- any Frobenius-root collision in a qualifying surrogate or official
  residue pattern;
- any finite matrix violating the exact collision normalization or floor;
- any missing requirement/evidence edge or incorrect status.

## Resource ceiling

Run the generic floor, minus-kernel, and F2 consumer verifiers in one Modal
container with one CPU, 1024 MiB RAM, a 120-second timeout, and no retries.
All sweeps are bounded; no official-size vector is allocated.

## Result

Modal app `ap-3u4NDxYLTav3KGsvw6nnhN` returned PASS after the weighted
Fourier normalization was added. The generic floor
verifier checked four complete matrices (`786` collisions, `168` ternary
kernel words); the minus verifier checked `4,094` order cases, `28`
surrogate orbit families, `15` official-pattern top orbits, and the M61
witness; the consumer contract passed at `7/7` statuses and `8/8` edges.
