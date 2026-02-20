# rice-leaf-segmentation
Image segmentation of rice plants using computer vision techniques to extract plant features from field images.

## Description

This project implements an image segmentation pipeline to isolate rice plants from background elements using color-based filtering and morphological image processing. The method focuses on detecting green vegetation regions by transforming the image into the HLS (Hue, Lightness, Saturation) color space, which allows more stable separation of plant color information from illumination effects commonly found in field-acquired images.

## Method Overview

1. **Image Input**
   The program reads all `.jpg` images from a specified directory and resizes them to reduce computational load while maintaining visual features.

2. **Color Space Conversion**
   The images are converted from the default BGR format to the HLS color space to better separate color information from lighting conditions. This conversion helps make the segmentation
   process more stable when images are captured under varying illumination in outdoor environments.

4. **Green Color Thresholding**
   A selected range of color values is applied to identify regions corresponding to rice plants. This step filters out most background elements and produces a binary mask that highlights
   the vegetation areas to be processed further.


6. **Morphological Refinement**
   To improve segmentation quality, several morphological operations are applied:

   * **Dilation**: Connects fragmented leaf regions.
   * **Closing**: Fills gaps and holes inside detected plant areas.
   * **Erosion**: Removes small noise and sharp artifacts.

   These operations ensure that the segmented plant appears as a continuous structure rather than scattered pixels.

7. **Mask Application**
   The refined binary mask is applied to the original image using a bitwise operation, producing the final segmented output where:

   * Rice plants are preserved.
   * Background (soil, shadows, debris) is suppressed.

8. **Output Generation**
   The processed images are automatically saved to an output directory with a new filename prefix, enabling batch processing of large datasets.

## Purpose

The segmentation results can be used as a preprocessing step for:

* Plant growth analysis
* Feature extraction for machine learning
* Vegetation coverage measurement
* Precision agriculture monitoring

## Key Characteristics

* Designed for real-world agricultural imagery with uneven lighting.
* Works on images captured from different cameras or smartphones.
* Fully automated batch processing.
* Uses classical computer vision techniques (no training required).
* Lightweight and suitable for rapid analysis workflows.

## Technologies Used

* Python
* OpenCV (image processing and morphology)
* NumPy (numerical operations)
* Matplotlib (image saving and visualization)

This project demonstrates a practical implementation of rule-based vegetation segmentation for agricultural image analysis.
