#!/usr/bin/env python3
"""Check a Chinese translation for mechanical problems.

Usage:
    python3 check_zh.py TARGET.md [--source SOURCE.md]

Reports:
  error   full-width punctuation inside inline code or fenced code blocks
  error   numbers that appear in the source but not the target, or vice versa
          (only when --source is given; counts include duplicates)
  warn    half-width , . ; : ! ? ( ) between CJK characters in prose
  warn    missing space between CJK and ASCII letters or digits in prose
  warn    more than one full-width colon in a single sentence of prose

The number comparison covers Arabic numerals only. Spelled-out numbers in the
source (one, twice, a dozen) are not detected and must be checked by hand.

Exit status is 1 when any error was found, otherwise 0.
"""

import argparse
import re
import sys
from collections import Counter

CJK = r"㐀-䶿一-鿿"
FULLWIDTH = "，。；：？！（）“”‘’《》、－／～"
INLINE_CODE = re.compile(r"`[^`\n]*`")
NUMBER = re.compile(r"\d+(?:\.\d+)?%?")
HALFWIDTH_BETWEEN_CJK = re.compile(rf"(?<=[{CJK}])[,.;:!?()](?=[{CJK}])")
CJK_THEN_ASCII = re.compile(rf"[{CJK}][A-Za-z0-9]")
ASCII_THEN_CJK = re.compile(rf"[A-Za-z0-9][{CJK}]")


def split_code(line):
    """Return (prose_only, code_segments) for one non-fenced line."""
    segments = INLINE_CODE.findall(line)
    prose = INLINE_CODE.sub(" ", line)
    return prose, segments


def check(path):
    errors, warnings = [], []
    in_fence = False
    with open(path, encoding="utf-8") as f:
        for n, raw in enumerate(f, 1):
            line = raw.rstrip("\n")
            if line.strip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                bad = [c for c in line if c in FULLWIDTH]
                if bad:
                    errors.append(f"{path}:{n}: full-width punctuation in code block: {''.join(bad)}")
                continue
            prose, code_segments = split_code(line)
            for seg in code_segments:
                bad = [c for c in seg if c in FULLWIDTH]
                if bad:
                    errors.append(f"{path}:{n}: full-width punctuation in inline code {seg}: {''.join(bad)}")
            for m in HALFWIDTH_BETWEEN_CJK.finditer(prose):
                warnings.append(f"{path}:{n}: half-width '{m.group()}' between Chinese characters")
            if CJK_THEN_ASCII.search(prose) or ASCII_THEN_CJK.search(prose):
                warnings.append(f"{path}:{n}: missing space between Chinese and ASCII letters/digits")
            # A short leading label such as "错例：" or "处理：" is not a colon in the sentence.
            body = re.sub(r"^\s*(?:[-*]\s*)?[^：]{1,8}：", "", prose, count=1)
            for sentence in re.split(r"[。！？]", body):
                if sentence.count("：") > 1:
                    warnings.append(f"{path}:{n}: more than one full-width colon in one sentence")
                    break
    return errors, warnings


def numbers_in(path):
    with open(path, encoding="utf-8") as f:
        return Counter(NUMBER.findall(f.read()))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target")
    ap.add_argument("--source", help="English source file; numbers are compared against it")
    args = ap.parse_args()

    errors, warnings = check(args.target)

    if args.source:
        src, tgt = numbers_in(args.source), numbers_in(args.target)
        for num in sorted(set(src) | set(tgt)):
            if src[num] != tgt[num]:
                errors.append(
                    f"number {num!r}: {src[num]} time(s) in source, {tgt[num]} time(s) in target"
                )

    for w in warnings:
        print("warn ", w)
    for e in errors:
        print("error", e)
    print(f"{len(errors)} error(s), {len(warnings)} warning(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
