#!/usr/bin/env python3
import os, sys

def flatten(root, exts=('.py','.js')):
    parts = []
    for dirpath, _, filenames in os.walk(root):
        for fn in sorted(filenames):
            if fn.endswith(exts):
                fp = os.path.join(dirpath, fn)
                with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read().replace('\n', ' ')
                parts.append(f'// FILE:{fp} {content}')
    return ' '.join(parts)

if __name__ == '__main__':
    try:
        import pyperclip
    except ImportError:
        print("Installing pyperclip module...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyperclip"])
        import pyperclip

    root = sys.argv[1] if len(sys.argv)>1 else '.'
    out = flatten(root)

    with open('one_line_codebase.txt','w', encoding='utf-8') as o:
        o.write(out)

    # Copy to clipboard
    pyperclip.copy(out)

    print("Created one_line_codebase.txt and copied content to clipboard")