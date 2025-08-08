from transformers import pipeline 

classifier_google = pipeline("image_classification",model="google")

classifier_resnet = pipeline("image_classification",model="resnet50")

classifier_facebook = pipeline("image_classification",model="facebook")


if __name__ == "__main__":
    
    print("this for kidding just do nothing")