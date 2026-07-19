# F5 P9: the W-COLLISION PAIR-MOMENT IDENTITY
# (stratum (i)'s residual open, posed in P8, now INSTRUMENTED)

Status: PROVED bookkeeping (elementary double counts, proofs inline) +
machine-replayed (f5_p9_wcollision_pair_moment_modal.py, 14 pairs, all
assertions exact). This is an INSTRUMENT in the P8 sense: it settles
the aggregation question for W-collisions and re-poses the residual as
a shift-pair-moment bound. It does NOT prove the anti-concentration
heart.

## Pre-registration

Question: does the W-collision count (the number of k-cores W carrying
>= 2 live slopes — P8's residual open for stratum (i)) admit exact
bookkeeping in the moment-template style (exact identity + fiber
regrouping + boundary collapse), and what is the residual after it?

Success criterion: an exact identity verified independently on both
sides; a fiber regrouping with the fiber factor named; the residual
posed as a named, adjacent quantity.

Failure criterion: an identity holding only under unstated genericity;
promoting the instrument to the anti-concentration bound; hiding the
near-pencil mass.

## Setup

As P8/F5-OS: pair (u, v) with v nonvanishing on D (v-vanishing points
carry the validity strip), U_z = u + z*v, rays = pairs (z, c) with c a
codeword and s_{z,c} = |supp(z,c)| >= A, supp(z,c) = {x : U_z(x) =
c(x)}. For a k-set W, mult(W) = #{z : the deg<k interpolant of U_z|_W
is a live ray}. Per (W, z) the interpolant is unique, so mult counts
slopes; distinct codewords agree on <= k-1 points, so two rays through
the same W have distinct slopes.

## T1 (pair-moment identity)

    sum_{|W|=k} C(mult(W), 2)
      = sum_{cross-slope ray pairs {(z,c),(z',c')}} C(|supp ^ supp'|, k).

Proof: count pairs (W, {r, r'}) with W inside supp(r) ^ supp(r') both
ways. Fixing W gives C(mult(W), 2) ray pairs (uniqueness per (W,z) +
the same-slope exclusion above); fixing the ray pair gives
C(|supp ^ supp'|, k) choices of W.

## T2 (fiber structure)

For a cross-slope pair, set g = (c - c')/(z - z'), f = c - z*g. Then

    supp(z,c) ^ supp(z',c') = JointAgr(f,g) := {x : u(x)=f(x), v(x)=g(x)}

EXACTLY (both inclusions are one-line substitutions), and the pair
{(z,c),(z',c')} is recovered from (f, g, {z, z'}) via c = f + z*g.
So the intersection size J depends only on (f, g): cross pairs sit in
fibers over codeword pairs, and J(f,g) is a JOINT AGREEMENT of the
received pair (u, v) with a codeword pair — the shift-pair object.

## T3 (regrouping)

    sum_{cross pairs} C(J, k)
      = sum_{(f,g)} C(L(f,g), 2) * C(J(f,g), k),

where L(f,g) = #{z : (z, f + z*g) is live} — the live-slope count of
the SHIFTED pair (u - f, v - g). Only (f,g) with J >= k contribute.

## T4 (pencil collapse at the t=2 boundary)

For every k-set W the sunflower pencil (P_W, Q_W) = (interp u|_W,
interp v|_W) satisfies interp(U_z|_W) = P_W + z*Q_W (linearity), so
mult(W) = L(P_W, Q_W): per-W multiplicity IS a shifted-pair live count.
Conversely any (f,g) with J(f,g) = k has (f,g) = (P_W, Q_W) for
W = JointAgr(f,g) (a deg<k polynomial agreeing with u on a k-set is its
interpolant). Hence in the far-pair regime (member cores <= A-2 = k at
t = 2, which is SPREADNESS itself — the cores ARE the JointAgr sets):

    #W-collision cores  =  #{k-sets W : L(P_W, Q_W) >= 2},
    collision pair-moment = sum_W C(L(P_W, Q_W), 2),

with per-core multiplicity capped by the sunflower lemma at
(n-k)/(t-d). The W-collision moment is EXACTLY the second moment of
pencil live counts — an SP-type quantity adjacent to the PROVED
v13_second_moment_shift_pair_identity (which stratifies sum_z N_w(z)^2
by ordered disjoint-root shift pairs).

## Replay

    ~/.venvs/modal/bin/modal run critical/nodes/xr_smallcore_spread_count/notes/f5_p9_wcollision_pair_moment_modal.py

Digest: F5_P9_WCOLLISION_PAIR_MOMENT_PASS. 14 official-shaped pairs
(k = n/2, t = 2, A = k+2; random + near-pencil; n = 12/16, q = 97).
T1-T4 asserted exactly on every pair (identity both sides independent;
fiber sets pointwise equal; regroup with independently recomputed L;
pencil bijection at J = k). Instructive data:

- random pairs: J-profile concentrated at J = k with a thin J = k+1
  tail; pair moment O(100) at n = 16; max mult 7 vs (n-k)/(t-d) — the
  verifier measures RAW multiplicities (no strips applied), so the
  d = 0 cap is not binding in-sample; the cap applies post-strip.
- near-pencil pairs: the planted codeword pair (f,g) carries L = q = 97
  (live at every slope) and C(97,2) = 4656 pairs at the planted J —
  ALL the collision mass sits on the one fiber the tangent/near-pencil
  strips remove before stratum (i) is counted. The strips and the
  far-pair hypothesis are load-bearing, exactly as the ledger says.

## What this settles / what remains

SETTLED: W-collisions need never be counted raw. They aggregate by
codeword-pair fibers with exact factor C(L,2)*C(J,k); at the t=2
boundary they ARE the second moment of pencil live counts, and the
per-core cap is the sunflower lemma's.

REMAINING (the re-posed residual): bound sum_W C(L(P_W, Q_W), 2) for
far pairs — anti-concentration of pencil live counts over the C(n,k)
pencils. This is the same anti-concentration heart the F5-OS ledger
already names, now carrying its exact bookkeeping. Natural next
instruments: the v13 shift-pair strata (PROVED) as the identity layer,
and the effective energy dichotomy (F2 packet, same day) as the
high-energy branch closer.
