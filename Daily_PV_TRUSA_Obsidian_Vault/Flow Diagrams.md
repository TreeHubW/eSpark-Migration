---
type: diagram
tags: [diagram]
---

# Flow Diagrams

## 1. The gap bridge

How the budget gap is explained. Each arrow into the residual is a term in its formula.

```mermaid
flowchart TD
  Q["Actual Production (MWh)"] --> T
  O["2026 HQ BU Prod (MWh)"] --> T
  T["Production Gap to BU (MWh)<br/>total gap to explain"]
  P["2026 techBU Prod (MWh)"] --> X
  O --> X
  X["HQ vs Tech BU Gap (MWh)"]
  AA["Irradiation Gap (MWh)"]
  AM["Availability BU Gap (MWh)"]
  AQ["Grid Availability BU Gap (MWh)"]
  AZ["Plant Performance (PR) gap (MWh)"]
  T --> BB
  X --> BB
  AA --> BB
  AM --> BB
  AQ --> BB
  AZ --> BB
  BB["Residual BU Gap (MWh)<br/>what is left over"]
  classDef cl fill:#ffe9c7,stroke:#c07a10,color:#222;
  class T,X,AA,AM,AQ,AZ,BB cl;
```

## 2. Full dependency flow

Every calculation in the Daily sheet, generated from the actual formulas. Purple = source tables, blue = monthly lookups, green = site-data pulls, orange = calculations. Site Name, Date and Month feed every lookup and are left out to keep it readable.

```mermaid
flowchart LR
  subgraph G2["Capacity"]
    n_K["MWac"]
    n_L["MWp"]
    n_M["Actual MWp"]
  end
  subgraph G3["Production vs Budget"]
    n_O["2026 HQ BU Prod (MWh)"]
    n_P["2026 techBU Prod (MWh)"]
    n_Q["Actual Production (MWh)"]
    n_T["Production Gap to BU (MWh)"]
    n_U["Production Gap to BU (%)"]
    n_W["Expected Prod - BU Assumptions (MWh)"]
    n_X["HQ vs Tech BU Gap (MWh)"]
  end
  subgraph G4["Irradiation"]
    n_Y["Expected Irradiation P50 POA (kWh-m2)"]
    n_Z["Actual Irradiation GPOA (kWh-m2)"]
    n_AA["Irradiation Gap (MWh)"]
    n_AB["Irradiation Gap (%)"]
    n_AC["Model Irradiation GHI (kWh-m2)"]
    n_AD["Actual Irradiation GHI (kWh-m2)"]
    n_AE["GHI Gap (%)"]
    n_AF["POA vs GHI % gap (vs model)"]
  end
  subgraph G6["Plant Availability"]
    n_AK["Expected Plant Availability"]
    n_AL["Actual Plant Availability"]
    n_AM["Availability BU Gap (MWh)"]
    n_AN["Availability BU Gap (%)"]
  end
  subgraph G7["Grid Availability"]
    n_AO["Expected Grid Availability"]
    n_AP["Actual Grid Availability"]
    n_AQ["Grid Availability BU Gap (MWh)"]
    n_AR["Grid Availability BU Gap (%)"]
    n_AS["Grid Availability Loss (MWh)"]
  end
  subgraph G8["Expected Energy & Performance Ratio"]
    n_AT["Expected Energy - Controllable (MWh)"]
    n_AU["Production @100% avail"]
    n_AV["Expected Energy - Actual POA & 100% PEA,GEA (MWh)"]
    n_AW["Other external losses"]
    n_AX["Expected Performance Ratio (PR)"]
    n_AY["Plant Performance (PR) Act"]
    n_AZ["Plant Performance (PR) gap (MWh)"]
    n_BA["Plant Performance (PR) gap %"]
  end
  subgraph G9["Residual Gap"]
    n_BB["Residual BU Gap (MWh)"]
    n_BC["Residual gap %"]
  end
  subgraph G10["Availability & Loss Breakdown"]
    n_BF["Substation AVL (%)"]
    n_BG["Inverter AVL (%)"]
    n_BH["Combiner AVL (%)"]
    n_BI["Tracker AVL(%)"]
    n_BJ["Plant Availability Loss (MWh)"]
    n_BK["BoS Loss (MWh)"]
    n_BL["Inverter Loss (MWh)"]
    n_BM["DC Loss (MWh)"]
    n_BN["Tracker Loss (MWh)"]
    n_BO["Residual Loss (MWh)"]
  end
  subgraph G11["Comments & QA"]
    n_BP["Loss Comments"]
    n_BQ["Data QA"]
  end
  MON[("Monthly_techData")]
  SITE[("Site data sheets")]
  MON --> n_K
  MON --> n_L
  MON --> n_M
  MON --> n_O
  MON --> n_P
  MON --> n_Y
  MON --> n_AC
  MON --> n_AK
  MON --> n_AO
  MON --> n_AW
  MON --> n_AX
  SITE --> n_Q
  SITE --> n_Z
  SITE --> n_AD
  SITE --> n_AL
  SITE --> n_AS
  SITE --> n_BF
  SITE --> n_BG
  SITE --> n_BH
  SITE --> n_BI
  n_Q --> n_T
  n_O --> n_T
  n_Q --> n_U
  n_O --> n_U
  n_M --> n_W
  n_Y --> n_W
  n_AK --> n_W
  n_AO --> n_W
  n_AX --> n_W
  n_AW --> n_W
  n_P --> n_X
  n_O --> n_X
  n_AB --> n_AA
  n_AV --> n_AA
  n_Z --> n_AB
  n_Y --> n_AB
  n_AD --> n_AE
  n_AC --> n_AE
  n_AB --> n_AF
  n_AE --> n_AF
  n_AL --> n_AM
  n_AK --> n_AM
  n_AV --> n_AM
  n_AN --> n_AM
  n_AL --> n_AN
  n_AK --> n_AN
  n_AS --> n_AP
  n_AV --> n_AP
  n_AR --> n_AQ
  n_AV --> n_AQ
  n_AP --> n_AR
  n_AO --> n_AR
  n_AV --> n_AT
  n_AS --> n_AT
  n_Q --> n_AU
  n_AP --> n_AU
  n_AL --> n_AU
  n_AS --> n_AU
  n_BJ --> n_AU
  n_M --> n_AV
  n_Z --> n_AV
  n_AX --> n_AV
  n_AW --> n_AV
  n_AU --> n_AY
  n_M --> n_AY
  n_Z --> n_AY
  n_BA --> n_AZ
  n_AV --> n_AZ
  n_AY --> n_BA
  n_AX --> n_BA
  n_T --> n_BB
  n_X --> n_BB
  n_AA --> n_BB
  n_AM --> n_BB
  n_AQ --> n_BB
  n_AZ --> n_BB
  n_BB --> n_BC
  n_AV --> n_BC
  n_BK --> n_BJ
  n_BL --> n_BJ
  n_BM --> n_BJ
  n_BN --> n_BJ
  n_BF --> n_BK
  n_AV --> n_BK
  n_BG --> n_BL
  n_AV --> n_BL
  n_BH --> n_BM
  n_AV --> n_BM
  n_BI --> n_BN
  n_AV --> n_BN
  n_Q --> n_BO
  n_BJ --> n_BO
  n_AZ --> n_BO
  n_AT --> n_BO
  n_AD --> n_BP
  n_Z --> n_BP
  n_BB --> n_BQ
  n_BO --> n_BQ
  classDef src fill:#d8c8f0,stroke:#6a4fa0,color:#222;
  classDef lk fill:#cfe8ff,stroke:#2a6db0,color:#222;
  classDef pl fill:#d4f4dd,stroke:#2e8b57,color:#222;
  classDef cl fill:#ffe9c7,stroke:#c07a10,color:#222;
  class MON,SITE src;
  class n_K,n_L,n_M,n_O,n_P,n_Y,n_AC,n_AK,n_AO,n_AW,n_AX lk;
  class n_Q,n_Z,n_AD,n_AL,n_AS,n_BF,n_BG,n_BH,n_BI pl;
  class n_T,n_U,n_W,n_X,n_AA,n_AB,n_AE,n_AF,n_AM,n_AN,n_AP,n_AQ,n_AR,n_AT,n_AU,n_AV,n_AY,n_AZ,n_BA,n_BB,n_BC,n_BJ,n_BK,n_BL,n_BM,n_BN,n_BO,n_BP,n_BQ cl;
```

If the big diagram is hard to read, use Obsidian's Graph view with the **Local graph** on a single formula or variable note, or zoom the diagram with Ctrl/Cmd + scroll.
