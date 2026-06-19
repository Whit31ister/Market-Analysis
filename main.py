"""Pipeline orchestrator for chart vision extraction."""

from argparse import ArgumentParser
from pathlib import Path

from src.extractor import extract_chart_features
from src.labeler import write_csv, write_json


SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png"}


def iter_chart_images(input_dir: Path) -> list[Path]:
    """Find supported chart screenshots in a directory."""
    return sorted(
        path
        for path in input_dir.iterdir()
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
    )


def run_pipeline(input_dir: Path, output_path: Path, output_format: str) -> None:
    """Extract chart features and write them as JSON or CSV."""
    records = [extract_chart_features(path) for path in iter_chart_images(input_dir)]

    if output_format == "json":
        write_json(records, output_path)
    else:
        write_csv(records, output_path)


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(description="Extract chart geometry from raw chart screenshots.")
    parser.add_argument("--input-dir", type=Path, default=Path("raw_charts"))
    parser.add_argument("--output", type=Path, default=Path("outputs/chart_features.json"))
    parser.add_argument("--format", choices=("json", "csv"), default="json")
    return parser


if __name__ == "__main__":
    args = build_parser().parse_args()
    run_pipeline(args.input_dir, args.output, args.format)

