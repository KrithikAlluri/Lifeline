# Biomarkers & Assays

This document describes the biomarkers supported by Lifeline, their clinical significance, assay methods, and interpretation guidelines.

## Supported Biomarkers

### Glucose
**Clinical Significance**: Primary marker for diabetes monitoring and management
**Method**: Glucose oxidase + peroxidase colorimetric assay
**Normal Range**: 70-100 mg/dL (fasting)
**Sample Volume**: 10 μL
**Analysis Time**: 3 minutes
**Interferences**: High hematocrit, extreme temperatures

**Assay Principle**:
1. Glucose oxidase converts glucose to gluconic acid and H₂O₂
2. Peroxidase catalyzes reaction with chromogen
3. Color intensity proportional to glucose concentration
4. Optical measurement at 505 nm

**Clinical Interpretation**:
- **Normal**: 70-100 mg/dL
- **Prediabetes**: 100-125 mg/dL
- **Diabetes**: >126 mg/dL
- **Hypoglycemia**: <70 mg/dL

### Creatinine
**Clinical Significance**: Kidney function assessment
**Method**: Jaffe reaction (alkaline picrate)
**Normal Range**: 0.6-1.2 mg/dL (adults)
**Sample Volume**: 12 μL
**Analysis Time**: 4 minutes
**Interferences**: Bilirubin, ketones, cephalosporins

**Assay Principle**:
1. Creatinine reacts with picric acid in alkaline solution
2. Forms orange-red complex
3. Color intensity measured at 520 nm
4. Concentration calculated from standard curve

**Clinical Interpretation**:
- **Normal**: 0.6-1.2 mg/dL
- **Mild elevation**: 1.3-2.0 mg/dL
- **Moderate elevation**: 2.1-5.0 mg/dL
- **Severe elevation**: >5.0 mg/dL

### Urea (BUN)
**Clinical Significance**: Kidney function and protein metabolism
**Method**: Urease + phenol-hypochlorite
**Normal Range**: 7-20 mg/dL
**Sample Volume**: 10 μL
**Analysis Time**: 4 minutes
**Interferences**: High protein diet, dehydration

**Assay Principle**:
1. Urease converts urea to ammonia and CO₂
2. Ammonia reacts with phenol and hypochlorite
3. Forms blue indophenol complex
4. Measured at 630 nm

**Clinical Interpretation**:
- **Normal**: 7-20 mg/dL
- **Mild elevation**: 21-30 mg/dL
- **Moderate elevation**: 31-60 mg/dL
- **Severe elevation**: >60 mg/dL

### Potassium
**Clinical Significance**: Electrolyte balance and cardiac function
**Method**: Ion-selective electrode
**Normal Range**: 3.5-5.0 mEq/L
**Sample Volume**: 15 μL
**Analysis Time**: 2 minutes
**Interferences**: Hemolysis, sample age

**Assay Principle**:
1. Potassium ions diffuse through selective membrane
2. Creates electrical potential
3. Potential proportional to K⁺ concentration
4. Calibrated against standard solutions

**Clinical Interpretation**:
- **Normal**: 3.5-5.0 mEq/L
- **Mild hypokalemia**: 3.0-3.4 mEq/L
- **Moderate hypokalemia**: 2.5-2.9 mEq/L
- **Severe hypokalemia**: <2.5 mEq/L
- **Hyperkalemia**: >5.0 mEq/L

### Albumin
**Clinical Significance**: Liver function and nutritional status
**Method**: Bromocresol green (BCG)
**Normal Range**: 3.4-5.4 g/dL
**Sample Volume**: 10 μL
**Analysis Time**: 3 minutes
**Interferences**: Bilirubin, lipids, hemolysis

**Assay Principle**:
1. Albumin binds bromocresol green
2. Forms green complex
3. Color intensity measured at 628 nm
4. Concentration calculated from standard curve

**Clinical Interpretation**:
- **Normal**: 3.4-5.4 g/dL
- **Mild decrease**: 3.0-3.3 g/dL
- **Moderate decrease**: 2.0-2.9 g/dL
- **Severe decrease**: <2.0 g/dL

### Hemoglobin
**Clinical Significance**: Anemia screening and oxygen transport
**Method**: Cyanmethemoglobin
**Normal Range**: 12-16 g/dL (adults)
**Sample Volume**: 5 μL
**Analysis Time**: 2 minutes
**Interferences**: Carboxyhemoglobin, methemoglobin

**Assay Principle**:
1. Hemoglobin converted to cyanmethemoglobin
2. Stable complex absorbs at 540 nm
3. Concentration calculated from absorbance
4. Calibrated against reference standards

**Clinical Interpretation**:
- **Normal**: 12-16 g/dL
- **Mild anemia**: 10-11.9 g/dL
- **Moderate anemia**: 8-9.9 g/dL
- **Severe anemia**: <8 g/dL

## Assay Development

### μPAD Fabrication
1. **Design**: Create hydrophobic barrier patterns
2. **Printing**: Wax printer deposits paraffin wax
3. **Heating**: Melt wax into paper substrate
4. **Reagent Deposition**: Apply assay chemicals
5. **Drying**: Allow complete evaporation
6. **Packaging**: Seal in moisture-proof container

### Calibration Standards
Each assay requires 5-point calibration:
- **Zero**: No analyte present
- **Low**: Below normal range
- **Normal**: Mid-range value
- **High**: Above normal range
- **Very High**: Maximum expected value

### Quality Control
- **Daily**: Run control samples
- **Weekly**: Full calibration
- **Monthly**: Performance validation
- **Quarterly**: Method comparison

## Performance Characteristics

### Accuracy
- **Glucose**: ±3% compared to reference
- **Creatinine**: ±5% compared to reference
- **Urea**: ±4% compared to reference
- **Potassium**: ±2% compared to reference
- **Albumin**: ±4% compared to reference
- **Hemoglobin**: ±3% compared to reference

### Precision
- **Within-run**: <3% CV
- **Between-run**: <5% CV
- **Between-day**: <7% CV
- **Between-lot**: <10% CV

### Linearity
- **Glucose**: 20-600 mg/dL
- **Creatinine**: 0.2-10 mg/dL
- **Urea**: 5-100 mg/dL
- **Potassium**: 2.0-8.0 mEq/L
- **Albumin**: 1.0-6.0 g/dL
- **Hemoglobin**: 5-20 g/dL

### Detection Limits
- **Glucose**: 5 mg/dL
- **Creatinine**: 0.1 mg/dL
- **Urea**: 2 mg/dL
- **Potassium**: 1.0 mEq/L
- **Albumin**: 0.5 g/dL
- **Hemoglobin**: 2 g/dL

## Interference Studies

### Common Interferents
- **Hemolysis**: Affects potassium, albumin
- **Lipemia**: Interferes with colorimetric assays
- **Bilirubin**: May affect creatinine, albumin
- **Temperature**: All assays temperature-sensitive
- **pH**: Affects enzyme-based assays

### Cross-Reactivity
- **Glucose**: Fructose, galactose minimal
- **Creatinine**: Cephalosporins, ketones
- **Urea**: Ammonia, amino acids
- **Potassium**: Sodium, lithium
- **Albumin**: Other proteins minimal
- **Hemoglobin**: Carboxyhemoglobin

## Clinical Applications

### Diabetes Management
- **Screening**: Fasting glucose
- **Monitoring**: Post-prandial glucose
- **Control**: HbA1c correlation
- **Complications**: Kidney function monitoring

### Kidney Disease
- **Screening**: Creatinine, urea
- **Staging**: GFR estimation
- **Monitoring**: Disease progression
- **Dialysis**: Adequacy assessment

### Electrolyte Disorders
- **Screening**: Potassium levels
- **Monitoring**: Treatment response
- **Emergency**: Critical values
- **Follow-up**: Long-term trends

### Liver Disease
- **Screening**: Albumin levels
- **Monitoring**: Disease progression
- **Nutrition**: Protein status
- **Prognosis**: Survival prediction

### Anemia
- **Screening**: Hemoglobin levels
- **Classification**: Anemia type
- **Monitoring**: Treatment response
- **Prevention**: Population screening

## Research Applications

### Population Studies
- **Epidemiology**: Disease prevalence
- **Screening**: Community health
- **Surveillance**: Disease trends
- **Intervention**: Program evaluation

### Clinical Trials
- **Efficacy**: Treatment response
- **Safety**: Adverse events
- **Pharmacokinetics**: Drug levels
- **Biomarkers**: Surrogate endpoints

### Point-of-Care
- **Emergency**: Rapid assessment
- **Remote**: Telemedicine
- **Resource-limited**: Low-cost testing
- **Disaster**: Field deployment

## Future Development

### New Assays
- **Cardiac**: Troponin, BNP, CK-MB
- **Inflammatory**: CRP, IL-6, TNF-α
- **Hormones**: Insulin, cortisol, thyroid
- **Vitamins**: B12, D, folate
- **Toxins**: Lead, mercury, arsenic

### Technology Improvements
- **Multi-analyte**: Simultaneous testing
- **Microfluidics**: Automated sample handling
- **Nanomaterials**: Enhanced sensitivity
- **Biosensors**: Real-time monitoring
- **AI**: Pattern recognition 