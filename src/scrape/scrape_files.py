import os

from src.scrape.split_code import split_code

def scrape_files(src_path, extensions=('.ts', '.tsx')):
    """
    Scrapes files from the given source path with specified extensions and extracts code examples.

    Args:
        src_path (str): The source directory path to search for files.
        extensions (tuple): A tuple of file extensions to filter the files. Defaults to ('.ts', '.tsx').

    Returns:
        list: A list of code examples extracted from the files.
    """
    skip_folders = {'model', 'svg', 'theme', '18n', 'prod', 'assets', 'routes'}
    skip_files = {'api.ts', 'config.ts'}
    examples = []

    for root, dirs, files in os.walk(src_path):
        dirs[:] = [d for d in dirs if d not in skip_folders]
        files.sort()
        for file in files:
            if file in skip_files or file.endswith('Elements.tsx') or file.endswith('styled.ts'):
                continue
            if file.endswith(extensions):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    code = f.read()
                    lines = code.split('\n')
                    total_lines = len(lines)
                    if total_lines < 48 or total_lines > 128:
                        continue
                    examples.extend(split_code(code))

    return examples