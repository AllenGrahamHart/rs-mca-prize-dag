#!/usr/bin/env python3
"""Remote replay entrypoint for the exact FLINT/PARI norm certificate."""

import modal

from experiments.prize_resolution.dli_wcl_engineered_norm_modal import app


assert isinstance(app, modal.App)
