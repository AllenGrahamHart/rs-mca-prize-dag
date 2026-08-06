#!/usr/bin/env python3
"""Remote replay entrypoint for the weight-4 class and norm sweep."""

import modal

from experiments.prize_resolution.dli_wcl_weight4_section_modal import app


assert isinstance(app, modal.App)
