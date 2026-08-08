# Audit

The primary sequential saturation and independent one-step Rabinowitsch
calculation agree on five unit cells and one survivor. The survivor field
sieve recomputes the complete localization, lex basis, and exact residue
degrees. The quotient replay reconstructs all eight literal points afresh,
checks inversion closure, verifies endpoint equations and localizers, and
then applies the first quotient norm without importing full-quotient
covariance.

Primary wall times were `95.91--191.05` seconds, one-step audit times were
`38.94--83.86` seconds, the field sieve took `103.23` seconds, and the
eight-point quotient replay took `38.72` seconds. Peak child RSS was at most
`607732 KiB`; all algebra ran remotely under Modal.

Pinned SHA-256 values:

```text
primary source    307e6085ce9197a4bf9509a968b17db81916cd7a0f668ed94f942fcfc376d980
primary wrapper   f93f2beb9bd82cbf62952ec61a6f2281bdfd2398e03ab84e8eb27c0fe0660613
primary output    a06471bf0fd676644e2ffd8d16108835c437ca32d3ea2d5d71332a63a354f96d
audit source      8b5356b26e4d11708849787869541c50612eb5052f31fbc120d4ebcd83a63b2f
audit wrapper     4a8dafcab3b459759e0dd88a05fa5f7530be5fa5fb8df9f17fd5c13e383b0675
audit output      c9641f2d1658927e008583a7ff50b4fbb09c30ed3172d8c02b487d43121400d1
field source      3b4abd06c88a729cdd57537242bc0bdab4a7b62f118b41c5fcb8a675db00cd35
field wrapper     a9f1709a896538d0e915fbe5f843e225098d861d4748e4d99733936dfad93a57
field output      d704fcd22a00959b1980dd6b598c88ac8ad6354808c3f3838629d0cb39fd84bc
quotient source   559d0327507bfcf6e7ec563f92c46a51e7ae6fb4e2743c2bb175a962a55b1211
quotient wrapper  c367faf6bcabd225d8cdac8e4309c017805079d9c82d3237cbc0dcd404c13fad
quotient output   be4c7d04c4dd24cf5d45816c083c3237f32721e6ed13634605aee85442e648e0
```
