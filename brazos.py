import numpy as np
import cv2
from math import acos, degrees

COLOR_PRIMARY =  (177, 170, 76)
COLOR_SECONDARY = (125, 120, 54)
COLOR_BG = (237, 227, 191)


class Brazos: 
    def __init__():
        pass

    @staticmethod
    def calcularAngulosCodos( frame, results, width, height):
        

            x1 = int(results.pose_landmarks.landmark[12].x * width)
            y1 = int(results.pose_landmarks.landmark[12].y * height)

            x2 = int(results.pose_landmarks.landmark[14].x * width)
            y2 = int(results.pose_landmarks.landmark[14].y * height)

            x3 = int(results.pose_landmarks.landmark[16].x * width)
            y3 = int(results.pose_landmarks.landmark[16].y * height)

            x4 = int(results.pose_landmarks.landmark[11].x * width)
            y4 = int(results.pose_landmarks.landmark[11].y * height)

            x5 = int(results.pose_landmarks.landmark[13].x * width)
            y5 = int(results.pose_landmarks.landmark[13].y * height)

            x6 = int(results.pose_landmarks.landmark[15].x * width)
            y6 = int(results.pose_landmarks.landmark[15].y * height)            

            # CALCULOS DE ANGULOS
            p1 = np.array([x1, y1])
            p2 = np.array([x2, y2])
            p3 = np.array([x3, y3])

            print("P1: ", p1)
            print("P2: ", p2)

            p4 = np.array([x4, y4])
            p5 = np.array([x5, y5])
            p6 = np.array([x6, y6])

            l1 = np.linalg.norm(p2 - p3)
            l2 = np.linalg.norm(p1 - p3)
            l3 = np.linalg.norm(p1 - p2)

            l4 = np.linalg.norm(p5 - p6)
            l5 = np.linalg.norm(p4 - p6)
            l6 = np.linalg.norm(p4 - p5)

            angle1 = degrees(acos((l1**2 + l3**2 - l2**2) / (2 * l1 * l3)))
            angle2 = degrees(acos((l4**2 + l6**2 - l5**2) / (2 * l4 * l6)))
        

            # DIBUJADO DE LAS LINEAS, TEXTO Y PUNTOS EN LA IMAGEN
            cv2.line(frame, (x1, y1), (x2, y2), COLOR_SECONDARY, 20)
            cv2.line(frame, (x2, y2), (x3, y3), COLOR_SECONDARY, 20)
            cv2.line(frame, (x1, y1), (x3, y3), COLOR_SECONDARY, 5)

            cv2.line(frame, (x4, y4), (x5, y5), COLOR_SECONDARY, 20)
            cv2.line(frame, (x5, y5), (x6, y6), COLOR_SECONDARY, 20)
            cv2.line(frame, (x4, y4), (x6, y6), COLOR_SECONDARY, 5)

            contours1 = np.array([[x1, y1], [x2, y2], [x3, y3]])
            cv2.fillPoly(frame, pts=[contours1], color=COLOR_BG)

            contours2 = np.array([[x4, y4], [x5, y5], [x6, y6]])
            cv2.fillPoly(frame, pts=[contours2], color=COLOR_BG)

            cv2.circle(frame, (x1, y1), 6, COLOR_PRIMARY, 4)
            cv2.circle(frame, (x2, y2), 6, COLOR_PRIMARY, 4)
            cv2.circle(frame, (x3, y3), 6, COLOR_PRIMARY, 4)

            cv2.circle(frame, (x4, y4), 6, COLOR_PRIMARY, 4)
            cv2.circle(frame, (x5, y5), 6, COLOR_PRIMARY, 4)
            cv2.circle(frame, (x6, y6), 6, COLOR_PRIMARY, 4)

            cv2.putText(frame, str(int(angle1)), (x2 - 60, y2), 1, 1.5,COLOR_BG, 2)

            cv2.putText(frame, str(int(angle2)), (x5 - 60, y5), 1, 1.5,COLOR_BG, 2)

            return (angle1, angle2)
