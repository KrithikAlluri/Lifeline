# Assembly Guide

This guide provides step-by-step instructions for assembling your Lifeline blood analyzer. The device consists of three main components: the optical reader, the μPAD cartridge, and the software interface.

## Bill of Materials (BOM)

### Electronics Components
- **Microcontroller**: ESP32-WROOM-32 ($8)
- **Display**: 1.3" OLED I2C Display ($3)
- **Battery**: 3.7V 2000mAh LiPo ($5)
- **Charging Module**: TP4056 ($2)
- **Optical Sensor**: TCS3200 Color Sensor ($4)
- **LED Array**: 4x RGB LEDs ($2)
- **PCB**: Custom designed ($3)

### Mechanical Components
- **Enclosure**: 3D printed case ($5)
- **Lens**: 6mm focal length lens ($2)
- **Springs**: Compression springs for cartridge holder ($1)
- **Screws**: M3x8mm screws (10x) ($1)

### μPAD Materials
- **Substrate**: Whatman #1 filter paper ($2)
- **Wax**: Paraffin wax for hydrophobic barriers ($1)
- **Reagents**: Assay-specific chemicals ($2)

**Total Cost: $45**

## Assembly Steps

### Step 1: PCB Assembly

1. **Solder ESP32 Module**
   - Place ESP32 on the PCB
   - Solder all pins carefully
   - Test continuity with multimeter

2. **Install Display**
   - Connect OLED display via I2C
   - Secure with mounting screws
   - Test display functionality

3. **Add Optical Components**
   - Mount TCS3200 sensor
   - Install LED array
   - Position lens assembly

### Step 2: Power System

1. **Battery Installation**
   - Connect LiPo battery to TP4056
   - Mount charging module
   - Test charging functionality

2. **Power Distribution**
   - Connect to ESP32 VIN
   - Add power switch
   - Verify voltage levels

### Step 3: Enclosure Assembly

1. **3D Printed Parts**
   - Print main enclosure
   - Print cartridge holder
   - Print battery compartment

2. **Mechanical Assembly**
   - Install PCB into enclosure
   - Mount display in front panel
   - Secure battery compartment

### Step 4: μPAD Fabrication

1. **Wax Printing**
   - Design hydrophobic barriers
   - Print wax patterns on filter paper
   - Heat to melt wax into paper

2. **Reagent Deposition**
   - Deposit assay reagents
   - Allow to dry completely
   - Store in sealed container

### Step 5: Software Installation

1. **Firmware Upload**
   - Connect ESP32 to computer
   - Upload Lifeline firmware
   - Test basic functionality

2. **Mobile App Setup**
   - Install Lifeline app
   - Pair with device via Bluetooth
   - Test communication

## Calibration

### Optical Calibration
1. Insert calibration μPAD
2. Run calibration sequence
3. Verify color sensor readings
4. Save calibration data

### Assay Calibration
1. Test with known samples
2. Establish standard curves
3. Validate measurement accuracy
4. Document calibration parameters

## Quality Control

### Pre-Assembly Checks
- Verify all components
- Test individual modules
- Check for damage

### Post-Assembly Testing
- Power-on self-test
- Optical system validation
- Communication testing
- Sample measurement accuracy

## Troubleshooting Assembly Issues

### Common Problems
- **Display not working**: Check I2C connections
- **Battery not charging**: Verify TP4056 wiring
- **Sensor readings erratic**: Check optical alignment
- **Bluetooth not pairing**: Reset ESP32

### Testing Procedures
1. Power system test
2. Display functionality test
3. Optical sensor test
4. Bluetooth communication test
5. Sample measurement test

## Safety Considerations

- Work in well-ventilated area
- Use appropriate PPE when soldering
- Handle LiPo batteries carefully
- Dispose of chemicals properly
- Follow local safety regulations

## Next Steps

After assembly, proceed to:
- [Getting Started](getting-started.md) for first-time setup
- [User Manual](user-manual.md) for operating procedures
- [Troubleshooting](troubleshooting.md) for common issues 