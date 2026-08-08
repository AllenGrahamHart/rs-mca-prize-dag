# Audit

The primary run reconstructs all `12 x 4` cells and uses one-step
Rabinowitsch localization. The audit reruns the same 48 equation and
localizer fingerprints with sequential ideal saturation. Both return unit in
every cell. The census contains 32 fixed-moving and 16 moving-moving cells;
each of `A,TA,OB,OI` and each common vertex occurs twelve times. All 48
equation tuples have distinct SHA-256 fingerprints. The 48 localizer products
fall into three exact fingerprints, with 13 factors in 32 cells and 14 in 16
cells.

Primary wall times were `3.67--7.96` seconds and audit wall times were
`3.68--8.94` seconds. Peak child RSS was at most `349572 KiB`; all Groebner
computations ran remotely on Modal.

Pinned SHA-256 values:

```text
classifier source   b095e6bd9dc9c0a8f58c8f96034f8650485e9cf41a4978e08a127a9492f66068
primary wrapper     53cd581574acd90e4f040adcb70810f77870ab899c086eb446f95bdf94744ed3
primary output      50fe7f422d8edd2e2600aa6ae7cf8abd98e7f04cea67a9d20609a7281ca1d3c7
audit wrapper       ad9efe70b883e8c2ea454b4d9b072765ab18783c20453ad1f2e453d57e80f0cc
audit output        a94b62570c0fc08f706501a0a442640d262430195ae276e17990ecaec13f38b7
```
