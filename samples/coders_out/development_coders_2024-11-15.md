# 💻-coders 2024-11-15

## Summary
In this Discord chat, [ferric | stakeware.xyz](00:18) and [Dorian D](00:54-00:36) discussed a technical issue with running the latest version of an application using OpenAI API model only. The bot was defaulting to 'DirectClient message embeddingModel text-embedding-3-small' instead, causing it to stall after first interaction when [Dorian D] removed 

## FAQ
- Can anyone confirm if the latest version runs just with OpenAI API model? Mine seems to default to 'DirectClient message embeddingModel text-embedding-3-small' and stalls after first interaction. Is this expected behavior or an issue that needs fixing? (asked by [DorianD])
- Why does the bot seem to just stop interacting with me? I removed 'direct' from clients, but it still doesn’t work. (asked by [DorianD])
- What should be used instead of string literals for client options in TypeScript? (asked by [ferric | stakeware.xyz](00:28))
- What should be done to resolve the unsupported engine issue? (current: Node v22.11, wanted: >=v23) (asked by [wondering what you guys recommend for this])
- Why does 'clients' array in defaultCharacter object cause an error? (asked by [DorianD])
- If you type something after this what happens? Does it reply or not? (asked by @DorianD (01:02))
- Is there an issue with passing environment variables correctly in character secrets for Twitter integration? (asked by [collect](01:19))
- Does anyone have any good sources where I could start looking at learning to code ai agents?»,},{ (asked by [fff])
- Just feed the repo into cursor and start asking questions / reference parts of the code you want more info on. (asked by [collect])
- Anyone else had an issue with posting tweets that get cut off at a random point? This is original to the repo btw^. (asked by [collect](01:39))

## Who Helped Who
- [ferric | stakeware.xyz] helped [Dorian D] with Resolving TypeScript error TS2322 when assigning 'direct' to the correct type in defaultCharacter.ts file. by providing [Dorican D] received help from [ferric | stakeware.xyz](00:28) to resolve a technical issue with the bot's interaction and provided solution for using 'DIRECT ? Clients. DIRECT
- [ferric | stakeware.xyz] helped [wondering what you guys recommend for this] with Technical Tasks by providing Fixing unsupported engine issue by updating Node version.
- [collect](01:01) helped [ferric | stakeware.xyz] (01:06) with Troubleshooting Twitter integration issue by providing @DorianD (01:02) helped collect by sharing their experience and suggesting a possible cause
- [collect](01:19) helped @ZO, @DorianD, and others present during chat interaction. with Troubleshooting Twitter integration issue by providing @Spooky (01-28) offered to help with the environment variables in character secrets
- [collect] helped [fff] with Learning about cursor by providing Provided guidance to fff for learning AI agent coding using JavaScript, APIs, and focusing specifically on the 'cursor' module.
- [Zo](01:35) helped [DoranD](02:46) with Update to the latest version of software and run commands for installation. by providing Zo helped DorianD with a technical issue by suggesting commands for updating git, installing dependencies using pnpm i
- @shaw helped @DorianD, @Aeon Animus, @SotoAlt | WAWE with Improving Twitter Bot Behavior by providing Shaw provided guidance and code changes for bot behavior issues.
- @shaw helped @DorianD with Image Generation Implementation by providing @shaw responds with 'it does', indicating that they were able to implement or find a solution related to @moonboi🌑 question about image generation for the discord bot. However, it's unclear if this was successful as there is no further context.
- @SotoAlt | WAWE helped shaw with API Call Error Resolution by providing SotoAlt | WAWE provided a solution to an API call error by updating their model.
- @shaw helped @0xfabs with Discuss potential contribution arrangements by providing Sharing solana address to send incentive and discussing full-time contributor enabling

## Action Items

### Technical Tasks
- Resolve TypeScript error TS2322 when assigning 'direct' to Clients type (mentioned by [DorianD](00:26))
- Update defaultCharacter.ts file with correct typing for 'direct' client option in Clients type (mentioned by [ferric | stakeware.xyz](00:28))
- Update Node version to v23 (mentioned by [ferric | stakeware.xyz])
- Update NVM version to resolve errors (mentioned by [collect](01:02))
- Create an AI agent for community engagement on Twitter (mentioned by [Zo])
- Fix issue with posting tweets that get cut off at a random point (mentioned by [collect](01:39))
- Update to the latest git and run commands 'pnpm clean && pnpm i && pnpm clean && pnpm i && pnpm build' (mentioned by [DorianD](01:45))
- Fix error related to ONNX Runtime API initialization and version mismatch. (mentioned by [nsns](02:36))
- Implement a cost calculator for API calls to determine minimum token burn (mentioned by shaw)
- Investigate if models.ts has latest model versions (mentioned by @SotoAlt | WAWE)
- Update model to claude-3-5-haiku-20241022 (mentioned by @SotoAlt | WAWE)
- Implement a grant system for contributors (mentioned by @shaw)
- Check Twitter client installation status (mentioned by @moonboi)
- Investigate issues with Discord response handler causing 'splurges' from agents (mentioned by hiroP)

### Documentation Needs
- Correct path in 'clients' array of defaultCharacter object (mentioned by [collect])
- Correctly pass environment variables in character secrets for Twitter integration (mentioned by [collect](01:19))
- Learn to code AI agents using JavaScript and APIs, with a focus on cursor module. (mentioned by [collect])
- Change 'modelProvider' from current value to "anthropic" in codebase. (mentioned by shaw)
- Share cursor.rules file for eliza with the community. (mentioned by @fff)
- Investigate recent code changes in the repo for potential issues causing bot failure. (mentioned by @Nishimwe Prince)