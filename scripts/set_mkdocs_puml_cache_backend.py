import sys
import yaml
import os

# File path to the mkdocs.yml file
MKDOCS_YML_PATH = os.path.join(os.path.dirname(__file__), '..', 'mkdocs.yml')

def toggle_cache_backend(state):
    """Toggle the plugins.plantuml.cache.backend key in the mkdocs.yml file."""
    with open(MKDOCS_YML_PATH, 'r') as file:
        config = yaml.safe_load(file)

    # Navigate to the specific key and modify it
    if 'plugins' in config:
        for plugin in config['plugins']:
            if isinstance(plugin, dict) and 'plantuml' in plugin:
                if 'cache' in plugin['plantuml'] and 'backend' in plugin['plantuml']['cache']:
                    if state == 'disable':
                        plugin['plantuml']['cache']['backend'] = 'disabled'
                    elif state == 'enable':
                        plugin['plantuml']['cache']['backend'] = 'local'

    # Write the updated configuration back to the file
    with open(MKDOCS_YML_PATH, 'w') as file:
        yaml.dump(config, file, default_flow_style=False)

# Add a custom loader to ignore unknown YAML tags
def ignore_unknown_tags(loader, tag_suffix, node):
    return None

yaml.add_multi_constructor('tag:yaml.org,2002:', ignore_unknown_tags, Loader=yaml.SafeLoader)

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ['disable', 'enable']:
        print("Usage: toggle_cache_backend.py <disable|enable>")
        sys.exit(1)

    toggle_cache_backend(sys.argv[1])