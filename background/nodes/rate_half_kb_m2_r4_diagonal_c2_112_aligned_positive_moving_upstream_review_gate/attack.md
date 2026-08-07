# Attack

1. Check out commit `05ff2348de8f2c0f99683875ff12a9a79dcf21ec` detached.
2. Run the Sage compiler with `--check` in fresh per-cell processes.
3. Run the Python verifier with `--check --tamper-selftest` under normal and
   optimized Python.
4. Audit `M01-R11` and `M03-R11`: `J` survives, `I` makes the localizer
   nilpotent of exact index two.
5. Audit the PR #1138 `M00-R11` operational pin and the complete-source
   `M01 -> M02` inversion.
6. Record reviewer identity, commands, outputs, and hashes; then promote this
   node to PROVED and consume it in the literal coverage table.
