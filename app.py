from detection.detect_vehicles import detect_vehicles
from traffic.get_traffic import get_traffic_data
from tts.azure_tts import announce
from utils.logger import log
import cv2

def main():
    log("Smart Traffic System Started")

    input_path = "inputs/sample_frame.jpg"
    output_path = "static/output.jpg"

    log("Running vehicle detection...")
    detect_vehicles(input_path, output_path)

    log("Fetching traffic data...")
    traffic_msg = get_traffic_data()

    log("Announcing traffic info...")
    announce(traffic_msg)

    log("Done. Output image saved at static/output.jpg")

if __name__ == "__main__":
    main()
