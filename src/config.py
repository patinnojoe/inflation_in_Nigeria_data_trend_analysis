from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUT_DIR = ROOT_DIR / "output"

# COlLORS
# Custom Hex Colors
NG_GREEN = "#006633"       # Primary deep flag green
NG_GOLD = "#E5A93C"        # Accent savannah gold
NG_DARK = "#2B2B2B"        # Crisp charcoal for text
NG_LIGHT_BG = "#F9FBF9"    # Subtle, off-white green tint for backgrounds