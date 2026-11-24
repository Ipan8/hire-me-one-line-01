from pathlib import Path

LINE = "I don't take sick days, I don't need onboarding, and I already read your entire codebase. The interview is over."

assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"

Path("/output").mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text(LINE, encoding="utf-8")
