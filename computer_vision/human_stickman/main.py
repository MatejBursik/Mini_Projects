#model source https://github.com/quanhua92/human-pose-estimation-opencv/blob/master/openpose.py

import cv2
import matplotlib.pyplot as plt

net = cv2.dnn.readNetFromTensorflow("graph_opt.pb")

#variables set as default by the model
inWidth = 368
inHeight = 368
thr = 0.2

BODY_PARTS = { "Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
               "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
               "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
               "LEye": 15, "REar": 16, "LEar": 17, "Background": 18 }

POSE_PAIRS = [ ["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
               ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
               ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
               ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"],
               ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"] ]

def read_image(frame):
    #image settings
    net.setInput(cv2.dnn.blobFromImage(frame, 1.0, (inWidth, inHeight), (127.5,127.5,127.5), swapRB=True, crop=False))
    
    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]
    
    out = net.forward()
    out = out[:, :19, :, :]  # MobileNet output [1, 57, -1, -1], we only need the first 19 elements

    assert(len(BODY_PARTS) == out.shape[1])

    points = []
    for i in range(len(BODY_PARTS)):
        # Slice heatmap of corresponging body's part.
        heatMap = out[0, i, :, :]

        # Originally, we try to find all the local maximums. To simplify a sample
        # we just find a global one. However only a single pose at the same time
        # could be detected this way.
        _, conf, _, point = cv2.minMaxLoc(heatMap)
        x = (frameWidth * point[0]) / out.shape[3]
        y = (frameHeight * point[1]) / out.shape[2]
        # Add a point if it's confidence is higher than threshold.
        points.append((int(x), int(y)) if conf > thr else None)

    for pair in POSE_PAIRS:
        partFrom = pair[0]
        partTo = pair[1]
        assert(partFrom in BODY_PARTS)
        assert(partTo in BODY_PARTS)

        idFrom = BODY_PARTS[partFrom]
        idTo = BODY_PARTS[partTo]

        if points[idFrom] and points[idTo]:
            cv2.line(frame, points[idFrom], points[idTo], (0, 255, 0), 3)
            cv2.ellipse(frame, points[idFrom], (3, 3), 0, 0, 360, (0, 0, 255), cv2.FILLED)
            cv2.ellipse(frame, points[idTo], (3, 3), 0, 0, 360, (0, 0, 255), cv2.FILLED)

    t, _ = net.getPerfProfile()
    freq = cv2.getTickFrequency() / 1000
    cv2.putText(frame, '%.2fms' % (t / freq), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    return frame

video = cv2.VideoCapture("video.mp4") #for live feed, replace the "path string" with 0 (camera index)
frame_number = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
sequence = []

counter = 0
while True:
    end, image = video.read()
    if not end:
        break
        
    sequence.append(read_image(image))
    counter += 1
    print(f"Tracking ({counter}/{frame_number})")


fps = video.get(cv2.CAP_PROP_FPS)
dimensions = (sequence[0].shape[1],sequence[0].shape[0])

print(f"FPS: {fps}\nDimensions: {dimensions}")
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output = cv2.VideoWriter("processed.mp4",fourcc,fps,dimensions)
for i,image in enumerate(sequence):
    output.write(image)
    print(f"Releasing ({i+1}/{len(sequence)})")

output.release()
print("Done")