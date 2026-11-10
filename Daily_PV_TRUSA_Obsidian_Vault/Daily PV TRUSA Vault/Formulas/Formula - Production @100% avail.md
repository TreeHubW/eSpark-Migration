---
type: formula
output: "[[Production @100% avail]]"
excel_column: AU
kind: "calculated"
variables: ["[[Actual Production (MWh)]]", "[[Actual Grid Availability]]", "[[Actual Plant Availability]]", "[[Grid Availability Loss (MWh)]]", "[[Plant Availability Loss (MWh)]]"]
tags: [formula, expected-energy-performance-ratio]
---

# Production @100% avail. (formula)

Produces [[Production @100% avail]]  |  Excel column AU  |  Group: Expected Energy & Performance Ratio

## Math

$$
E_{100} = \begin{cases} \text{blank} & E_{act} = 0 \\ \max\!\left(\dfrac{E_{act}}{A_{grid}^{act} + A_{plant}^{act} - 1},\; E_{act} - L_{grid} - L_{plant}\right) & \text{otherwise} \end{cases}
$$

## In plain English

Takes the larger of two reconstructions: scale production up by the two availabilities, or add back the grid and plant loss energies.

## Inputs

- [[Actual Production (MWh)]] (MWh)
- [[Actual Grid Availability]] (ratio)
- [[Actual Plant Availability]] (ratio)
- [[Grid Availability Loss (MWh)]] (MWh)
- [[Plant Availability Loss (MWh)]] (MWh)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =IF([Actual Production [MWh]]=0,"",MAX([Actual Production [MWh]]/([Actual Grid Availability]+[Actual Plant Availability]-1),[Actual Production [MWh]]-[Grid Availability Loss [MWh]]-[Plant Availability Loss (MWh)]))
> ```
