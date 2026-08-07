#!/usr/bin/env python3
"""Remote regeneration entrypoint for the first-64 weight-six packet."""

import modal

from experiments.prize_resolution.dli_wcl_ell1_weight6_admissible_mitm_modal import app


assert isinstance(app, modal.App)
