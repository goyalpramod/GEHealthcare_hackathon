import cv2
import mediapipe as mp
import numpy as np
import math
import time
import tkinter as tk
from PIL import ImageTk, Image
import tkinter.simpledialog as simpledialog

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

skull_toggle = False
skull_info_toggle = False
liver_toggle = False
liver_info_toggle = False
heart_toggle = False
heart_info_toggle = False
respiratory_toggle = False
respiratory_info_toggle = False
skull_info = """The skull is a bone protective cavity for the brain.[1] The skull is composed of four types of bone i.e., cranial bones, facial bones, ear ossicles and hyoid bone"""
liver_info = """The liver is essential for digesting food and ridding your body of toxic substances. Liver disease can be inherited (genetic)."""
heart_info = """The Heart pumps blood through the blood vessels of the circulatory system. The pumped blood carries oxygen and nutrients to the body, while carrying metabolic waste such as carbon dioxide to the lungs"""
respiratory_info = """longs"""

def toggle_skull():
    global skull_toggle
    skull_toggle = not skull_toggle


def toggle_liver():
    global liver_toggle
    liver_toggle = not liver_toggle


def toggle_heart():
    global heart_toggle
    heart_toggle = not heart_toggle
def toggle_respiratory():
    global respiratory_toggle
    respiratory_toggle = not respiratory_toggle


def toggle_skull_info():
    global skull_info_toggle
    skull_info_toggle = not skull_info_toggle


def toggle_liver_info():
    global liver_info_toggle
    liver_info_toggle = not liver_info_toggle


def toggle_heart_info():
    global heart_info_toggle
    heart_info_toggle = not heart_info_toggle
def toggle_respiratory_info():
    global respiratory_info_toggle
    respiratory_info_toggle = not respiratory_info_toggle


def edit_skull_info():
    global skull_info
    skull_info = simpledialog.askstring("Edit Skull Info", "Enter new information for the skull:",
                                        initialvalue=skull_info)
    if skull_info is None:  # Restore if canceled
        skull_info = ...


def edit_liver_info():
    global liver_info
    liver_info = simpledialog.askstring("Edit Liver Info", "Enter new information for the liver:",
                                        initialvalue=liver_info)
    if liver_info is None:  # Restore if canceled
        liver_info = ...


def edit_heart_info():
    global heart_info
    heart_info = simpledialog.askstring("Edit Heart Info", "Enter new information for the heart:",
                                        initialvalue=heart_info)
    if heart_info is None:  # Restore if canceled
        heart_info = ...
def edit_respiratory_info():
    global respiratory_info
    respiratory_info = simpledialog.askstring("Edit respiratory Info", "Enter new information for the respiratory:",
                                        initialvalue=respiratory_info)
    if respiratory_info is None:  # Restore if canceled
        respiratory_info = ...


def load_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if img.shape[2] != 4:
        alpha_channel = np.ones(img.shape[:2], dtype=img.dtype) * 255
        img = cv2.merge((img, alpha_channel))
    return img


def get_landmarks(frame, pose):
    RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(RGB)
    pose_landmarks = None
    if results.pose_landmarks:
        pose_landmarks = results.pose_landmarks
    return pose_landmarks


def overlay_skull_image(frame, overlay_img, landmarks):
    if landmarks:
        left_eye = landmarks.landmark[mp_pose.PoseLandmark.LEFT_EYE_INNER]
        left_ear = landmarks.landmark[mp_pose.PoseLandmark.LEFT_EAR]
        right_ear = landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EAR]
        right_mouth = landmarks.landmark[mp_pose.PoseLandmark.MOUTH_RIGHT]
        print(left_eye.visibility)
        if (left_ear.visibility > 0.1 and right_ear.visibility > 0.5 and left_eye.visibility > 0.9
                and right_mouth.visibility > 0.9):
            # Calculate rotation angle in radians
            radians = math.atan2(right_ear.y - left_ear.y, right_ear.x - left_ear.x)

            # Convert to degrees
            angle = -(math.degrees(radians) + 180) % 360

            # Rotate the overlay image
            m = cv2.getRotationMatrix2D(tuple(np.divide(overlay_img.shape[:2], 2)), angle, 1)
            overlay_img = cv2.warpAffine(overlay_img, m, overlay_img.shape[:2])

            skull_x = int((left_ear.x + (1 / 2) * (right_ear.x - left_ear.x)) * frame.shape[1])
            skull_y = int(max(left_ear.y, right_ear.y) * frame.shape[0])

            dist_ears = np.sqrt((right_ear.x - left_ear.x) ** 2 + (right_ear.y - left_ear.y) ** 2)
            skull_width = int(frame.shape[1] * dist_ears * 2.7)
            aspect_ratio = overlay_img.shape[1] / overlay_img.shape[0]
            skull_height = int(skull_width / aspect_ratio)

            skull_image_resized = cv2.resize(overlay_img, (skull_width, skull_height), interpolation=cv2.INTER_AREA)

            skull_y = min(max(skull_y - skull_height // 2, 0), frame.shape[0] - skull_height)
            skull_x = min(max(skull_x - skull_width // 2, 0), frame.shape[1] - skull_width)

            skull_channels = cv2.split(skull_image_resized)

            mask = cv2.cvtColor(skull_channels[3], cv2.COLOR_GRAY2BGR)
            mask = mask / 255.0

            r, g, b, a = skull_channels
            skull_channels_rgb = cv2.merge([r, g, b])
            skull_portion = frame[skull_y:skull_y + skull_height, skull_x:skull_x + skull_width]

            overlay = skull_channels_rgb * mask + skull_portion * (1 - mask)
            overlay = np.uint8(overlay)

            frame[skull_y:skull_y + skull_height, skull_x:skull_x + skull_width] = overlay
            info_box_origin = (skull_x - 100, skull_y + 290)

            info_text = str(skull_info)

            if skull_info_toggle:
                cv2.rectangle(frame,
                              info_box_origin,
                              (info_box_origin[0] + 480, info_box_origin[1] - 80),
                              (255, 225, 255),
                              cv2.FILLED)
                step = 45
                for i in range(0, len(info_text), step):
                    cv2.putText(frame,
                                info_text[i:i + step] if len(info_text) - i > step else info_text[i:],
                                (info_box_origin[0] + 10, info_box_origin[1] - 65 + int(i / step * 20)),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.6,
                                (0, 0, 0),
                                1)

        return frame


def overlay_liver_image(frame, overlay_img, location, landmarks):
    if landmarks:
        right_shoulder = landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        right_hip = landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP]
        if right_hip.visibility > 0.1:
            overlay_x, overlay_y = location
            liver_x = int((right_shoulder.x + (3 / 5) * (right_hip.x - right_shoulder.x)) * frame.shape[1]) - 15
            liver_y = int((right_shoulder.y + (3 / 5) * (right_hip.y - right_shoulder.y)) * frame.shape[0]) - 60
            dist_shoulder_hip = np.sqrt((right_hip.x - right_shoulder.x) ** 2 + (right_hip.y - right_shoulder.y) ** 2)
            liver_width = int(frame.shape[1] * dist_shoulder_hip * 0.4)
            aspect_ratio = overlay_img.shape[1] / overlay_img.shape[0]
            liver_height = int(liver_width / aspect_ratio)
            liver_image_resized = cv2.resize(overlay_img, (liver_width, liver_height), interpolation=cv2.INTER_AREA)
            liver_y = min(max(liver_y, 0), frame.shape[0] - liver_height)
            liver_x = min(max(liver_x, 0), frame.shape[1] - liver_width)
            liver_channels = cv2.split(liver_image_resized)
            mask = cv2.cvtColor(liver_channels[3], cv2.COLOR_GRAY2BGR)
            mask = mask / 255.0
            r, g, b, a = liver_channels
            liver_channels_rgb = cv2.merge([r, g, b])
            liver_portion = frame[liver_y:liver_y + liver_height, liver_x:liver_x + liver_width]
            overlay = liver_channels_rgb * mask + liver_portion * (1 - mask)
            overlay = np.uint8(overlay)
            frame[liver_y:liver_y + liver_height, liver_x:liver_x + liver_width] = overlay
            info_box_origin = (liver_x - 80, liver_y - 20)  # Placing the info box above the respiratory
            info_text = str(liver_info)
            info_text_line1 = 'The liver is essential for digesting food and'
            info_text_line2 = 'ridding your body of toxic substances.'
            info_text_line3 = 'Liver disease can be inherited (genetic).'
            if liver_info_toggle:
                cv2.rectangle(frame,
                              info_box_origin,
                              (info_box_origin[0] + 430, info_box_origin[1] - 80),
                              (255, 225, 255),
                              cv2.FILLED)

                step = 50
                for i in range(0, len(info_text), step):
                    cv2.putText(frame,
                                info_text[i:i + step] if len(info_text) - i > step else info_text[i:],
                                (info_box_origin[0] + 10, info_box_origin[1] - 65 + int(i / step * 20)),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.6,
                                (0, 0, 0),
                                1)
    return frame


def overlay_left_arm_image(frame, overlay_img, landmarks):
    if landmarks:
        left_shoulder = landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
        left_wrist = landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
        if left_shoulder.visibility > 0.5 and left_wrist.visibility > 0.5:
            dist_shoulder_wrist = np.sqrt(
                (left_wrist.x - left_shoulder.x) ** 2 + (left_wrist.y - left_shoulder.y) ** 2
            )
            arm_width = int(frame.shape[1] * dist_shoulder_wrist * 0.75)
            aspect_ratio = overlay_img.shape[1] / overlay_img.shape[0]
            arm_height = int(arm_width / aspect_ratio)
            arm_x = int((left_shoulder.x + left_wrist.x) / 2 * frame.shape[1])
            arm_y = int((left_shoulder.y + left_wrist.y) / 2 * frame.shape[0])
            arm_image_resized = cv2.resize(overlay_img, (arm_width, arm_height), interpolation=cv2.INTER_AREA)
            arm_y = min(max(arm_y - arm_height // 2, 0), frame.shape[0] - arm_height)
            arm_x = min(max(arm_x - arm_width // 2, 0), frame.shape[1] - arm_width)
            arm_channels = cv2.split(arm_image_resized)
            mask = cv2.cvtColor(arm_channels[3], cv2.COLOR_GRAY2BGR)
            mask = mask / 255.0
            r, g, b, a = arm_channels
            arm_channels_rgb = cv2.merge([r, g, b])
            arm_portion = frame[arm_y:arm_y + arm_height, arm_x:arm_x + arm_width]
            overlay = arm_channels_rgb * mask + arm_portion * (1 - mask)
            overlay = np.uint8(overlay)
            frame[arm_y:arm_y + arm_height, arm_x:arm_x + arm_width] = overlay

    return frame


def overlay_torso_image(frame, overlay_img, landmarks):
    if landmarks:
        left_shoulder = landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
        right_shoulder = landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        left_hip = landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
        right_hip = landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP]
        if all(landmark.visibility > 0.5 for landmark in [left_shoulder, right_shoulder, left_hip, right_hip]):
            x = min(left_shoulder.x, left_hip.x) * frame.shape[1] - 80
            y = min(left_shoulder.y, right_shoulder.y) * frame.shape[0]
            width = max(right_shoulder.x, right_hip.x) * frame.shape[1] - x
            height = max(left_hip.y, right_hip.y) * frame.shape[0] - y
            # Convert all to int
            x, y, width, height = int(x), int(y), abs(int(width)), abs(int(height))

            overlay_img_resized = cv2.resize(overlay_img, (width, height), interpolation=cv2.INTER_AREA)
            overlay_channels = cv2.split(overlay_img_resized)
            mask = cv2.cvtColor(overlay_channels[3], cv2.COLOR_GRAY2BGR)
            mask = mask / 255.0
            r, g, b, a = overlay_channels
            overlay_channels_rgb = cv2.merge([r, g, b])
            torso_portion = frame[y:y + height, x:x + width]
            overlay = overlay_channels_rgb * mask + torso_portion * (1 - mask)
            overlay = np.uint8(overlay)
            frame[y:y + height, x:x + width] = overlay
    return frame


def overlay_heart_image(frame, overlay_img, landmarks):
    if landmarks:
        left_shoulder = landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
        right_shoulder = landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        current_time = time.time()
        scale_factor = 1 + 0.05 * math.sin(15 * current_time)
        heart_x_cache = int((left_shoulder.x + (1 / 2) * (right_shoulder.x - left_shoulder.x)) * frame.shape[1]) - 30
        heart_y_cache = int((left_shoulder.y + (1 / 2) * (right_shoulder.y - left_shoulder.y)) * frame.shape[0]) + 30

        dist_shoulder = np.sqrt((right_shoulder.x - left_shoulder.x) ** 2 + (right_shoulder.y - left_shoulder.y) ** 2)
        heart_width = int(scale_factor * frame.shape[1] * dist_shoulder * 0.6)
        aspect_ratio = overlay_img.shape[1] / overlay_img.shape[0]
        heart_height = int(scale_factor * heart_width / aspect_ratio)

        heart_image_resized = cv2.resize(overlay_img, (heart_width, heart_height), interpolation=cv2.INTER_AREA)

        heart_y = min(max(heart_y_cache, 0), frame.shape[0] - heart_height)
        heart_x = min(max(heart_x_cache, 0), frame.shape[1] - heart_width)

        heart_channels = cv2.split(heart_image_resized)

        mask = cv2.cvtColor(heart_channels[3], cv2.COLOR_GRAY2BGR)
        mask = mask / 255.0

        r, g, b, a = heart_channels
        heart_channels_rgb = cv2.merge([r, g, b])
        heart_portion = frame[heart_y:heart_y + heart_height, heart_x:heart_x + heart_width]

        overlay = heart_channels_rgb * mask + heart_portion * (1 - mask)
        overlay = np.uint8(overlay)

        frame[heart_y:heart_y + heart_height, heart_x:heart_x + heart_width] = overlay
        info_text = str(heart_info)
        # Create a rectangle for the pop up and add some text
        info_box_origin = (heart_x_cache - 140, heart_y_cache - 20)  # Placing the info box above the heart
        if heart_info_toggle:
            cv2.rectangle(frame,
                          info_box_origin,
                          (info_box_origin[0] + 550, info_box_origin[1] - 80),
                          (255, 225, 255),
                          cv2.FILLED)
            step = 50
            for i in range(0, len(info_text), step):
                cv2.putText(frame,
                            info_text[i:i + step] if len(info_text) - i > step else info_text[i:],
                            (info_box_origin[0] + 10, info_box_origin[1] - 65 + int(i / step * 20)),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6,
                            (0, 0, 0),
                            1)

        return frame


def overlay_respiratory_image(frame, overlay_img, landmarks):
    if landmarks:
        left_shoulder = landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
        right_shoulder = landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        left_hip = landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
        right_hip = landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP]

        # Assume that the lungs are located in the middle of these four points
        respiratory_y_cache = int((left_shoulder.y + right_shoulder.y + left_hip.y + right_hip.y) / 4 * frame.shape[0])
        respiratory_x_cache = int((left_shoulder.x + right_shoulder.x + left_hip.x + right_hip.x) / 4 * frame.shape[1])

        # Calculate width and height similar to other overlay_ functions here
        dist_shoulder = np.sqrt((right_shoulder.x - left_shoulder.x) ** 2 +
                                (right_shoulder.y - left_shoulder.y) ** 2)
        respiratory_width = int(frame.shape[1] * dist_shoulder*1.2)
        aspect_ratio = overlay_img.shape[1] / overlay_img.shape[0]
        respiratory_height = int(respiratory_width / aspect_ratio)

        respiratory_image_resized = cv2.resize(overlay_img, (respiratory_width, respiratory_height),
                                               interpolation=cv2.INTER_AREA)
        respiratory_y = min(max(respiratory_y_cache, 0), frame.shape[0] - respiratory_height)-120
        respiratory_x = min(max(respiratory_x_cache, 0), frame.shape[1] - respiratory_width)-60
        # Similar to other overlay_ functions here, blend the resized respiratory image with the frame
        respiratory_channels = cv2.split(respiratory_image_resized)
        mask = cv2.cvtColor(respiratory_channels[3], cv2.COLOR_GRAY2BGR)
        mask = mask / 255.0

        r, g, b, a = respiratory_channels
        respiratory_channels_rgb = cv2.merge([r, g, b])
        # respiratory_portion = frame[respiratory_y:respiratory_y + respiratory_height,
        #                       respiratory_x:respiratory_x + respiratory_width]

        # # overlay = respiratory_channels_rgb * mask + respiratory_portion * (1 - mask)
        # respiratory_y = min(max(respiratory_y, 0), frame.shape[0] - respiratory_height)
        # respiratory_x = min(max(respiratory_x, 0), frame.shape[1] - respiratory_width)

        respiratory_portion = frame[respiratory_y:respiratory_y + respiratory_height,
                              respiratory_x:respiratory_x + respiratory_width]

        overlay = respiratory_channels_rgb * mask + respiratory_portion * (1 - mask)
        overlay = np.uint8(overlay)
        frame[respiratory_y:respiratory_y + respiratory_height,
        respiratory_x:respiratory_x + respiratory_width] = overlay
        info_text = respiratory_info
        info_box_origin = (respiratory_x_cache - 40, respiratory_y_cache - 100)
        if respiratory_info_toggle:
            cv2.rectangle(frame,
                          info_box_origin,
                          (info_box_origin[0] + 550, info_box_origin[1] - 80),
                          (255, 225, 255),
                          cv2.FILLED)
            step = 50
            for i in range(0, len(info_text), step):
                cv2.putText(frame,
                            info_text[i:i + step] if len(info_text) - i > step else info_text[i:],
                            (info_box_origin[0] + 10, info_box_origin[1] - 65 + int(i / step * 20)),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6,
                            (0, 0, 0),
                            1)

    return frame


def main():
    global skull_toggle, liver_toggle, heart_toggle

    skull_toggle = False
    liver_toggle = False
    heart_toggle = False

    skull_image = load_image('images/skull_image.png')
    liver_image = load_image('images/liver_image.png')
    heart_image = load_image('images/heart_image.png')
    respiratory_image = load_image('images/respiratory_image.png')
    left_arm_image = load_image('images/left_arm.png')
    torso_image = load_image('images/torso.png')
    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()
    if not ret:
        print("Failed to open the webcam.")
        exit(1)

    root = tk.Tk()
    height, width, _ = frame.shape
    root.geometry(f"{width + 40}x{height + 500}")
    root.title("AR Organ Projection")
    # root.geometry("1280x720")
    root.configure(background="light grey")

    panel = tk.Label(root)
    panel.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    main_frame = tk.Frame(root, bg="light grey")
    main_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

    def create_organ_frame(parent, organ_name, toggle_command, toggle_info_command, edit_info_command):
        frame = tk.LabelFrame(parent, text=organ_name, font=("Helvetica", 20), bg="white", bd=5)

        tk.Button(frame, text=f"Toggle {organ_name} Overlay", command=toggle_command, height=2, width=20,
                  bg="light green").pack(side="top", padx=5, pady=5)
        tk.Button(frame, text=f"Toggle {organ_name} Info", command=toggle_info_command, height=2, width=20,
                  bg="light blue").pack(side="top", padx=5, pady=5)
        tk.Button(frame, text=f"Edit {organ_name} Info", command=edit_info_command, height=2, width=20,
                  bg="light yellow").pack(side="top", padx=5, pady=5)

        return frame

    skull_frame = create_organ_frame(main_frame, 'Skull', toggle_skull, toggle_skull_info, edit_skull_info)
    skull_frame.grid(row=0, column=0, padx=15)

    liver_frame = create_organ_frame(main_frame, 'Liver', toggle_liver, toggle_liver_info, edit_liver_info)
    liver_frame.grid(row=0, column=1, padx=15)

    heart_frame = create_organ_frame(main_frame, 'Heart', toggle_heart, toggle_heart_info, edit_heart_info)
    heart_frame.grid(row=0, column=2, padx=15)

    respiratory_frame = create_organ_frame(main_frame, 'respiratory', toggle_respiratory, toggle_respiratory_info, edit_respiratory_info)
    respiratory_frame.grid(row=0, column=3, padx=15)

    def video_loop():
        ret, frame = cap.read()
        if not ret:
            return
        # print(frame.shape)
        landmarks = get_landmarks(frame, pose)
        # frame = overlay_left_arm_image(frame, left_arm_image, landmarks)
        # frame = overlay_torso_image(frame, torso_image, landmarks)
        if respiratory_toggle:
            frame = overlay_respiratory_image(frame, respiratory_image, landmarks)
        if liver_toggle:
            frame = overlay_liver_image(frame, liver_image, (0, 0), landmarks)
        if heart_toggle:
            frame = overlay_heart_image(frame, heart_image, landmarks)
        if skull_toggle:
            frame = overlay_skull_image(frame, skull_image, landmarks)
        mp_drawing.draw_landmarks(frame, landmarks, mp_pose.POSE_CONNECTIONS)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)

        panel.imgtk = imgtk
        panel.configure(image=imgtk)
        root.after(10, video_loop)

    video_loop()
    root.mainloop()

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
