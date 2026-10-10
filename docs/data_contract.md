# Proposed Ball-by-Ball Data Contract

**Status: preliminary, not source-verified.** Adapt and document this contract once a dataset is chosen.

| Field | Type | Meaning |
|---|---|---|
| match_id | identifier | Stable source match ID |
| innings | integer | Innings number |
| over | integer | Source over number, usually starting at zero |
| ball | number | Source delivery number within over; **not** assumed to be a legal-ball count |
| striker | string | Batter ID/name according to source |
| bowler | string | Bowler ID/name according to source |
| batter_runs | integer | Runs credited to batter |
| total_runs | integer | All runs scored on event, including extras |
| is_wide | 0 or 1 | Delivery was wide |
| is_no_ball | 0 or 1 | Delivery was no-ball |

## Cautions
- Cricket datasets differ in how illegal deliveries are recorded; repeated over/ball labels can be legitimate, so do **not** deduplicate on `match_id + over + ball` alone.
- Wickets, bye/leg-bye extras, penalty runs, super overs, retired out and DLS require source-specific handling before production calculations.
- An event with no ball faced by striker can still have a delivery record. Define exclusions carefully.
- Keep unprocessed licensed source files out of Git until redistributability is confirmed.

Synthetic test examples are for development only; they are **not** IPL observations.
