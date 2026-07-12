# Every paper figure is the output of a script (Plan Week 8: `make figures` on a clean clone).
.PHONY: help install install-dev test lint figures stats clean

help:
	@echo "install      install the package (core deps only)"
	@echo "install-dev  editable install with dev + experiments + plot extras"
	@echo "test         run the test suite (bound verification is the Week 3 gate)"
	@echo "lint         ruff check"
	@echo "stats        collect per-layer/head statistics (see experiments/configs/)"
	@echo "figures      regenerate every paper figure from results/ (no GPU needed)"
	@echo "clean        remove build/cache artifacts"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev,experiments,plot]"

test:
	pytest -q

lint:
	ruff check src tests

# Regenerates all figures from committed raw outputs in results/. Must work GPU-free.
figures:
	python scripts/plot_allocation_heatmap.py
	python scripts/plot_bound_vs_measured.py
	python scripts/plot_allocation_compare.py

stats:
	python experiments/01_collect_stats.py --config experiments/configs/llama32_1b.yaml

clean:
	rm -rf build dist *.egg-info .pytest_cache .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
