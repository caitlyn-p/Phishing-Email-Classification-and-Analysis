import nbformat
from pathlib import Path

folder = Path("/Users/USER/Documents/School/2025-2026/Spring 2026/I 320D Text Mining and NLP Essentials/Group Project/Phishing-Email-Classification-and-Analysis")

for path in folder.glob("*.ipynb"):
	nb = nbformat.read(path, as_version=nbformat.NO_CONVERT)
	
	changed = False
	if "widgets" in nb.metadata:
		widgets_meta = dict(nb.metadata["widgets"])
		if "state" not in widgets_meta:
			widgets_meta["state"] = {}
			nb.metadata["widgets"] = widgets_meta
			changed = True

	if changed:
		nbformat.write(nb, path)
		print(f"Fixed: {path}")
	else:
		print(f"No change: {path}")
