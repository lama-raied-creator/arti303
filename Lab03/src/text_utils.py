"""Utilities for cleaning and formatting text."""


def clean_name(raw):
    """Clean a name by normalizing spaces and applying title case."""
    cleaned = " ".join(raw.split())
    return cleaned.title()
