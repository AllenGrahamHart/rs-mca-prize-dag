#!/usr/bin/env python3
"""Remote exact replay entrypoint for the weight-six norm certificate."""

import modal

from experiments.prize_resolution.dli_wcl_ell2_weight6_recursive_norm_full_modal import app


assert isinstance(app, modal.App)
