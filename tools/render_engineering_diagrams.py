"""Render the 117 source diagrams as accessible engineering-document SVGs."""
import argparse
import concurrent.futures
import hashlib
import html
import json
import re
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def render(project, annex, cli, config):
    pid = project['id']
    source = ROOT/'visuals/projects'/f'{pid}.mmd'
    output = source.with_suffix('.svg')
    result = subprocess.run(['node', str(cli), '-i', str(source), '-o', str(output),
                             '-c', str(config), '-b', 'white'],
                            capture_output=True, text=True, encoding='utf-8', timeout=90)
    if result.returncode:
        raise RuntimeError(pid+': '+result.stdout+' '+result.stderr)
    svg = output.read_text(encoding='utf-8')
    start = svg.index('<svg')
    end = svg.index('>', start)
    tag = svg[start:end]
    tag = re.sub(r'\s(?:role|aria-labelledby)="[^"]*"', '', tag)
    tag += ' role="img" aria-labelledby="atlas-title atlas-description"'
    title = html.escape(pid+' '+project['name']+' engineering architecture')
    description = html.escape(annex['figure_caption'])
    svg = svg[:start]+tag+'><title id="atlas-title">'+title+'</title><desc id="atlas-description">'+description+'</desc>'+svg[end+1:]
    ET.fromstring(svg)
    output.write_bytes((svg.rstrip()+'\n').encode('utf-8'))
    return {'project_id':pid,'source':str(source.relative_to(ROOT/'visuals')).replace('\\','/'),
            'svg':str(output.relative_to(ROOT/'visuals')).replace('\\','/'),
            'source_sha256':digest(source),'svg_sha256':digest(output),'svg_bytes':output.stat().st_size}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cli', type=Path, default=ROOT/'tools/node_modules/@mermaid-js/mermaid-cli/src/cli.js')
    parser.add_argument('--workers', type=int, default=2)
    args = parser.parse_args()
    if not args.cli.is_file():
        parser.error('CLI not found; run npm install in tools/, or supply --cli.')
    if not 1 <= args.workers <= 8:
        parser.error('--workers must be between 1 and 8.')
    config = ROOT/'tools/mermaid-config.json'
    projects = json.loads((ROOT/'catalog/projects.json').read_text(encoding='utf-8'))
    annexes = {a['id']:a for a in json.loads((ROOT/'catalog/engineering_annexes.json').read_text(encoding='utf-8'))}
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        pending = [executor.submit(render,p,annexes[p['id']],args.cli.resolve(),config) for p in projects]
        for future in concurrent.futures.as_completed(pending):
            results.append(future.result())
            if len(results)%10 == 0 or len(results)==len(projects):
                print(f'Rendered {len(results)}/{len(projects)} engineering diagrams.', flush=True)
    results.sort(key=lambda r:r['project_id'])
    manifest = {'purpose':'Engineering model/interface architecture; not empirical result figures.',
                'renderer':'Mermaid CLI 12.0.0','config_sha256':digest(config),
                'figures':results,'count':len(results)}
    (ROOT/'visuals/engineering_figure_manifest.json').write_bytes((json.dumps(manifest,indent=2)+'\n').encode('utf-8'))

if __name__=='__main__':main()
