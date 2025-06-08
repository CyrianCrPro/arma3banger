#!/usr/bin/env python3
import os
import argparse
from pathlib import Path

def rename_path(path: Path, new_name: str) -> Path:
    """Rename path to new_name in the same parent directory. Returns the new Path."""
    target = path.parent / new_name
    if target.exists():
        print(f"⚠️ Skipping rename because '{target}' already exists.")
        return path
    path.rename(target)
    return target

def process_mods_folder(base_dir: Path):
    if not base_dir.is_dir():
        raise NotADirectoryError(f"Base path '{base_dir}' is not a directory.")

    # Step 1: Clean up top-level entries in mods/
    for entry in list(base_dir.iterdir()):
        clean_name = entry.name.lower().replace('@', '')
        if clean_name != entry.name:
            print(f"Renaming top-level '{entry.name}' → '{clean_name}'")
            entry = rename_path(entry, clean_name)

        # Only directories can contain an addons/ subdir
        if entry.is_dir():
            # Step 2: Find any addons folder (case-insensitive) and rename it
            for sub in list(entry.iterdir()):
                if sub.is_dir() and sub.name.lower() == 'addons':
                    if sub.name != 'addons':
                        print(f"Renaming '{sub.name}' → 'addons'")
                        sub = rename_path(sub, 'addons')

                    # Step 3: Inside addons/, lowercase all file names
                    for root, _, files in os.walk(sub):
                        root_path = Path(root)
                        for fname in files:
                            if fname != fname.lower():
                                old_file = root_path / fname
                                new_file = root_path / fname.lower()
                                if new_file.exists():
                                    print(f"⚠️ Skipping '{old_file}' – target '{new_file}' exists.")
                                    continue
                                print(f"Renaming file '{old_file.name}' → '{new_file.name}'")
                                old_file.rename(new_file)

def main():
    parser = argparse.ArgumentParser(
        description="Normalize your 'mods/' directory: "
                    "strip '@' and lowercase top-level names, "
                    "ensure 'addons' folders are lowercase, "
                    "and lowercase all files inside them."
    )
    parser.add_argument(
        'mods_path',
        nargs='?',
        default='mods',
        help="Path to your 'mods' directory (default: './mods')"
    )
    args = parser.parse_args()
    base = Path(args.mods_path)
    try:
        process_mods_folder(base)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()