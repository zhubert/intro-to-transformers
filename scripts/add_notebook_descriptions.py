#!/usr/bin/env python3
"""
Add description metadata to Jupyter notebooks for better SEO and social media unfurling.
Extracts descriptions from the first few markdown cells of each notebook.
"""

import json
import re
from pathlib import Path


def extract_description(notebook_path):
    """Extract a description from the notebook's markdown cells."""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # Collect text from first few markdown cells (skip title)
    text_parts = []
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'markdown':
            source = ''.join(cell.get('source', []))
            # Skip if it's just a title (starts with #)
            if source.strip().startswith('#') and '\n' not in source.strip():
                continue
            # Clean up MyST directives and markdown
            source = re.sub(r':::\{[^}]+\}', '', source)  # Remove MyST directives
            source = re.sub(r':::', '', source)
            source = re.sub(r'\*\*([^*]+)\*\*', r'\1', source)  # Bold
            source = re.sub(r'\*([^*]+)\*', r'\1', source)  # Italic
            source = re.sub(r'`([^`]+)`', r'\1', source)  # Code
            source = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', source)  # Links
            source = re.sub(r'#+\s+', '', source)  # Headers
            source = source.strip()
            if source:
                text_parts.append(source)
            # Stop after collecting a few meaningful paragraphs
            if len(' '.join(text_parts)) > 100:
                break

    # Join and truncate to reasonable length
    description = ' '.join(text_parts)
    # Take first sentence or two
    sentences = re.split(r'(?<=[.!?])\s+', description)
    if sentences:
        # Use first 1-2 sentences, max 160 chars
        desc = sentences[0]
        if len(desc) < 100 and len(sentences) > 1:
            desc = f"{sentences[0]} {sentences[1]}"
        # Truncate if too long
        if len(desc) > 160:
            desc = desc[:157] + '...'
        return desc

    return None


def add_description_to_notebook(notebook_path):
    """Add description metadata to notebook if not already present."""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # Check if description already exists
    metadata = nb.get('metadata', {})
    if 'description' in metadata:
        print(f"  ✓ {notebook_path.name} already has description")
        return False

    # Extract description
    description = extract_description(notebook_path)
    if not description:
        print(f"  ⚠ {notebook_path.name} - could not extract description")
        return False

    # Add description to metadata
    metadata['description'] = description
    metadata['thumbnail'] = 'intro.png'  # Use default thumbnail
    nb['metadata'] = metadata

    # Write back
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

    print(f"  ✓ {notebook_path.name}: {description[:60]}...")
    return True


def main():
    """Process all notebooks in the repository."""
    repo_root = Path(__file__).parent.parent

    # Find all notebooks
    notebooks = list(repo_root.glob('**/*.ipynb'))
    notebooks = [nb for nb in notebooks if '.ipynb_checkpoints' not in str(nb)]

    print(f"Found {len(notebooks)} notebooks")
    print()

    updated = 0
    for notebook in sorted(notebooks):
        if add_description_to_notebook(notebook):
            updated += 1

    print()
    print(f"Updated {updated} notebooks")


if __name__ == '__main__':
    main()
