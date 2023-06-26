import cv2, os

name = input("Video name: ")
fps = int(input("Video FPS: "))
path = "images"
out_path = name + ".mp4"
files = os.listdir(path)
images = []

for i in files:
    images.append(path +"/"+ i)

frame = cv2.imread(images[0])
dimensions = (frame.shape[1],frame.shape[0])
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video = cv2.VideoWriter(out_path, fourcc, fps, dimensions)

for i,img in enumerate(images):
    video.write(cv2.imread(img))
    print(f"Releasing ({i+1}/{len(images)})")

video.release()
print("Done")