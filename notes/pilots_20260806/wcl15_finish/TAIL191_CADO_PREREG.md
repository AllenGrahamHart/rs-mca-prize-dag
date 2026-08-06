# WCL `(1,5)` tail-191 bounded CADO-NFS attempt - preregistration

- **date:** 2026-08-06
- **consumer:** `dli_wcl_slot_1_5_emptiness`
- **norm:**
  `648504938724625892617537595827566622528651020454874372151735040370465231483079169`
- **size/status:** 269 bits, 81 digits, composite
- **FactorDB check:** id `1100000009050891514`, status `C`, no proper factor
- **CADO-NFS source:** official commit
  `9bb8fc0799bbaaf0b47a1edf573ecf5e0cf8e46a`
- **portable image:** official `factoring-full` image at
  `sha256:d89bc19b6a1a9dd00b8c95cd97d60faca73ecbfc3ea71b5e20ec0403b1b3fc10`

## Decision

The ten bounded ECM/PARI/FLINT attempts found no divisor, but the complete
easy replay and 193-tail certificate now make this integer the sole residual
of the exhaustive WCL `(1,5)` route.  Run one bounded general number field
sieve attempt with the official CADO-NFS implementation.  Build from the
pinned source commit, run 16 local threads, and persist the complete work
directory on a dedicated Modal volume.

The inner process receives SIGINT at 1,200 seconds and up to 60 seconds for a
graceful checkpoint before termination.  The wrapper records command,
elapsed time, exit mode, work-directory inventory, log tail, parameter
snapshots, and every proper divisor printed into a small text artifact.  A
timeout is `PARTIAL`, not negative evidence; its work directory is suitable
for an explicitly repriced future resume.  No resume is authorized here.

## Predictions and gates

**P1.**  The pinned CADO build starts and leaves a reusable parameters/database
checkpoint.  Packaging failure is an operational null run.

**P2.**  The attempt reaches relation collection or later inside 1,200 seconds.
Earlier progress is banked but does not justify a same-budget retry.

**P3.**  CADO returns at least one proper divisor.  Any returned divisor must
divide the exact norm; complete factorization and independent primality are
checked in a separate certificate before node promotion.

## Resource ceiling

One Modal container uses 16 CPUs, 32 GiB, and a 1,500-second function cap;
the CADO process has a 1,200-second work cap.  The execution is expected below
`$0.50`, with a conservative metered ceiling of `$1`.  This is the only
authorized run.  It replaces neither the external NFS request nor its
primality-certificate requirements unless it returns a complete factorization.

```text
tools/ramguard modal -- modal run --detach \
  notes/pilots_20260806/wcl15_finish/tail191_cado_modal.py
```

## Operational null run

App `ap-sCB8nacFFU9jokMNrVx0ti` built and cached official CADO-NFS commit
`9bb8fc079`, but the installed current CLI rejected the README-style
`workdir=/path` token and exited code 2 in 0.590 seconds.  It produced no
parameter snapshot and consumed none of the factoring budget.  Under P1 this
is an operational null run.  One corrected invocation using the installed
CLI's printed `--workdir /path` form is authorized; all resource and no-resume
limits remain unchanged.

App `ap-PIC4pd0lqASVDIf6r2xeL9` used that corrected invocation and reached
polynomial selection, but every `polyselect` work unit exited `-4` (`SIGILL`)
before doing useful work.  The source image had been compiled on a Modal image
builder exposing AVX-512 and then scheduled on a runtime CPU without AVX-512.
CADO consequently found no polynomial and exited with `IndexError` after
16.277 seconds.  The complete operational record is
`tail191_cado_result.json`, digest
`4262ab8f331f08fef8d0b6f9147ba542ae21d21c9931a6d92a3329690c33a0ff`.
This is another P1 operational null, not a factoring attempt.

One portable-image correction is authorized.  It uses CADO-NFS's official
`factoring-full` image pinned at the digest above and a fresh work directory
`/work/tail191-cado-portable-v1`; none of the CPU-incompatible database is
reused.  The same 1,200-second process cap, 16-CPU allocation, cost ceiling,
and no-resume rule apply.  Its output is
`tail191_cado_portable_result.json`.  A registry, image-start, or executable
discovery failure remains an operational null; once polynomial selection runs
successfully, the one authorized factoring attempt has begun.

App `ap-0BRu4pvRf6kx8RzCRkvFHx` pulled the pinned official image and found
`/usr/local/bin/cado-nfs.py`, but Modal's required `add_python` layer replaced
the image's Python site packages.  CADO exited on `ModuleNotFoundError: flask`
before making a parameter snapshot, after 0.449 seconds.  The operational
record is `tail191_cado_portable_result.json`, digest
`dd4055ab0784535746a457976168950bba8b5b9fee37abed7158aa0b2d480602`.
Under the explicit image-start clause this is a P1 operational null.

One dependency-layer correction is authorized: install only `flask` and
`requests`, the runtime dependencies used by the pinned CADO source build, on
top of the same immutable official image.  It uses the fresh work directory
`/work/tail191-cado-portable-v2` and writes
`tail191_cado_portable_v2_result.json`.  All compute and no-resume limits are
unchanged; no further packaging retry is authorized by this preregistration.

## Successful result

App `ap-gyFwY6AxmBrU0NioPlsJ5C` completed normally in 80.456646 seconds.
It reached square root and returned the complete split

```text
2618025003265620701077592958097921
*
247707694890502006805474333259382717013127180289.
```

The work packet contains 320 files and 115,220,826 bytes, result digest
`73b759d20b4d03bf05b8b71b3c629eea14849f5631752d66ccef3d1fe61bfd43`,
and local file SHA-256
`c093d5e05aea1e2b2851042e550f89cf44f093c8b1714c80780efd27b72ec608`.
P3 passed. Independent primality and gate checks are in
`TAIL191_FACTOR_CERT_PREREG.md` and `tail191_factor_cert.json`.
