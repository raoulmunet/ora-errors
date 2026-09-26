from __future__ import annotations
import argparse,json
from .core import lookup,normalize_code,search

def _print_item(code,item):
    print(f"{code} — {item['title']}\n\nWhat it means\n{item['meaning']}\n")
    print("Common causes")
    for x in item["causes"]: print(f"- {x}")
    print("\nCheck next")
    for x in item["checks"]: print(f"- {x}")

def main(argv=None):
    p=argparse.ArgumentParser(description="Explain common Oracle ORA errors.")
    p.add_argument("code",nargs="?")
    p.add_argument("--search")
    p.add_argument("--format",choices=("text","json"),default="text")
    a=p.parse_args(argv)
    if a.search:
        results=search(a.search)
        if a.format=="json":
            print(json.dumps([{"code":c,**i} for c,i in results],indent=2))
        else:
            for c,i in results: print(f"{c} — {i['title']}")
        return 0
    if not a.code: p.error("provide an ORA code or --search TEXT")
    code=normalize_code(a.code); item=lookup(code)
    if not item:
        print(f"{code}: not in the local catalog")
        return 2
    if a.format=="json": print(json.dumps({"code":code,**item},indent=2))
    else: _print_item(code,item)
    return 0
if __name__=="__main__": raise SystemExit(main())
