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

[[Data QA]] = TRUE if either of these is true:

- the absolute value of [[Residual BU Gap (MWh)]] is greater than 50
- the absolute value of [[Residual Loss (MWh)]] is greater than 50

## In plain English

TRUE if either residual is more than 50 MWh in absolute value. The 50 MWh threshold is hardcoded.

## Inputs

- [[Residual BU Gap (MWh)]] (MWh)
- [[Residual Loss (MWh)]] (MWh)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =OR([Residual BU Gap [MWh]]>50,[Residual BU Gap [MWh]]<-50,[Residual Loss (MWh)]>50,[Residual Loss (MWh)]<-50)
> ```
