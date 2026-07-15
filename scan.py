#!/usr/bin/env python3
"""grill-master ready scan: open + unclaimed (or stale-claimed >24h) + all blockers closed.

Usage: python3 scan.py [effort-dir]    (defaults to cwd)
"""
import datetime
import os
import re
import sys

d = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.getcwd()
today = datetime.date.today()


def fmatter(p):
    t = open(p).read().split("---")
    return t[1] if len(t) > 2 else ""


def field(fm, k):
    m = re.search(rf'^{k}:\s*"?([^"\n]*)"?\s*$', fm, re.M)
    return m.group(1).strip() if m else ""


def deps(fm):
    m = re.search(r"^blockers:\n((?:\s+-\s+.*\n)*)", fm, re.M)
    return re.findall(r"([\w-]+\.svx)", m.group(1)) if m else []


def live(assignee):
    m = re.search(r"(\d{4}-\d{2}-\d{2})", assignee)
    return bool(m) and (today - datetime.date.fromisoformat(m.group(1))).days < 1


STEP_TYPES = {"step", "question"}  # "question" = pre-2026-07-15 contract

files = {f: fmatter(os.path.join(d, f)) for f in os.listdir(d) if f.endswith(".svx")}
closed = {f for f, fm in files.items() if field(fm, "status") == "closed"}
ready = 0
for f, fm in sorted(files.items()):
    if field(fm, "type") not in STEP_TYPES or field(fm, "status") != "open":
        continue
    if live(field(fm, "assignee")):
        continue
    if all(b in closed for b in deps(fm)):
        print(f"READY: {f} — {field(fm, 'title')}")
        ready += 1
open_steps = sum(1 for fm in files.values() if field(fm, "type") in STEP_TYPES and field(fm, "status") == "open")
print(f"{ready} ready / {open_steps} open")
