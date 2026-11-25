"""Fonctions utilitaires communes de traitement de texte."""
import unicodedata

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def normalize(text: str) -> str:
    """Majuscules, sans accents, uniquement les lettres A-Z."""
    decomposed = unicodedata.normalize("NFD", text.upper())
    return "".join(c for c in decomposed if c in ALPHABET)


def split_blocks(text: str, size: int, filler: str = "X") -> list[str]:
    """Découpe en blocs de `size` lettres (complète le dernier avec `filler`)."""
    if size < 1:
        raise ValueError("La taille des blocs doit être >= 1")
    padded = text + filler * (-len(text) % size)
    return [padded[i : i + size] for i in range(0, len(padded), size)]
