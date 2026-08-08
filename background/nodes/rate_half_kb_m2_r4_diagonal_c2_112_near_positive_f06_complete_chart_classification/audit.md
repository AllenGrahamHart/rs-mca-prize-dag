# Audit

The primary and audit reconstruct each system in separate Sage processes
from the pinned generic source solver. The primary uses successive ideal
saturations and records every intermediate basis. The audit uses one fresh
Rabinowitsch variable and no primary intermediate ideal.

All twelve Modal tasks passed. Primary wall times were `108.29--350.86`
seconds and audit wall times were `47.57--114.40` seconds. Peak child RSS was
at most `592208 KiB` in the primary and `553212 KiB` in the audit.

Pinned SHA-256 values:

```text
primary source   24bc724ddcf77e29605404090f5a3fefa05269fd0d6897cb63761079b7216e39
primary wrapper  e5e11bfd2e6240e988ea39cb928f039ec713ae70d16dff260092dbb4c6ff79a2
primary output   6c5cd3f8f3502bf0ec42a7255027ab434b8099e9e749435cc564555cf540f46d
audit source     c3eaeb6866f95d71ab086d4087fa823a7d9b37d71c5fa18d150681d13e89947c
audit wrapper    42604aa6b69bf5b6ba4c6f20a6b22dd592b04bf5ca80090353a64b80268184f4
audit output     0d8ecaf55b445900e4a59d4ad1f1fa0a0fdb97eb2093718eb08db4c660ef05eb
```
