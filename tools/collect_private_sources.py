#!/usr/bin/env python3
"""Collect selected source files into a NEW PRIVATE ZIP; never flash or upload."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import zipfile

EXTENSIONS = {'.c', '.h', '.cpp', '.hpp', '.cmake', '.pio', '.py', '.ps1', '.md', '.patch', '.diff'}
NAMES = {'CMakeLists.txt', 'LICENSE', 'COPYING', 'NOTICE', '.gitmodules', '.gitignore'}
SKIP = {'.git', '.ssh', '.venv', 'venv', 'node_modules', '__pycache__', 'private', 'originals', 'evidence'}
SECRET = re.compile(rb'(?im)-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY|github_pat_[A-Za-z0-9_]{10,}|gh[pousr]_[A-Za-z0-9]{20,}|^\s*(?:password|api_key|access_token)\s*=\s*[\x22\x27][^\x22\x27\r\n]+[\x22\x27]')


def collect(source, output):
    source = Path(source).resolve(strict=True)
    output = Path(output).absolute()
    if not source.is_dir():
        raise ValueError('Source must be a directory.')
    # Reject every symlink in the destination path before creating anything.
    if any(p.is_symlink() for p in [output, *output.parents]):
        raise ValueError('Output path must not contain symlinks.')
    resolved_output = output.resolve()
    if resolved_output == source or source in resolved_output.parents:
        raise ValueError('Choose an output outside the source directory.')
    if output.exists():
        raise ValueError('Output already exists; choose a new filename.')
    manifest, excluded = [], []
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, 'x', zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(source.rglob('*')):
            relative = path.relative_to(source)
            if any(part.lower() in SKIP or part.lower().startswith('build') for part in relative.parts):
                continue
            if path.is_symlink() or any(p.is_symlink() for p in path.parents if p != source):
                continue
            if not path.is_file():
                continue
            if path.suffix.lower() not in EXTENSIONS and path.name not in NAMES:
                continue
            if path.stat().st_size > 4 * 1024 * 1024:
                excluded.append({'path':relative.as_posix(), 'reason':'over 4 MiB'})
                continue
            data = path.read_bytes()
            if SECRET.search(data):
                excluded.append({'path':relative.as_posix(), 'reason':'possible credential'})
                continue
            archive.writestr('sources/' + relative.as_posix(), data)
            manifest.append({'path':relative.as_posix(), 'bytes':len(data), 'sha256':hashlib.sha256(data).hexdigest()})
        archive.writestr('MANIFEST.json', json.dumps({'files':manifest, 'excluded':excluded}, indent=2))
        archive.writestr('PRIVATE-NOTICE.txt', 'PRIVATE REVIEW ONLY. May contain personal paths, comments and third-party code. Credential detection is incomplete. Review before sharing. No firmware, binary dumps or build outputs are selected. Original files were not edited.\n')
    return {'collected':len(manifest), 'excluded':len(excluded)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', help='Explicit project directory; not the whole user profile')
    parser.add_argument('output', help='NEW private ZIP outside the source directory')
    args = parser.parse_args()
    try:
        result = collect(args.source, args.output)
    except (OSError, ValueError, zipfile.BadZipFile) as error:
        parser.exit(1, 'Collection failed: ' + str(error) + '\n')
    print(json.dumps(result))
    print('Private review only. Nothing uploaded. Originals unchanged.')


if __name__ == '__main__':
    main()
