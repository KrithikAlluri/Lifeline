# Software Setup

This document provides comprehensive instructions for installing and configuring the software components of the Lifeline system, including firmware, mobile applications, and development tools.

## System Requirements

### Hardware Requirements
- **ESP32 Development Board**: ESP32-WROOM-32 or equivalent
- **Computer**: Windows 10+, macOS 10.14+, or Linux Ubuntu 18.04+
- **Mobile Device**: iOS 12+ or Android 8+
- **Internet Connection**: For downloads and updates

### Software Requirements
- **Arduino IDE**: Version 2.0 or later
- **Python**: Version 3.8 or later
- **Git**: Version 2.20 or later
- **Node.js**: Version 16 or later (for mobile app development)

## ESP32 Firmware Installation

### Step 1: Arduino IDE Setup

1. **Download Arduino IDE**
   - Visit [arduino.cc](https://www.arduino.cc/en/software)
   - Download version 2.0 or later
   - Install following platform-specific instructions

2. **Add ESP32 Board Manager**
   - Open Arduino IDE
   - Go to File → Preferences
   - Add URL: `https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json`
   - Click OK

3. **Install ESP32 Board Package**
   - Go to Tools → Board → Boards Manager
   - Search for "ESP32"
   - Install "ESP32 by Espressif Systems"
   - Select ESP32 Dev Module board

### Step 2: Install Required Libraries

1. **Open Library Manager**
   - Go to Tools → Manage Libraries
   - Search and install the following libraries:

**Required Libraries**
- **TCS3200**: Color sensor library
- **U8g2**: OLED display library
- **BluetoothSerial**: ESP32 Bluetooth library
- **WiFi**: WiFi connectivity library
- **ArduinoJson**: JSON parsing library
- **Preferences**: Non-volatile storage

2. **Verify Installation**
   - Check that all libraries are installed
   - Verify no compilation errors
   - Test basic examples

### Step 3: Upload Firmware

1. **Download Lifeline Firmware**
   ```bash
   git clone https://github.com/KrithikAlluri/Lifeline.git
   cd Lifeline/firmware
   ```

2. **Configure Board Settings**
   - Board: "ESP32 Dev Module"
   - Upload Speed: "115200"
   - CPU Frequency: "240MHz"
   - Flash Frequency: "80MHz"
   - Flash Mode: "QIO"
   - Flash Size: "4MB"
   - Partition Scheme: "Default 4MB with spiffs"

3. **Upload Firmware**
   - Connect ESP32 via USB
   - Select correct COM port
   - Click Upload button
   - Wait for upload completion
   - Verify upload success

### Step 4: Verify Installation

1. **Check Serial Monitor**
   - Open Serial Monitor (115200 baud)
   - Verify startup messages
   - Check for error messages
   - Confirm sensor initialization

2. **Test Basic Functions**
   - Power on device
   - Check display initialization
   - Test button responses
   - Verify Bluetooth pairing

## Mobile Application Setup

### iOS Application

1. **Installation Options**
   - **App Store**: Search for "Lifeline Blood Analyzer"
   - **TestFlight**: For beta testing
   - **Development**: Xcode for custom builds

2. **Initial Setup**
   - Launch application
   - Grant Bluetooth permissions
   - Create user account
   - Complete device pairing

3. **Configuration**
   - Set measurement units
   - Configure notification preferences
   - Enable data synchronization
   - Set privacy options

### Android Application

1. **Installation Options**
   - **Google Play**: Search for "Lifeline Blood Analyzer"
   - **APK**: Direct installation from website
   - **Development**: Android Studio for custom builds

2. **Initial Setup**
   - Launch application
   - Grant permissions (Bluetooth, Storage)
   - Create user account
   - Complete device pairing

3. **Configuration**
   - Set measurement units
   - Configure notification preferences
   - Enable data synchronization
   - Set privacy options

## Development Environment Setup

### Python Development

1. **Install Python**
   ```bash
   # Windows
   Download from python.org
   
   # macOS
   brew install python3
   
   # Linux
   sudo apt-get install python3 python3-pip
   ```

2. **Install Required Packages**
   ```bash
   pip install numpy pandas matplotlib
   pip install opencv-python scikit-learn
   pip install flask requests
   pip install jupyter notebook
   ```

3. **Clone Repository**
   ```bash
   git clone https://github.com/KrithikAlluri/Lifeline.git
   cd Lifeline/python
   pip install -r requirements.txt
   ```

### Web Dashboard Setup

1. **Install Node.js**
   ```bash
   # Download from nodejs.org
   # Or use package manager
   ```

2. **Install Dependencies**
   ```bash
   cd Lifeline/web-dashboard
   npm install
   ```

3. **Start Development Server**
   ```bash
   npm start
   ```

4. **Build for Production**
   ```bash
   npm run build
   ```

## Configuration Files

### ESP32 Configuration

**config.h**
```cpp
// Device Configuration
#define DEVICE_NAME "Lifeline"
#define FIRMWARE_VERSION "1.0.0"
#define HARDWARE_VERSION "1.0"

// Pin Definitions
#define TCS3200_S0 4
#define TCS3200_S1 5
#define TCS3200_S2 6
#define TCS3200_S3 7
#define TCS3200_OUT 8

#define OLED_SDA 21
#define OLED_SCL 22

#define POWER_BUTTON 0
#define LED_PIN 2

// Calibration Parameters
#define CALIBRATION_POINTS 5
#define MEASUREMENT_AVERAGES 10
#define STABILIZATION_TIME 3000
```

### Mobile App Configuration

**config.json**
```json
{
  "api": {
    "baseUrl": "https://api.lifeline.dev",
    "timeout": 30000
  },
  "bluetooth": {
    "serviceUUID": "12345678-1234-1234-1234-123456789abc",
    "characteristicUUID": "87654321-4321-4321-4321-cba987654321"
  },
  "measurements": {
    "units": "mg/dL",
    "decimalPlaces": 1,
    "timeout": 300000
  }
}
```

## Communication Setup

### Bluetooth Configuration

1. **Service UUIDs**
   - **Device Information**: 180A
   - **Battery Service**: 180F
   - **Custom Service**: 12345678-1234-1234-1234-123456789abc

2. **Characteristic UUIDs**
   - **Device Name**: 2A00
   - **Battery Level**: 2A19
   - **Measurement Data**: 87654321-4321-4321-4321-cba987654321
   - **Calibration Data**: 87654321-4321-4321-4321-cba987654322

3. **Data Format**
   ```json
   {
     "timestamp": "2024-01-01T12:00:00Z",
     "assay": "glucose",
     "value": 120.5,
     "unit": "mg/dL",
     "quality": "good"
   }
   ```

### WiFi Configuration

1. **Network Setup**
   - SSID: "Lifeline_Device"
   - Password: "lifeline123"
   - Security: WPA2

2. **OTA Updates**
   - Server: "https://firmware.lifeline.dev"
   - Check Frequency: Daily
   - Auto Update: Enabled

## Database Setup

### Local Storage (SQLite)

**Schema**
```sql
CREATE TABLE measurements (
    id INTEGER PRIMARY KEY,
    timestamp TEXT NOT NULL,
    assay TEXT NOT NULL,
    value REAL NOT NULL,
    unit TEXT NOT NULL,
    quality TEXT,
    user_id TEXT
);

CREATE TABLE calibrations (
    id INTEGER PRIMARY KEY,
    assay TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    slope REAL NOT NULL,
    intercept REAL NOT NULL,
    r_squared REAL
);

CREATE TABLE users (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT,
    created_at TEXT NOT NULL
);
```

### Cloud Synchronization

1. **AWS DynamoDB Setup**
   - Region: us-east-1
   - Table: lifeline-measurements
   - Index: user-timestamp-index

2. **Data Sync**
   - Frequency: Real-time
   - Conflict Resolution: Server wins
   - Encryption: AES-256

## Testing and Validation

### Unit Testing

1. **ESP32 Tests**
   ```cpp
   void testColorSensor() {
     // Test TCS3200 functionality
   }
   
   void testDisplay() {
     // Test OLED display
   }
   
   void testBluetooth() {
     // Test BLE communication
   }
   ```

2. **Mobile App Tests**
   ```javascript
   describe('Measurement Tests', () => {
     it('should process glucose measurement', () => {
       // Test measurement processing
     });
   });
   ```

### Integration Testing

1. **End-to-End Tests**
   - Sample collection to result display
   - Bluetooth communication
   - Data synchronization
   - Error handling

2. **Performance Tests**
   - Battery life testing
   - Memory usage monitoring
   - Response time measurement
   - Accuracy validation

## Troubleshooting

### Common Installation Issues

**ESP32 Upload Problems**
- **Port not found**: Check USB connection and drivers
- **Upload failed**: Try different upload speed
- **Compilation errors**: Verify library installation

**Mobile App Issues**
- **Bluetooth not working**: Check permissions
- **App crashes**: Clear cache and reinstall
- **Sync problems**: Check internet connection

**Development Environment**
- **Python errors**: Update pip and packages
- **Node.js issues**: Check version compatibility
- **Git problems**: Verify repository access

### Debugging Tools

1. **Serial Monitor**
   - Baud rate: 115200
   - View debug messages
   - Monitor sensor data
   - Check error logs

2. **Mobile Debug**
   - Enable developer options
   - View logcat (Android)
   - Use Xcode console (iOS)
   - Monitor network traffic

3. **Performance Monitoring**
   - Battery usage tracking
   - Memory leak detection
   - CPU usage monitoring
   - Network performance

## Security Considerations

### Data Protection
- **Encryption**: AES-256 for all data
- **Authentication**: Secure user login
- **Authorization**: Role-based access
- **Audit Trail**: Complete activity logging

### Network Security
- **HTTPS**: All API communications
- **Certificate Pinning**: Prevent MITM attacks
- **Token-based Auth**: JWT tokens
- **Rate Limiting**: Prevent abuse

### Device Security
- **Firmware Signing**: Prevent tampering
- **Secure Boot**: Verify firmware integrity
- **Encrypted Storage**: Protect sensitive data
- **Regular Updates**: Security patches

## Maintenance and Updates

### Regular Maintenance
- **Firmware Updates**: Monthly security patches
- **App Updates**: Feature releases
- **Library Updates**: Dependency management
- **Security Audits**: Vulnerability assessment

### Backup and Recovery
- **Configuration Backup**: Export settings
- **Data Backup**: Cloud synchronization
- **Firmware Backup**: Recovery images
- **Documentation**: Keep procedures updated 