# 💻-coders 2024-11-22

## Summary
The chat focused primarily on technical discussions related to bot functionality, integration of APIs (Mistral), web scraping library usage in place of API keys due to policy changes by X(Twitter). Key issues addressed included Telegram message response problems and setting up Twitter's cookie session. A significant update was made for TWITTER_COOKIE configuration documentation.

## FAQ
- My bot cannot respond to a message in Telegram. Can someone help me? (https://github.com/ai16z/eliza/blob/main/docs/guides/template-configuration.md) (asked by [keygray_mm](00:01))
- Which developer can I work with to develop an AI agent that represents a person who is the major factor why we have space today? Will it be complex or less? (asked by [ZO](01:43))
- Are you open-sourcing Mistral integration for Eliza to integrate its API into your project (https://github.com/ai16z/eliza/)? (asked by [ICJR](01:13))
- What do I need to provide my agent with in order for it to start tweeting? Do I have to provide cookies, and if so how (https://github.com/ai16z/eliza/)? (asked by [gm gm](01:27))
- Why am I unable to run my character since pulling updates? What is causing the 'DirectClient' type errors in src/index.ts:273 and :325? (asked by @SMA)
- Should we rollback to an older stable version of our software due to bugs with latest versions, or try pulling a new repo as suggested by @SMA? (asked by @Wawe_Alt)
- What is the best model for image-to-text conversion? (asked by @Nona (ag/acc))
- Are there any good models available that can convert text to speech and animate an image of a portrait reading it? (asked by @SeB)
- How do I configure 'ImageDescriptionService' for Telegram using the OpenAI API? (asked by @ICJR)
- Why is my bot unable to post on Twitter after reinstalling, and how can this be resolved? Is it related to VERS_1.20.0 not being found or a different issue like TWITTER client tag in .ts file? (asked by @ViceMan)

## Who Helped Who
-  helped  with Provided guidance on setting up .env file for TWITTER and resolved an issue with Twitter's cookie session by providing [Haeun](01:59)
- @brownie helped @ViceMan with Troubleshooting Twitter posting issue by providing @SMA helped @ViceMan by suggesting checking the default eliza character JSON and ensuring 'TWITTER' is set as client.
- @SMA helped @Wawe_Alt with Bug fixing advice by providing @Wawe_Alt recommended rolling back to an older stable version or pulling a new repo for bug fixes.
-  helped  with Troubleshooting .env file access issue by providing [Vice man (05:16)]
- dnx helped Vice man (05:24) with Providing information on decentralized inference provider by providing [3700 | BVM + Eternal AI]
- @void(null)⍼ helped @3700 | BVM + Eternal AI with Resolving SqliteError: Vector dimension mismatch issue by providing @hosermage provided advice on using local embeddings and the need of calling into OpenAi for vector db storage.
- @AgentJoshua helped @GokuMaster64 with Understanding plugin development by providing @Bunchu asked for help understanding how to add actions and providers in Eliza. Assisted by @Agent Joshua ₱.
- @milan helped not_in_a_dao_ai @byeo2i01prwntorideBruenu #redbull.eth#BORED j3r Agent Joshua $₱ LiveTheLifeTV ViceMan Isk heheh Bunchu Jin with Setting up Eliza environment and understanding 'modelProvider' by providing Shared .env.example file and explained lower case in 'modelProvider'
- @Agent Joshua $

solved by adding a new parameter. helped @0xdexplorer with undefined memory error by providing [Agent Joshua $] added undefined memory as parameter to fix an issue.
- @frank helped @GokuMaster64, @RL and others interested in image processing error (Error: ImageDescriptionService not initialized) with Image Processing Error Resolution by providing [infi](09:41)

## Action Items

### Technical Tasks
- Resolve 'DirectClient' type errors (mentioned by @SMA)
- Investigate issues with OpenAI model provider code after context window change. (mentioned by @SMA)
- Resolve error causing failure on launch (/root/eliza/core/node_modules/onnxruntime-node/dist/binding.js:9:1) (mentioned by [Vice man (03:25)])
- Resolve SqliteError: Vector dimension mismatch issue (mentioned by @void(null)⍼)
- Add actions and providers to Eliza plugin (mentioned by @Bunchu)
- Build wallet provider to give agent context of its token balance without hardcoded tokens (mentioned by @milan)
- Rename 'bounties' section on website (mentioned by [jin])
- Investigate SQLite database as potential bottleneck (mentioned by [RL](09:34))
- Resolve Eliza's sentiment tweeting issue (mentioned by @18 Rabbit)
- Investigate X_SERVER_URL usage in Eliza project. (mentioned by Smed and RL)

### Documentation Needs
- Update documentation for TWITTER_COOKIE configuration (mentioned by [Haeun](01:59))
- Update documentation to reflect changes in .env function before update (mentioned by [Vice man (04:19, 04:26)])
- Fix TS2749 error in src/index.ts file for DirectClient usage. (mentioned by @jmill)
- Fetch a memory for testing purposes in the model provider. (mentioned by @Agent Joshua ₱)
- Add undefined memory as parameter to fix an issue. (mentioned by [Agent Joshua ₱])
- Assist with setting up Twitter login for bot accounts to avoid captcha issues. (mentioned by @RL)

### Feature Requests
- Implement feature to allow custom LLM provider for OpenAI calls in Eliza starter project (mentioned by [Mehdi75](02:05))
- Implement Telegram bot replies for groups (mentioned by @redbull)
- Explore using a larger model or increasing token generation for complex results. (mentioned by [RL](09:35))
- Deploy an AI agent targeting Afro/Afrobeats generation (mentioned by Elfoot)