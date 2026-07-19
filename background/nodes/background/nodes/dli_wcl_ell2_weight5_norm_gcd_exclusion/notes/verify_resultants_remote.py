#!/usr/bin/env python3
"""Remote exact replay entrypoint for the weight-5 norm-gcd certificate."""

import modal

from experiments.prize_resolution.dli_wcl_pair_norm_gcd_probe_modal import app


assert isinstance(app, modal.App)

