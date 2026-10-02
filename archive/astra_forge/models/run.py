"""Run an educational kernel: python -m models.run --model orbit --output /tmp/astra-orbit.json"""
import argparse
import json
import platform
from pathlib import Path
from .reference import DEMOS


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model',choices=sorted(DEMOS),required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    payload=DEMOS[args.model]()
    payload.update(model=args.model,python_version=platform.python_version(),input_kind='synthetic',live_data=False)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(payload,indent=2)+'\n')
    print(f'{args.model}: {len(payload["rows"])} synthetic rows written to {args.output}')


if __name__=='__main__': main()
