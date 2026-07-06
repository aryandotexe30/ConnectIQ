from pathlib import Path


class Settings:

    PROJECT_ROOT = Path(__file__).resolve().parent.parent

    DATA_FOLDER = PROJECT_ROOT / "data"

    INPUT_FOLDER = DATA_FOLDER / "input"

    OUTPUT_FOLDER = DATA_FOLDER / "output"

    INPUT_FOLDER.mkdir(parents=True, exist_ok=True)

    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)