from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from PIL import Image
import io
import base64
import cv2
import numpy as np
import mediapipe as mp
from tkinter_GUI import overlay_heart_image, overlay_liver_image, overlay_skull_image, get_landmarks, load_image

app = Flask(__name__)

skull_image = load_image('images/skull_image.png')
liver_image = load_image('images/liver_image.png')
heart_image = load_image('images/heart_image.png')
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

@app.route('/')
def upload_file():
   return render_template('index.html')

@app.route("/process_frame", methods=["POST"])
def process_frame():
    file = None
    process_button = None

    # Check if the POST request has the file part
    if 'image' in request.files:
        file = request.files['image']
    if 'button' in request.form:
        process_button = request.form["button"]

    # check if the post request has the file part
    if file:
        image = Image.open(file.stream)  # PIL image
        frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        landmarks = get_landmarks(frame, pose)

        if process_button == 'liver_button':
            frame = overlay_liver_image(frame, liver_image, (0, 0), landmarks)
        elif process_button == 'heart_button':
            frame = overlay_heart_image(frame, heart_image, landmarks)
        elif process_button == 'skull_button':
            frame = overlay_skull_image(frame, skull_image, landmarks)

        ret, encoded_frame = cv2.imencode('.jpg', frame)
        frame_string = base64.b64encode(encoded_frame.tobytes()).decode('utf-8')
        print("data:image/jpeg;base64," + frame_string)
        return jsonify({"frame": frame_string})

    return 'No file part'

if __name__ == '__main__':
    app.run(debug = True)