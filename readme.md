# The real-time human pose estimation and walking speed measurement, powered by YOLOv8 with a webcam

In this project, we apply computer vision to deliver a solution for human pose and walking speed recognition. Specifically focusing on measuring the patients' walking speed in the rehabilitation dorm.
This project aims to provide a low-cost solution, user-friendly, and easy to distribute.

**Fig.1** The image demonstrates how to detect the walking speed. With the known distance between these two points of START and END, timing a person's walking from START to END can determine the walking speed.

<img src="https://github.com/PanithanS/Webcam-Pose-Estimation-using-YOLOv8/assets/83627892/fd0bff1e-03b9-478d-bc0d-c6a0f18ee0d9" width="900">

## The multidisciplinary impact of measuring walking speed
We certainly focus on measuring walking speed for rehabilitation, which serves as a foundational step with broader implications across various domains. Here are the perspectives that might be addressed in the future:

**Rehabilitation Innovation:** By initially focusing on measuring walking speed for rehabilitation purposes, the project can pioneer innovative methods and technologies tailored to the specific needs of patients recovering from injuries, surgeries, or medical conditions affecting mobility.

**Interdisciplinary Collaboration:** As the project progresses, it may involve collaboration with experts from diverse fields such as healthcare, engineering, data science, and biomechanics. These interdisciplinary collaborations can lead to the exchange of ideas, methodologies, and technologies, fostering innovation and cross-pollination of knowledge.

**Technology Transfer:** The methodologies and technologies developed for measuring walking speed in rehabilitation settings can be adapted and transferred to other domains such as sports science, gerontology, urban planning, and assistive technology. This technology transfer process can accelerate progress in these fields by leveraging existing expertise and infrastructure.

**Data-driven Insights:** Gathering data on walking speed in rehabilitation settings can provide valuable insights into patient progress, treatment effectiveness, and rehabilitation outcomes. Analyzing this data using machine learning, statistical modeling, or biomechanical simulations can reveal patterns, correlations, and predictive factors applicable across various domains.

Overall, while initially focusing on measuring walking speed for rehabilitation purposes, the project has the potential to lay a solid foundation for advancements and applications in diverse domains, ultimately contributing to improved health, mobility, and well-being across populations.

## Demonstration 01: Run "main.py" with a webcam connected
**Vid. 1** The demonstration of a person walking from the "START" to the "END" point with a time-stamp. If one knows the exact distance between two points, this can indicate the walking speed.
- The clock, mouse position, starting time, and ending time were shown, respectively, at the top-left corner of the video from top to bottom.
- We can draw or redraw the START BOX and END BOX using the mouse, enabling users to easily reposition the camera with a flexible design for any walking path.
- Once the boxes are defined, their positions will be saved. The next time the program is run, there is no need to redraw them (assuming the camera remains unmoved).
- The timing clock will start only when the person is in the START box, and the timing clock will not stop until the person is in the END box.

https://github.com/PanithanS/Webcam-Pose-Estimation-using-YOLOv8/assets/83627892/a074d7ca-1160-4373-92fd-e60b03d0ef5a

## Requirement
1. PyTorch(CPU)
see more on the PyTorch site: https://pytorch.org/get-started/locally/

```Python
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```
2. Ultralytics for the YOLOv8 pose estimation

```Python
pip install ultralytics
```
3. OpenCV for Python (already installed in Anaconda), but if not, please try:
```Python
conda install conda-forge::opencv
```
## Inspiration and Acknowledgments
- The idea cannot be implemented without the pre-trained model of YOLOv8 from: https://github.com/ultralytics.
