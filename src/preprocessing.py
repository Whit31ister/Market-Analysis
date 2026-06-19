"""Image preprocessing helpers for chart screenshots."""

from pathlib import Path

import cv2
import numpy as np


def load_chart_image(image_path: Path) -> np.ndarray:
    """Load a chart image from disk as a BGR OpenCV array."""
    image = cv2.imread(str(image_path))
    if image is None:
        raise FileNotFoundError(f"Could not read image: {image_path}")
    return image


def preprocess_image(image: np.ndarray) -> np.ndarray:
    """Convert a chart image to a thresholded grayscale mask."""
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(grayscale, (5, 5), 0)
    return cv2.adaptiveThreshold(
        blurred,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        21,
        7,
    )


def find_candidate_regions(mask: np.ndarray, min_area: int = 50) -> list[dict[str, int]]:
    """Return bounding boxes for visual regions large enough to inspect."""
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    regions: list[dict[str, int]] = []

    for contour in contours:
        x, y, width, height = cv2.boundingRect(contour)
        area = width * height
        if area >= min_area:
            regions.append({"x": x, "y": y, "width": width, "height": height, "area": area})

    return sorted(regions, key=lambda region: (region["y"], region["x"]))

