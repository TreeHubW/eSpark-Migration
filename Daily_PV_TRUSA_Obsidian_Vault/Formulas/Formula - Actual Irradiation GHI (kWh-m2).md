---
type: formula
output: "[[Actual Irradiation GHI (kWh-m2)]]"
excel_column: AD
kind: "site-data pull"
variables: ["[[Site Name]]", "[[Date]]"]
sources: ["[[Site Data Source Map]]"]
tags: [formula, irradiation]
---

# Actual Irradiation GHI [kWh/m2] (formula)

Produces [[Actual Irradiation GHI (kWh-m2)]]  |  Excel column AD  |  Group: Irradiation

## Math

[[Actual Irradiation GHI (kWh-m2)]] = value from the site's own data sheet on the matching [[Date]]

## In plain English

Same nested-IF pattern as the other pulls. See [[Site Data Source Map]].

## Inputs

- [[Site Name]] (text)
- [[Date]] (date)

## Data sources

- [[Site Data Source Map]]

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =IF([Site Name]="Oberon 1A",SUMIFS(Oberon[GHI (kW/m2/day)],Oberon[Date],[Date]),IF([Site Name]="Rayos del Sol",SUMIFS(RayosData!D:D,RayosData!A:A,[Date]),IF([Site Name]="Ellis",SUMIFS(EllisData!D:D,EllisData!A:A,[Date]),IF([Site Name]="Myrtle",SUMIFS(Myrtle[GHI (kW/m2/day)],Myrtle[Date],[Date]),IF([Site Name]="Danish",SUMIFS(Danish[GHI (kW/m2/day)],Danish[Date],[Date]),IF([Site Name]="Skysol",SUMIFS(Skysol[GHI (kW/m2/day)],Skysol[Date],[Date]),IF([Site Name]="Big Sky",SUMIFS(BigSkyData!G:G,BigSkyData!B:B,[Date]),IF([Site Name]="Montpelier",SUMIFS(MontpelierData!G:G,MontpelierData!B:B,[Date]),IF([Site Name]="Hill",SUMIFS(Hill1Data!G:G,Hill1Data!A:A,[Date]),IF([Site Name]="Cottonwood",SUMIFS(CottonwoodData!G:G,CottonwoodData!A:A,[Date]),IF([Site Name]="Clinton",SUMIFS(ClintonData!G:G,ClintonData!B:B,[Date]),IF([Site Name]="Brazoria",SUMIFS(BrazoriaData!G:G,BrazoriaData!B:B,[Date]),IF([Site Name]="Hill 2",SUMIFS(Hill2Data!G:G,Hill2Data!B:B,[Date]),"!")))))))))))))
> ```
