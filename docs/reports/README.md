# Technical reports

The **long-form, no-page-limit record**. Where the paper is a disciplined 8-page compression of
the result, the technical report is the maximal version: full derivations, engineering detail,
dead ends, and negative results that don't fit an arXiv submission but are the most valuable
thing to a future researcher (often yourself, in six months).

> **Write the report as you go, not after.** If the report is current, the paper is an editing
> job — you're selecting and tightening, not writing from a blank page. This is the single
> highest-leverage habit in the repo.

## Layout

```
reports/
├── README.md              this index
├── TEMPLATE.md            copy for a new report
└── main/                  the primary technical report (grows weekly)
    └── report.md
```

## What belongs here (and not in the paper)

| Belongs in the report | Belongs in the paper |
|-----------------------|----------------------|
| Every proof step, including the ugly ones | The clean statement + proof sketch |
| Negative results, failed bounds, what didn't work | (maybe one line in limitations) |
| Engineering notes: hooks, patching gotchas, numerics | (nothing) |
| All ablations and diagnostics | The 1–2 that make the point |
| The reasoning behind scope cuts | (nothing) |

## Reports

| Report | Scope | Status |
|--------|-------|--------|
| [main/report.md](main/report.md) | The full account of the bound, the allocation rule, and its validation. | 🌱 outline |
