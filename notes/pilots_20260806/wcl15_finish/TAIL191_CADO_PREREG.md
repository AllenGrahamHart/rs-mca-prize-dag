# WCL `(1,5)` tail-191 bounded CADO-NFS attempt - preregistration

- **date:** 2026-08-06
- **consumer:** `dli_wcl_slot_1_5_emptiness`
- **norm:**
  `648504938724625892617537595827566622528651020454874372151735040370465231483079169`
- **size/status:** 269 bits, 81 digits, composite
- **FactorDB check:** id `1100000009050891514`, status `C`, no proper factor
- **CADO-NFS source:** official commit
  `9bb8fc0799bbaaf0b47a1edf573ecf5e0cf8e46a`

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
