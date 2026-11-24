# V-90 User Guide

MkDocs (Material) source for the V-90 plug-ins user guide, published at https://docs.neyrinck.com/v90/.

## Build

    pip install mkdocs-material
    mkdocs serve      # preview at http://127.0.0.1:8000
    ./deploy.sh       # build site/, commit and push; the GitHub action copies site/ to docs-neyrinck/v90

## Generated content

- `docs/plugins/{reverbs,reflections,modulations,pitch-change}.md` are generated from
  `tools/templates/*.md.in`: each `{{table <page> <memory>}}` becomes that program's parameter table
  (LCD name, host name, range, default), read from the plug-ins' generated `*Types.cpp` and the spx90
  program catalog. Edit the templates, not the .md files, then run `python3 tools/gen_plugin_pages.py`.
- `docs/images/*.png` are drawn from the plug-ins' own panel graphics and layout.json by
  `python3 tools/render_screenshots.py` (needs Pillow).

Both read the V-90 source from `V90_SRC` (default `~/Code/ncontrol_symph_1_0/internal/N-Control/V90`).
