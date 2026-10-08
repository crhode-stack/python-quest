# PYTHON QUEST
### A gamified apprenticeship: Level 1 to Level 10, beginner syntax to measurement mastery

---

## THE PREMISE

Codefinity works because it chops learning into small units, rewards you immediately, and never lets you sit still long enough to get bored. The weakness is that the XP is fake: it measures time served, not capability gained.

This version keeps the dopamine and fixes the measurement. Every point of XP here is earned by producing something that exists afterwards: a solved kata, a committed file, a cleared boss fight. You cannot grind XP by watching videos.

**The campaign runs in two acts.**

Act One (Levels 1 to 5) is the Python language itself, beginner to advanced. You will speedrun the early levels because you already know most of it, but you must pass the skip test to claim the XP. Act Two (Levels 6 to 10) is where Python stops being the subject and becomes the instrument: measurement rigour for campaign analytics. Sample sizing, minimum detectable effect, experiment design, uplift modelling, and the engineering that makes those results trustworthy.

Act Two is the part that pays. Act One is the part that makes Act Two possible.

---

## THE RULES

**Rule 1: XP requires an artefact.** Reading is worth nothing. Watching is worth nothing. A file on disk, a commit, a passing test, a written answer: those are worth XP. If you cannot point at the thing, you did not earn the points.

**Rule 2: You write first, the AI reviews second.** Any quest where an assistant produced the first draft scores zero. Write it badly, get it working, then ask for a harsh review and diff against your version. That inversion is the whole engine.

**Rule 3: The streak is sacred.** One Daily Kata, fifteen minutes minimum, most days. The streak multiplier is the single biggest XP lever in the game and it is the only one that compounds.

**Rule 4: No level skipping, but speedrunning is encouraged.** Each level has a Skip Test. Pass it and you bank the level's XP at half rate and move on immediately. Fail it and you run the quests. Levels 1 to 3 should mostly be speedruns for you. Be honest on the tests; cheating here only costs you later.

**Rule 5: One repo.** `python-quest` on GitHub, public, from day one. Every quest lands in it. The commit history is your save file and your portfolio at the same time.

---

## THE XP ECONOMY

| Action | XP | Notes |
|---|---|---|
| Daily Kata (15 min, one small problem solved) | 15 | The heartbeat of the game |
| Concept drilled (written explanation in your own words, committed) | 10 | Must be your words, not pasted |
| Side Quest cleared | 50 | Optional, but they are where the fun is |
| Main Quest cleared | 100 | Mandatory for level progression |
| Boss Fight cleared | 250 | Timed, no assistance, one attempt per week |
| Skip Test passed | Half the level's quest XP | Speedrun bonus |
| **Multipliers and bonuses** | | |
| Shipped to the public repo with a README | +50 | Per quest, not per commit |
| Written up (a paragraph explaining what you learned) | +25 | Per quest |
| Tests written for your own code | +50 | Per quest, Level 4 onward |
| 7 day streak | x1.2 on everything that week | |
| 21 day streak | x1.5 on everything that week | |
| 50 day streak | x2.0 on everything that week | Rare. Worth chasing |
| **Penalties** | | |
| Streak broken | Multiplier resets to x1.0 | Not a disaster, just a reset |
| Quest completed in a notebook with no module extraction (Level 4+) | 0 XP | Notebooks are scratchpads, not deliverables |
| Quest where the AI wrote the first draft | 0 XP | You will know. Be honest |

---

## THE LEVEL LADDER

| Lvl | Title | XP to enter | Theme |
|---|---|---|---|
| 1 | Initiate | 0 | Syntax, types, control flow |
| 2 | Apprentice | 300 | Functions, collections, comprehensions |
| 3 | Journeyman | 700 | Files, errors, modules, environments, Git |
| 4 | Adept | 1,200 | NumPy, pandas, the data layer |
| 5 | Artisan | 1,900 | Idiomatic Python, objects, generators, decorators |
| 6 | Experimenter | 2,800 | Sample sizing, MDE, power, experiment design |
| 7 | Causalist | 3,900 | Uplift modelling, incrementality, causal inference |
| 8 | Engineer | 5,200 | Testing, packaging, reproducibility, simulation |
| 9 | Architect | 6,700 | Performance, pipelines, production measurement |
| 10 | Grandmaster | 8,500 | Publish, teach, contribute, New Game Plus |

At roughly six focused hours a week with a decent streak, Level 10 lands in about ten to eleven months. Push harder and it compresses. The ladder is deliberately slow at the top because Levels 8 to 10 are where capability actually consolidates.

---

# ACT ONE: THE LANGUAGE

---

## LEVEL 1: INITIATE
*Syntax, types, control flow*

### Skip Test (pass this and bank 250 XP, move straight to Level 2)
Without running anything, write down the output of each. All five correct, in under ten minutes.

1. `print(type(5 / 2), type(5 // 2))`
2. `x = [1, 2, 3]; y = x; y.append(4); print(x)`
3. `print("3" * 3, 3 * 3)`
4. `print(bool(""), bool("0"), bool([]), bool([0]))`
5. `for i in range(3, 0, -1): print(i, end=" ")`

If you got all five, you are past this level. Claim the XP and go.

### Concepts (10 XP each)
Variables and dynamic typing. The numeric tower (int, float, Decimal, and why floats lie). Strings and f-strings. Booleans and truthiness. Lists, tuples, dicts, sets, and when each is correct. `if` / `elif` / `else`. `for` and `while`. `range`. `break`, `continue`, `else` on loops (almost nobody knows loops have an `else`). Indentation as syntax. `None` and why `is None` not `== None`.

### Main Quest: The Morse Revival (100 XP)
You wrote a Morse code translator in Turbo Pascal at school. Write it again in Python, from memory of the problem rather than the old code. Encode and decode, handle unknown characters, handle word spacing. Keep it to one file, no classes, no imports beyond the standard library.

Then open the Pascal version in your head and write three sentences on what Python let you drop entirely.

### Side Quest: The Floating Point Trap (50 XP)
Write a short script that demonstrates why `0.1 + 0.2 != 0.3`, then fix it three ways: `round()`, `math.isclose()`, and `Decimal`. Write one line on which you would use in a financial calculation and why.

### Boss Fight: FIZZBUZZ, THEN THE REMATCH (250 XP)
Twenty minutes, timed, no help.

Round 1: classic FizzBuzz.
Round 2: make the rules data driven, so `{3: "Fizz", 5: "Buzz", 7: "Bazz"}` works without touching the loop logic.
Round 3: explain in writing why Round 2 is better and what principle you just used.

Round 2 is the actual boss. Most people who "know Python" fail it on the first attempt because they reach for more `if` statements instead of iterating the mapping.

### Loot Drop
`python -i script.py` runs the script then drops you into a live REPL with all its state intact. Faster than print debugging, faster than a notebook.

### Achievement: **Hello Again** (Common)
*Return to a language you left behind in 1999.*

---

## LEVEL 2: APPRENTICE
*Functions, collections, comprehensions*

### Skip Test (pass and bank 300 XP)
1. Why is `def f(x, acc=[])` a bug? Show the failing sequence of calls.
2. Rewrite `[x for x in data if x > 0]` as a generator and explain the memory difference.
3. What does `*args` do, what does `**kwargs` do, and what does a bare `*` in a signature do?
4. Given a list of dicts, sort by one key descending and a second ascending, in one line.

### Concepts (10 XP each)
Function definition, arguments, defaults, and the mutable default trap. Scope and `LEGB`. `return` versus printing. Unpacking and starred assignment. List, dict and set comprehensions. Generator expressions. `lambda` and when it is worse than a named function. `enumerate`, `zip`, `sorted` with `key`, `any`, `all`, `min` and `max` with `key`. `collections`: `Counter`, `defaultdict`, `deque`, `namedtuple`.

### Main Quest: The Campaign Response Counter (100 XP)
Generate a synthetic campaign response file: 50,000 rows of customer ID, segment, channel, offer, sent date, and responded flag. Then, using only the standard library (no pandas, this is the point), compute:

- Response rate by segment and channel
- The top five offers by response rate, with a minimum volume threshold
- A `Counter` of responses by week
- Customers who appear in more than one campaign

Write it with comprehensions and `collections`, not nested loops with accumulator lists. When it works, count how many `for` statements you used. If it is more than four, refactor.

This is the exact shape of work you have done in Unica and SAS. Doing it bare, without a dataframe library, is what makes the idioms stick.

### Side Quest: The Comprehension Ladder (50 XP)
Take five pieces of loop-and-append code from your Main Quest and rewrite each as a comprehension. Then take one of them back to a loop because the comprehension was doing three things at once and had become unreadable. Write two sentences on where the line is.

### Side Quest: Cartesian Reckoning (50 XP)
You once found a colleague's query running for fifteen hours because of a cartesian join. Write a tiny Python simulation of it: two lists, a nested loop, and a counter showing the output size growing as the product of inputs. Then produce a matplotlib plot of input size against output size.

You explained this with Venn diagrams once. Now you have a second explanation that runs.

### Boss Fight: THE PIPELINE, UNASSISTED (250 XP)
Forty-five minutes, timed, no help, no AI.

You are handed a messy CSV of campaign contacts: inconsistent date formats, a segment column with trailing whitespace and mixed case, a flag column holding `Y` / `N` / `1` / `0` / blank, and duplicate customer IDs where the later row is the correct one.

Write a function chain, standard library only, that reads it, normalises everything, deduplicates correctly, and returns clean records. Then write three assertions that would have caught each defect.

### Loot Drop
`collections.Counter(data).most_common(5)`. One line for a frequency ranking you have hand written in SQL a thousand times.

### Achievement: **Comprehension Fluency** (Uncommon)
*Write a working nested comprehension on the first attempt, and understand it the next day.*

---

## LEVEL 3: JOURNEYMAN
*Files, errors, modules, environments, Git*

### Skip Test (pass and bank 350 XP)
1. What is the difference between `except Exception`, `except:` and `except BaseException`, and why does the middle one occasionally lose you an afternoon?
2. What does `if __name__ == "__main__":` actually do?
3. Write a context manager with `contextlib.contextmanager` that times a block of code.
4. What does `uv` replace, and name three things it does faster.

### Concepts (10 XP each)
`pathlib` instead of `os.path`. Reading and writing text, CSV and JSON. Encodings and why your file has a BOM. Exceptions: raising, catching, custom exception classes, `raise ... from ...`, and the EAFP principle (try it and handle the failure, rather than checking first). `finally` and `else` on try blocks. Context managers and `with`. Modules, packages, `__init__.py`, imports and circular import pain. Virtual environments. `logging` instead of `print`. Git: branch, commit, rebase, `.gitignore`, and writing a commit message someone can read in six months.

### The Toolchain Initiation (worth 100 XP, do it once)
Set this up now and never think about it again.

| Install | Replaces | Why |
|---|---|---|
| `uv` | pip, venv, pyenv, poetry | One tool. `uv venv`, `uv add`, `uv run`, `uv python install 3.13` |
| `ruff` | black, flake8, isort, pylint | One tool, near instant. `ruff check --fix`, `ruff format` |
| `ipython` | the bare REPL | `%timeit`, `%debug`, `??` to view any object's source |
| `rich` | `print` on complex objects | `rich.inspect(obj)` shows you structure instantly |

### Main Quest: The Campaign Loader (100 XP)
Turn your Level 2 script into a real module. A package directory, a `__main__` entry point, `pathlib` for all file access, a custom `DataQualityError` hierarchy, structured logging to a file, and a config file holding thresholds instead of magic numbers hardcoded in the logic.

It must run as `python -m campaign_loader data/contacts.csv` and produce a log you could hand to someone else when it fails at 3am.

### Side Quest: The Git Archaeology (50 XP)
Take your repo and do five things you have probably never done: an interactive rebase to tidy three messy commits into one, a `git bisect` to find which commit broke something (break it deliberately first), a `git stash` and restore, a tag, and a branch that you merge via a pull request on your own repo.

Reviewing your own PR feels absurd the first time and teaches you more than reading about it.

### Side Quest: The Exception Hierarchy (50 XP)
Design and implement an exception hierarchy for campaign data: a base `CampaignError`, then `SourceUnavailable`, `SchemaViolation`, `DuplicateContactError`, `ThresholdBreach`. Make each one carry useful context (which file, which row, which value). Then write a single handler at the top level that logs each differently.

### Boss Fight: THE 3AM PAGE (250 XP)
Sixty minutes, timed.

Take your Campaign Loader. Deliberately break it in a way you will forget: a schema change, a silent partial read, an encoding shift, a timezone bug that duplicates a day. Commit the break. Wait seven days.

Then open your own log file with no memory of what you did, diagnose it from the logs alone, fix it, and write a one page post mortem with a preventive control.

If your logs were not good enough to diagnose it, you failed the boss and the real lesson is the logging, not the bug.

### Loot Drop
`breakpoint()`. Built in since Python 3.7, drops you straight into the debugger at that line with everything alive. Delete your print statements.

### Achievement: **Reproducible** (Uncommon)
*Hand someone your repo. They run it successfully without asking you a single question.*

---

## LEVEL 4: ADEPT
*NumPy, pandas, and the data layer*

### Skip Test (pass and bank 400 XP)
1. Explain broadcasting using a concrete 2D plus 1D example.
2. In pandas, when does an operation return a view and when a copy, and what breaks because of it?
3. Rewrite a four step reassignment chain (`df = df[...]; df["x"] = ...; df = df.groupby(...)`) as a single method chain.
4. What does `groupby().transform()` do that `groupby().agg()` cannot?

### Concepts (10 XP each)
NumPy arrays, dtypes, vectorisation, broadcasting, `axis` semantics, boolean masking, `where`. Pandas: Series and DataFrame, indexes and why they cause pain, `loc` versus `iloc`, method chaining with `assign` and `pipe`, `groupby` with `agg` and `transform`, `merge` and its validate argument, reshaping with `pivot_table` and `melt`, categorical dtypes, and the datetime accessor. Then DuckDB: querying a DataFrame with SQL directly, which for you is a shortcut most Python learners never find.

### The SQL Bridge (worth 100 XP, do it early)
You think relationally. Lean into it rather than fighting it.

```python
import duckdb
duckdb.sql("SELECT segment, AVG(responded) FROM df GROUP BY 1").df()
```

That works on any DataFrame in memory, on Parquet files, on CSVs, with no server and no setup. For your first few months in pandas, dropping into SQL for the hard parts and back out for the rest will make you productive in a week rather than a quarter. It is not cheating. It is using the thing you are already excellent at.

### Main Quest: The Campaign Dataset Builder (100 XP)
Build a proper analytical dataset from your synthetic campaign data, as a chained pandas pipeline with no intermediate reassignment:

- Join contacts, responses and customer attributes with `validate=` set correctly on every merge
- Derive recency, frequency and monetary features
- Bucket into segments
- Produce a response rate matrix by segment and channel
- Flag every row where the data contradicts itself

Then do the whole thing again in DuckDB SQL and compare the two for readability. Keep both in the repo. Write a paragraph on which you would hand to a colleague.

### Side Quest: The Memory Audit (50 XP)
Load a 2 million row DataFrame. Measure its memory with `df.info(memory_usage="deep")`. Then halve it: downcast numerics, convert low cardinality strings to categoricals, parse dates properly. Record the before and after. Write one line explaining why a categorical is cheaper.

### Side Quest: Grosvenor Redux (50 XP)
Your VBA automation at Grosvenor cut a daily process from an hour to fifteen minutes. Rebuild that process in Python on synthetic data, and time it. Then write three sentences comparing the two approaches honestly, including anything VBA did better.

### Boss Fight: THE DIRTY HANDOVER (250 XP)
Ninety minutes, timed, one attempt.

Generate (or have an assistant generate) a 500,000 row campaign file with planted defects: mixed date formats, trailing whitespace, duplicate keys with subtle differences, encoding artefacts, numeric columns stored as text with thousands separators, and a column where four percent of values are a sentinel like `-999`.

Deliver three things inside ninety minutes: a documented list of every defect you found, a cleaned Parquet output, and a reconciliation report proving row counts and totals tie back to source.

Re-run this boss with a fresh file once a month, forever. It is precisely the shape of a technical take home test, and it stays sharp only with repetition.

### Loot Drop
`df.pipe(lambda d: (print(d.shape), d)[1])`. Insert a debug print into the middle of a method chain without breaking the chain.

### Achievement: **Chain of Custody** (Rare)
*Write a twelve step pandas pipeline with zero intermediate variables, and have it still be readable.*

---

## LEVEL 5: ARTISAN
*Idiomatic Python, objects, generators, decorators*

### Skip Test (pass and bank 450 XP)
1. What is the difference between `__str__` and `__repr__`, and which should a data class prioritise?
2. What does `yield` actually do to a function, mechanically?
3. Write a decorator that takes an argument. Explain what happens at import time versus call time.
4. When is a `dataclass` the right answer and when is a plain dict better?

### Concepts (10 XP each)
The data model and the idea that Python is a protocol language: implement `__iter__` and every tool in the language works on your object for free. `__init__`, `__repr__`, `__eq__`, `__len__`, `__getitem__`, `__enter__` and `__exit__`. Dataclasses, frozen dataclasses, `field(default_factory=...)`. Enums instead of magic strings. Generators and `yield`, generator pipelines, laziness. Decorators, `functools.wraps`, `functools.cache`, `partial`, `singledispatch`. `itertools`: `groupby`, `chain`, `islice`, `pairwise`, `accumulate`. Type hints and what `mypy` catches.

### Main Quest: The KiwiSaver Rebuild (100 XP)
This is the highest leverage exercise in Act One.

Your award winning ANZ KiwiSaver campaign pipeline involved fuzzy matching and a QC framework. Rebuild it in idiomatic Python on synthetic data:

- A `MatchCandidate` frozen dataclass instead of loose tuples
- A generator pipeline: read, then normalise, then score, then filter, then report. Nothing materialises until the end
- `rapidfuzz` for the scoring
- A custom exception hierarchy for quality failures
- A `Counter` based QC summary
- Full type hints, passing `mypy`

You know this domain completely, so every ounce of attention goes to the Python. That is the point.

### Side Quest: The Protocol Object (50 XP)
Build a `CampaignResults` class that supports `len()`, iteration, indexing, `in`, and printing nicely. Then demonstrate that it works with `sorted()`, `list()`, a `for` loop and a comprehension without you writing any extra code. That moment is when the data model clicks.

### Side Quest: The Decorator Toolkit (50 XP)
Write three decorators you will actually reuse: `@timed` (logs execution time), `@retry(times=3)` (retries on exception with backoff), and `@validate_schema(expected_columns)` (raises if a returned DataFrame is missing columns). Put them in a `utils` module in your repo.

### Boss Fight: THE HOSTILE REVIEW (250 XP)
Open a pull request against your own repo containing the KiwiSaver Rebuild. Then prompt an assistant: *"You are a staff Python engineer known for harsh, specific code review. Review this diff for idiom, naming, error handling and design. Do not rewrite anything. Leave line comments only."*

You clear the boss by responding to every single comment: either fixing it, or writing a defence of why you disagree. The defences are worth more than the fixes. Taste forms when you argue.

### Loot Drop
`functools.cache` on a pure function. Sometimes a thousandfold speedup for one line of code.

### Achievement: **Artisan** (Rare)
*Someone else reads your code and does not need to ask you what it does.*

### END OF ACT ONE
At this point you have crossed from "writes Python scripts" to "writes Python". Bank the XP. Act Two is where it earns money.

---

# ACT TWO: THE INSTRUMENT

*From here, Python is not the subject. Measurement is. You are building toward being the person who can prove, defensibly, whether a campaign worked.*

---

## LEVEL 6: EXPERIMENTER
*Sample sizing, minimum detectable effect, power, experiment design*

**Starting position:** you have already done significance testing in Excel, and the Ministry of Justice industrial action analysis is a real applied example of it. So you skip the entry level and start where most analysts stop: asking the question in reverse.

Significance testing asks "given this result, is it real?". Sample sizing asks "how large must the control group be to detect a lift of a given size, before we spend the money?". Same mathematics, but one of them happens after the campaign and one of them makes you useful before it.

### Concepts (10 XP each)
Statistical power, and why 80% is a convention rather than a law. Type I and Type II error, and the business cost asymmetry between them (a false positive ships a bad offer, a false negative kills a good one). Minimum detectable effect. Sample size formulas for proportions and for means. `statsmodels.stats.power`: `NormalIndPower`, `proportion_effectsize`, `tt_ind_solve_power`. Effect sizes, Cohen's h and d. Confidence intervals, and why they communicate better than p values to a stakeholder. Multiple comparisons and the family wise error problem when you test eleven segments. Sequential testing and the peeking problem. Randomisation units: customer, household, or geography, and why the wrong unit invalidates everything. Holdout group design. Contamination and spillover.

### Main Quest: The Sample Size Calculator (100 XP)
Build a real tool, not a notebook. A module plus a CLI that takes baseline conversion rate, minimum detectable effect, power, significance level and expected daily volume, and returns required sample size per arm and days to run.

Then extend it with the three things that make it genuinely useful in a campaign setting:

- Handle unequal split ratios (90/10 holdouts are normal and change the maths)
- Handle a revenue metric as well as a conversion rate (means, not just proportions)
- Output a plain English sentence a marketing manager can act on: "To detect a 2 percentage point lift on a 12% baseline at 80% power, you need 4,700 customers in each arm, which is 9 days at current volume."

That last output is the deliverable. The maths is table stakes. Being the analyst who hands over a sentence instead of a spreadsheet is the differentiator.

### Side Quest: The Power Curve (50 XP)
Plot minimum detectable effect against sample size for three baseline rates. Then write the three sentences you would say in a meeting when someone asks why you cannot measure a 0.5% lift on a 3,000 person campaign. Having that explanation ready, with a chart, is a genuinely common moment.

### Side Quest: The Peeking Simulation (50 XP)
Simulate an A/B test with no true effect. Check for significance after every 100 observations and stop as soon as p is under 0.05. Run it a thousand times. Record how often you declared a false win.

The number is around 20 to 30 percent rather than the 5 percent people assume. Demonstrating this once, with your own code, is what makes you refuse to peek for the rest of your career.

### Side Quest: The MoJ Rewrite (50 XP)
Redo the Ministry of Justice industrial action analysis in Python on reconstructed data. Then add what you did not do at the time: a formal seasonal decomposition, a confidence interval on the effect, and a power calculation showing what size of effect you *could* have detected given the sample you had.

Your current telling of that story is a stakeholder story. This converts it into a statistical one, which is how it should lead for measurement roles.

### Boss Fight: THE EXPERIMENT DESIGN BRIEF (250 XP)
Sixty minutes, timed, written deliverable, no code required.

A product manager wants to test a new onboarding email sequence. They tell you: 40,000 customers per month, current 30 day activation rate of 18%, and they "think it will help a lot". They want results in two weeks.

Produce a one page design: randomisation unit, split, sample size, minimum detectable effect achievable in two weeks, what you would measure as primary and secondary metrics, guardrail metrics, how long it actually needs to run, and the honest paragraph about what you cannot tell them in two weeks.

You clear the boss if the document would survive a sceptical stakeholder who wants the answer faster.

### Loot Drop
`scipy.stats.bootstrap`. A confidence interval for literally any statistic, with no distributional assumptions, in three lines. When someone asks for a CI on a median or a ratio, this is the answer.

### Achievement: **Before, Not After** (Rare)
*Be consulted on a test design before it launches rather than asked to rescue it afterwards.*

---

## LEVEL 7: CAUSALIST
*Uplift modelling, incrementality, causal inference*

This is the deepest moat in campaign analytics and the hardest thing to fake. Most campaign analysts report response rates. A causalist reports incremental value, which is a completely different and much more defensible number.

### Concepts (10 XP each)
The fundamental problem of causal inference: you never observe both outcomes for the same person. Correlation, confounding, and selection bias in targeted campaigns (your responders look better because you targeted better customers, not because the campaign worked). Average treatment effect versus conditional average treatment effect. Uplift as the difference in response probability between treated and untreated, per individual. The four quadrant framework: persuadables, sure things, lost causes, and sleeping dogs. Sleeping dogs are the important one, because targeting them actively destroys value, and response modelling cannot see them at all.

Then the methods: two model (T learner) and single model with treatment interaction (S learner), uplift trees, X learner. Qini curves and the Qini coefficient. Uplift decile charts. Propensity score matching for when you have no control group. Difference in differences. Geo experiments and matched market tests. Synthetic control, briefly.

### Main Quest: The Uplift Model (100 XP)
Using the Hillstrom email dataset (a free, well known marketing uplift dataset with a real randomised treatment) or synthetic data if you prefer:

- Build a conventional response model first. Note who it would target
- Build a two model uplift estimator
- Build an S learner with a treatment interaction term
- Produce Qini curves for all three and compare
- Identify the sleeping dogs: the segment where contact *reduces* response
- Quantify the business impact: "targeting by uplift rather than response, at the same contact volume, increases incremental conversions by X"

That final sentence is the entire value proposition of uplift modelling, and it is a sentence very few analysts in the Australian market can produce from their own work.

### Side Quest: The Sleeping Dog Hunt (50 XP)
On your model output, isolate the negative uplift segment and characterise it. Who are they? Why might contact hurt? Write the half page you would send to a campaign manager recommending they be suppressed, with the estimated value of suppressing them.

### Side Quest: No Control Group (50 XP)
The common real world situation: the campaign already ran, with no holdout. Implement propensity score matching to construct a synthetic control from non contacted customers. Then write the honest caveats paragraph: what this can and cannot tell you, and what you would insist on next time.

That caveats paragraph is the professional skill. The matching is the easy part.

### Side Quest: The Incrementality Explainer (50 XP)
Build a small interactive visual (matplotlib is fine) that shows a non technical audience the difference between response rate and incremental lift, using one worked campaign. Present it to someone who does not work in data. If they get it, you clear the quest.

### Boss Fight: THE CHALLENGED RESULT (250 XP)
Twenty minutes, spoken aloud, no slides, one visual.

You present an uplift finding: the campaign the business is proud of generated almost no incremental value, because most responders would have converted anyway. Have an assistant role play a marketing director with budget tied to that campaign's reported ROI, who does not believe you and has an incentive not to.

Defend it for twenty minutes. No jargon. No hiding behind methodology. You clear the boss when you can hold the position with the same calm you used on the Ministry of Justice national manager, and when you can explain the method in terms they can repeat to their own boss.

Record it. Watch it back. That is where the real feedback is.

### Loot Drop
`causalml` and `scikit-uplift`. Two open source libraries implementing uplift estimators and Qini metrics so you do not hand roll them. Learn the maths first, then use the library, never the reverse.

### Achievement: **The Counterfactual** (Epic)
*Tell a business their favourite campaign did nothing, prove it, and still be in the room afterwards.*

---

## LEVEL 8: ENGINEER
*Testing, packaging, reproducibility, simulation*

An uplift number nobody can reproduce is an opinion. This level converts your analysis into something that survives scrutiny, which in a regulated environment is the whole ballgame.

### Concepts (10 XP each)
pytest: fixtures, parametrisation, `conftest.py`, `tmp_path`, monkeypatching. Testing data transformations with small hand built input and expected output frames. Property based testing with Hypothesis: assert properties that hold for all inputs rather than specific cases. Strict type checking with `mypy`. Pydantic for validating inputs at system boundaries. Packaging with `pyproject.toml` and `uv build`. Pre commit hooks. GitHub Actions running lint, type check and tests on every push. Seeding randomness so results reproduce exactly. Simulation as a testing method: if your estimator cannot recover a known effect you injected, it is broken.

### Main Quest: The Measurement Package (100 XP)
Turn your Level 6 sample size calculator and Level 7 uplift code into one installable package: `campaign-measurement`.

- Full test suite above 85% coverage
- Hypothesis tests on the statistical functions (sample size must never be negative; it must increase monotonically as MDE decreases)
- Strict type hints
- `pyproject.toml`, CI pipeline, CHANGELOG, README with worked examples
- Published to PyPI

A published Python package answers the "is he actually technical?" question permanently, and it does so before anyone interviews you.

### Side Quest: The Simulation Test (50 XP)
The most important test in all of measurement work. Generate synthetic data where you *know* the true uplift because you injected it. Run your estimator. Does it recover the true value inside its confidence interval?

Vary the true effect across a range and plot estimated against actual. Any deviation from the diagonal is a bug in your method, not in the data. Almost nobody does this and it catches real errors.

### Side Quest: The Hostile Inheritance (50 XP)
Fork a small, messy, real open source Python project. Without adding features: write characterisation tests around the existing behaviour, add type hints incrementally, and refactor one module. Six hours, time boxed.

This simulates the first six weeks of any contract you take, and it is excellent preparation for the "how would you approach an unfamiliar codebase" interview question.

### Boss Fight: THE REPRODUCIBILITY AUDIT (250 XP)
Hand your repo to someone else (or to a fresh environment with no help from you). They must be able to clone it, install it, run the full analysis, and get *byte identical* numbers to the ones in your README.

You fail if they have to ask you a single question. You fail if a seed was unset. You fail if a path was absolute. You fail if a dependency was unpinned.

This is the exact standard a regulator would apply, and the exact standard most analytics work does not meet.

### Loot Drop
`pytest -x --lf`. Stop at the first failure, and on the next run start from where it failed. Halves your debugging loop immediately.

### Achievement: **Byte Identical** (Epic)
*Someone reproduces your result exactly, on a different machine, a month later.*

---

## LEVEL 9: ARCHITECT
*Performance, pipelines, production measurement*

### Concepts (10 XP each)
Profiling before optimising, always: `cProfile`, `py-spy`, `scalene`. The cost model: attribute lookup, function call overhead, why vectorised beats looped. Memory: reference counting, `__slots__`, why pandas uses several times the memory of your source file. Polars and lazy evaluation. Parquet and Arrow. Concurrency and when each kind applies: threading for I/O, multiprocessing for CPU, asyncio for high concurrency I/O. The GIL, what it prevents and what it does not. Then the production side: scheduling, orchestration, monitoring an experiment while it runs, guardrail metric alerting, and automated stopping rules.

### Main Quest: The Measurement Platform (100 XP)
Build the end to end thing:

- Ingest campaign and response data on a schedule, with retries and logging
- Land it to Parquet, load to BigQuery or DuckDB
- Transform with a proper modelled layer (this is where your dbt work connects, if you want it to)
- Run the uplift estimation as a scheduled job
- Output a dashboard showing incremental lift per campaign with confidence intervals, not just response rates
- A data quality gate that fails the pipeline rather than warning, when a contract breaks
- A written one page architecture decision record

This single project demonstrates the entire job you are aiming at. It is worth more in an interview than any certificate.

### Side Quest: The Fifty Times Speedup (50 XP)
Take the slowest thing you have built in this quest and make it fifty times faster, with evidence. Profile first, state a hypothesis for each change, measure after each one, and reject any optimisation that does not show a measured win. Write it up with before and after numbers.

### Side Quest: The Guardrail Monitor (50 XP)
Build a monitor that watches a running experiment and alerts when a guardrail metric (unsubscribes, complaints, cost per acquisition) degrades beyond a threshold. Include the stopping rule and the logic for distinguishing a real problem from noise.

### Boss Fight: THE CAPACITY BRIEF (250 XP)
You are told the nightly measurement job processing 2 million rows must handle 200 million within six months, on the same budget.

Produce a written technical assessment: where it breaks first, what profiling shows, three architectural options with cost and complexity trade offs, and a recommendation. Then implement the recommendation and prove it with benchmarks.

### Loot Drop
`py-spy top --pid <pid>`. Profile a *running* process with no code changes and no restart. `py-spy dump --pid <pid>` gets you a stack trace of a hung process. This alone will make you the person people call.

### Achievement: **Architect** (Epic)
*Draw your pipeline end to end on a whiteboard, name every failure mode, and name the control that catches each.*

---

## LEVEL 10: GRANDMASTER
*Publish, teach, contribute, New Game Plus*

There is no boss fight here. Mastery is not a level you clear; it is four practices you do not stop.

### The Four Practices

**Publish (250 XP per piece, repeatable).** Write up the peeking simulation, the sleeping dog finding, the sample size calculator, the reproducibility standard. The campaign analytics community is small and unusually receptive to practitioner writing, and it is the cheapest inbound channel a contractor has.

**Contribute (500 XP).** One merged pull request to a library with more than a thousand stars. Start with documentation on something you actually use: `causalml`, `scikit-uplift`, `statsmodels`, `polars`. It is permanent, verifiable, and no CV bullet matches it.

**Teach (250 XP per session, repeatable).** You come from a family of teachers and the instinct is already there: the Venn diagram explanation of a cartesian join, the code repositories you build to share with teams. Formalise it. Present at a Sydney Python or PyData meetup. Mentor on Exercism. You will discover what you do not understand within thirty seconds of trying to explain it.

**Read source (50 XP per session, weekly).** Fifteen minutes a week reading a library you use. Start small and beautifully written: `attrs`, `tenacity`, `typer`. Style is absorbed, never taught.

### Achievement: **Grandmaster** (Legendary)
*Earn 8,500 XP. Everything in your repo runs, is tested, and has a reader other than you.*

### NEW GAME PLUS
Run the whole ladder again, in a harder mode of your choosing:

- **Hard mode:** no AI assistance at any point, for ninety days
- **Speedrun mode:** every boss fight at half the time limit
- **Depth mode:** take one Act Two level and go to genuine research depth. Causal inference is a field, not a technique, and Level 7 only scratches it
- **Teaching mode:** run the entire ladder with someone else, as their mentor. You will find the gaps instantly

---

## THE DAILY AND WEEKLY LOOP

**Daily (15 to 30 min): The Kata.** One small problem. Sources, in order of usefulness to you: Exercism's Python track with a mentor review requested (free, human, and the mentors are ruthless about idiom), Python Morsels (paid, exceptional written explanations of every alternative solution), Advent of Code archives, or a single function extracted from whatever you are building.

**Weekly (one block of 3 to 4 hours): The Quest.** One main or side quest. Uninterrupted. Phone elsewhere.

**Weekly (30 min): The Ledger.** Update XP, note the streak, and write one paragraph on what you learned. That paragraph becomes your blog later, and the act of writing it is what moves things into long term memory.

**Monthly: The Boss Rematch.** Re-run the Dirty Handover with a fresh file, timed. It is the single best proxy for a technical take home test and it degrades fast without practice.

---

## THE LEDGER

Keep this at the top of your repo README. Update it weekly. Watching the number move is the entire mechanic.

```
PYTHON QUEST: LEDGER
Started:            ____________
Current level:      ____ / 10
XP:                 ______ / 8,500
Current streak:     ____ days     Multiplier: x____
Longest streak:     ____ days

QUESTS CLEARED
Level 1  [ ][ ][ ]      Boss [ ]    Skip test [ ]
Level 2  [ ][ ][ ]      Boss [ ]    Skip test [ ]
Level 3  [ ][ ][ ]      Boss [ ]    Skip test [ ]
Level 4  [ ][ ][ ]      Boss [ ]    Skip test [ ]
Level 5  [ ][ ][ ]      Boss [ ]    Skip test [ ]
Level 6  [ ][ ][ ][ ]   Boss [ ]
Level 7  [ ][ ][ ][ ]   Boss [ ]
Level 8  [ ][ ][ ]      Boss [ ]
Level 9  [ ][ ][ ]      Boss [ ]
Level 10 ongoing

ACHIEVEMENTS
[ ] Hello Again            (Common)
[ ] Comprehension Fluency  (Uncommon)
[ ] Reproducible           (Uncommon)
[ ] Chain of Custody       (Rare)
[ ] Artisan                (Rare)
[ ] Before, Not After      (Rare)
[ ] The Counterfactual     (Epic)
[ ] Byte Identical         (Epic)
[ ] Architect              (Epic)
[ ] Grandmaster            (Legendary)

HIDDEN ACHIEVEMENTS (discovered by doing, not by reading)
[ ] ???    [ ] ???    [ ] ???
```

The three hidden achievements unlock for: using something you built here in paid work; someone else using a tool you wrote; and answering a question in an interview with "I built that, here is the repo".

---

## GAME OVER CONDITIONS

The ways this run ends badly, and how to avoid each.

| Failure | What it looks like | The save |
|---|---|---|
| **Tutorial hopping** | Six courses open, nothing shipped | No new resource until the current quest is in the repo |
| **Notebook graveyard** | Everything lives in `Untitled7.ipynb` | Modules from Level 4 onward. Notebooks are for exploring, not delivering |
| **AI first draft** | The code works and you cannot explain it | Write first, review second. Zero XP otherwise, and you will know |
| **Grinding Act One** | Comfortable with syntax, never reach measurement | Take the skip tests honestly. Levels 1 to 3 should be weeks, not months |
| **Theory spiral** | Three months on causal inference papers, no model built | Build first, descend into theory afterwards, not before |
| **Invisible work** | Excellent code, all of it local | Public repo. Weekly commits. The history is the credential |
| **Streak perfectionism** | Miss two days, abandon the game | The streak resets, the XP does not. Start the streak again tomorrow |

---

## WHY THIS LADDER AND NOT ANOTHER ONE

A note on the shape of it, since you should understand the design and not just follow it.

Act One is shorter than it looks because you are not a beginner and the skip tests exist to let you prove it. The risk for you was never difficulty; it was plateauing at competent scripter, which is why Level 5 is heavier than Levels 1 to 4 combined and why the KiwiSaver rebuild sits there.

Act Two is the entire point. Sample sizing, uplift modelling and incrementality are a narrow, deep, defensible specialisation, and they are the part of campaign analytics that most practitioners cannot do. Your mathematics degree, your campaign delivery background in Unica and IBM Campaign, and the fact that you have already done significance testing on real data mean you start Act Two further along than almost anyone else attempting it.

Level 8 exists because a measurement result that cannot be reproduced is worthless in financial services, and reproducibility is an engineering skill rather than a statistical one. It is the step most analysts skip, and it is the one that makes a regulator's question answerable.

And the boss fights are mostly not coding problems. The Experiment Design Brief, the Challenged Result, the Reproducibility Audit and the Capacity Brief are all judgement and communication, because that is where sixteen years of experience is visible and where a bootcamp graduate has nothing.

---

*Level 1 starts with the skip test. Take it tonight, and if you pass it, you are already 250 XP in.*
