---
type: formula
output: "[[Actual Production (MWh)]]"
excel_column: Q
kind: "site-data pull"
variables: ["[[Site Name]]", "[[Date]]"]
sources: ["[[Site Data Source Map]]"]
tags: [formula, production-vs-budget]
---

# Actual Production [MWh] (formula)

Produces [[Actual Production (MWh)]]  |  Excel column Q  |  Group: Production vs Budget

## Math

$$
E_{act} = \text{value from the site's own data sheet on the matching Date}
$$

## In plain English

Nested IF on Site Name picks the right sheet/table for the site, then SUMIFS matches on Date. Returns '!' if the site is not in the list. See [[Site Data Source Map]].

## Inputs

- [[Site Name]] (text)
- [[Date]] (date)

## Data sources

- [[Site Data Source Map]]

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =IF([Site Name]="Oberon 1A",SUMIFS(OberonData!B:B,OberonData!A:A,[Date]),IF([Site Name]="Rayos del Sol",SUMIFS(RayosData!B:B,RayosData!A:A,[Date]),IF([Site Name]="Ellis",SUMIFS(EllisData!B:B,EllisData!A:A,[Date]),IF([Site Name]="Myrtle",SUMIFS(Myrtle[Myrtle Production (MWh)],Myrtle[Date],[Date]),IF([Site Name]="Danish",SUMIFS(Danish[Danish Production (MWh)],Danish[Date],[Date]),IF([Site Name]="Skysol",SUMIFS(Skysol[Production (MWh)],Skysol[Date],[Date]),IF([Site Name]="Cottonwood",SUMIFS(CottonwoodData!E:E,CottonwoodData!A:A,[Date]),IF([Site Name]="Big Sky",SUMIFS(BigSkyData!E:E,BigSkyData!B:B,[Date]),IF([Site Name]="Montpelier",SUMIFS(MontpelierData!E:E,MontpelierData!B:B,[Date]),IF([Site Name]="Clinton",SUMIFS(ClintonData!E:E,ClintonData!B:B,[Date]),IF([Site Name]="Hill",SUMIFS(Hill1Data!E:E,Hill1Data!A:A,[Date]),IF([Site Name]="Brazoria",SUMIFS(BrazoriaData!E:E,BrazoriaData!B:B,[Date]),IF([Site Name]="Hill 2",SUMIFS(Hill2Data!E:E,Hill2Data!B:B,[Date]),"!")))))))))))))
> ```
