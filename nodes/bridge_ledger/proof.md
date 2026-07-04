# bridge_ledger proof

## Predicate nodes

- `ld_bridge`
- `ldsw_ld_separation`
- `mca_from_ca_reduction`

## Claim

The bridge ledger has no silent object crossing.

## Proof

There are three bridge types used by the critical DAG.

First, `ld_bridge` proves the line-decoding bridge on the simple-pole family:
the LD, MCA, and CA slope sets coincide there, so a statement may cross those
objects only through that explicit simple-pole bridge.

Second, `mca_from_ca_reduction` proves the reduction from CA to MCA up to half
the minimum distance. This records the only global CA-to-MCA loss used by the
compiler path.

Third, `ldsw_ld_separation` proves that LD_sw does not imply ABF/GG
line-decodability. Hence the ledger cannot silently reverse the LD_sw
direction or use LD_sw as a substitute for the ABF/GG line object.

These rows exhaust the object crossings represented by the bridge layer:
simple-pole LD/MCA/CA equality, global CA-to-MCA reduction with its loss, and
the LD_sw separation guard. Therefore every crossing is named and the silent
crossing failure mode is excluded.

