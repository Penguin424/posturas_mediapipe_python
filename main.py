from io import BytesIO, StringIO
from PIL import Image
from flask import Flask, render_template, Response;
import cv2
from brazos import Brazos
from espalda import Espalda
from piernas import Piernas
from flask_socketio import SocketIO, emit
import numpy as np
import mediapipe as mp
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app, cors_allowed_origins='http://localhost:3001')

COLOR_PRIMARY =  (177, 170, 76)
COLOR_SECONDARY = (125, 120, 54)
COLOR_BG = (237, 227, 191)

# cap = cv2.VideoCapture("media/video.mp4")

cap = cv2.VideoCapture(0)


codo_izquierdo = []
codo_derecho = []

rodilla_izquierda = []
rodilla_derecha = []

espalda = []

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# def generate():
#     with mp_pose.Pose(
#     static_image_mode=True
#     ) as pose:
#         while True:
#             ret, frame = cap.read()
        
#             if not ret:                            
#                 cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
#                 continue
            

            
#             height, width, _ = frame.shape
#             frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             results = pose.process(frame_rgb)
            

#             if results.pose_landmarks is not None:
#                 rodilla_iz, rodilla_de = Piernas.calcularAngulosRodillas(frame, results, width, height)
#                 codo_iz, codo_de = Brazos.calcularAngulosCodos(frame, results, width, height)
#                 epalda_ang = Espalda.calcularAngulosDorsal(frame, results, width, height)

#                 rodilla_izquierda.append(rodilla_iz)
#                 rodilla_derecha.append(rodilla_de)

#                 codo_izquierdo.append(codo_iz)
#                 codo_derecho.append(codo_de)

#                 espalda.append(epalda_ang)

                
#             codo_iznp = np.array(codo_izquierdo)
#             codo_derechonp = np.array(codo_derecho)

#             rodilla_iznp = np.array(rodilla_izquierda)
#             rodilla_derechonp = np.array(rodilla_derecha)

#             espaldanp = np.array(espalda)

            
#             if results.pose_landmarks is not None:
#                 cv2.rectangle(frame, (0, 0), (350, 180), COLOR_BG, cv2.FILLED)
#                 cv2.putText(frame, "CODO IZQUIERDO: " + " MIN " + str(int(codo_iznp.min())) + " MAX " + str(int(codo_iznp.max())), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLOR_PRIMARY, 2)
#                 cv2.putText(frame, "CODO DERECHO: " + " MIN " + str(int(codo_derechonp.min())) + " MAX " + str(int(codo_derechonp.max())), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLOR_PRIMARY, 2)
#                 cv2.putText(frame, "RODILLA IZQUIERDA: " + " MIN " + str(int(rodilla_iznp.min())) + " MAX " + str(int(rodilla_iznp.max())), (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLOR_PRIMARY, 2)
#                 cv2.putText(frame, "RODILLA DERECHA: " + " MIN " + str(int(rodilla_derechonp.min())) + " MAX " + str(int(rodilla_derechonp.max())), (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLOR_PRIMARY, 2)
#                 cv2.putText(frame, "ESPALDA: " + " MIN " + str(int(espaldanp.min())) + " MAX " + str(int(espaldanp.max())), (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLOR_PRIMARY, 2)
            

            
            
#             frame = cv2.resize(frame, (1080, 720))
#             cv2.imshow("DETECTOR DE POSTURA", frame)

#             (flag, encodedImage) = cv2.imencode(".jpg", frame);

#             if not flag:
#                 continue

#             yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')

#             # if cv2.waitKey(1) & 0xFF == 27:
#             #     break

@app.route('/')
def index():
    return render_template('index.html')

def readb64(uri):    
    encoded_data = uri.split(',')[1]
    sbuf = BytesIO()
    sbuf.write(base64.b64decode(encoded_data.encode('ascii')))
    pimg = Image.open(sbuf)
    return cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)

    

@socketio.on('message')
def handle_message(data):

    # with open('text.txt', 'w') as f:
    #     f.write(data + '\n')

    # frame = readb64(data)
    
    # with mp_pose.Pose(
    #     static_image_mode=True
    # ) as pose:
    #     height, width, _ = frame.shape
    #     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #     results = pose.process(frame_rgb)
            

    #     if results.pose_landmarks is not None:
    #         rodilla_iz, rodilla_de = Piernas.calcularAngulosRodillas(frame, results, width, height)
    #         codo_iz, codo_de = Brazos.calcularAngulosCodos(frame, results, width, height)
    #         epalda_ang = Espalda.calcularAngulosDorsal(frame, results, width, height)
    #         rodilla_izquierda.append(rodilla_iz)
    #         rodilla_derecha.append(rodilla_de)
    #         codo_izquierdo.append(codo_iz)
    #         codo_derecho.append(codo_de)
    #         espalda.append(epalda_ang)
            
    #     codo_iznp = np.array(codo_izquierdo)
    #     codo_derechonp = np.array(codo_derecho)
    #     rodilla_iznp = np.array(rodilla_izquierda)
    #     rodilla_derechonp = np.array(rodilla_derecha)
    #     espaldanp = np.array(espalda)
        
    #     if results.pose_landmarks is not None:
    #         cv2.rectangle(frame, (0, 0), (350, 180), COLOR_BG, cv2.FILLED)
    #         cv2.putText(frame, "CODO IZQUIERDO: " + " MIN " + str(int(codo_iznp.min())) + " MAX " + str(int(codo_iznp.max())), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLOR_PRIMARY, 2)
    #         cv2.putText(frame, "CODO DERECHO: " + " MIN " + str(int(codo_derechonp.min())) + " MAX " + str(int(codo_derechonp.max())), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLOR_PRIMARY, 2)
    #         cv2.putText(frame, "RODILLA IZQUIERDA: " + " MIN " + str(int(rodilla_iznp.min())) + " MAX " + str(int(rodilla_iznp.max())), (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLOR_PRIMARY, 2)
    #         cv2.putText(frame, "RODILLA DERECHA: " + " MIN " + str(int(rodilla_derechonp.min())) + " MAX " + str(int(rodilla_derechonp.max())), (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLOR_PRIMARY, 2)
    #         cv2.putText(frame, "ESPALDA: " + " MIN " + str(int(espaldanp.min())) + " MAX " + str(int(espaldanp.max())), (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLOR_PRIMARY, 2)
        
        
        
    #     frame = cv2.resize(frame, (1080, 720))

        

    #     converted = cv2.imencode('.jpeg', frame)[1]
        

    #     # emit('message', base64.b64decode(converted))

        emit('message', data)
        
        
        
            # if cv2.waitKey(1) & 0xFF == 27:
            #     break
        




# @app.route('/video_feed')
# def video_feed():
#     return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')
    
if __name__ == '__main__':    
    socketio.run(app, host='192.168.15.157', port=3000, debug=True)
    # app.run(debug=True, host='192.168.15.157', port=3000)


# cap.release()