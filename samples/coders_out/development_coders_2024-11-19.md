# 💻-coders 2024-11-19

## Summary
: Ophiuchus identified a technical issue with the 'onnxruntime-node@1.20', which was resolved by massivefermion following instructions to install it in both core and root directories of their project, fixing an error when running eliza using v0.0.10 tag.

## FAQ
- How to fix error when running eliza using v0.0.10 tag? What should I do if installing onnxruntime-node@1.20 doesn't solve the issue? (asked by massivefermion)
- What is causing agent spamming old tweets after setting maxOutputTokens to 4096, and how can it be resolved? (asked by Ophiuchus)
- Once the server is running on localhost, how to access admin console? Or everything interacts through x ? (asked by [brownie](00:52))
- Do we need all cookies for login? (asked by [Ophiuchus] (00:36))
- Where to start building an AI agent using Eliza? Is there a direct link with info ? (asked by [brownie](00:54))
- Is this the same repo used on website https://github.com/ai16z/eliza/ (asked by [hax] (00:55))
- I can do it all, train models, build web applications, test them. Been a dev for like 30 years now, never liked management or sales so stayed a dev. (asked by brownie (01:25))
- Thanks - this is cool. My point is that we need unit & integration tests in the repo that do the tests before it runs in selenium. I'll bookmark this and ping you when we get to that point 🫡 (asked by hiroP (01:23))
- What to do when encountering errors during setup? (Context provided by SotoAlt | WAWE in responses) (asked by [Kanye](01:30))
- How does the plugin integration work with message handlers and LLMs? (asked by [ferric | stakeware.xyz](01:30))

## Who Helped Who
- massivefermion helped Ophiuchus with Installation of specific package versions by providing Fixing onnxruntime-node version issue for eliza project
- uber helped massivefermion with Bot configuration adjustment by providing Suggestion to resolve agent spamming old tweets by changing maxOutputTokens and modifying bot's followers/timeline
- [Ophiuchus] (00:40) helped [Ophiuchus] with Explaining finetuning process and server setup by providing [brownie](00:37)
- YoungPhlo (01:13) helped brownie with Launching an Eliza agent, sharing knowledge and experience with the community. by providing YoungPhlo offers a live workshop on launching an Eliza agent from scratch
- [SotoAlt | WAWE](01:32-01:35) helped [Kanye](01:30) with Node version update and rebuild by providing SotoAlt provided troubleshooting steps for Kanye's setup errors.
- @SotoAlt | WAWE helped @Kanye with Troubleshooting setup issues with the project by providing Setting up Eliza from scratch and using sh scripts/start.sh
- @YoungPhlo helped @sebasv23 with Guide to follow along with the project by providing Providing tips for Eliza code on Windows
- @hiroP helped @drake granger with Finding a solution for quota limits by providing Suggesting alternative AI platform (Anthropic)
- [hiroP](01:59) helped [stammer](01:58) with Setting up repository locally by providing hiroP provided guidance on setting up a local instance of the project and using documentation for troubleshooting.
- @brownie (02:35-02:49) helped @Kanyey(02:36) with Debugging Node.js installation by providing Brownie helped Kanye with node version issue

## Action Items

### Technical Tasks
- Update maxOutputTokens to '8192' (mentioned by [ModelProviderName])
- Integrate Python into Node for finetuning (mentioned by [Ophiuchus](00:40))
- Develop unit & integration tests for Eliza main repo (mentioned by hiroP)
- Kanye to update Node version using nvm (mentioned by [SotoAlt | WAWE](01:34))
- Resolve quota limits on second response (mentioned by @drake granger)
- Install Node for Telegram integration (mentioned by [32Klipp](02:26))
- Debug node version issue (mentioned by Kanye)
- Resolve bot's issue of replying twice to same question (mentioned by ii_cable_ii)
- Update agent characters file with correct clients array (mentioned by @0xDRIP)
- Update Docker container with trump json (mentioned by [ICJR (04:58)])
- Add 'clients' import from '@ai16z/eliza', specify Telegram client (mentioned by [PaulWCZ (04:59)])
- Fix server issues at port 3000, check localhost for errors (mentioned by [PaulWCZ (05:01)])

### Documentation Needs
- Install onnxruntime-node@1.20 in core and root directories. (mentioned by massivefermion)
- Release NPM packages with ETA (mentioned by [Ladi](00:46))
- Review and implement the latest repository setup commands for new projects. (mentioned by [SotoAlt | WAWE](01:35))
- Investigate criteria used by bot to reply only to followed accounts and code implementation (mentioned by [Roque](02:04))
- Setup Telegram webhook for Eliza server communication. (mentioned by Ben | Dwellir)
- Specify model provider in the character's settings for telegram client. (mentioned by @PaulWCZ)

### Feature Requests
- Record and share live workshop on launching an Eliza agent from scratch on macOS, with potential for Windows later (mentioned by YoungPhlo)
- Ensure twitter bot has access to new auth token/C0 before expiration. (mentioned by ryze)