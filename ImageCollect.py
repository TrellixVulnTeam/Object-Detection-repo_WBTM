# Import the necesarry libraries
from genericpath import exists
import  cv2
import  uuid
import  os
import  time
import pathlib

# Label for Images
labels  = ['good','bad']
nImage  = 5

# Setup Folder
ADD_PATH    = os.path.join('Tensorflow', 'workspace', 'images', 'collectedImages')
CURR_PATH   = pathlib.Path().resolve()
IMG_PATH    = os.path.join(CURR_PATH, ADD_PATH)

if not os.path.exists(IMG_PATH):
    os.makedirs(IMG_PATH)


for label in labels:
    path    = os.path.join(IMG_PATH, label)
    if not os.path.exists(path):
        os.makedirs(path)

# Images Collection
def imageCollect(labels, IMG_PATH, nImage):
    labels      = labels
    IMG_PATH    = IMG_PATH
    nImage      = nImage

    for label in labels:
        cap    = cv2.VideoCapture(0)
        print('Collecting images for {}'.format(label))
        time.sleep(5)
        for imageNum in range(nImage):
            print('Collecting image {}'.format(imageNum))
            ret, frame = cap.read()
            imageName  = os.path.join(IMG_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
            cv2.imwrite(imageName, frame)
            cv2.imshow('frame', frame)
            time.sleep(2)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

# imageCollect(labels, IMG_PATH, nImage)

# Setting labelImg
LABELING_PATH   = os.path.join('Tensorflow', 'labelimg')

if not os.path.exists(LABELING_PATH):
    os.makedirs(LABELING_PATH)