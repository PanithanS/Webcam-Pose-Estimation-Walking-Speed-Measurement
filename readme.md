# The real-time human pose estimation, powered by YOLOv8 with the webcam 

This project is dedicated to applying computer vision to deliver a dependable and efficient solution for human pose recognition specifically focusing on measuring the walking speed of cardiac surgery patients in the rehabilitation dorm.

## Requirements
First, we use PyTorch(CPU)
see more on the PyTorch site: https://pytorch.org/get-started/locally/

```Python
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```
Then, we need to install an Ultralytics for the YOLOv8 pose estimation

```Python
pip install ultralytics
```

## Challenging Context: Low-budget, highly reliable, and user-friendly for low-level users.

Figure 1 illustrates the concept of detecting the walking speed of an individual moving from point A to point B. With the known distance between these two points, the methodology involves timing the passage of the person from A to B to determine their walking speed.
![image](https://github.com/PanithanS/Webcam-Pose-Estimation-using-YOLOv8/assets/83627892/15128a3b-c158-44bf-a05c-0f5338fd00c0)

## _
This project is under development!
