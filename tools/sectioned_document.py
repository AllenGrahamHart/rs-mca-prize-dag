#!/usr/bin/env python3
"""Compile compatibility documents from ordered semantic source shards."""

from __future__ import annotations

import json
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = "sectioned-document-v1"


class SectionedDocumentError(RuntimeError):
    """Raised for an incomplete or unsafe sectioned-document manifest."""


def load_manifest(path: Path, root: Path = ROOT) -> dict:
    payload = json.loads(path.read_text())
    if payload.get("schema") != SCHEMA:
        raise SectionedDocumentError(f"{path}: schema")
    output = payload.get("output")
    sections = payload.get("sections")
    if not isinstance(output, str) or not isinstance(sections, list) or not sections:
        raise SectionedDocumentError(f"{path}: output/sections")
    if len(sections) != len(set(sections)):
        raise SectionedDocumentError(f"{path}: duplicate section")
    output_path = (root / output).resolve()
    try:
        output_path.relative_to(root.resolve())
    except ValueError as error:
        raise SectionedDocumentError(f"{path}: output escapes root") from error
    section_paths = []
    for value in sections:
        if not isinstance(value, str):
            raise SectionedDocumentError(f"{path}: non-string section")
        section = (root / value).resolve()
        try:
            section.relative_to(root.resolve())
        except ValueError as error:
            raise SectionedDocumentError(
                f"{path}: section escapes root: {value}"
            ) from error
        if not section.is_file():
            raise SectionedDocumentError(f"{path}: missing section {value}")
        section_paths.append(section)
    return {
        "output": output_path,
        "sections": section_paths,
        "payload": payload,
    }


def compiled_text(path: Path, root: Path = ROOT) -> str:
    document = load_manifest(path, root)
    return "".join(section.read_text() for section in document["sections"])


def write_document(path: Path, root: Path = ROOT) -> Path:
    document = load_manifest(path, root)
    output = document["output"]
    temporary = output.with_suffix(output.suffix + ".tmp")
    temporary.write_text(
        "".join(section.read_text() for section in document["sections"])
    )
    os.replace(temporary, output)
    return output
