from ultralytics import YOLO

LABELS = {0: 'card_ability', 1: 'cost', 2: 'crew', 3: 'damage_1', 4: 'damage_2', 5: 'damage_3', 6: 'miss', 7: 'name', 8: 'reactor', 9: 'shield', 10: 'shippart_name', 11: 'thruster', 12: 'type'}


class IMGmodel:
    def __init__(self):
        pass


    def predict():
        model = YOLO('weights/best.pt')
        return model.predict(
        source='Test',
        conf=0.10,
        save=True,
        save_txt=True
        )

# results = IMGmodel.predict()
