---
type: formula
output: "[[Expected Prod - BU Assumptions (MWh)]]"
excel_column: W
kind: "calculated"
variables: ["[[Actual MWp]]", "[[Expected Irradiation P50 POA (kWh-m2)]]", "[[Expected Plant Availability]]", "[[Expected Grid Availability]]", "[[Expected Performance Ratio (PR)]]", "[[Other external losses]]"]
tags: [formula, production-vs-budget]
---

# Expected Prod - BU Assumptions [MWh] (formula)

Produces [[Expected Prod - BU Assumptions (MWh)]]  |  Excel column W  |  Group: Production vs Budget

## Math

[[Expected Prod - BU Assumptions (MWh)]] = [[Actual MWp]] × [[Expected Irradiation P50 POA (kWh-m2)]] × ([[Expected Plant Availability]] + [[Expected Grid Availability]] + [[Expected Performance Ratio (PR)]] − [[Other external losses]] − 2)

## In plain English

The bracket works out to PR minus other external losses minus plant unavailability (1 - expected plant availability) minus grid unavailability (1 - expected grid availability), i.e. an additive-loss model. The '-2' is what turns the two availabilities into their losses.

## Inputs

- [[Actual MWp]] (MWp)
- [[Expected Irradiation P50 POA (kWh-m2)]] (kWh/m2 per day)
- [[Expected Plant Availability]] (ratio)
- [[Expected Grid Availability]] (ratio)
- [[Expected Performance Ratio (PR)]] (ratio)
- [[Other external losses]] (ratio)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =[Actual MWp]*[Expected Irradiation P50 POA [kWh/m2]]*([Expected Plant Availability]+[Expected Grid Availability]+[Expected Performance Ratio (PR)]-[Other external losses]-2)
> ```
