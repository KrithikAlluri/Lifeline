# System Architecture

This document describes the overall system architecture of Lifeline, including hardware components, software integration, and data flow from sample collection to result display.

## System Overview

Lifeline is an edge-powered blood testing kit that integrates custom hardware, AI, and user-friendly software. The system combines microfluidic paper-based analytical devices (μPADs) with electrochemical sensors and optical analysis, paired with a fine-tuned Gemma 3n multimodal model running fully on-device for intelligent result interpretation.

## Hardware Architecture

### Core Components

**ESP32 Microcontroller**
- **ESP32-WROOM-32**: Dual-core 240 MHz processor
- **Memory**: 520 KB SRAM, 4 MB Flash
- **Connectivity**: WiFi 802.11 b/g/n, Bluetooth 4.2
- **GPIO**: 34 pins for sensor interfacing
- **ADC**: 18 channels, 12-bit resolution
- **Function**: Handles analog data acquisition from cartridges

**Raspberry Pi 4 (8GB)**
- **CPU**: Quad-core ARM Cortex-A72 at 1.5GHz
- **RAM**: 8GB LPDDR4
- **Storage**: MicroSD card (32GB+ recommended)
- **Connectivity**: WiFi, Bluetooth, USB 3.0
- **Function**: Runs AI model and user interface

**Optical System**
- **Camera Module**: Raspberry Pi Camera Module v2
- **Resolution**: 8MP (3280x2464 pixels)
- **Sensor**: Sony IMX219
- **Lens**: Fixed focus, 3.04mm focal length
- **Function**: Captures high-resolution images of colorimetric strips

**Display Interface**
- **Touchscreen Display**: 7" capacitive touchscreen
- **Resolution**: 1024x600 pixels
- **Interface**: HDMI and USB for touch
- **Power**: 5V, 500mA consumption
- **Function**: User interface and result display

**Power System**
- **Battery**: 3.7V 2000mAh LiPo
- **Charging**: TP4056 module with USB-C input
- **Runtime**: 8 hours continuous operation
- **Standby**: 72 hours
- **Charging Time**: 2 hours

**Cartridge System**
- **Holder**: Spring-loaded cartridge holder
- **Detection**: Optical sample detection
- **Sealing**: O-ring for light isolation
- **Ejection**: Manual release mechanism

## Data Flow Architecture

### Sample Processing Pipeline

```
Blood Sample → μPAD/EC Sensor → Optical/Electrical Analysis → ESP32 Processing → Result Display/Export
```

**Step 1: Sample Collection**
- Finger prick with sterile lancet
- Collect 10-15 μL blood sample
- Apply to μPAD sample zone or EC sensor
- Allow capillary action (2-3 seconds)

**Step 2: Sample Detection**
- Insert cartridge into holder
- Optical sensor detects sample presence
- Verify sample volume and distribution
- Begin analysis sequence

**Step 3: Analysis**
- **Optical Assays**: Colorimetric analysis with TCS3200
- **EC Assays**: Amperometric/potentiometric measurement
- **Processing Time**: 3-5 minutes depending on assay
- **Temperature Control**: Maintained at 25±2°C

**Step 4: Data Processing**
- Raw sensor data acquisition
- Calibration curve application
- Concentration calculation
- Quality control validation

**Step 5: Result Output**
- Display on OLED screen
- Bluetooth transmission to mobile app
- Local storage in SQLite database
- Optional cloud synchronization

## Software Architecture

### Firmware (ESP32)

**Core Functions**
- Sensor data acquisition
- Real-time analysis algorithms
- User interface management
- Bluetooth communication
- Power management

**Key Libraries**
- **TCS3200**: Color sensor interface
- **U8g2**: OLED display driver
- **BluetoothSerial**: BLE communication
- **WiFi**: OTA updates and cloud sync

**Data Processing Pipeline**
```
Raw Sensor Data → Signal Conditioning → Calibration → Concentration Calculation → Quality Control → Result Output
```

### Mobile Application

**Platform**: React Native (iOS/Android)
**Database**: SQLite local + cloud sync
**API**: RESTful JSON communication
**Security**: AES-256 encryption

**Key Features**
- Device pairing and management
- Real-time result display
- Historical data browsing
- Data export and sharing
- User account management

## Modular Design

### Hardware Modules

**Optical Module**
- TCS3200 sensor assembly
- LED array with diffuser
- Lens and focus mechanism
- Light-tight cartridge holder

**Electronics Module**
- ESP32 development board
- Power management circuit
- Sensor interface board
- Display mounting bracket

**Power Module**
- LiPo battery pack
- TP4056 charging circuit
- Power switch and indicators
- USB-C charging port

**Enclosure Module**
- 3D printed case components
- Cartridge holder mechanism
- Display window and buttons
- Ventilation and cooling

### Software Modules

**Sensor Interface Layer**
- TCS3200 driver
- ADC sampling routines
- I2C communication
- GPIO control

**Analysis Engine**
- Calibration algorithms
- Concentration calculations
- Quality control checks
- Error handling

**User Interface Layer**
- Menu system
- Result display
- Settings management
- Help system

**Communication Layer**
- Bluetooth stack
- Data formatting
- Sync protocols
- Error recovery

## Expandability

### Hardware Expansion
- **Additional Sensors**: Support for new assay types
- **Multi-channel**: Parallel analysis capabilities
- **External Peripherals**: Printer, barcode scanner
- **Modular Cartridges**: Swappable assay modules

### Software Expansion
- **New Assays**: Configurable assay parameters
- **AI Integration**: Machine learning for pattern recognition
- **Cloud Analytics**: Advanced data processing
- **API Development**: Third-party integrations

### Research Applications
- **Custom Assays**: User-defined protocols
- **Data Export**: Research-grade data formats
- **Validation Tools**: Performance assessment
- **Collaboration**: Multi-site studies

## Performance Specifications

### Analytical Performance
- **Accuracy**: ±5% compared to reference methods
- **Precision**: ±3% coefficient of variation
- **Detection Limit**: 1 mg/dL for most analytes
- **Dynamic Range**: 10-1000 mg/dL
- **Analysis Time**: 3-5 minutes per assay

### Operational Performance
- **Sample Volume**: 10-15 μL
- **Temperature Range**: 15-35°C
- **Humidity Range**: 20-80% RH
- **Battery Life**: 8 hours continuous
- **Data Storage**: 1000 measurements local

### Connectivity Performance
- **Bluetooth Range**: 10 meters
- **Data Transfer**: 1 MB/s
- **Sync Frequency**: Real-time bidirectional
- **Offline Operation**: Full functionality without internet

## Quality Assurance

### Calibration System
- **5-point Calibration**: Zero, low, normal, high, very high
- **Automatic Validation**: Quality control checks
- **Drift Detection**: Continuous monitoring
- **Recalibration Alerts**: Timely reminders

### Data Integrity
- **Encryption**: AES-256 for all data
- **Backup**: Automatic cloud synchronization
- **Audit Trail**: Complete measurement history
- **Version Control**: Software and calibration tracking

### Safety Features
- **Sample Detection**: Prevents false readings
- **Error Handling**: Graceful failure modes
- **Battery Protection**: Overcharge/overdischarge protection
- **Temperature Monitoring**: Prevents overheating

## Future Development

### Hardware Upgrades
- **Multi-wavelength**: Enhanced optical system
- **Microfluidics**: Automated sample handling
- **Wireless Charging**: Qi-compatible charging
- **Ruggedized Design**: IP67 protection

### Software Enhancements
- **AI Algorithms**: Machine learning analysis
- **Advanced Analytics**: Trend analysis and prediction
- **Telemedicine**: Remote monitoring capabilities
- **Research Tools**: Custom protocol development

### Assay Expansion
- **Cardiac Markers**: Troponin, BNP, CK-MB
- **Inflammatory**: CRP, IL-6, TNF-α
- **Hormones**: Insulin, cortisol, thyroid
- **Vitamins**: B12, D, folate
- **Toxins**: Lead, mercury, arsenic 