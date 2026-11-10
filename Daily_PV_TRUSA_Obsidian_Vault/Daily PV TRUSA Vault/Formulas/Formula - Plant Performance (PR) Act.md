---
type: formula
output: "[[Plant Performance (PR) Act]]"
excel_column: AY
kind: "calculated"
variables: ["[[Production @100% avail]]", "[[Actual MWp]]", "[[Actual Irradiation GPOA (kWh-m2)]]"]
tags: [formula, expected-energy-performance-ratio]
---

# Plant Performance (PR) Act (formula)

Produces [[Plant Performance (PR) Act]]  |  Excel column AY  |  Group: Expected Energy & Performance Ratio

## Math

$$
PR_{act} = \frac{E_{100}}{P_{p,act} \cdot H_{GPOA}}
$$

## In plain English

Production at 100% availability divided by (MWp times POA irradiation). Blank if that production is blank.

## Inputs

- [[Production @100% avail]] (MWh)
- [[Actual MWp]] (MWp)
- [[Actual Irradiation GPOA (kWh-m2)]] (kWh/m2 per day)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =IFERROR([Production @100% avail.]/([Actual MWp]*[Actual Irradiation GPOA [kWh/m2]]),"")
> ```
