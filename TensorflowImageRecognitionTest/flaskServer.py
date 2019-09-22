from flask import Flask, request
import face_recognition
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"
@app.route('check-image', method = ['GET'])
def checkImage():
    if(request.method="GET"):
        compareImages = []
        imageStrings = []
        for filename in os.listdir("./images"):
            if(filename.endswith(".jpg")):
                curr = face_recognition.load_image_file(os.path.join(directory, filename))
                compareImages.append(curr)
                imageStrings.append(filename[:-3])
        #image from phone
        image = **placeholder**
        knownEncodings = []
        for (i in in range(len(compareImages))):
            knownEncodings.append(face_recognition.face_encodings(compareImages[i])[0])
        results = face_recognition.compare_faces(knownEncodings, image)
        for (i in range(len(results))):
            if(results[i]) {
                match = imageStrings[i]
                break;
            }

@app.route('save-image', method = ['POST'])
def saveImage():
    if(request.method = "POST"):
        #Save image into images folder with First name as the file name
        #Ex. Tony.jpg



if __name__ == '__main__':
    print("running server")
    app.run(port=3000) #run app in debug mode on port 5000
