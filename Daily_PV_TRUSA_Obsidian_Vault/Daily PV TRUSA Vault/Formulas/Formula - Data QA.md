---
type: formula
output: "[[Data QA]]"
excel_column: BQ
kind: "calculated"
variables: ["[[Residual BU Gap (MWh)]]", "[[Residual Loss (MWh)]]"]
tags: [formula, comments-qa]
---

# Data QA (formula)

Produces [[Data QA]]  |  Excel column BQ  |  Group: Comments & QA

## Math

$$
\text{Data QA} = \left(|R_{BU}| > 50\right) \lor \left(|R_{loss}| > 50\right)
$$

## In plain English

TRUE if either residual is more than 50 MWh in absolute value. The 50 MWh threshold is hardcoded.

## Inputs

- [[Residual BU Gap (MWh)]] (MWh)
- [[Residual Loss (MWh)]] (MWh)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =OR([Residual BU Gap [MWh]]>50,[Residual BU Gap [MWh]]<-50,[Residual Loss (MWh)]>50,[Residual Loss (MWh)]<-50)
> ```
