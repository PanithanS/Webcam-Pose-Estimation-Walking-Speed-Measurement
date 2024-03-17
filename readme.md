# The real-time human pose estimation, powered by YOLOv8 with the webcam 
This project is dedicated to applying computer vision to deliver a dependable and efficient solution for human pose recognition specifically focusing on measuring the walking speed of cardiac surgery patients in the rehabilitation dorm.
Aim: Low-budget, user-friendly, and easy to distribute.

## Why do we measure walking speed and pose estimation
We certainly focus on measuring walking speed for rehabilitation, which serves as a foundational step with broader implications across various domains. Here's how:

**Rehabilitation Innovation:** By initially focusing on measuring walking speed for rehabilitation purposes, the project can pioneer innovative methods and technologies tailored to the specific needs of patients recovering from injuries, surgeries, or medical conditions affecting mobility. This can include developing specialized equipment, software algorithms, or wearable devices optimized for rehabilitation settings.

**Interdisciplinary Collaboration:** As the project progresses, it may involve collaboration with experts from diverse fields such as healthcare, engineering, data science, and biomechanics. These interdisciplinary collaborations can lead to the exchange of ideas, methodologies, and technologies, fostering innovation and cross-pollination of knowledge.

**Technology Transfer:** The methodologies and technologies developed for measuring walking speed in rehabilitation settings can be adapted and transferred to other domains such as sports science, gerontology, urban planning, and assistive technology. This technology transfer process can accelerate progress in these fields by leveraging existing expertise and infrastructure.

**Data-driven Insights:** Gathering data on walking speed in rehabilitation settings can provide valuable insights into patient progress, treatment effectiveness, and rehabilitation outcomes. Analyzing this data using machine learning, statistical modeling, or biomechanical simulations can reveal patterns, correlations, and predictive factors applicable across various domains.

**Impact Assessment:** Demonstrating the effectiveness of measuring walking speed in rehabilitation can have ripple effects in terms of healthcare policy, resource allocation, and patient care standards. By quantifying the benefits in terms of improved patient outcomes, reduced healthcare costs, and enhanced quality of life, the project can advocate for broader adoption and integration of similar methodologies in healthcare systems worldwide.

Overall, while initially focusing on measuring walking speed for rehabilitation purposes, the project has the potential to lay a solid foundation for advancements and applications in diverse domains, ultimately contributing to improved health, mobility, and well-being across populations.

## Overview
**Fig.1** illustrates the concept of detecting the walking speed of an individual moving from point A to point B. With the known distance between these two points, the methodology involves timing the passage of the person from A to B to determine their walking speed.
<img src="https://github.com/PanithanS/Webcam-Pose-Estimation-using-YOLOv8/assets/83627892/45885927-a822-495b-9735-9077ec6843cf" width="780">


## Demonstration 01: Running 'main' with a webcam connected
**Vid. 1** Below is the demonstration for timing the passage of the person from the "START" to the "END" point. 
<video src="https://github.com/PanithanS/Webcam-Pose-Estimation-using-YOLOv8/assets/83627892/12de9def-dbf8-480f-886a-ebe74dbc76d0">

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
