#!/usr/bin/env python3
"""Scan text-based Power BI artefacts for suspected secrets without printing values."""
from __future__ import annotations
import argparse
import pathlib
import re
import sys

PATTERNS = [
    ("client secret", re.compile(r"(?i)(client[_ -]?secret|clientsecret)\s*[:=]\s*[\"']?([^\s\"';,]{8,})")),
    ("api key", re.compile(r"(?i)(api[_ -]?key|apikey|subscription[_ -]?key)\s*[:=]\s*[\"']?([^\s\"';,]{8,})")),
    ("password", re.compile(r"(?i)(password|pwd)\s*[:=]\s*[\"']?([^\s\"';,]{6,})")),
    ("bearer token", re.compile(r"(?i)bearer\s+([A-Za-z0-9._~+\-/=]{16,})")),
    ("access token", re.compile(r"(?i)(access[_ -]?token|refresh[_ -]?token)\s*[:=]\s*[\"']?([^\s\"';,]{12,})")),
    ("signed URL", re.compile(r"(?i)(sig|signature|sharedaccesssignature)=([^&\s]{8,})")),
]
EXTENSIONS = {".tmdl", ".json", ".m", ".pq", ".txt", ".xml", ".yaml", ".yml", ".ps1", ".py", ".csv"}

def redacted(value: str) -> str:
    if len(value) <= 4:
        return "[REDACTED]"
    return value[:2] + "…" + value[-2:]

def scan(root: pathlib.Path) -> list[tuple[str, int, str, str]]:
    findings = []
    files = [root] if root.is_file() else [p for p in root.rglob("*") if p.is_file()]
    for path in files:
        if path.suffix.lower() not in EXTENSIONS:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for line_no, line in enumerate(text.splitlines(), 1):
            for label, pattern in PATTERNS:
                for match in pattern.finditer(line):
                    value = match.group(match.lastindex or 1)
                    findings.append((str(path), line_no, label, redacted(value)))
    return findings

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    findings = scan(pathlib.Path(args.path))
    if findings:
        print("STOP: suspected secrets detected. Do not submit these files to an AI system.")
        for path, line, label, preview in findings:
            print(f"{path}:{line}: {label}: {preview}")
        return 2
    print("No suspected secrets detected by pattern scan. This is not a guarantee; complete manual review is still required.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
