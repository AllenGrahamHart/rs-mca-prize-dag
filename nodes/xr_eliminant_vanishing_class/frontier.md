# frontier: xr_eliminant_vanishing_class

No new local census was run in this working copy. The WSL laptop should not
run the E32-extended enumeration.

## What is already banked

- `xr_triangle_eliminant_form` is PROVED: the rank-jump/eliminant normal form
  and evaluator exist.
- E32-MERGED reports no profile-forced vanishing in the checked rows.
- E32-COORD reports zero coordinate-special vanishings across 382,200 exact
  toy placements.

## What was checked here

The recorded Modal app for E32-extended (`ap-gVR6MjqiBK4vxY9U1ABUZ7`) has no
usable result in the retrieved logs; it only reports that the app was stopped.
Therefore this node cannot cite E32-extended as a certificate.

## Current dependency split

The node's old "classify identically-vanishing configurations" language has
sharpened into two separate obligations:

- `xr_profile_eliminant_nonvanishing`: now conditional on the proved
  minor-specialization semantics and the remaining coverage node
  `xr_profile_minor_certificate_coverage`.
- `xr_coordinate_hypersurface_reduction`: once the profile eliminant is
  nonzero, coordinate-special stagnation lies on a proper determinantal
  hypersurface. This reduction is now proved.

The true remaining content is
`xr_profile_minor_certificate_coverage`: produce a nonzero minor certificate
for every unpaid non-boundary light profile. The hypersurface reduction is
already the nonzero-eliminant branch used by `xr_light_triangle_eliminant`.

## Smallest next step

Do not run the full E32 enumeration locally. Either:

- obtain a complete remote `E32_RESULTS` certificate for the n=9..13 extension;
  or
- prove `XR-V1` directly from the MDS normal-form matrix by identifying a
  profile-dependent nonzero minor.
