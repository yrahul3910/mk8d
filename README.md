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

### PRs

* We do not accept pushes to master. Any requests for access will be denied.
* All PRs must be reviewed by at least two contributors of the repo.
* All PRs must pass all checks before merging. Collaborators do not have permission to override the automated checks. This is on purpose.
* All PRs must be squashed and merged. Do not merge PRs with multiple commits.
* All PRs must be rebased on top of master before merging. Do not merge PRs with merge commits.
* All PRs must be up to date with master before merging. Do not merge PRs with conflicts.
* All PRs must have a description. Do not merge PRs with empty descriptions.
* All PRs must have a title. Do not merge PRs with empty titles.
* All PRs must be from a branch with a descriptive name. Do not use generic names.

*Note:* Some of the above rules were not followed for the first few PRs. We will henceforth enforce them.

### General

We use [ruff](https://beta.ruff.rs) for linting. You can find the code style in `pyproject.toml`. After adding your code,
lint it with `ruff check . --fix`.

### Pre-commit Hooks

We use `pre-commit` for code quality checks. Use `pre-commit install` to install the hooks. Then, you can run them with
`pre-commmit run --all-files`.

**Important:** After cloning the project, run `pre-commit install` first.

# Output

The code should produce an `output.json` similar to the below:

```json
{
    "user": [
        {
            "1": {
                "config": {
                    "character": "Baby Mario, Baby Luigi, Dry Bones, Mii (Light)",
                    "kart": "Badwagon, Standard ATV (Quad), GLA",
                    "tire": "Monster, Hot Monster, Ancient",
                    "glider": "Wario Wing, Plane Glider, Gold Glider, Paraglider"
                },
                "optimizer_name": "bo",
                "score": 12
            }
        },
        {
            "2": {
                "config": {
                    "character": "Baby Peach, Baby Daisy",
                    "kart": "Circuit Special, B Dasher, P-Wing",
                    "tire": "Metal, Gold Tires",
                    "glider": "Super Glider, Waddle Wing, Hylian Kite"
                },
                "optimizer_name": "bo",
                "score": 31
            }
        },
        {
            "3": {
                "config": {
                    "character": "Koopa Troopa, Lakitu, Browser Jr",
                    "kart": "Mach 8, Sports Coupe, Inkstriker",
                    "tire": "Standard, Blue Standard, GLA Tires",
                    "glider": "Wario Wing, Plane Glider, Gold Glider, Paraglider"
                },
                "optimizer_name": "bo",
                "score": 13
            }
        },
        {
            "4": {
                "config": {
                    "character": "Mario, Ludwig, Mii (Medium)",
                    "kart": "Pipe Frame, Varmint, City Tripper",
                    "tire": "Metal, Gold Tires",
                    "glider": "Super Glider, Waddle Wing, Hylian Kite"
                },
                "optimizer_name": "bo",
                "score": 123
            }
        },
        {
            "5": {
                "config": {
                    "character": "Toad, Shy Guy, Larry",
                    "kart": "Mach 8, Sports Coupe, Inkstriker",
                    "tire": "Off-Road, Retro Off-Road, Triforce Tires",
                    "glider": "Wario Wing, Plane Glider, Gold Glider, Paraglider"
                },
                "optimizer_name": "bo",
                "score": 43
            }
        },
        {
            "6": {
                "config": {
                    "character": "Baby Mario, Baby Luigi, Dry Bones, Mii (Light)",
                    "kart": "Badwagon, Standard ATV (Quad), GLA",
                    "tire": "Monster, Hot Monster, Ancient",
                    "glider": "Peach Parasol, Parafoil, Bowser Kite, MKTV Parafoil"
                },
                "optimizer_name": "bo",
                "score": 12
            }
        },
        {
            "7": {
                "config": {
                    "character": "Toad, Shy Guy, Larry",
                    "kart": "Cat Cruiser, Comet, Yoshi Bike, Teddy Buggy",
                    "tire": "Roller, Azure Roller",
                    "glider": "Peach Parasol, Parafoil, Bowser Kite, MKTV Parafoil"
                },
                "optimizer_name": "bo",
                "score": 321
            }
        },
        {
            "8": {
                "config": {
                    "character": "Baby Mario, Baby Luigi, Dry Bones, Mii (Light)",
                    "kart": "Badwagon, Standard ATV (Quad), GLA",
                    "tire": "Monster, Hot Monster, Ancient",
                    "glider": "Cloud Glider, Parachute, Flower Glider, Paper Glider"
                },
                "optimizer_name": "bo",
                "score": 423
            }
        },
        {
            "9": {
                "config": {
                    "character": "Bowser, Morton, Mii (Heavy)",
                    "kart": "Badwagon, Standard ATV (Quad), GLA",
                    "tire": "Monster, Hot Monster, Ancient",
                    "glider": "Wario Wing, Plane Glider, Gold Glider, Paraglider"
                },
                "optimizer_name": "bo",
                "score": 12
            }
        },
        {
            "10": {
                "config": {
                    "character": "Peach, Daisy, Yoshi",
                    "kart": "Badwagon, Standard ATV (Quad), GLA",
                    "tire": "Monster, Hot Monster, Ancient",
                    "glider": "Peach Parasol, Parafoil, Bowser Kite, MKTV Parafoil"
                },
                "optimizer_name": "bo",
                "score": 34
            }
        }
    ]
}
```
