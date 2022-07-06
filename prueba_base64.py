import base64
from io import BytesIO
from PIL import Image
import cv2
import numpy as np


def readb64(uri):
    # encoded_data = uri.split(',')[1]
    # nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    # img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # return img
    encoded_data = uri.split(',')[1]
    sbuf = BytesIO()
    sbuf.write(base64.b64decode(encoded_data.encode('ascii')))
    pimg = Image.open(sbuf)
    return cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)


with open('text.txt', 'r') as f:
    r = f.read()
    r = r.split('\n')

    for i in r:
        img = readb64(i)
        img = cv2.resize(img, (1080, 720))

        cv2.imshow("DETECTOR DE POSTURA",img)

        cv2.waitKey(0)



    




    





