"""Format extracted chart vectors into ML-ready records."""

import csv
import json
from pathlib import Path
from typing import Iterable


def write_json(records: Iterable[dict], output_path: Path) -> None:
    """Write extracted chart records to JSON."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(list(records), handle, indent=2)


def write_csv(records: Iterable[dict], output_path: Path) -> None:
    """Write flattened candidate regions to CSV."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    rows: list[dict] = []

    for record in records:
        for region in record["regions"]:
            rows.append(
                {
                    "image": record["image"],
                    "image_width": record["width"],
                    "image_height": record["height"],
                    **region,
                }
            )

    fieldnames = ["image", "image_width", "image_height", "x", "y", "width", "height", "area"]
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

