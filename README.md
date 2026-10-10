# IPL Analytics Pipeline 🏏

**Status:** Foundation stage — no match statistics or model performance claims yet.

## Decision question
Which IPL players create the most value relative to their role, opportunities and (when reliable auction data is available) acquisition cost?

This project will connect **cricket analysis, business decisions and reproducible data workflows**, using Python, SQL and Power BI.

## Planned analytical workflow
1. **Ingest** licensed/public match-level or ball-by-ball datasets; record source, years, rights and update cadence.
2. **Validate** schema, match/player IDs, missing values and batting/bowling innings.
3. **Transform** observations to reproducible phase- and role-aware player features.
4. **Evaluate** metrics against simple baselines, holdout seasons and transparent assumptions.
5. **Visualise** insights in Power BI and communicate selection or auction decisions.

## Initial metric definitions (proposals, not validated findings)
- Batting: runs per ball, boundary share, phase-adjusted strike rate, sample size.
- Bowling: runs conceded per legal ball, wickets per ball, phase and venue context.
- Value: context-adjusted contribution per opportunity; compare with auction prices only when definitions align.

## Reproduce the starting point
```bash
python -m pip install -r requirements.txt
python -m pytest
```

`src/ipl_analytics/metrics.py` contains tested **elementary** cricket arithmetic. This does not yet represent a complete pipeline or a validated player impact model.

## Roadmap
- [ ] Identify and document legally reusable source dataset
- [ ] Implement ingestion, data dictionaries, automated data-quality checks
- [ ] Define role- and phase-adjusted metrics with stakeholder review
- [ ] Implement SQL analysis and reproducible exports
- [ ] Backtest or evaluate any predictive model, report uncertainty
- [ ] Build dashboard with sources, metric definitions and screenshots
- [ ] Publish decision memo with limitations and reproducible results

**Author:** Hitesh Srinivas · [LinkedIn](https://www.linkedin.com/in/hitesh-s-116380252/)
