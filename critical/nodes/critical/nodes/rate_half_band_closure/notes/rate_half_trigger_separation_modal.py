#!/usr/bin/env python3
"""Separate the ordinary-list and MCA graded-prefix triggers at rate 1/2.

This is a route audit, not a list-size upper bound.  It maximizes the certified
lower counts supplied by the proved quotient-remainder pigeonhole and by its
fixed-tail (qcore) subfamily at the two endpoints of the residual band.
"""

import modal


app = modal.App("rs-mca-rate-half-trigger-separation")
image = modal.Image.debian_slim().pip_install("mpmath")

N = 1 << 41
K = 1 << 40
BAND = ((1 << 33) + 1, 8_592_912_738)
FIELD_BITS = ("razor-bottom", "255.90000002"), ("cap", "256")


@app.function(image=image, cpu=2.0, memory=2048, timeout=300)
def audit():
    from mpmath import mp

    mp.dps = 70
    log2 = lambda x: mp.log(x, 2)

    def log2_binom(n, r):
        if r < 0 or r > n:
            return mp.ninf
        return (
            mp.loggamma(n + 1)
            - mp.loggamma(r + 1)
            - mp.loggamma(n - r + 1)
        ) / mp.log(2)

    rows = []
    for t in BAND:
        agreement = K + t
        for q_name, q_text in FIELD_BITS:
            q_bits = mp.mpf(q_text)
            list_trigger = q_bits - 128
            mca_trigger = q_bits - 40
            best_general = None
            best_fixed = None
            fixed_candidates = []
            threshold_candidates = []
            for e in range(1, 41):
                c = 1 << e
                quotient = N // c
                m, s = divmod(agreement, c)
                if not (0 <= m <= quotient and 0 <= s < c):
                    continue
                d, t_rem = divmod(t, c)
                assert t_rem == s

                # Exact prefix weight for K=k:
                # residue 0 occurs d times and residues 1..s occur d+1 times.
                weight = d + s * (d + 1)
                general = (
                    log2_binom(quotient, m)
                    + log2_binom(N - m * c, s)
                    - q_bits * weight
                )
                candidate = (general, e, d, s, weight)
                if best_general is None or candidate[0] > best_general[0]:
                    best_general = candidate

                # Hold one s-tail T0 fixed in a distinguished c-fiber.  The
                # varying support is a union of m other fibers.  Its first d
                # quotient coefficients must be pigeonholed.  At d=0 this is
                # exactly the qcore family C(N/c-1,k/c).
                if s and m <= quotient - 1:
                    fixed = log2_binom(quotient - 1, m) - q_bits * d
                    candidate = (fixed, e, d, s)
                    fixed_candidates.append(candidate)
                    threshold_candidates.append(
                        ((fixed + q_bits * d + 128) / (d + 1), e, d, s)
                    )
                    if best_fixed is None or candidate[0] > best_fixed[0]:
                        best_fixed = candidate

            assert best_general is not None and best_fixed is not None
            rows.append(
                {
                    "t": t,
                    "q": q_name,
                    "q_bits": str(q_bits),
                    "list_trigger_bits": str(list_trigger),
                    "mca_conversion_trigger_bits": str(mca_trigger),
                    "trigger_separation_bits": str(mca_trigger - list_trigger),
                    "best_general_prefix": {
                        "log2_lower_count": str(best_general[0]),
                        "scale_e": best_general[1],
                        "d": best_general[2],
                        "s": best_general[3],
                        "weight": best_general[4],
                        "list_margin_bits": str(best_general[0] - list_trigger),
                    },
                    "best_fixed_tail": {
                        "log2_lower_count": str(best_fixed[0]),
                        "scale_e": best_fixed[1],
                        "d": best_fixed[2],
                        "s": best_fixed[3],
                        "list_margin_bits": str(best_fixed[0] - list_trigger),
                    },
                    "top_fixed_tail": [
                        {
                            "log2_lower_count": str(candidate[0]),
                            "scale_e": candidate[1],
                            "d": candidate[2],
                            "s": candidate[3],
                            "list_margin_bits": str(candidate[0] - list_trigger),
                            "q_threshold_bits": str(
                                (candidate[0] + q_bits * candidate[2] + 128)
                                / (candidate[2] + 1)
                            ),
                        }
                        for candidate in sorted(
                            fixed_candidates, reverse=True
                        )[:8]
                    ],
                    "best_fixed_tail_q_threshold": {
                        "q_threshold_bits": str(max(threshold_candidates)[0]),
                        "scale_e": max(threshold_candidates)[1],
                        "d": max(threshold_candidates)[2],
                        "s": max(threshold_candidates)[3],
                    },
                }
            )

    return rows


@app.local_entrypoint()
def main():
    import json

    print(json.dumps(audit.remote(), indent=2))
