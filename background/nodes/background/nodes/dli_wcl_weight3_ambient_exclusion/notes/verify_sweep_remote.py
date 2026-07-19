#!/usr/bin/env python3
"""Remote replay entrypoint for the exact FLINT/PARI class sweep."""

import modal

from experiments.prize_resolution.dli_wcl_weight3_classes_modal import app


assert isinstance(app, modal.App)
