---
type: formula
output: "[[Residual Loss (MWh)]]"
excel_column: BO
kind: "calculated"
variables: ["[[Actual Production (MWh)]]", "[[Plant Availability Loss (MWh)]]", "[[Plant Performance (PR) gap (MWh)]]", "[[Expected Energy - Controllable (MWh)]]"]
tags: [formula, availability-loss-breakdown]
---

# Residual Loss (MWh) (formula)

Produces [[Residual Loss (MWh)]]  |  Excel column BO  |  Group: Availability & Loss Breakdown

## Math

$$
R_{loss} = E_{act} - \left(L_{plant} + \Delta E_{PR}\right) - E_{ctrl}
$$

## In plain English

Actual production minus (plant availability loss + PR gap) minus expected controllable energy. Together with Residual BU Gap this feeds the Data QA flag.

## Inputs

- [[Actual Production (MWh)]] (MWh)
- [[Plant Availability Loss (MWh)]] (MWh)
- [[Plant Performance (PR) gap (MWh)]] (MWh)
- [[Expected Energy - Controllable (MWh)]] (MWh)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =[Actual Production [MWh]]-SUM([Plant Availability Loss (MWh)],[Plant Performance (PR) gap [MWh]])-[Expected Energy - Controllable (MWh)]
> ```
