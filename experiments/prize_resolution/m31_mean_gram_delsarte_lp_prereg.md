# M31 mean-Gram next-cell Delsarte screen

## Question

At the first unpaid mean-centered Mersenne support `e=65455`, can the
ordinary Johnson-scheme Delsarte LP improve the punctured explanation-list
cap enough to pay the MCA profile?

The punctured block parameters are

```text
n=983127,       A=1999,       pair intersection c<=5.
```

The proved mean-centered cap is `16203700`.  The exact slope profile is
`17120123`, while the budget is `16777215`.  Holding the other cumulative
caps fixed, an endpoint list cap at most `15860792` would pay the cell.

## Method

Solve the standard Johnson-scheme inner-distribution LP with six variables,
at Johnson distances `A-5,...,A`.  For eigenspace `k`, use

```text
Q_k(i)=E_i(k)/(C(A,i)C(n-A,i)),
E_i(k)=sum_j (-1)^(i-j) C(A-j,A-i) C(A-k,j)
                              C(n-A+j-k,j).
```

The worker evaluates the exact integer sum by a term recurrence, converts
only the final ratio to floating point, and solves with SciPy/HiGHS.  Each
distance variable is bounded by the already-proved total cap.  If the full
matrix misses the deadline, the worker solves the completed-prefix
relaxation and reports that result explicitly as partial.

## Decision rule

- **PAYMENT SIGNAL:** LP optimum at most `15860792`; seek an exact rational
  dual certificate.
- **USEFUL SIGNAL:** LP optimum below `16203700`; it improves the proved raw
  cap but may not pay the slope profile.
- **NO SIGNAL:** full LP optimum at least `16203700`.
- A partial, failed, or unstable solve is inconclusive and changes no DAG
  status.

## Resource contract

One initial Modal container, two CPUs, 1 GiB RAM, and a 60-second function
timeout.  If that returns a healthy partial matrix, allow one staged
completion rerun with the same memory and at most 240 seconds.  Every run
returns its partial or complete result before shutdown; no further scaling
run is authorized.
