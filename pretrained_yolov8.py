from ultralytics import YOLO

model = YOLO("yolov8l-seg.pt")
model.predict(source = 'busyroad.png',save = True,conf =0.5,save_txt = True,show=True)
