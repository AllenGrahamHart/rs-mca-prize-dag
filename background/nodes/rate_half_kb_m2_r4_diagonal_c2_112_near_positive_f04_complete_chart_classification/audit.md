# Audit

The primary and audit reconstruct each four-equation system in separate
Sage processes from the pinned generic `5 x 5` source solver. The primary
uses successive ideal saturations and records every intermediate basis. The
audit uses one fresh Rabinowitsch variable, the product of all sixteen chart
factors, and no intermediate ideal from the primary.

All twelve Modal tasks passed. Primary wall times were `118.01--521.10`
seconds and audit wall times were `47.01--79.93` seconds. Peak child RSS was
at most `617540 KiB` in the primary and `550296 KiB` in the audit.

Pinned SHA-256 values:

```text
primary source   648207609ded916a62a544d5ce5bda2a0fa3434885b564298ec1dc449d5586f8
primary wrapper  fe2a32bc3aefc0801a95dfd46cecdf6db7e274384ec3acaddf403ce7314a0fdf
primary output   1e80a9e74711d649c8df2281117019bb6e02503ca81d40a0826df4c6895e5941
audit source     31eaa8782c77751d38a3094d66ac02a148bc28ae4366c6c4cb8897ae88dacebf
audit wrapper    a102e6ce60100a894b2a4ce8125e08d1c6c121dae46fcc5a168a7ca52dad6426
audit output     b0460a44f92d885944ef3916bbdf0c8295e04ef7a3442057e5683c949d0f60aa
```
