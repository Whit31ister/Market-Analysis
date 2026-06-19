# Market-Analysis

Market-Analysis is a Python computer vision pipeline for extracting structured geometry from chart screenshots. The project is designed to ingest raw chart images, detect visual regions such as candles, lines, and other plotted elements, and export the detected coordinates as JSON or CSV data for later analysis or machine learning dataset preparation.

## Project Goal

Build a reusable chart image parser that can:

- Load raw chart screenshots in PNG, JPG, or JPEG format.
- Preprocess chart images with grayscale conversion, blur, thresholding, and contour detection.
- Extract candidate bounding boxes for chart elements.
- Export extracted image metadata and geometric coordinates into structured files.
- Provide a clean foundation for adding support/resistance detection, trend line detection, and candlestick-specific labeling.

## Directory Structure

```text
Market-Analysis/
├── raw_charts/
│   └── .gitkeep
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── extractor.py
│   └── labeler.py
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
```

## Components

| Path | Purpose |
| --- | --- |
| `raw_charts/` | Drop raw chart screenshots here. |
| `src/preprocessing.py` | Loads images, creates threshold masks, and finds candidate visual regions. |
| `src/extractor.py` | Runs extraction for a single chart image and returns structured metadata. |
| `src/labeler.py` | Writes extracted records to JSON or flattened CSV. |
| `main.py` | Command-line pipeline orchestrator. |
| `requirements.txt` | Core Python dependencies. |

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Place chart screenshots inside `raw_charts/`.

Run the pipeline with default settings:

```bash
python main.py
```

This writes JSON output to:

```text
outputs/chart_features.json
```

Export CSV instead:

```bash
python main.py --format csv --output outputs/chart_features.csv
```

Use a custom input directory:

```bash
python main.py --input-dir path/to/charts --output outputs/features.json
```

## Output Format

JSON output contains one record per image:

```json
[
  {
    "image": "raw_charts/example.png",
    "width": 1280,
    "height": 720,
    "regions": [
      {
        "x": 100,
        "y": 240,
        "width": 18,
        "height": 64,
        "area": 1152
      }
    ]
  }
]
```

CSV output flattens each detected region into a row with image metadata and bounding box coordinates.

## Current Status

This is an early scaffold. The current implementation detects general candidate regions from chart images using OpenCV contours. It does not yet classify detected regions as candlesticks, support/resistance lines, trend lines, or indicators.

## Planned Improvements

- Add chart area detection to ignore browser UI, axes, and legends.
- Add color masking for green/red candlestick extraction.
- Add line detection for support, resistance, and trend lines.
- Add configurable filters for contour size and aspect ratio.
- Add test images and validation fixtures.
- Add labeled dataset export formats for ML training workflows.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
