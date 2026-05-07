#!/usr/bin/env python3
"""Slug helpers for youtube_metadata_collector."""

from __future__ import annotations

import re
import unicodedata


STOPWORD_PREFIXES = {
    "the",
    "a",
    "an",
    "why",
    "how",
    "what",
    "this",
    "that",
    "biggest",
    "best",
    "amazing",
    "incredible",
    "beautiful",
}


def slugify(text: str, max_words: int = 9) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    ascii_text = ascii_text.lower().replace("&", " and ")
    ascii_text = re.sub(r"['`]", "", ascii_text)
    words = re.findall(r"[a-z0-9]+", ascii_text)
    if max_words > 0:
        words = words[:max_words]
    return "-".join(words)


def choose_slug_base(title: str) -> str:
    """Choose a concise title phrase for a note slug."""
    clean = re.sub(r"\s+", " ", title).strip()
    if not clean:
        return ""

    if ":" in clean:
        suffix = clean.rsplit(":", 1)[1].strip()
        if 1 <= len(suffix.split()) <= 8:
            return suffix

    theorem_match = re.search(r"([A-Z][A-Za-z'’-]+(?:\s+[A-Z][A-Za-z'’-]+)*\s+Theorem)\b", clean)
    if theorem_match:
        return theorem_match.group(1)

    words = clean.split()
    while len(words) > 2 and slugify(words[0], max_words=1) in STOPWORD_PREFIXES:
        words.pop(0)
    return " ".join(words)

