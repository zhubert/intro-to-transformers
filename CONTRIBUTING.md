# Contributing

This document covers development setup for maintainers.

## Building the Book

The book is built with [MyST](https://mystmd.org/):

```bash
# Install MyST CLI
npm install

# Start the development server
npx myst start

# Build for production
npx myst build --html
```

## Project Structure

```
intro-to-transformers/
├── understanding-gradients/      # Hand-calculated forward & backward pass
├── building-a-transformer/       # PyTorch implementation from scratch
├── fine-tuning-a-transformer/    # SFT, RLHF, DPO techniques
├── from-noise-to-images/         # Diffusion models and flow matching
├── reasoning-with-transformers/  # CoT, MCTS, GRPO, distillation
├── intro.md                      # Book landing page
├── myst.yml                      # MyST configuration
└── pyproject.toml                # Python dependencies
```
