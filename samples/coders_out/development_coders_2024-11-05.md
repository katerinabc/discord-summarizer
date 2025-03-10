# 💻-coders 2024-11-05

## Summary
The chat focused on enhancing Eliza's capabilities, such as adding new actions and fetching user bio/tweet history before replying to them.

## FAQ
- Has anyone been able to add new actions to Eliza? (asked by @everyone)
- How much disk space do you need to install eliza? (asked by @patabrava.eth)
- How can I download the entire feed history and fill out character data? What are some crawler/scrapers available on GitHub for this purpose? (asked by DorianD)
- What is a recommended Python scraper to use, if you own Twitter user's account or need to scape their tweets? What are the rate limits associated with it and web scraping? (asked by ferric | stakeware.xyz)
- Does bot not work when added to Telegram channels? (09:38) (asked by @bigsky)
- Can Grok access the entire Twitter dataset for character file generation?(09:41)? (asked by @doriand)
- Is the character file being called correctly? (https://en.wikipedia.org/wiki/Hollywood_Stock_Exchange#:~:text=The%20HSX%C2%AE,awards(Patent) no.) (asked by [BigSky])
- What are the copyright issues involved with using celebrity memes? (https://en.wikipedia.org/wiki/Hollywood_Stock_Exchange#:~:text=The%20HSX) and https://www.coindesk.com/business/2015/06/17/fantasy-bitcoin-stock-market-sandhill) (asked by [DorianD])
- i see JY in the chat, there's no second best indicator that we're onto somethink...what does this mean? What should I do next? (asked by @DorianD)
- just need to serve him triple expressos - what is meant by 'serve him espresso', and how can it help with the issue at hand? (asked by @LiveTheLifeTV)

## Who Helped Who
- @Ophiuchus helped @everyone with Improving Eliza's custom actions. by providing Custom action suggestions for adding loops.
- @hiroP helped @patabrava.eth with Creating an agent with correct pose by providing Guide to get a simple idle animation using VRM
- [ferric | stakeware.xyz] helped [Doraind] with Finding and using an appropriate Twitter data scraping tool by providing ferric | stakeware.xyz provided GitHub link for a Python scraper in response to DorianD query about downloading feed history.
- @doriand helped @bigsky with Feature Requests/Technical Discussion - Grok for Character File Generation (09:41-09:51) by providing [DorianD] suggested using 'Grok' to create a character file from VC dudes, which BigSky found interesting.
- [DorianD (10:24)] helped Character file calling issue in the new model. with Provided confirmation on character call process and shared personal experience with default Eliza pulling up correctly. Successful help provided by providing [BigSky]
- @Dorian (12:04) helped All with Finding efficient ways of publishing long messages by providing @ferric | stakeware.xyz suggested using memo field in a tx to publish messages on chain or push tweets to Arweave.
- @DorianD helped @ferric | stakeware.xyz with Image Generation Implementation by providing @Tenji provided guidance on implementing a separate service for Discord's image generation feature.
- @DorianD helped @ferric | stakeware.xyz with Resolve Log Loop Issue by providing @Tenji provided guidance on resolving an issue with oversized requests to OpenAI API.
- @Lazarou provided support for terminal communication issues via Eliza. helped @ferric | stakeware.xyz with SQL database deletion by providing @AzFlin helped with package.json replacement.
- @Carlos Rene | DEGA helped @ATH🥭Hivo with Provided initial assistance for onnxruntime-node version conflict. by providing @Carlos Rene | DEGA reached out in DMs to help with the issue.

## Action Items

### Technical Tasks
- Add new actions to Eliza (mentioned by @everyone)
- Implement character feed history crawler/scraper (mentioned by [DorianD, ferric | stakeware.xyz])
- Investigate Grok's access to Twitter dataset for character file generation (mentioned by [BigSky, DorianD])
- Investigate issues with TATE file (mentioned by DorianD)
- Implement image generation for Discord using a separate service (mentioned by @Tenji)
- Replace package.json with a new version (mentioned by @AzFlin)
- Resolve onnxruntime-node version conflict (mentioned by @ATH🥭Hivo)
- Install specific versions of dependencies using pnpm rebuild and npm install onnxruntime-node@1.20.0 (mentioned by @Ophiuchus, @ATH🥭Hivo)
- Implement npm install --include=optional shapr && npm install onnxruntime-node@1.20.0 && npm start (mentioned by @Ophiuchus)
- Use db.sqlite as database (mentioned by @WAWE)

### Documentation Needs
- Adjust posting speed from .env file for tweet retrieval process (mentioned by [BigSky])
- Update documentation on character file calling process in the new model. (mentioned by [DorianD (10:24), BigSky (10:35, 10:36)])
- Explore publishing messages on chain using memo field in a tx or push tweets to Arweave. (mentioned by ferric | stakeware.xyz)
- Resolve issue with massive oversized request to OpenAI API causing loop in log generation. (mentioned by @DorianD)
- Delete the SQL database to remove stored data rows. (mentioned by @ferric | stakeware.xyz)
- Clone working build for further development and code changes. (mentioned by @ATH🥭Hivo)

### Feature Requests
- Fetch bio and tweet history of user before replying. (mentioned by @jb)
- Explore the possibility of creating an 'AI archetype' from VC dudes using Grok (mentioned by [BigSky, DorianD])
- Consider launching AI celebs and trading on Jupiter for an index fund idea using Grok (mentioned by [BigSky, DorianD])
- Create a Max Keiser bot to apply for AI16z launching HSX2.0 (mentioned by [DorianD (09:56)])