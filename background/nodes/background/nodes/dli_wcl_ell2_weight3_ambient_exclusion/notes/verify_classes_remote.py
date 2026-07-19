#!/usr/bin/env python3
"""Remote generation entrypoint for ell=2 weight-3 classes and norms."""

import modal

from experiments.prize_resolution.dli_wcl_ell2_weight3_classes_modal import app


assert isinstance(app, modal.App)
