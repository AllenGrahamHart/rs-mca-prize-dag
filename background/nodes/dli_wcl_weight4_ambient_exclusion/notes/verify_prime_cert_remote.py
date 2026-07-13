#!/usr/bin/env python3
"""Remote replay entrypoint for the weight-4 Pocklington shards."""

import modal

from experiments.prize_resolution.dli_wcl_weight4_prime_cert_modal import app


assert isinstance(app, modal.App)
