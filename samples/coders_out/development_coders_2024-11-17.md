# 💻-coders 2024-11-17

## Summary
The chat focused on technical discussions regarding character selection issues, API key problems for different groq versions, finetuning models, increasing creativity in agents' responses by adjusting chaos parameters or incorporating real-world knowledge. The community members helped each other with specific errors and provided solutions.

## FAQ
- I've finetuned a model, what do now? (asked by puremood)
- Is the API key for a different version of groq? (asked by boyaloxer)
- Can agents be more creative and have real-world knowledge instead of relying only on character files? (asked by LaserRiot)
- Do I need to download my entire model and upload it on Hugging Face? It's 100GB! Or can I just use the adapter instead? What are your thoughts? (asked by [puremood])
- Which base model is being used for bots, and why might switching to Grok be beneficial due to its intrinsic live knowledge feed feature? (asked by [LaserRiot](0:36))
- What's the ticker for boredom adjustment? Is it a dial we can set here? (asked by @Shannon Code (emblem vault))
- Does this system ignore things not directed at it, and is its prompt tunable? (asked by @ferric | stakeware.xyz)
- What errors are you getting? (asked by @boyaloxer)
- Can anyone tell me what happens after this error message? (asked by @Lady lotus (02:49))
- Do you need a dev account for the Twitter bot or can it be configured with a normal one? (asked by @Roque(02:56))

## Who Helped Who
- griffin was having trouble selecting a specific model in the command line tool. helped Bitang with Resolving errors after refreshing code and adding build step by providing boyaloxer helped griffin with API key issue
- [Shannon Code (emblem vault)](0:51) helped All with Discussing potential solutions for bots triggering Twitter’s TOS. by providing [LaserRiot](0:47) shares a relevant link about Twitter's ToS concerns.
- @Oguz Serdar helped [Other Bots] with Improving bot interactions and user experience by providing 'Kitten persona' vibes with other bots to create a friendly atmosphere.
- [Shannon Code (emblem vault)] helped [gy | CLONE] with Finding and using ai16z framework docs by providing Guidance on finding documentation for building an AI16Z agent.
- @loaf(02:39) helped @Lady lotus with Troubleshoot node version and potential fixes for eliza main commit issue. by providing @SMA (02:53) and @Oguz Serdar provided guidance on troubleshooting the agent errors, suggesting it might be compatibility issues with Node.js versions.
- @SMA helped All members needing assistance with Node.js issues or other technical queries. with Provide support for node version compatibility and troubleshooting via DMS by providing @Oguz Serdar (02:41) offered help in Discord direct messages due to his fully doxxed account.
- [Oguz Serdar] helped [Lady lotus] with Troubleshooting AI Model Selection by providing Oguz Serdar provided guidance on testing model providers and using API keys in .env file.
- [SotoAlt | WAWE](03:31) helped [Mr. frogwifcat, collect](03:34) with Provide work samples for project collaboration or review. by providing Moyai offered to send works via DM
- [Oguz Serdar](03:28) helped [SotoAlt | WAWE, 0xaryan](03:31) with Assist in creating character file and defining model provider. by providing Moyai offered to help with design
- @roque helped kbrownfitness with Integration of AI components by providing Roque helped integrate a knowledge processor and content generator with X for Discord.

## Action Items

### Technical Tasks
- Finetune model for better performance (mentioned by puremood)
- Check if the provided link answers questions about making agents more chaotic/creative and adding knowledge to bots (mentioned by [uber](0:36))
- Consider swapping models from Sonnet 3.5 via API to Grok for intrinsic live knowledge feed. (mentioned by [LaserRiot](0:40))
- Implement logic on top of interactions.ts to manage bot-to-bot chat (mentioned by @Oguz Serdar)
- Implementing allocation-related features using LP for pool fees. (mentioned by [Shannon Code (emblem vault)])
- Investigate errors after new commits from eliza main (mentioned by @SMA)
- Testing model providers by changing .env file (mentioned by [Lady lotus, Oguz Serdar])
- Create character file with model provider definition (mentioned by [Oguz Serdar](03:28))
- Fix tweet validation rules for 'right content' (mentioned by kbrownfitness)
- Set up model locally for project development. (mentioned by @Oblong)
- Discuss RAG implementation, data scraping methods (mentioned by MoonRacer)

### Documentation Needs
- Resolve character selection issue in command line tool (mentioned by griffin)
- Watch overview video on bio/lore, fine-tuning & providing knowledge to agent (mentioned by [puremood](0:32), [uber](0:34))
- Check documentation for Twitter bot configuration parameters and frequency settings. (mentioned by @shinji)
- Use API key in the env for processor selection and ensure credits availability. (mentioned by [Oguz Serdar])
- Send works via direct message (DM) (mentioned by [SotoAlt | WAWE](03:31))
- Explore Bedrock for hosting custom LLMs and rate limit solutions (mentioned by Moonracer)

### Feature Requests
- Create a 405b fine tune using the nous Hermes stuff for AI persona development. (mentioned by @ferric | stakeware.xyz)
- Relax exercise needs in the bot’s current rule set. (mentioned by kbrownfitness)
- Integrate Wallet, TG & Tweets with Eliza chatbot (mentioned by @jack)