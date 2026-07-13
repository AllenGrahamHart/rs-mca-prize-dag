#!/usr/bin/env python3
"""Remote generation entrypoint for ell=2 weight-3 prime certificates."""

import modal

from experiments.prize_resolution.dli_wcl_ell2_weight3_prime_cert_modal import app


assert isinstance(app, modal.App)
