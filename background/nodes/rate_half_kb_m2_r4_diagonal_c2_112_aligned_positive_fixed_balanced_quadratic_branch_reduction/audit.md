# Audit

1. All four literal cells are compiled directly; no orbit transport closes a
   cell.
2. The generic and rank-drop localizers are different. The rank-drop proof
   never inverts `V` or a factor created only after `w=-U/V`.
3. Factors are removed over `QQ` only when they divide an exact named unit;
   the resulting identities are then reduced in the deployed characteristic.
4. The first generic probe found the correct three-core reduction. Small-prime
   `p=1009` bases timed out and are retained only as negative engineering data.
5. Two serializer failures occurred after mathematical reductions completed;
   neither failed run is used. The final ledgers contain `PASS=4` and `PASS=8`.
6. Peak child memory in the final ledgers stayed below 0.51 GB per container.
7. `verify.py` checks exact cell coverage, factors, dimensions, basis hashes,
   terminal claims, localizer zeros, file hashes, and hostile mutations.
