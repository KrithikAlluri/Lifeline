# Lifeline Documentation

> **Blood Testing, Anywhere. Under $50.**

Welcome to the complete documentation for Lifeline, a low-cost, home-fabricated blood analyzer for essential biomarkers. This documentation provides everything you need to build, set up, and operate your own Lifeline device.

## Project Overview

Lifeline is a portable, affordable blood testing device designed to make essential biomarker analysis accessible to students, researchers, and communities worldwide. The system combines microfluidic paper-based analytical devices (μPADs) with electrochemical sensors and optical analysis to provide accurate, rapid blood testing capabilities.

### What Lifeline Solves

- **Access Gap**: Brings laboratory-quality testing to resource-limited settings
- **Cost Barrier**: Reduces testing costs from hundreds to under $50 per device
- **Knowledge Barrier**: Provides open-source design for education and research
- **Geographic Barrier**: Enables testing in remote or disaster-affected areas

### Who Benefits

- **Students**: Learn about biosensors and medical diagnostics
- **Researchers**: Conduct field studies and clinical research
- **Communities**: Access basic health screening in underserved areas
- **Educators**: Teach biomedical engineering and public health
- **Developers**: Build upon open-source platform for new applications

## Quick Start

- **[Assembly Guide](assembly.md)** - Step-by-step instructions to build your Lifeline
- **[Getting Started](getting-started.md)** - First-time setup and calibration
- **[User Manual](user-manual.md)** - How to operate your device
- **[Troubleshooting](troubleshooting.md)** - Common issues and solutions

## What You'll Find Here

### Assembly & Setup
- Complete bill of materials (BOM)
- Step-by-step assembly instructions
- μPAD fabrication guide
- Software installation
- Initial calibration

### Technical Details
- System architecture overview
- Electrochemical assay process
- Supported biomarkers
- Data management and export
- Safety considerations

### User Guides
- Operating procedures for users
- Technician maintenance guide
- Data interpretation
- Quality control protocols

### Advanced Topics
- Custom assay development
- Hardware modifications
- Software customization
- Research applications

## Supported Biomarkers

Lifeline currently supports the following essential biomarkers:

| Biomarker | Method | Normal Range | Clinical Significance |
|-----------|--------|--------------|---------------------|
| **Glucose** | GOx assay | 70-100 mg/dL | Diabetes monitoring |
| **Creatinine** | Jaffe reaction | 0.6-1.2 mg/dL | Kidney function |
| **Urea (BUN)** | Urease method | 7-20 mg/dL | Kidney function |
| **Potassium** | Ion-selective | 3.5-5.0 mEq/L | Electrolyte balance |
| **Albumin** | Bromocresol green | 3.4-5.4 g/dL | Liver function |
| **Hemoglobin** | Cyanmethemoglobin | 12-16 g/dL | Anemia screening |

## Cost Breakdown

**Total BOM: <$50**

- Optical components: $15
- Electronics: $20
- μPAD materials: $5
- Enclosure: $5
- Software: Free (open source)

## Safety & Compliance

> **Important**: Lifeline is designed for educational and research purposes. For clinical use, consult with healthcare professionals and ensure compliance with local regulations.

- **Biosafety Level 1** compatible
- **Single-use** μPADs prevent cross-contamination
- **Disposable** components for easy cleanup
- **Open-source** design for transparency

## Key Features

- **Portable**: Fits in your pocket
- **Battery-powered**: No external power required
- **Bluetooth connectivity**: Results to your phone
- **Open-source**: Full design files available
- **Modular**: Easy to customize and extend
- **Low-cost**: Under $50 total materials

## Documentation Structure

```
docs/
├── README.md              # This overview
├── system-architecture.md # System design and workflow
├── assembly.md            # Assembly instructions
├── micropad-fabrication.md # μPAD fabrication guide
├── electrochemical-assays.md # EC assay instructions
├── software-setup.md      # Software installation
├── getting-started.md     # First-time setup
├── user-manual.md         # Operating procedures
├── data-management.md     # Data handling and export
├── technical-specs.md     # System architecture
├── biomarkers.md          # Assay details
├── troubleshooting.md     # Common issues
├── safety-compliance.md   # Safety guidelines
├── maintenance.md         # Maintenance procedures
├── patent-research.md     # IP and research notes
├── contributing.md        # How to contribute
└── _sidebar.md            # Navigation sidebar
```

## Community & Support

- **GitHub**: [https://github.com/KrithikAlluri/Lifeline](https://github.com/KrithikAlluri/Lifeline)
- **Issues**: Report bugs and request features
- **Discussions**: Ask questions and share projects
- **Contributions**: Submit improvements and new assays

## License

This project is open source and available under the [MIT License](https://github.com/KrithikAlluri/Lifeline/blob/main/LICENSE).

---

*Built with care for accessible healthcare technology*
