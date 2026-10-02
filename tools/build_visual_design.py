#!/usr/bin/env python3
"""Generate original, accessible ATLAS document artwork using only Python stdlib.

The artwork visualizes portfolio metadata and proposed field contracts. It never
creates observations, measurements, numerical results or readiness scores.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import math
import re
import textwrap
import xml.etree.ElementTree as ET
from pathlib import Path

NAVY = '#071d31'
MIDNIGHT = '#0d2a43'
TEAL = '#65d8c0'
COPPER = '#e9ac78'
INK = '#16324a'
MUTED = '#52687b'
PAPER = '#f7f8f5'
WHITE = '#ffffff'
RULE = '#dce5e7'
EXPECTED = {'A': 12, 'B': 28, 'C': 30, 'D': 7, 'E': 8, 'F': 2,
            'G': 8, 'H': 9, 'I': 13}
SESSION_NAMES = {
    'A': 'Math, Physics & Chemistry', 'B': 'Earth & Environmental Engineering',
    'C': 'Astronomy & Space Physics', 'D': 'Aeronautics', 'E': 'ASCEND',
    'F': 'Education & Public Outreach', 'G': 'Exploration Systems Engineering',
    'H': 'Planetary Science', 'I': 'Aerospace Technology',
}


def esc(value):
    return html.escape(str(value), quote=True)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def number(value):
    return f'{value:,.2f}'.rstrip('0').rstrip('.')


def text(x, y, value, size=18, fill=INK, weight=400, family='Arial, Helvetica, sans-serif',
         anchor='start', spacing=None):
    letter = f' letter-spacing="{spacing}"' if spacing is not None else ''
    return (f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" '
            f'font-weight="{weight}" font-family="{family}" text-anchor="{anchor}"{letter}>'
            f'{esc(value)}</text>')


def wrapped(value, width):
    return textwrap.wrap(str(value), width=width, break_long_words=True,
                         break_on_hyphens=False, replace_whitespace=True) or ['—']


def lines(x, y, values, size=18, gap=24, fill=INK, weight=400, family='Arial, Helvetica, sans-serif'):
    return ''.join(text(x, y + i * gap, v, size, fill, weight, family) for i, v in enumerate(values))


def rect(x, y, width, height, fill, radius=0, stroke=None, extra=''):
    stroke_attr = f' stroke="{stroke}"' if stroke else ''
    return (f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
            f'rx="{radius}" fill="{fill}"{stroke_attr}{extra}/>')


def line(x1, y1, x2, y2, stroke=RULE, width=1, extra=''):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{stroke}" stroke-width="{width}"{extra}/>')


def svg(width, height, title, description, body, defs=''):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description">'
            f'<title id="title">{esc(title)}</title><desc id="description">{esc(description)}</desc>'
            + ('<defs>' + defs + '</defs>' if defs else '') + body + '</svg>\n')


def orbital_motif(cx, cy, radius, color=TEAL, opacity=1, letters=False):
    out = [f'<g opacity="{opacity}">']
    for scale, angle in [(1, -28), (.76, 34), (.50, -28)]:
        out.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{radius * scale:.2f}" '
                   f'ry="{radius * scale * .58:.2f}" fill="none" stroke="{color}" '
                   f'stroke-width="1.4" transform="rotate({angle} {cx} {cy})"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{radius * .25:.2f}" fill="{MIDNIGHT}" '
               f'stroke="{COPPER}" stroke-width="2"/>')
    for i in range(9):
        a = math.radians(-100 + i * 40)
        px, py = cx + radius * math.cos(a), cy + radius * .68 * math.sin(a)
        out.append(f'<circle cx="{px:.2f}" cy="{py:.2f}" r="{17 if letters else 4}" '
                   f'fill="{NAVY if letters else COPPER}" stroke="{color}" stroke-width="1.2"/>')
        if letters:
            out.append(text(f'{px:.2f}', f'{py + 5:.2f}', chr(65+i), 14, TEAL, 700, anchor='middle'))
    out.append('</g>')
    return ''.join(out)


def totals(projects, annexes):
    return {'projects': len(projects), 'sessions': len({p['session'] for p in projects}),
            'fields': sum(len(a['data_dictionary']) for a in annexes),
            'requirements': sum(len(a['requirements']) for a in annexes),
            'planned_verification_cases': sum(len(a['verification_cases']) for a in annexes)}


def hero(projects, annexes):
    counts = totals(projects, annexes)
    w, h = 1600, 610
    defs = ('<linearGradient id="space" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="{NAVY}"/><stop offset="1" stop-color="#143c53"/>'
            '</linearGradient><pattern id="technical-grid" width="50" height="50" patternUnits="userSpaceOnUse">'
            '<path d="M 50 0 L 0 0 0 50" fill="none" stroke="#5a90a2" stroke-width=".6" opacity=".18"/>'
            '</pattern>')
    out = [rect(0, 0, w, h, 'url(#space)', 28), rect(0, 0, w, h, 'url(#technical-grid)', 28)]
    out += [line(64, 62, 108, 62, TEAL, 3),
            text(125, 68, 'ENGINEERING RESEARCH / DOCUMENT COLLECTION', 16, TEAL, 700, spacing=2),
            text(64, 218, 'ATLAS', 136, WHITE, 700, spacing=5),
            text(68, 272, 'Ideas with structure. Data with context.', 30, '#d4e6e9', 400),
            text(68, 325, '117 projects. Every original idea. One coherent engineering archive.', 20, '#b6cfd8'),
            text(68, 361, 'Models  /  field contracts  /  uncertainty  /  verification  /  cited resources', 17, '#a8c0cf')]
    out.append(orbital_motif(1300, 230, 206, TEAL, .83, True))
    out += [text(1300, 224, 'A–I', 24, COPPER, 700, anchor='middle'),
            text(1300, 248, 'RESEARCH', 12, '#c5d9e1', 700, anchor='middle', spacing=2)]
    for i in range(24):
        x, y = 780 + (i * 47 % 690), 44 + (i * 83 % 320)
        out.append(f'<circle cx="{x}" cy="{y}" r="{1 + i % 2}" fill="#dae9ef" opacity=".45"/>')
    cards = [(counts['projects'], 'PROJECT RECORDS'), (counts['sessions'], 'ORDERED SESSIONS'),
             (counts['fields'], 'DEFINED DATA FIELDS'), (counts['planned_verification_cases'], 'PLANNED CHECKS')]
    for i, (value, label) in enumerate(cards):
        x = 64 + i * 374
        out.append(rect(x, 424, 350, 114, '#0b263c', 14, '#28506a'))
        out += [text(x + 25, 482, f'{value:,}', 44, WHITE, 700),
                text(x + 25, 514, label, 13, TEAL if i != 3 else COPPER, 700, spacing=1.2)]
    out += [text(68, 581, 'DOCUMENTATION COUNTS · PROJECT EMPIRICAL VALIDATION PENDING', 13, '#b0c6d2', 400, spacing=.8),
            text(1530, 581, 'NASA-INSPIRED · INDEPENDENT', 12, '#b0c6d2', anchor='end')]
    return svg(w, h, 'ATLAS engineering research document collection',
               f"{counts['projects']} project records in {counts['sessions']} ordered sessions, "
               f"with {counts['fields']} defined data fields and {counts['planned_verification_cases']} planned verification cases. "
               'The orbital illustration is decorative, not scientific data. Empirical project validation remains pending. NASA-inspired independent documentation; no NASA affiliation.',
               ''.join(out), defs)


def session_card(letter, projects, annexes):
    selected = [p for p in projects if p['session'] == letter]
    included = [a for a in annexes if a['id'].startswith(letter)]
    counts = totals(selected, included)
    w, h = 640, 290
    out = [rect(0, 0, w, h, NAVY, 18)]
    out.append(orbital_motif(563, 74, 79, TEAL, .32))
    out += [rect(28, 28, 56, 56, '#143b53', 12),
            text(56, 68, letter, 34, TEAL, 700, anchor='middle'),
            text(101, 48, f'SESSION {letter}', 13, COPPER, 700, spacing=1.8)]
    title_lines = wrapped(SESSION_NAMES[letter], 32)
    out.append(lines(101, 80, title_lines, 24, 29, WHITE, 700))
    out.append(line(28, 145, 611, 145, '#2c4e63'))
    metrics = [(counts['projects'], 'projects'), (counts['fields'], 'fields'),
               (counts['planned_verification_cases'], 'planned checks')]
    for i, (value, label) in enumerate(metrics):
        x = 28 + i * 199
        out += [text(x, 192, str(value), 35, WHITE, 700), text(x, 216, label, 15, '#bbd0db')]
    out += [line(28, 238, 611, 238, '#2c4e63'),
            text(28, 267, 'Research design + analysis · source order preserved', 14, '#a6c3d0')]
    return svg(w, h, f'Session {letter}: {SESSION_NAMES[letter]}',
               f"{counts['projects']} projects, {counts['fields']} proposed data fields, and "
               f"{counts['planned_verification_cases']} planned verification cases. These counts are documentation metadata, not completed experimental work.",
               ''.join(out))


def field_layout(row):
    return {'name': wrapped(row['field'], 36),
            'type': wrapped(row['type'], 46),
            'unit': wrapped(row['unit'], 46),
            'meaning': wrapped(row['meaning'], 53)}


def field_height(layout):
    # Every type, unit and meaning is printed in full. Dynamic heights prevent clipping.
    return 52 + len(layout['name']) * 25 + 26 + len(layout['type']) * 22 + 26 + len(layout['unit']) * 22 + 23 + len(layout['meaning']) * 20


def field_card(row, layout, ordinal, x, y, width, height):
    out = [rect(x, y, width, height, WHITE, 14, RULE), rect(x, y + 18, 4, height - 36, '#277f79', 2)]
    out.append(text(x + 22, y + 28, f'{ordinal:02d} / FIELD DEFINITION', 11, '#477478', 700, spacing=1.3))
    cursor = y + 56
    out.append(lines(x + 22, cursor, layout['name'], 19, 25, INK, 700,
                     'Consolas, Menlo, monospace'))
    cursor += len(layout['name']) * 25 + 5
    out.append(text(x + 22, cursor, 'TYPE', 11, MUTED, 700, spacing=1.2))
    cursor += 24
    out.append(lines(x + 22, cursor, layout['type'], 16, 22, '#174f5c'))
    cursor += len(layout['type']) * 22 + 5
    out.append(text(x + 22, cursor, 'UNIT', 11, MUTED, 700, spacing=1.2))
    cursor += 24
    out.append(lines(x + 22, cursor, layout['unit'], 16, 22, INK))
    cursor += len(layout['unit']) * 22 + 7
    out.append(lines(x + 22, cursor, layout['meaning'], 14, 20, MUTED))
    return ''.join(out)


def data_map(project, annex):
    pid, fields = project['id'], annex['data_dictionary']
    layouts = [field_layout(row) for row in fields]
    row_heights = [max(field_height(l) for l in layouts[i:i+2]) for i in range(0, len(layouts), 2)]
    mission = project['name'].split('—')[0].strip()
    mission_lines = wrapped(mission, 48)
    heading_extra = max(0, len(mission_lines) - 1) * 35
    first_y = 250 + heading_extra
    field_end = first_y + sum(row_heights) + (len(row_heights) - 1) * 20
    footer_y = field_end + 44
    w, h = 1040, footer_y + 238
    out = [rect(0, 0, w, h, PAPER, 18), rect(0, 0, w, 12, '#1d676d', 6)]
    out += [text(38, 49, f'{pid} / DATA DEFINITION ATLAS', 13, '#206870', 700, spacing=1.4),
            text(1000, 49, f'{len(fields):02d} FIELDS', 13, '#206870', 700, anchor='end', spacing=1.4),
            lines(38, 98, mission_lines, 29, 35, INK, 700)]
    sub_y = 132 + heading_extra
    out += [text(38, sub_y, 'PROPOSED DATA CONTRACT', 15, '#80542f', 700, spacing=.7),
            text(38, sub_y + 28, 'No project observations acquired · acquisition template contains headers only', 16, MUTED),
            text(38, sub_y + 56, 'Field names, types and units below come directly from the versioned engineering dictionary.', 15, MUTED),
            line(38, sub_y + 79, 1002, sub_y + 79, RULE)]
    y = first_y
    for row_index, height in enumerate(row_heights):
        for col in range(2):
            index = row_index * 2 + col
            if index >= len(fields):
                out.append(rect(538, y, 464, height, '#edf3f0', 14, '#d8e5df'))
                out.append(orbital_motif(770, y + height * .43, min(95, height * .27), '#3a9183', .46))
                out += [text(770, y + height - 44, 'DEFINED FIELDS ≠ ACQUIRED DATA', 12, '#44776f', 700, anchor='middle'),
                        text(770, y + height - 22, 'A contract specifies a future record.', 14, '#44776f', anchor='middle')]
                continue
            out.append(field_card(fields[index], layouts[index], index + 1, 38 + col * 500, y, 464, height))
        y += height + 20
    out.append(text(38, footer_y, 'THE RECORD ENVELOPE', 12, '#206870', 700, spacing=1.5))
    steps = [('01', 'COLLECT', 'Future acquisition'), ('02', 'QUALIFY', 'Frame + calibration'),
             ('03', 'VALIDATE', 'Shape + domain rules'), ('04', 'PRESERVE', 'Version + provenance')]
    for i, (no, label, detail) in enumerate(steps):
        x = 38 + i * 250
        out.append(rect(x, footer_y + 20, 214, 92, MIDNIGHT if i == 3 else '#edf2f1', 12))
        fill = WHITE if i == 3 else INK
        out += [text(x + 18, footer_y + 44, no, 11, TEAL if i == 3 else '#48787d', 700),
                text(x + 18, footer_y + 68, label, 17, fill, 700),
                text(x + 18, footer_y + 91, detail, 13, '#c4d6df' if i == 3 else MUTED)]
        if i < 3:
            out.append(line(x + 219, footer_y + 65, x + 242, footer_y + 65, '#61948b', 1.5))
            out.append(f'<path d="M{x+235} {footer_y+60} L{x+242} {footer_y+65} L{x+235} {footer_y+70}" '
                       'fill="none" stroke="#61948b" stroke-width="1.5"/>')
    out += [text(38, footer_y + 146, 'Missing values stay unknown; zero is never a substitute for an absent measurement.', 15, MUTED),
            text(38, footer_y + 174, 'A schema checks structure. Physical bounds, covariance, units and calibration still require domain checks.', 14, MUTED),
            line(38, footer_y + 192, 1002, footer_y + 192, RULE),
            text(38, footer_y + 218, f'ATLAS / SESSION {project["session"]} / {pid} · Source: engineering_annexes.json', 11, '#627b88'),
            text(1002, footer_y + 218, 'SCHEMATIC · NO EXPERIMENTAL RESULTS', 11, '#80542f', anchor='end')]
    description = (f'Proposed data contract for {pid}, {project["name"]}. No project observations have been acquired. '
                   'Every dictionary field is shown with its type and unit: '
                   + '; '.join(f'{r["field"]}, type {r["type"]}, unit {r["unit"]}' for r in fields)
                   + '. The collection, qualification, validation and preservation flow is planned, not executed.')
    return svg(w, h, f'{pid} proposed data contract — {len(fields)} defined fields', description, ''.join(out))


def source_file(repo, name):
    for folder in ('registry', 'catalog'):
        candidate = repo / folder / name
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(f'{name} not found in registry/ or catalog/ under {repo}')


def save_svg(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    ET.fromstring(content)
    path.write_bytes(content.encode('utf-8'))


def generate(repo, out, co_locate=False):
    """Write deterministic artwork and return its manifest.

    ``repo`` and ``out`` accept pathlib paths or strings. With ``co_locate=True``,
    ``out`` must be inside ``repo`` and project destinations come from the
    canonical path register. No observations or numerical data are written.
    """
    repo, out = Path(repo).resolve(), Path(out).resolve()
    project_source = source_file(repo, 'projects.json')
    annex_source = source_file(repo, 'engineering_annexes.json')
    projects = json.loads(project_source.read_text(encoding='utf-8'))
    annexes = json.loads(annex_source.read_text(encoding='utf-8'))
    wanted = [f'{s}{i:02}' for s, count in EXPECTED.items() for i in range(1, count + 1)]
    assert len(projects) == 117 and [p['id'] for p in projects] == wanted, 'The supplied A–I project order must be preserved.'
    assert [a['id'] for a in annexes] == wanted, 'Engineering annex order must match the canonical projects.'
    amap = {a['id']: a for a in annexes}
    for p in projects:
        dictionary = amap[p['id']]['data_dictionary']
        assert dictionary and len({r['field'] for r in dictionary}) == len(dictionary), p['id']
        for row in dictionary:
            assert all(k in row for k in ('field', 'type', 'unit', 'meaning')), (p['id'], row)
    d03 = next(p for p in projects if p['id'] == 'D03')
    assert len(d03.get('subprojects', [])) >= 2, 'Both supplied D03 work packages must remain.'
    project_paths = None
    path_source = None
    if co_locate:
        if not out.is_relative_to(repo):
            raise ValueError('co_locate requires out inside repo for portable manifest paths.')
        path_source = source_file(repo, 'project_paths.json')
        path_rows = json.loads(path_source.read_text(encoding='utf-8'))
        assert [r['id'] for r in path_rows] == wanted, 'Project paths must preserve canonical A–I order.'
        project_paths = {r['id']: repo / r['directory'] for r in path_rows}
        assert all(p.resolve().is_relative_to(repo / 'research') for p in project_paths.values()), 'Project figure destinations must remain inside research/.'
    assets = []
    def emit(relative, content, kind, project_id=None, destination=None):
        file = destination if destination is not None else out / relative
        save_svg(file, content)
        manifest_path = str(file.relative_to(repo if co_locate else out)).replace('\\', '/')
        row = {'path': manifest_path, 'kind': kind, 'sha256': digest(file), 'bytes': file.stat().st_size}
        if project_id:
            row.update(project_id=project_id, fields=len(amap[project_id]['data_dictionary']))
        assets.append(row)
    emit('hero.svg', hero(projects, annexes), 'decorative_portfolio_metadata')
    for letter in EXPECTED:
        emit(f'sessions/{letter}.svg', session_card(letter, projects, annexes), 'session_metadata')
    for project in projects:
        destination = project_paths[project['id']] / 'figures/data-map.svg' if project_paths else None
        emit(f'projects/{project["id"]}.svg', data_map(project, amap[project['id']]),
             'proposed_data_contract', project['id'], destination)
    input_hashes = {str(project_source.relative_to(repo)).replace('\\', '/'): digest(project_source),
                    str(annex_source.relative_to(repo)).replace('\\', '/'): digest(annex_source)}
    if path_source:
        input_hashes[str(path_source.relative_to(repo)).replace('\\', '/')] = digest(path_source)
    manifest = {
        'generator': 'ATLAS visual design generator / Python standard library',
        'purpose': 'Original document artwork and exact field inventories; no observations or numerical results generated.',
        'input_hashes': input_hashes,
        'asset_path_base': 'repository root' if co_locate else 'output directory',
        'palette': {'navy': NAVY, 'midnight': MIDNIGHT, 'teal': TEAL, 'copper': COPPER,
                    'ink': INK, 'muted': MUTED, 'paper': PAPER, 'white': WHITE, 'rule': RULE},
        'fonts': {'body': 'Arial, Helvetica, sans-serif', 'field_names': 'Consolas, Menlo, monospace'},
        'counts': totals(projects, annexes), 'project_order': wanted,
        'session_counts': {s: {'projects': EXPECTED[s],
                              'fields': sum(len(a['data_dictionary']) for a in annexes if a['id'].startswith(s)),
                              'planned_verification_cases': sum(len(a['verification_cases']) for a in annexes if a['id'].startswith(s))}
                           for s in EXPECTED},
        'asset_count': len(assets), 'assets': assets,
        'evidence_labels': {'proposed_data_contract': 'No project observations acquired; empty acquisition templates.',
                            'session_metadata': 'Counts of specified documentation artifacts.',
                            'decorative_portfolio_metadata': 'Original orbital motifs; documentation counts, no NASA logo.'},
    }
    (out / 'visual_design_manifest.json').write_bytes((json.dumps(manifest, indent=2, ensure_ascii=False) + '\n').encode('utf-8'))
    print(f'Generated {len(assets)} SVG assets: 1 hero, 9 session cards, 117 proposed data maps; '
          f'{manifest["counts"]["fields"]} complete dictionary field definitions.')
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True, help='Engineering repository root')
    parser.add_argument('--out', type=Path, required=True, help='Directory for generated SVG artwork')
    parser.add_argument('--co-locate', action='store_true',
                        help='Place field maps in project figures/ using registry/project_paths.json; --out must be inside the repository.')
    args = parser.parse_args()
    generate(args.repo, args.out, args.co_locate)


if __name__ == '__main__':
    main()
