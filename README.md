# Mario Kart 8 Deluxe Optimization

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/yrahul3910/mk8d/master.svg)](https://results.pre-commit.ci/latest/github/yrahul3910/mk8d/master)

# Setting up

* Install dependencies: `pip install -r requirements.txt`
* Install pre-commit hooks: `pre-commit install`
* Run the program: `python3 main.py`

# Recommendation algorithms

## Random

Randomly picks a configuration each time.

## Bayesian optimization

Uses Gaussian Process optimization from [scikit-optimize](https://scikit-optimize.github.io/stable/) to optimize the configuration.

# Contributing

## Style Guide

### General

We use [ruff](https://beta.ruff.rs) for linting. You can find the code style in `pyproject.toml`. After adding your code,
lint it with `ruff check . --fix`.

### Pre-commit Hooks

We use `pre-commit` for code quality checks. Use `pre-commit install` to install the hooks. Then, you can run them with
`pre-commmit run --all-files`.

**Important:** After cloning the project, run `pre-commit install` first.
