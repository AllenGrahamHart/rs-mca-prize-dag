#!/usr/bin/env python3
"""Remote generation entrypoint for the bounded weight-5 MITM packet."""

import modal

from experiments.prize_resolution.dli_wcl_terminal_weight5_mitm_modal import app


assert isinstance(app, modal.App)
