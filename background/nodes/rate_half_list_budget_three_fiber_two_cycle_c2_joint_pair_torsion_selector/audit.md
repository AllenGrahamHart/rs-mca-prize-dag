# Audit

1. The gcd contains all three inputs. Omitting `Rbar` restores the old
   outer-only false positives.
2. The trace shift is `z-2`, since
   `(A+B)^2/(AB)-2=A/B+B/A`.
3. The recurrence subtracts `2` after every squaring and the terminal test is
   also against `2`.
4. The exponent uses forty doublings, giving `N=2^40`.
5. The selector identifies trace classes. Distinct pairs can have the same
   trace and must still be matched against the roots of `D_*` during replay.
6. Passing the selector is not a proof of canonical span, either gap
   equation, or a full cycle.
