"""MakeFun entry script."""

import os


def main() -> None:
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, 'entry.txt')
    
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        f.write("I can time travel one day into the past, but only as a passive witness trapped inside yesterday's drywall.")


if __name__ == '__main__':
    main()
