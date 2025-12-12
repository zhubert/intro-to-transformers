#!/usr/bin/env python3
"""
Remove bold opening lines from Jupyter notebooks.

The pattern we're removing is: after a title line (# Title), there's a bold
description line (**Description text**) that should be removed.
"""

import json
import sys
from pathlib import Path

# List of all 54 notebooks with opening lines to remove
NOTEBOOKS = [
    "building-a-transformer/00_introduction.ipynb",
    "building-a-transformer/01_embeddings.ipynb",
    "building-a-transformer/02_attention.ipynb",
    "building-a-transformer/03_multi_head_attention.ipynb",
    "building-a-transformer/04_feedforward.ipynb",
    "building-a-transformer/05_transformer_block.ipynb",
    "building-a-transformer/06_complete_model.ipynb",
    "building-a-transformer/07_training.ipynb",
    "building-a-transformer/08_kv_cache.ipynb",
    "building-a-transformer/09_interpretability.ipynb",
    "fine-tuning-a-transformer/00_introduction.ipynb",
    "fine-tuning-a-transformer/01_why_post_training.ipynb",
    "fine-tuning-a-transformer/02_project_overview.ipynb",
    "fine-tuning-a-transformer/03_sft_introduction.ipynb",
    "fine-tuning-a-transformer/04_sft_formatting.ipynb",
    "fine-tuning-a-transformer/05_sft_loss_masking.ipynb",
    "fine-tuning-a-transformer/07_sft_lora.ipynb",
    "fine-tuning-a-transformer/08_reward_introduction.ipynb",
    "fine-tuning-a-transformer/09_reward_preference_data.ipynb",
    "fine-tuning-a-transformer/10_reward_training.ipynb",
    "fine-tuning-a-transformer/11_reward_evaluation.ipynb",
    "fine-tuning-a-transformer/12_rlhf_introduction.ipynb",
    "fine-tuning-a-transformer/13_rlhf_ppo.ipynb",
    "fine-tuning-a-transformer/14_rlhf_kl_penalty.ipynb",
    "fine-tuning-a-transformer/15_rlhf_dynamics.ipynb",
    "fine-tuning-a-transformer/16_rlhf_reference.ipynb",
    "fine-tuning-a-transformer/17_dpo_introduction.ipynb",
    "fine-tuning-a-transformer/19_dpo_loss.ipynb",
    "fine-tuning-a-transformer/20_dpo_training.ipynb",
    "fine-tuning-a-transformer/21_advanced_memory.ipynb",
    "fine-tuning-a-transformer/22_advanced_hyperparams.ipynb",
    "fine-tuning-a-transformer/23_advanced_evaluation.ipynb",
    "fine-tuning-a-transformer/24_advanced_pitfalls.ipynb",
    "fine-tuning-a-transformer/25_try_it.ipynb",
    "reasoning-with-transformers/01_chain_of_thought.ipynb",
    "reasoning-with-transformers/02_self_consistency.ipynb",
    "reasoning-with-transformers/03_tree_of_thoughts.ipynb",
    "reasoning-with-transformers/04_process_reward_model.ipynb",
    "reasoning-with-transformers/05_best_of_n.ipynb",
    "reasoning-with-transformers/06_mcts.ipynb",
    "reasoning-with-transformers/07_budget_forcing.ipynb",
    "reasoning-with-transformers/08_grpo.ipynb",
    "reasoning-with-transformers/09_distillation.ipynb",
    "understanding-gradients/00_introduction.ipynb",
    "understanding-gradients/01_tokenization_embeddings.ipynb",
    "understanding-gradients/02_qkv_projections.ipynb",
    "understanding-gradients/03_attention.ipynb",
    "understanding-gradients/04_multi_head.ipynb",
    "understanding-gradients/05_feedforward.ipynb",
    "understanding-gradients/06_layer_norm.ipynb",
    "understanding-gradients/07_loss.ipynb",
    "understanding-gradients/08_grad_loss.ipynb",
    "understanding-gradients/09_grad_backprop.ipynb",
    "understanding-gradients/10_optimizer.ipynb",
]


def remove_opening_line(notebook_path: Path) -> bool:
    """
    Remove the bold opening line from the first markdown cell.

    Returns True if the file was modified, False otherwise.
    """
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
    except Exception as e:
        print(f"Error reading {notebook_path}: {e}", file=sys.stderr)
        return False

    # Check if there are any cells
    if not notebook.get('cells'):
        print(f"No cells found in {notebook_path}", file=sys.stderr)
        return False

    first_cell = notebook['cells'][0]

    # Verify it's a markdown cell
    if first_cell.get('cell_type') != 'markdown':
        print(f"First cell is not markdown in {notebook_path}", file=sys.stderr)
        return False

    # Get the source (can be a string or list of strings)
    source = first_cell.get('source', [])
    is_string = isinstance(source, str)

    if is_string:
        # Convert string to list of lines
        source_list = source.split('\n')
    else:
        # Already a list, but each item has \n at the end
        source_list = [line.rstrip('\n') for line in source]

    # Check if we have at least 3 lines (title + blank + opening line)
    if len(source_list) < 3:
        print(f"Not enough lines in first cell of {notebook_path}", file=sys.stderr)
        return False

    # Check if line 0 is a title, line 1 is blank, and line 2 is bold text
    line0 = source_list[0].strip()
    line1 = source_list[1].strip()
    line2 = source_list[2].strip()

    if not line0.startswith('#'):
        print(f"First line is not a title in {notebook_path}: {line0[:50]}", file=sys.stderr)
        return False

    if line1 != '':
        print(f"Second line is not blank in {notebook_path}: {repr(line1[:50])}", file=sys.stderr)
        return False

    if not (line2.startswith('**') and line2.endswith('**')):
        print(f"Third line is not bold text in {notebook_path}: {line2[:50]}", file=sys.stderr)
        return False

    # Remove lines 1 and 2 (blank line + bold opening line)
    new_source_list = [source_list[0]]  # Keep the title

    # Add remaining lines starting from index 3
    new_source_list.extend(source_list[3:])

    # Convert back to the original format
    if is_string:
        new_source = '\n'.join(new_source_list)
    else:
        # Add back the \n to each line for list format
        new_source = [line + '\n' if i < len(new_source_list) - 1 else line
                      for i, line in enumerate(new_source_list)]

    # Update the cell
    first_cell['source'] = new_source

    # Write back
    try:
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)
            f.write('\n')  # Add final newline
        return True
    except Exception as e:
        print(f"Error writing {notebook_path}: {e}", file=sys.stderr)
        return False


def main():
    base_path = Path(__file__).parent
    modified_count = 0
    error_count = 0

    for notebook_rel in NOTEBOOKS:
        notebook_path = base_path / notebook_rel

        if not notebook_path.exists():
            print(f"Notebook not found: {notebook_path}", file=sys.stderr)
            error_count += 1
            continue

        print(f"Processing {notebook_rel}...", end=' ')
        if remove_opening_line(notebook_path):
            print("✓")
            modified_count += 1
        else:
            print("✗")
            error_count += 1

    print()
    print(f"Modified: {modified_count}/{len(NOTEBOOKS)}")
    print(f"Errors: {error_count}/{len(NOTEBOOKS)}")

    return 0 if error_count == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
