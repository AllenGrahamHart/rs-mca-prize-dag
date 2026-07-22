# Audit

## Verdict

The quotient-space proof is basis-independent and applies to any linear code.
For affine lines every noncontained fixed-support factor has degree one, so
the squarefree lcm degree is exactly the number of distinct slopes.

## Scope checks

- The all-zero quotient pair is assigned `g_S=1`; otherwise it would falsely
  contribute every slope from a contained support.
- Zero coordinate forms are omitted before taking the gcd.
- The lcm is radical, so repeated supports and repeated threshold appearances
  of one slope cost one factor.
- The theorem concerns finite affine slopes. A projective point at infinity
  needs the homogeneous analogue and is outside the XR finite-slope slot.

## Limitations

Writing an lcm over an exponentially large family is an exact definition, not
a feasible official-row algorithm. A closing theorem must expose enough
quotient symmetry or syndrome structure to bound or construct the radical lcm
without enumerating supports.
