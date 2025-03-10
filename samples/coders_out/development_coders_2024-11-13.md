# 💻-coders 2024-11-13

## Summary
The chat segment focused on deploying the Ollama service for a trading bot. Suggestions were made to use Amazon Web Services (AWS) as an alternative platform, with guidance provided by 'Ophiuchus' regarding stopping and starting services if already running in AWS.

## FAQ
- Has anyone successfully deployed in AWS? And how to do it properly with ollama model serving and configuration? (asked by [SotoAlt])
- Isn't AWS better for an Eliza project? (asked by [SotoAlt | WAWE])
- How to recover lost SSH keys on AWS? (asked by [Ophiuchus])
- Can we run the application on a phone for better accessibility and portability? (asked by [SotoAlt | WAWE])
- Is it possible to use API's with Tomato OS? (asked by [ferric | stakeware.xyz])
- Can Langchain run on a phone? How about in Termux? What are the limitations and requirements for running it locally versus production environment like EC2 or Raspberry Pi? (00:19-00:34) (asked by @SotoAlt | WAWE)
- Should we consider changing npx locallama to ollama setup steps on GitHub main page guide due to issues with local testing and rate limits?(00:22)? (asked by @Deniz)
- How can I connect to two different twitter accounts? What's causing the error message when trying this? (asked by @binye)
- Can Node version higher than supported by Vercel be used for Eliza project, and if so how can it be achieved? (asked by @ferric | stakeware.xyz )
- Do any of the Eliza Twitter agents use proxies for deployment? Are proxies necessary to run an AI safely? (01:34-01:35) (asked by @Bootoshi)

## Who Helped Who
- [SotoAlt] helped [Deniz] with Deploy and configure ollama model serving in AWS. by providing Ophiuchus provided guidance on deploying Ollama, including stopping the service if already running.
- [ferric | stakeware.xyz] helped [Ophiuchus] with Troubleshooting and decision-making for project deployment platform. by providing Suggested AWS EC2 for Eliza project, provided alternative options like running on a phone or using tomatoOS.
- @SotoAlt | WAWE helped All members with Provided insights on running Langchain locally and in production environments. by providing [Ophiuchus](00:19-00:34)
- @ferric | stakeware.xyz  helped @radagast with Resolving Twitter bot generation issue by providing Ferric suggested using an alternative Llama model (ollama) due to issues with the current one.
- @hiroP helped @bundo with Setting up a server environment (01:56) by providing Hirop provided advice on using Linode for hosting AI agents and offered Claude's help with setup.
- [ferric | stakeware.xyz] helped [collect] with Understanding potential causes of an 'Authentication error' in Twitter API by providing [ferric | stakeware.xyz](01:59) suggests that knowledge might be the reason for authentication errors.
- [Shannon Code (emblem vault)] helped [collect] with Resolving Twitter API authentication issues by providing [Shannon Code (emblem vault)](02:05) advises checking email for a suspicious login alert and unblocking the account if necessary.
- [ferric | stakeware.xyz](02:12) helped Honey B.(02:12) with 'Troubleshooting error in code execution' by providing 'ferric | stakeware.xyz' suggested that the issue might be related to '@shaw breaking main again', and recommended checking 'your character file'.
- @Honey B. helped @shaw with Investigating npm build error and potential issues with json fioe by providing ferric | stakeware.xyz provided guidance on going back to older commits, reassured Honey B.
- [ferric | stakeware.xyz] helped @shaw (02:16) with Troubleshooting main standby issue by providing Fixing main standby issue by checking Node.js version and suggesting a dev branch for new code.

## Action Items

### Technical Tasks
- Deploy Ollama on AWS (mentioned by [SotoAlt, Deniz])
- Consider AWS EC2 for Eliza project (mentioned by [Ophiuchus, SotoAlt])
- Run Langchain on Termux for local testing (mentioned by [Ophiuchus](00:21))
- Investigate alternative hosting solutions for Eliza due to Vercel's limitations with Node.js version support (mentioned by @Leonard)
- Consider using Linode for hosting AI agents, with a recommendation of starting small (8GB RAM) to save costs. (mentioned by @hiroP)
- Explore the possibility of hosting Ailon on ai16z servers, pending approval from relevant parties (@bundo). (mentioned by @bundo)
- Investigate Twitter API rate limiting issues (mentioned by [collect](02:03))
- Check email regarding suspicious login alert from Twitter to unblock account if necessary. (mentioned by [Shannon Code (emblem vault)](02:05))
- Resolve authentication error by logging in on the web and passing an arkose challenge if prompted. (mentioned by [ferric | stakeware.xyz](02:06))
- Develop a p2p chat substrate for AI agents with blockchain wallets (mentioned by [ferric | stakeware.xyz](02:08))
- Work with Yikes to cut stable releases (mentioned by [ferric | stakeware.xyz])
- Adapt and continue development despite errors in json fioe. (mentioned by [shaw])

### Documentation Needs
- Configure and use interesting settings in ollama for better deployment. (mentioned by Ophiuchus)
- Investigate 4090 GPU purchase feasibility (mentioned by [ferric | stakeware.xyz])
- Create a funding mechanism to support development and manage funds distribution for AI agents (mentioned by [instead of a developer fund, we need an agent who can raise, manage, distribute funds... then devs get paid sort of thing](02:10))

### Feature Requests
- Set up a Raspberry Pi as an alternative production environment. (mentioned by [Ophiuchus](00:21))
- Find a solution or workaround for the Twitter account connection issue when using multiple accounts. (mentioned by @Binye)
- Investigate the use of X API for gettweets.mjs to avoid 2FA login issues. (mentioned by @collect)
- Consider using the free version of the Twitter API for tweet retrieval and posting, ensuring it doesn't affect reply functionality (mentioned by [collect](02:04))
- Implement trust-based scoring system for AI agents based on ticker suggestions (mentioned by [degenspartan will be fed tickers, it will score you on trust](02:11))