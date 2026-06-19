"""Feature extraction for chart images."""

from pathlib import Path

from .preprocessing import find_candidate_regions, load_chart_image, preprocess_image


def extract_chart_features(image_path: Path) -> dict:
    """Extract geometric candidates from a single chart screenshot."""
    image = load_chart_image(image_path)
    mask = preprocess_image(image)
    regions = find_candidate_regions(mask)

    return {
        "image": str(image_path),
        "width": int(image.shape[1]),
        "height": int(image.shape[0]),
        "regions": regions,
    }

