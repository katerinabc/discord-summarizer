# 💻-coders 2024-11-03

## Summary
The discussion focused on how to implement a personalized language model within the 'Eliza' platform. The proposed solutions included editing default character files and setting Anthropic API key as provider.

## FAQ
- How can I implement my own fine-tuned LLM for Twitter instead of the default in Eliza? »,    (asked by @SMA (00:14))
- What’s the workflow for finetuning an LLM? Like Ollama and stuff? (asked by @SotoAlt | WAWE (00:42))
- Are 405b models better than others in terms of performance or capabilities? (asked by @ferric | stakeware.xyz (00:47))
- Does the current code sample? I haven't read through how it builds the prompt. (asked by @ferric)
- Do you really need a finetune do u??? (referring to @SMA) (asked by @Ophiuchus)
- Does getting data in the right shape sound hard? (https://www.llama.com/docs/how-to-guides/fine-tuning/) (asked by [ferric | stakeware.xyz])
- Should I use a biography paragraph for character bio and lore? (https://www.llama.com/docs/how-to-guides/fine-tuning/) (asked by [SMA](01:36))
- Can I DM you the statements to check if they'd work? (https://www[-]llama.com/docs/how-to-guides/fine-tuning/) (asked by [SMA](01:36))
- Is it working now? (asked by [SMA](01:39))
- How do I disable Telegram component? How to rename 'trump.character.js' in the repo and where is '.env file?' (asked by [SMA](01:03))

## Who Helped Who
- @SotoAlt | WAWE, @Ophiuchus helped @sma (00:14) with Implement custom fine-tuned LLM for Twitter in Eliza by providing Editing character file and setting Anthropic API key
- @Ophiuchus helped @SotoAlt | WAWE (00:42) with Understanding the finetune workflow for an LLM by providing Finetuning LLM using A100 GPUs
- @ferric helped @Ophiuchus with Improving the character dataset handling in codebase. by providing Finetuning an agent with user/agent write/response json blob suggested by ferric
- [ferric | stakeware.xyz] (01:15) helped [SMA](01:36) with Improve character bio and lore generation by providing Finetune LLM on OpenAI
- [SMA](01:03) helped [Ophiuchus](01:14) with Editing character file by providing Renaming 'trump.character.js'
- [Ophiuchus] helped [SMA] with Locating necessary files by providing Ophiuchus provided the location of a needed character file in core/src/core directory.
- [whobody](01:20) helped [SMA](01:20) with Project development assistance by providing Ophiuchus offers onsite work and help for free
- [Ophiuchus, whobody] helped [SMA] with Documentation by providing Discussing and agreeing on documenting Eliza's process, editing default character for video recording.
- [whobody] helped [big dookie (03:11)] with Understanding how to proceed with Twitter handler issue by providing LiveTheLifeTV provided an explanation of the Eliza repo and its role in their project.
- LiveTheLifeTV helped @gm with Technical Tasks by providing Fixing bot by resetting the .env in core folder.

## Action Items

### Technical Tasks
- Edit default character file for Eliza (mentioned by @SotoAlt | WAWE)
- Set Anthropic API key and use it as the provider in Eliza settings. (mentioned by @Ophiuchus)
- Finetuning LLM using A100 GPUs (mentioned by @Ophiuchus)
- Finetune an agent with user/agent write/response json blob (mentioned by @ferric)
- Finetune LLM on OpenAI (mentioned by [SMA](01:15))
- Use long paragraph as context for single statements in agent's responses. (mentioned by [ferric | stakeware.xyz](01:36))
- Disable Telegram component (mentioned by [SMA](01:03))
- Set up Discord Bot (mentioned by [SMA](01:19))
- Record conversation to reduce overlap (mentioned by [whobody](01:20))
- Document Eliza documentary process (mentioned by [Ophiuchus, whobody])
- Deep dive into code for better understanding (mentioned by [Ophiuchus (01:37)])

### Documentation Needs
- Check out 'Together' for finetune API usage. (mentioned by @ferric)
- Rename 'trump.character.js' in the repo to match new name. (mentioned by [SMA](01:03))
- Update character file in core/src/core directory. (mentioned by [Ophiuchus](01:17))
- Change default character in template file for SMA project (mentioned by [SMA](01:20))
- Edit default character for the video recording. (mentioned by SMA)
- Update node to latest version before installation. (mentioned by [Ophiuchus (04:36)])
- Update documentation for .env variable configuration (mentioned by @jin)

### Feature Requests
- Use the https://github.com/ai16z/characterfile on archive for character dataset (mentioned by @Ophiuchus)
- Iterate on template provided by Claude for character bio and lore. (mentioned by [SotoAlt | WAWE](01:37))