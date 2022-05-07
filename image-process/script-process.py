from PIL import Image
from db.banco import *

import os
import cv2
import pytesseract
import PIL.Image

path =  "image-process\obj"
os.chdir(path)

def convert_image(file):
    img_gray = Image.open(f'{file}.jpg')
    img_gray = img_gray.convert('L')
    img_gray.save(f"../gray-images/{file}_gray.jpg")
    
    return cv2.imread(f"../gray-images/{file}_gray.jpg")

def get_coordenates(img):
    fl = open(f'{file}.txt', 'r')
    data = fl.readlines()
    fl.close() 
    return data

def extract_box(data):
    for dt in data:
        class_id, x_center, y_center, w, h = map(float, dt.split(' '))
        x_center, y_center, w, h = float(x_center), float(y_center), float(w), float(h)
        x_center = round(x_center * dw)
        y_center = round(y_center * dh)
        w = round(w * dw)
        h = round(h * dh)
        x = round(x_center - w / 2)
        y = round(y_center - h / 2)

        return img[y:y + h, x:x + w]
        
def tesseract(file):
    return pytesseract.image_to_string(PIL.Image.open(f"../plates/{file}.jpg"), config ='--oem 3 --psm 6')

if __name__ == '__main__':
    
    banco = create_db('../db/pardal.db')
    cursor = banco.cursor()
    create_table(cursor)

    img = ""

    try:
        for file in os.listdir():
            if file.endswith(".txt"):
                file = file.split(".")[0]
                img = convert_image(file)
                dh, dw, _ = img.shape
                coordinates = get_coordenates(img)
                imgCrop = extract_box(coordinates)
                cv2.imwrite(f"../plates/{file}.jpg", imgCrop)

                insert_db(" ".join(coordinates).strip('\n'), tesseract(file).strip('\n'), f'{file}.jpg', f'../gray-images/{file}_gray.jpg', cursor)
    except:
        pass
    commit_db(banco)
    consulta_db(cursor)
    close_db(banco)



