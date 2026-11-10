---
type: formula
output: "[[Plant Availability Loss (MWh)]]"
excel_column: BJ
kind: "calculated"
variables: ["[[BoS Loss (MWh)]]", "[[Inverter Loss (MWh)]]", "[[DC Loss (MWh)]]", "[[Tracker Loss (MWh)]]"]
tags: [formula, availability-loss-breakdown]
---

# Plant Availability Loss (MWh) (formula)

Produces [[Plant Availability Loss (MWh)]]  |  Excel column BJ  |  Group: Availability & Loss Breakdown

## Math

$$
L_{plant} = L_{BoS} + L_{inv} + L_{DC} + L_{trk}
$$

## In plain English

Sum of BoS, inverter, DC and tracker losses.

## Inputs

- [[BoS Loss (MWh)]] (MWh)
- [[Inverter Loss (MWh)]] (MWh)
- [[DC Loss (MWh)]] (MWh)
- [[Tracker Loss (MWh)]] (MWh)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =SUM([BoS Loss (MWh)]:[Tracker Loss (MWh)])
> ```
