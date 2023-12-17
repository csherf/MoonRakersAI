from ultralytics import YOLO



class IMGmodel:
    def __init__(self):
        pass


    def predict():
        model = YOLO('weights/best.pt')
        model.predict(
        source='Test',
        conf=0.50
        )


IMGmodel.predict()