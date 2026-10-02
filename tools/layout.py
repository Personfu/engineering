"""Canonical, human-readable paths for the ATLAS engineering library."""
import os
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def slug(name):
    return re.sub(r'[^a-z0-9]+','-',name.lower()).strip('-')

def project_directory(project):
    return ROOT/'research'/project['session']/(project['id']+'-'+slug(project['name']))

def project_document(project):
    return project_directory(project)/'README.md'

def relative(source_file,target_file):
    return os.path.relpath(target_file,source_file.parent).replace('\\','/')

def rebase_markdown(content,source_file,destination_file,local_anchors_to_source=False):
    """Rebase actual Markdown links while preserving external URLs and anchors."""
    def change(match):
        target=match.group(1)
        if '://' in target:return match.group(0)
        if target.startswith('#'):
            return '('+relative(destination_file,source_file)+target+')' if local_anchors_to_source else match.group(0)
        path,sep,anchor=target.partition('#')
        absolute=(source_file.parent/path).resolve()
        return '('+relative(destination_file,absolute)+(sep+anchor if sep else '')+')'
    # A physical expression such as ](1-e^{-tau}) is not a Markdown link.
    blocks=re.split(r'(```.*?```|\$\$.*?\$\$)',content,flags=re.S)
    for i in range(0,len(blocks),2):
        # Looking behind each closing bracket also handles images inside links.
        blocks[i]=re.sub(r'(?<=\])\(([^)\s]+)\)',change,blocks[i])
    return ''.join(blocks)
