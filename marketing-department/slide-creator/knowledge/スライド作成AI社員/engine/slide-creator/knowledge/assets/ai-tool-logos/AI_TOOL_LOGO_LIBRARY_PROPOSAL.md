# AI Tool Logo Library Proposal

Purpose: keep one central local logo/reference library for all 8 X buzz systems.

The image generation flow should:

1. Extract tool names from the post text.
2. Match them against `manifest.json` aliases.
3. Select up to 4 relevant local logo images.
4. Pass those images into the OpenAI Images edit endpoint as reference images.
5. Generate a clean 3:4 diagram that naturally incorporates only the relevant logos.

Do not post-process overlay these tool logos. They are generation references.

## Initial Tool Set

This set was chosen from past post frequency across the local buzz-system/archive files.

High priority:

- Claude / Claude Code / Anthropic
- GPT-5.5 / GPT-5 / ChatGPT / OpenAI / Codex
- Gemini / Gemini CLI / Nano Banana
- Obsidian / MCP / Cursor / GitHub Copilot / Windsurf
- サンプルエージェント / サンプルプロダクト
- DeepSeek / Grok / Qwen

Medium priority:

- Canva / Notion / Figma / NotebookLM
- Supabase / Firebase / v0 / Replit / Lovable / Bolt
- Perplexity / Manus / Devin / Mistral

Creative/video/audio priority:

- Sora / Veo / Runway / Midjourney / Kling / ElevenLabs

## Frequency Snapshot

- `Claude`: 54472
- `Claude Code`: 31874
- `Anthropic`: 20139
- `GPT-5`: 14280
- `OpenAI`: 12078
- `Codex`: 10909
- `GPT-5.5`: 10516
- `Obsidian`: 7057
- `MCP`: 5592
- `Cursor`: 4224
- `Gemini`: 3775
- `ChatGPT`: 3044
- `DeepSeek`: 2825
- `Grok`: 2074
- `Copilot`: 1762
- `Gemini CLI`: 808
- `Qwen`: 795
- `NotebookLM`: 691
- `Nano Banana`: 601
- `Lovable`: 583
- `Perplexity`: 430
- `Windsurf`: 306
- `Sora`: 243
- `ElevenLabs`: 148
- `Mistral`: 145
- `Manus`: 101
- `サンプルエージェント`: added from サンプルプロダクト/サンプルエージェント knowledge notes
- `サンプルプロダクト`: added from サンプルプロダクト account/archive context

## Asset Policy

- Start with clean local PNGs from official domains/favicons.
- Replace important assets with official press-kit or repository logos when available.
- Keep file paths stable; update only the image file behind each manifest entry.
- Avoid adding more than 4 reference images to a single generation because `gpt-image-2` uses high-fidelity image inputs and extra image inputs increase cost.
