# Scripts

These helpers are intentionally lightweight and use only the Python standard library.

## Commands

Create a new note folder:

```bash
python3 scripts/new_note.py "Gradient Descent Intuition" --domain machine-learning
```

Validate metadata:

```bash
python3 scripts/validate_metadata.py --notes notes --sources sources/youtube/metadata
```

Build one LaTeX note:

```bash
python3 scripts/build_latex.py notes/machine-learning/gradient-descent-intuition/note.tex
```

Build all notes:

```bash
python3 scripts/build_latex.py --all notes
```

Update indexes:

```bash
python3 scripts/update_index.py --notes notes --knowledge-base knowledge-base
```

