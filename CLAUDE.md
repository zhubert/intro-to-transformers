# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

An educational resource teaching how transformers and diffusion models work through hands-on implementation. The content is structured as a MyST book with Jupyter notebooks.

## Commands

### Python Environment
```bash
uv sync                           # Install/sync dependencies
source .venv/bin/activate         # Activate virtual environment
```

### Book Development (MyST)
```bash
npm run start                     # Start dev server with live reload
npm run build                     # Build static HTML to _build/
npx myst start                    # Alternative: run myst directly
```

### Jupyter
```bash
jupyter notebook                  # Start Jupyter server
```

## Architecture

### Content Sections

Four main learning paths, each in its own directory:

1. **understanding-gradients/** — Hand-calculated transformer forward/backward pass using pure Python (no NumPy/PyTorch). Notebooks 00-10 cover tokenization through AdamW optimization.

2. **building-a-transformer/** — PyTorch implementation from scratch. Notebooks 00-09 cover embeddings, attention, training, KV-cache, and interpretability.

3. **fine-tuning-a-transformer/** — Post-training techniques. Notebooks 00-25 cover SFT (instruction formatting, loss masking, LoRA), reward modeling, RLHF (PPO, KL penalty), and DPO.

4. **from-noise-to-images/** — Diffusion models. Notebooks 01-05 cover flow matching, DiT architecture, conditioning, and latent diffusion.

### Book Configuration

- **myst.yml** — Table of contents, project metadata, site options
- **intro.md** — Book landing page
- **intro.png** — Book logo

### Writing Style

See https://github.com/zhubert/styleguide for the author's voice: conversational, technically fluent, story-driven. Key patterns include short punchy sentences, parenthetical asides, and teaching through narrative.
