# DLI WCL ell=1 weight-6 exclusion on 128 extension rows

- **status:** PROVED
- **closure:** computation
- **consumer:** `dli_wcl_slot_1_6_emptiness`

## Statement

There is no reduced signed weight-6 relation at an order-512 root on the 128
explicit official generated-field rows in the banked panel.  The panel has 64
rows in each exact class

```text
p = k 2^39 + 1, k odd, ord_(2^41)(p)=4, q=p^4;
p = k 2^40 + 1, k odd, ord_(2^41)(p)=2, q=p^2.
```

All 128 characteristics are prime, all fields satisfy `q<2^256`, and
`mu_512` lies in the prime field.  Equivalently, after rotating one term to
`1`, no six distinct order-512 roots with no antipodal pair sum to zero on a
listed row.

## Certificate

For every row, full factorization of `p-1=k*2^v` gives a direct Pocklington
primality certificate.  Exact meet-in-the-middle search constructs all
`129,540` legal pairs and scans all `21,849,080` legal triples.  The complete
panel therefore certifies `16,581,120` pair records and `2,796,682,240` triple
iterations with no hit.  A separately implemented sorted-pair search replays
both endpoints of both extension classes.

## Nonclaims

This is finite exact evidence, not the universal WCL `(1,6)` theorem.  It does
not cover every characteristic, the nonsplit-on-`mu_512` extension classes,
other weights or levels, or WCL-ZONE.  The consumer remains `TARGET`.

## Falsifier

One listed composite characteristic, one row outside the official field
contract, an incomplete pair/triple count, or one compatible six-set summing
to zero on a listed row.
