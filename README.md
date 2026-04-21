# Microclimate Systems for Extended Wear

This repository explores how extended-wear textile systems—starting with socks—can improve wear tolerance and reduce replacement burden in constrained environments such as space.

Rather than optimizing a single material property, this project models how **small textile design changes propagate through physiological, behavioral, and system-level constraints** to influence:

- wear duration  
- replacement frequency  
- total mass and waste  

---

## Core Thesis

In many environments, garments are not replaced when they fail materially—but when humans stop tolerating them.

> **Wear tolerance—not durability—is the primary constraint.**

This repository models wear tolerance as a function of:
- textile design  
- physiological response  
- behavioral limits  

---

## Problem

In space, clothing is a consumable system.

- Astronauts wear garments for multiple days without laundering  
- Clothing is replaced based on discomfort, odor, or irritation  
- Each astronaut uses ~150 lbs of clothing per year  

This creates a system where:

> replacement frequency is driven by human tolerance, not material lifespan

---

## Why the Foot

The foot is a high-contact, high-risk interface:

- continuous contact with surfaces or footwear  
- localized pressure and shear  
- heat and moisture accumulation  
- high contribution to overall discomfort  

Socks are also a primary driver of replacement cycles, making them a high-leverage intervention point.

---

## Design Direction

This project explores multiple design strategies:

- Seamless construction → reduce friction points  
- Targeted compression → stabilize fit and support circulation  
- Moisture-gradient knit → regulate skin environment  
- Split-toe structures → reduce inter-toe friction  
- Grip surfaces → improve contact stability (especially in low-gravity)  
- Partial coverage (“toe koozie” concept) → isolate high-friction zones  

---

## Selective Coverage (“Toe Koozie”) Hypothesis

Astronaut anecdotes describe the use of partial socks protecting only high-contact areas, sometimes referred to informally as “toe koozies.”

This suggests a broader design hypothesis:

> **Full-foot coverage may introduce unnecessary thermal and moisture load, while targeted protection may extend wear tolerance.**

This project treats selective coverage as a **testable systems hypothesis**, not a validated solution.

---

## Model Architecture

This repository models wear tolerance across three interacting layers:

### 1. Textile → Physiology Model (`textile_to_physiology_model.py`)
Maps textile properties to physiological response:

- moisture load  
- thermal load  
- friction and pressure  
- circulation effects  

→ outputs: **discomfort + physiological strain**

---

### 2. Behavioral Model (“Ick Factor”) (`ick_factor_model.py`)
Informally named, but intentionally included.

Models the point at which users discontinue wear due to:

- odor  
- moisture perception  
- contamination (including debris accumulation)  
- sensory irritation  
- environmental risk (e.g., mold, trapped moisture)  

> In practice, garments are often removed due to perception, not failure.

This layer captures **real-world behavioral limits** that override otherwise acceptable system performance.

---

### 3. System / Mission Model (`model.py`)
Translates wear tolerance into system-level outcomes:

- replacement frequency  
- total garment count  
- total mass  

→ connects human experience to mission logistics

---

## Study Approach (Conceptual)

We propose a randomized crossover wear framework comparing:

- baseline systems  
- optimized full-coverage designs  
- selective/partial coverage designs  

**Primary endpoint:**

> time to voluntary removal (wear tolerance)

Supporting measurements:

- localized discomfort  
- temperature and moisture  
- subjective experience  

---

## Mission Impact Model

Small increases in wear tolerance scale nonlinearly across mission duration.

| Condition  | Days per Pair | Total Pairs | Total Mass |
|-----------|--------------|------------|------------|
| Baseline  | 2            | 540        | 32.4 kg    |
| Optimized | 5            | 216        | 12.9 kg    |
| Reduction | —            | ↓ 60%      | ↓ 19.5 kg  |

---

## Healthcare & Human Systems (Bridge Evidence)

Existing literature supports relevant mechanisms:

### Plantar Pressure & Tissue Risk
- uneven pressure distribution contributes to skin breakdown and ulcer formation  
- compression and cushioning can reduce localized stress  

### Moisture & Skin Integrity
- prolonged moisture exposure increases friction and infection risk  
- textile structure influences thermal and moisture regulation  

### Sensorimotor / Vestibular Role
- the foot contributes to balance and spatial awareness  
- compression and tactile feedback may improve stability in low-feedback environments  

**Implication:**

> textile systems influence both skin health and human performance

---

## Cross-Domain Applications

This model extends beyond space:

- **Military / field use** → long-duration load-bearing wear  
- **First responders / EMTs** → extended shifts without change  
- **Clinical populations (e.g., stroke, diabetic foot)** → skin integrity + support  
- **Athletics (running, climbing)** → friction + performance tradeoffs  
- **Wearable sensing (e.g., step counting)** → signal stability depends on fit and contact  

**Core principle:**

> foot-interface design is context-dependent and system-level

---

## Why Wearables Often Fail

Many wearable systems fail not because they don’t work—but because people stop wearing them.

Common failure modes:

- discomfort  
- maintenance burden  
- poor integration into daily behavior  

This project focuses on:

> **extending wear tolerance as the primary adoption constraint**

---

## Personal Motivation (Yes, This Is a Real Problem)

This work is partly informed by firsthand experience in extended-wear, high-load environments.

During field use (e.g., ROTC rucks carrying ~1/3 body weight), socks often became saturated and physically uncomfortable—but still technically wearable. Blisters and pressure could be tolerated.

What could not be tolerated was the **psychological discomfort**:

- wet fabric sloshing inside the shoe  
- loss of fit and stability  
- buildup of heat, friction, and general “grossness”  

The workaround was not elegant:

- double socking  
- improvised compression (e.g., using hair ties to reduce heel gapping)  
- constant adjustment to regain stability  

This happened before having any formal framework for:

- compression zones  
- moisture management  
- fit optimization  

In retrospect, this is exactly what the model captures:

> people don’t stop wearing systems when they fail—they stop when they become intolerable

Similarly, while astronauts may adapt behaviorally (e.g., going barefoot or using toes for grip), this project assumes those are **short-term adaptations, not scalable design solutions**.

---

## Current Status

- Concept development complete  
- Model architecture defined (textile → physiology → behavior → system)  
- Scenario modeling and visualization (Tableau, hypothetical data)  
- Materials exploration informed by external inputs  

This repository represents an **in-progress system model**, not a finalized product.

---

## Future Work

- Validate selective vs full coverage designs  
- Incorporate spatial (foot-region) failure modeling  
- Integrate real-world wear data  
- Expand behavioral modeling (compliance, perception)  
- Explore clinical and accessibility-focused applications  

---

## Summary

This project reframes textile design as a human-system problem:

> **how long a person can tolerate wearing something**

By modeling wear tolerance across:

- physiology  
- perception  
- environment  

we connect design decisions to:

- human experience  
- system efficiency  
- real-world adoption  
