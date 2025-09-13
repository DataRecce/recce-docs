#!/usr/bin/env python3
import os
import re
from collections import defaultdict
from pathlib import Path

def find_image_references(docs_path):
    """Find all image references in markdown files and map them to sections."""
    image_usage = defaultdict(list)
    section_images = defaultdict(set)
    
    # Pattern to match image references
    image_pattern = r'!\[.*?\]\((.*?assets/images/.*?)\)'
    
    for root, dirs, files in os.walk(docs_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, docs_path)
                
                # Determine section from path
                path_parts = rel_path.split(os.sep)
                section = path_parts[0] if path_parts[0] != '.' else 'root'
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    matches = re.findall(image_pattern, content)
                    
                    for match in matches:
                        # Normalize the path (remove ../ prefixes)
                        normalized_path = match
                        while normalized_path.startswith('../'):
                            normalized_path = normalized_path[3:]
                        
                        image_usage[normalized_path].append({
                            'file': rel_path,
                            'section': section,
                            'original_path': match
                        })
                        section_images[section].add(normalized_path)
    
    return image_usage, section_images

def main():
    docs_path = './docs'
    image_usage, section_images = find_image_references(docs_path)
    
    print("=== IMAGE USAGE ANALYSIS ===\n")
    
    print("Images by section:")
    for section, images in sorted(section_images.items()):
        print(f"\n{section}:")
        for img in sorted(images):
            print(f"  - {img}")
    
    print("\n\n=== DETAILED IMAGE USAGE ===\n")
    
    for image_path, usages in sorted(image_usage.items()):
        print(f"{image_path}:")
        sections = set()
        for usage in usages:
            print(f"  Used in: {usage['file']} (section: {usage['section']})")
            sections.add(usage['section'])
        
        if len(sections) == 1:
            section = list(sections)[0]
            print(f"  → Should move to: assets/images/{section}/")
        else:
            print(f"  → Used in multiple sections: {', '.join(sorted(sections))}")
            print(f"  → Keep in: assets/images/shared/ or assess individual usage")
        print()

if __name__ == "__main__":
    main()