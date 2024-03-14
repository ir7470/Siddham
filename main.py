import cv2
import time

def main():
    # Open the default camera (typically the first camera connected to the system)
    cap = cv2.VideoCapture(0)

    # Check if the camera was opened successfully
    if not cap.isOpened():
        print("Error: Unable to open the camera.")
        return

    # Define the interval (in seconds) for capturing photos
    interval = 5  # Change this value to set the interval between captures

    while True:
        # Start time for capturing the photo
        start_time = time.time()

        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if the frame was captured successfully
        if not ret:
            print("Error: Unable to capture frame.")
            break

        # Display the captured frame
        cv2.imshow('Camera', frame)

        # Check for the 'q' key press to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Calculate the time elapsed since the start of capturing
        elapsed_time = time.time() - start_time

        # Check if the elapsed time exceeds the interval
        if elapsed_time >= interval:
            # Save the captured frame as an image (you may want to change the file path)
            cv2.imwrite(f"captured_photo_{time.strftime('%Y%m%d_%H%M%S')}.jpg", frame)
            print("Photo captured.")

    # Release the camera
    cap.release()
    # Close all OpenCV windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
