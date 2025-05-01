import os
import subprocess

# Paths
PUML_FILE = "docs/models/models.puml"
OUTPUT_DIR = "docs/assets/generated"
MARKDOWN_FILE = "docs/models/models.md"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Generate SVG from PUML
output_svg = os.path.join(OUTPUT_DIR, "models.svg")
subprocess.run([
    "plantuml", "-tsvg", PUML_FILE, "-o", OUTPUT_DIR
], check=True)

# Update Markdown file
with open(MARKDOWN_FILE, "w") as md_file:
    md_file.write("# Models Documentation\n\n")
    md_file.write("This documentation includes the generated diagram from the PUML file.\n\n")
    md_file.write(f"![Models Diagram](../assets/generated/models.svg)\n")

print("Documentation generated successfully.")