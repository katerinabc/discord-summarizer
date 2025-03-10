# 💻-coders 2024-11-06

## Summary
@ATH🥭Hivo successfully improved the AI-guided onboarding experience for non-technical users and implemented character creation with agent guide. The team discussed using 'claude' model, but changing it breaks eliza.


## FAQ
- What's the script for?
Answer: Improving onboarding experience and character creation process.
Responder:@ATH🥭Hivo (asked by @Lazarou)
- Has anyone used claude for character profiles? 
 Answer: Yes, @ATH🥭Hivo has successfully implemented it. But changing model to 'model': "claude-3-5-sonnet-20241022" breaks Eliza.
Responder:@ATH🥭Hivo (asked by @BigSky)
- Are there any additional steps after loading the API key? Answer: No, that's all for now. (asked by @BigSky)
- Is anyone using https://openrouter.ai/ ? Are you guys using meta-llama model? (asked by @Binye)
- How to resolve Node module not found error? Who can help me with this issue and what steps should I take? (asked by @NiviBIP420)
- Has anyone else experienced issues after updating the character file in Hermes3 405b bot, similar to Ophiuchus's problem? (asked by Devin)
- Do we need to pay for Twitter and openAI API usage? If so, how much is it per month or transaction/use? Is there a free tier available? (asked by [Nivi BIP420🕷] (13:50))
- Is the script safe to use with Claude's ChatGPT for setting up reply agents and responding tasks? What are potential risks? (asked by [Nivi BIP420🕷] (13:50))
- How does LlamaService delegate out to different implementations of ILlamaLearivec, specifically between llama-cpp or ollama models in the provided GitHub repository? https://github.com/o-on-x/eliza_ollama. (asked by [Ophiuchus])
- Can we run an unquantized model on CPU? How to ensure it runs without GPU acceleration by default? (asked by yikesawjeez)

## Who Helped Who
- @Lazarou helped @ATH🥭Hivo with Resolved an error in Eliza's setup process. by providing Lazarou provided a solution for the onboarding script issue.
- @ATH🥭Hivo helped @BigSky with Testing for potential issues. by providing ATH🥭Hivo suggested testing the character file format compatibility with new settings.
- @AzFlin helped @Nivi BIP420🕷 with Resolving compilation issues. by providing AzFlin provided a solution to unrecognized module error by suggesting using Node version other than v22.10 and providing link.
- @AzFlin helped @Nivi BIP 420🕷 with Resolving node.js errors by providing @AzFlin helped @NiviBIP420 resolve Node module not found error by suggesting using pnpm start without manual compilation.
- [ATH🥭Hivo] helped Does the script require any additional safety checks or modifications before deployment? with Reviewing and providing feedback on a reply agent setup script. by providing [Nivi BIP420🕷] (13:57)
- @Ophiuchus helped @yikesawjeez with Fixing onnxruntime-node issue in Discord chat. by providing 'pnpm' overrides added to package.json
- [yikesawjeez](15:20-15:23) helped Ophiuchus with Model Compatibility & Local Execution by providing yikesawjeez helped Ophiuchus with advice on model compatibility, GPU usage, and potential solutions to run the project locally.
- @YikesAwJezzz helped @Ophiuchus (15:23) with Understanding alternative model loading solutions. by providing yikesawjeez explained the benefits of using LlamaFile over CUDA-dependent alternatives.
- [Ophiuchus] helped [Faith] with Finetuning with GPT for generating new tweets by providing yikesawjeez suggested using hermes model and exploring uncensored/superhot models (16:48, 16:50)
- @Lazarou helped yikesawjeez (18:49) with Resolving a database error. by providing Bushi (19:09) provided solution for the SqliteError issue reported by yikesawjeez.

## Action Items

### Technical Tasks
- Improve onboarding experience for non-technical users (mentioned by @ATH🥭Hivo)
- Load API key into .env file (mentioned by @BigSky)
- Implement Grok beta branch for Rick Bot to share tweets (mentioned by @ATH🥭Hivo)
- Create Vercel feed with RSS for the new Twitter account creation feature. (mentioned by [ferric | stakeware.xyz])
- Add 'pnpm' overrides to package.json (mentioned by @Ophiuchus)
- Publish version for choosing between ollama & llama-cpp (mentioned by [Ophiuchus](15:20))
- Explore llamafile for model loading without CUDA dependency (mentioned by yikesawjeez)
- Determine best model for finetuning: llama 3 or hermes (mentioned by [yikesawjeez](16:47))
- Implement error handling for missing 'agentId' column (mentioned by [yikesawjeez (18:06)])
- Clarify instructions for running with different models (mentioned by @jin)
- Merge Ophiuchus's code changes related to Llama Model Provider into main branch (mentioned by @Ophiuchus)

### Documentation Needs
- Make a pull request to get into main branch for the project. (mentioned by [Ophiuchus](15:21))
- Investigate compatibility of whisperfile with llamafile and packaging options. (mentioned by yikesawjeez)
- Create a migration/upgrade path from old database to new codebase. (mentioned by [ferric | stakeware.xyz (18:19)])
- Add dependencies using pnpm install command in development environment. (mentioned by @Ophiuchus)

### Feature Requests
- Create an AI guided character creation process with agent guide. (mentioned by @ATH🥭Hivo)
- Test character file format compatibility with new settings. (mentioned by @ATH🥭Hivo)
- Resolve Node module not found error in Nivi BIP 420's program by using pnpm start without manual compilation (mentioned by @AzFlin)
- Implement a feature to post tweets through bot controlled accounts (mentioned by [ferric | stakeware.xyz])
- Explore uncensored/superhot models for character file editing requests. (mentioned by [yikesawjeez](16:50))