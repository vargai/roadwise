import csv
import importlib.util
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GUIDE_SCRIPT = ROOT / "output" / "pdf" / "create_hungarian_printable_guide.py"


def load_guide_data():
    spec = importlib.util.spec_from_file_location("hu_guide", GUIDE_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def update_csv(path, guide):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = list(reader.fieldnames or [])

    if not rows or "Name" not in fieldnames:
        return False

    for col in ["Description_HU", "Tip_HU"]:
        if col not in fieldnames:
            fieldnames.append(col)

    changed = False
    for row in rows:
        name = row.get("Name", "")
        description, tip = guide.describe(name)
        if row.get("Description_HU") != description:
            row["Description_HU"] = description
            changed = True
        if row.get("Tip_HU") != tip:
            row["Tip_HU"] = tip
            changed = True

    if changed:
        temp_path = path.with_suffix(path.suffix + ".tmp")
        with temp_path.open("w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        os.replace(temp_path, path)
    return changed


def main():
    guide = load_guide_data()
    targets = sorted((ROOT / "version2").glob("*.csv")) + sorted(ROOT.glob("*.csv"))
    changed = []
    failed = []
    for path in targets:
        try:
            if update_csv(path, guide):
                changed.append(path)
        except PermissionError as exc:
            failed.append((path, exc))

    print("Updated files:")
    for path in changed:
        print(path.relative_to(ROOT))
    if failed:
        print("Failed files:")
        for path, exc in failed:
            print(path.relative_to(ROOT), exc)


if __name__ == "__main__":
    main()
