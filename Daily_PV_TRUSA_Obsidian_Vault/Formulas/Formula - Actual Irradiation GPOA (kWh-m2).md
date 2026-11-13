---
type: formula
output: "[[Actual Irradiation GPOA (kWh-m2)]]"
excel_column: Z
kind: "site-data pull"
variables: ["[[Site Name]]", "[[Date]]"]
sources: ["[[Site Data Source Map]]"]
tags: [formula, irradiation]
---

# Actual Irradiation GPOA [kWh/m2] (formula)

Produces [[Actual Irradiation GPOA (kWh-m2)]]  |  Excel column Z  |  Group: Irradiation

## Math

[[Actual Irradiation GPOA (kWh-m2)]] = value from the site's own data sheet on the matching [[Date]]

## In plain English

Same nested-IF pattern as Actual Production, using the irradiance column of each site's data. See [[Site Data Source Map]].

## Inputs

- [[Site Name]] (text)
- [[Date]] (date)

## Data sources

- [[Site Data Source Map]]

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =IF([Site Name]="Oberon 1A",SUMIFS(Oberon[Irradiance],Oberon[Date],[Date]),IF([Site Name]="Rayos del Sol",SUMIFS(RayosData!C:C,RayosData!A:A,[Date]),IF([Site Name]="Ellis",SUMIFS(EllisData!C:C,EllisData!A:A,[Date]),IF([Site Name]="Myrtle",SUMIFS(Myrtle[Irradiation (kW/m2/day)],Myrtle[Date],[Date]),IF([Site Name]="Danish",SUMIFS(Danish[Irradiation (kW/m2/day)],Danish[Date],[Date]),IF([Site Name]="Skysol",SUMIFS(Skysol[Irradiation (kW/m2/day)],Skysol[Date],[Date]),IF([Site Name]="Big Sky",SUMIFS(BigSkyData!F:F,BigSkyData!B:B,[Date]),IF([Site Name]="Hill",SUMIFS(Hill1Data!F:F,Hill1Data!A:A,[Date]),IF([Site Name]="Cottonwood",SUMIFS(CottonwoodData!F:F,CottonwoodData!A:A,[Date]),IF([Site Name]="Clinton",SUMIFS(ClintonData!F:F,ClintonData!B:B,[Date]),IF([Site Name]="Brazoria",SUMIFS(BrazoriaData!F:F,BrazoriaData!B:B,[Date]),IF([Site Name]="Montpelier",SUMIFS(MontpelierData!F:F,MontpelierData!B:B,[Date]),IF([Site Name]="Hill 2",SUMIFS(Hill2Data!F:F,Hill2Data!B:B,[Date]),"!")))))))))))))
> ```
