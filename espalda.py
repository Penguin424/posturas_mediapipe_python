import numpy as np
import cv2
from math import acos, degrees

COLOR_PRIMARY =  (177, 170, 76)
COLOR_SECONDARY = (125, 120, 54)
COLOR_BG = (237, 227, 191)

class Espalda:
    def __init__():
        pass

    @staticmethod
    def calcularAngulosDorsal( frame, results, width, height):            
        puntoMedioAlto = Espalda.calcularPuntoMedio(11, 12, results, width, height)
        puntoMedioBaja = Espalda.calcularPuntoMedio(23, 24, results, width, height)
        puntoMedioMedia = Espalda.calcularPuntoMedio(12, 23, results, width, height)

        p1 = np.array(puntoMedioAlto)
        p2 = np.array(puntoMedioMedia)
        p3 = np.array(puntoMedioBaja)

        l1 = np.linalg.norm(p2 - p3)
        l2 = np.linalg.norm(p1 - p3)
        l3 = np.linalg.norm(p1 - p2)

        contours1 = np.array([puntoMedioAlto, puntoMedioMedia, puntoMedioBaja])
            

        angle1 = degrees(acos((l1**2 + l3**2 - l2**2) / (2 * l1 * l3)))


        cv2.line(frame, puntoMedioAlto, puntoMedioMedia, COLOR_SECONDARY, 20)
        cv2.line(frame, puntoMedioMedia, puntoMedioBaja, COLOR_SECONDARY, 20)
        cv2.line(frame, puntoMedioAlto, puntoMedioBaja, COLOR_SECONDARY, 5)

                        
        cv2.circle(frame, puntoMedioAlto, 6, COLOR_PRIMARY, 4)
        cv2.circle(frame, puntoMedioBaja, 6, COLOR_PRIMARY, 4)
        cv2.circle(frame, puntoMedioMedia, 6, COLOR_PRIMARY, 4)

        cv2.fillPoly(frame, pts=[contours1], color=COLOR_BG)

        cv2.putText(frame, str(int(angle1)), (puntoMedioMedia[0] - 60, puntoMedioMedia[1]), 1, 1.5,COLOR_BG, 2)

        return angle1


    @staticmethod
    def calcularPuntoMedio( p1, p2, results, width, height):
            x1 = int(results.pose_landmarks.landmark[p1].x * width)
            y1 = int(results.pose_landmarks.landmark[p1].y * height)
                                
            x3 = int(results.pose_landmarks.landmark[p2].x * width)
            y3 = int(results.pose_landmarks.landmark[p2].y * height)


            x2 = int((x1 + x3) // 2)
            y2 = int((y1 + y3) // 2)

            return (x2, y2)

            

            