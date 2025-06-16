     # Smart Traffic Management System 🚦

  This system detects traffic congestion and vehicles using:
- YOLOv8 for real-time object detection
- MapMyIndia API for congestion data
- Azure Cognitive Services (TTS) to announce traffic conditions


## 💡 Features
- Vehicle detection from images (YOLOv8)
- Traffic data fetched via MapMyIndia's API
- Audio announcements using Azure Text-to-Speech
- Stores traffic data in local JSON files
- Works offline (except for APIs)



## 🛠 File Structure

    smart-traffic-system/
    ├── app.py
    ├── detection/...
    ├── traffic/...
    ├── tts/...
    ├── config/
    ├── utils/
    ├── inputs/
    ├── static/
    ├── requirements.txt
    └── README.md

## ✅ Setup Instructions
### 1. Clone the repo
git clone https://github.com/yourusername/smart-traffic-system.git
cd smart-traffic-system

### 2. Install dependencies
pip install -r requirements.txt

### 3. Get API Keys
- MapMyIndia API: https://developer.mapmyindia.com
- Azure TTS Key: https://portal.azure.com

### 4. Add your keys to config/config.json

### 5. Add test image as inputs/test_input.jpg

### 6. Run the app
python app.py
 
