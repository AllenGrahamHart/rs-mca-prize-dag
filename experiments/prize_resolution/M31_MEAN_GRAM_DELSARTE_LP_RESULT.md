# M31 mean-Gram next-cell Delsarte result

## Verdict

`NO_SIGNAL`.  The complete ordinary Johnson-scheme Delsarte LP does not
improve the proved mean-centered explanation-list cap at the first unpaid
Mersenne support.

For

```text
(n,A,c)=(983127,1999,5),
```

the relevant values are

```text
proved raw cap:       16203700
LP optimum:           16203700.200638048
payment threshold:    15860792
```

The minimum of the proved and LP bounds remains `16203700`.  Consequently
the exact slope profile remains `17120123`, above budget `16777215`.

## Replay

The worker used six distance variables and all 1,999 Johnson eigenspace
constraints.  Dual-Hahn numerators were computed by exact integer
recurrence, with only final normalized ratios converted to floating point.
HiGHS terminated normally with two positive variables and zero reported
minimum inequality slack.

The initial run returned a healthy 541-row partial relaxation with the same
objective.  The one authorized completion rerun returned the full matrix.

- partial app: `ap-7CJw55he3qUkakWZSfvCnn`;
- full app: `ap-s1CgqT4b9VaKbStMrw8MHG`.

## Consequence

Do not spend more compute on the ordinary support-only Delsarte LP for this
cell.  A useful theorem must retain structure erased by binary support
projection, such as slope ownership, explanation amplitudes, or the
full-lift codimension-one extension.  This numerical screen changes no DAG
status and is not an unsafe certificate.
