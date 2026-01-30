from flask import Flask, Response
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0) # 0 = webcam par défaut

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        # Encodage en JPEG pour le streaming
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        # Format multipart pour le navigateur/OpenCV
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    # 0.0.0.0 permet l'accès depuis WSL (qui est sur un réseau virtuel)
    app.run(host='0.0.0.0', port=5000)
