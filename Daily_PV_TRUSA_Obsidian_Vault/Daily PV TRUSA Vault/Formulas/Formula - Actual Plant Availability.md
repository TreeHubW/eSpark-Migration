---
type: formula
output: "[[Actual Plant Availability]]"
excel_column: AL
kind: "site-data pull"
variables: ["[[Site Name]]", "[[Date]]"]
sources: ["[[Site Data Source Map]]"]
tags: [formula, plant-availability]
---

# Actual Plant Availability (formula)

Produces [[Actual Plant Availability]]  |  Excel column AL  |  Group: Plant Availability

## Math

$$
A_{plant}^{act} = \text{value from the site's own data sheet on the matching Date}
$$

## In plain English

Nested IF on Site Name, AVERAGEIFS on Date, wrapped in IFERROR (returns '!' on failure). See [[Site Data Source Map]].

## Inputs

- [[Site Name]] (text)
- [[Date]] (date)

## Data sources

- [[Site Data Source Map]]

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =IFERROR(IF([Site Name]="Oberon 1A",AVERAGEIFS(Oberon[Availability (%)],Oberon[Date],[Date]),IF([Site Name]="Rayos del Sol",AVERAGEIFS(RayosData!N:N,RayosData!A:A,[Date]),IF([Site Name]="Ellis",AVERAGEIFS(EllisData!N:N,EllisData!A:A,[Date]),IF([Site Name]="Myrtle",AVERAGEIFS(Myrtle[Availability (%)],Myrtle[Date],[Date]),IF([Site Name]="Danish",AVERAGEIFS(DanishData!Q:Q,DanishData!A:A,[Date]),IF([Site Name]="Skysol",AVERAGEIFS(SkysolData!Q:Q,SkysolData!B:B,[Date]),IF([Site Name]="Hill",AVERAGEIFS(Hill1Data!Q:Q,Hill1Data!A:A,[Date]),IF([Site Name]="Big Sky",AVERAGEIFS(BigSkyData!Q:Q,BigSkyData!B:B,[Date]),IF([Site Name]="Montpelier",AVERAGEIFS(MontpelierData!Q:Q,MontpelierData!B:B,[Date]),IF([Site Name]="Cottonwood",AVERAGEIFS(CottonwoodData!Q:Q,CottonwoodData!A:A,[Date]),IF([Site Name]="Brazoria",AVERAGEIFS(BrazoriaData!Q:Q,BrazoriaData!B:B,[Date]),IF([Site Name]="Clinton",AVERAGEIFS(ClintonData!Q:Q,ClintonData!B:B,[Date]),IF([Site Name]="Hill 2",AVERAGEIFS(Hill2Data!Q:Q,Hill2Data!B:B,[Date]),"!"))))))))))))),"!")
> ```
