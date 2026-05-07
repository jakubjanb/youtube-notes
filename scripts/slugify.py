#!/usr/bin/env python3
"""Convert note titles into clean filesystem slugs."""

from __future__ import annotations

import argparse
import re
import unicodedata


def slugify(text: str) -> str:
    """Return a lowercase kebab-case ASCII slug."""
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    ascii_text = ascii_text.lower().replace("&", " and ")
    ascii_text = re.sub(r"['`]", "", ascii_text)
    ascii_text = re.sub(r"[^a-z0-9]+", "-", ascii_text)
    return ascii_text.strip("-")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("title", help="Title to convert into a slug.")
    args = parser.parse_args()

    slug = slugify(args.title)
    if not slug:
        parser.error("title did not contain any slug-safe characters")
    print(slug)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

