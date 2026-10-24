"""Download PrimeKG (kg.csv) from Harvard Dataverse into data/."""
from pathlib import Path
import shutil
import urllib.request

DATA_URL = "https://dataverse.harvard.edu/api/access/datafile/6180620"
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "kg.csv"


def main() -> None:
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    if DATA_PATH.exists():
        print(f"Already downloaded: {DATA_PATH}")
        return
    print("Downloading PrimeKG (about 1 GB)...")
    # Dataverse returns 403 to Python's default user agent, so identify as a browser.
    request = urllib.request.Request(DATA_URL, headers={"User-Agent": "Mozilla/5.0"})
    partial = DATA_PATH.with_suffix(".part")
    with urllib.request.urlopen(request) as response, open(partial, "wb") as f:
        shutil.copyfileobj(response, f)
    partial.rename(DATA_PATH)
    print(f"Saved to {DATA_PATH} ({DATA_PATH.stat().st_size / 1e9:.2f} GB)")


if __name__ == "__main__":
    main()
