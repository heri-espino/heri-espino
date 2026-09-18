from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

OUTPUT = Path("assets/about.svg")

# Replace these with the paths printed by the previous script.
FONT_DISPLAY = r"C:\path\to\NeueHaasGroteskDisplayPro.ttf"
FONT_TEXT = r"C:\path\to\NeueHaasGroteskTextPro.ttf"

# Force Matplotlib to convert text into SVG paths.
plt.rcParams["svg.fonttype"] = "path"


# ---------------------------------------------------------
# Fonts
# ---------------------------------------------------------

display_font = FontProperties(
    fname=FONT_DISPLAY,
    size=28,
)

text_font = FontProperties(
    fname=FONT_TEXT,
    size=13,
)


# ---------------------------------------------------------
# Canvas
# ---------------------------------------------------------

fig = plt.figure(
    figsize=(12, 2.0),
    dpi=100,
)

fig.patch.set_alpha(0)

ax = fig.add_axes([0, 0, 1, 1])

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")


# ---------------------------------------------------------
# Typography
# ---------------------------------------------------------

ax.text(
    0.5,
    0.65,
    "HERIBERTO ESPINO",
    fontproperties=display_font,
    color="#5157CE",
    horizontalalignment="center",
    verticalalignment="center",
)

ax.text(
    0.5,
    0.32,
    "Exploring probability, geometry, and machine learning through mathematics and data.",
    fontproperties=text_font,
    color="#8A8A98",
    horizontalalignment="center",
    verticalalignment="center",
)


# ---------------------------------------------------------
# Export
# ---------------------------------------------------------

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

fig.savefig(
    OUTPUT,
    format="svg",
    transparent=True,
    bbox_inches="tight",
    pad_inches=0.03,
)

plt.close(fig)

print(f"Saved to {OUTPUT}")