---
type: source
tags: [source]
---

# Monthly_techData

Table on the **Monthly PV TRUSA** sheet. One row per site per month. The Daily table looks values up here using Site Name and Month as the key.

## Daily variables fed by this monthly table

| Daily variable | Monthly column | Method |
|---|---|---|
| [[MWac]] | `MWac` | SUMIFS |
| [[MWp]] | `MWp` | SUMIFS |
| [[Actual MWp]] | `Actual MWp` | SUMIFS |
| [[2026 HQ BU Prod (MWh)]] | `2026 HQ BU Prod [MWh]` | SUMIFS / days in month |
| [[2026 techBU Prod (MWh)]] | `2026 techBU Prod [MWh]` | SUMIFS / days in month |
| [[Expected Irradiation P50 POA (kWh-m2)]] | `Expected Irradiation P50 POA [kWh/m2]` | SUMIFS / days in month |
| [[Model Irradiation GHI (kWh-m2)]] | `Expected Irradiation GHI [kWh/m2]` | SUMIFS / days in month |
| [[Expected Plant Availability]] | `Expected Plant Availability` | AVERAGEIFS |
| [[Expected Grid Availability]] | `Expected Grid Availability` | AVERAGEIFS |
| [[Other external losses]] | `Other external losses` | AVERAGEIFS |
| [[Expected Performance Ratio (PR)]] | `Expected Performance Ratio (PR)` | AVERAGEIFS |

Variables that carry a monthly total (budget production, irradiation) are divided by the number of days in the month to give a daily value. Variables that are ratios (availability, PR, losses) are averaged instead.
