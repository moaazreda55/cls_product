from transformers import pipeline 


classifier_google = pipeline("image-classification",model="models/google")

classifier_resnet = pipeline("image-classification",model="models/resnet50")

classifier_facebook = pipeline("image-classification",model="models/facebook")


if __name__ == "__main__":
    
    print("this for kidding just do nothing")

    