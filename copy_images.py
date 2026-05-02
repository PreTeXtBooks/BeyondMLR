#!/usr/bin/env python3
"""
Copy and prepare images for the PreTeXt book build.

This script copies figures from the bookdown-generated output and static
data images into the pretext/assets/generated-assets/ directory that
PreTeXt uses when rendering the book.

The publication.ptx sets `external="../assets"`, so image source paths in
the .ptx files are resolved relative to pretext/assets/.  All generated
figures therefore live under pretext/assets/generated-assets/.

Naming conventions used in the .ptx source files:
  1. fig-{chunk}.png  – used by most chapters (strip -1 suffix, add fig- prefix)
  2. {chunk}.png      – used by ch_multilevel_intro (strip -1 suffix, no prefix)
  3. {chunk}-1.png    – used by ch_3level (keep the -1 suffix from bookdown)

The script produces all three variants for every bookdown figure so that
every chapter finds its images regardless of which convention it follows.

Special static images (diagrams produced with knitr::include_graphics) are
copied from data/ into generated-assets/ with their expected PTX names.

The Philippines map is also copied into pretext/assets/data/ because it is
referenced in ch_poisson_regression.ptx as source="data/map_of_philippines.jpg".
"""

import shutil
from pathlib import Path


def main():
    script_dir = Path(__file__).parent

    # Source directories
    bookdown_figs = script_dir / "docs" / "bookdown-BeyondMLR_files" / "figure-html"
    data_dir = script_dir / "data"

    # Destination directories
    # pretext/assets/ is the external-assets root declared in publication.ptx
    generated_assets = script_dir / "pretext" / "assets" / "generated-assets"
    pretext_data = script_dir / "pretext" / "assets" / "data"

    print("Preparing images for PreTeXt book...")

    # Create destination directories
    generated_assets.mkdir(parents=True, exist_ok=True)
    pretext_data.mkdir(parents=True, exist_ok=True)

    images_copied = 0

    # ------------------------------------------------------------------
    # 1. Bookdown R-generated figures
    #    Bookdown names them {chunk}-1.png.
    #    We copy each figure under all three naming conventions so that
    #    every chapter can find its figures.
    # ------------------------------------------------------------------
    if bookdown_figs.is_dir():
        for src in sorted(bookdown_figs.glob("*-1.png")):
            # e.g. "OLSassumptions-1.png"
            bookdown_name = src.name          # OLSassumptions-1.png
            chunk = src.stem[:-2]             # strip the trailing "-1"
            #                                   → OLSassumptions

            # Variant 3: keep bookdown name  (ch_3level style)
            dst3 = generated_assets / bookdown_name
            shutil.copy2(src, dst3)

            # Variant 1: add fig- prefix     (most chapters)
            dst1 = generated_assets / f"fig-{chunk}.png"
            shutil.copy2(src, dst1)

            # Variant 2: plain chunk name    (ch_multilevel_intro style)
            dst2 = generated_assets / f"{chunk}.png"
            shutil.copy2(src, dst2)

            images_copied += 1

        print(f"  Copied {images_copied} bookdown figures (×3 naming variants)")
    else:
        print(f"  Warning: bookdown figures directory not found: {bookdown_figs}")

    # ------------------------------------------------------------------
    # 2. Special static diagram images
    #    These are referenced in the .ptx files with specific target names.
    # ------------------------------------------------------------------
    static_maps = [
        # (source_file, target_name_in_generated_assets)
        # Note: source filenames preserve the original capitalisation as
        # committed to the repository (e.g. .PNG vs .png).
        ("StudyDesignDiagram.PNG",          "seedstudy-1.png"),
        ("DamsTreesStructure.png",          "fig-DamsTreesStructure.png"),
        ("ParametricBootstrapDiagram9.png", "fig-parabootdiagram.png"),
    ]
    for src_name, dst_name in static_maps:
        src = data_dir / src_name
        if src.exists():
            shutil.copy2(src, generated_assets / dst_name)
            print(f"  Static image: {src_name} -> generated-assets/{dst_name}")
        else:
            print(f"  Warning: static image not found: {src}")

    # ------------------------------------------------------------------
    # 3. Data-directory images referenced directly as data/...
    #    e.g. ch_poisson_regression.ptx: source="data/map_of_philippines.jpg"
    # ------------------------------------------------------------------
    data_images = ["map_of_philippines.jpg"]
    for img_name in data_images:
        src = data_dir / img_name
        if src.exists():
            shutil.copy2(src, pretext_data / img_name)
            print(f"  Data image: {img_name} -> assets/data/{img_name}")
        else:
            print(f"  Warning: data image not found: {src}")

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    total = len(list(generated_assets.iterdir()))
    print(f"\nComplete! {total} files in pretext/assets/generated-assets/")

    return 0


if __name__ == "__main__":
    exit(main())
