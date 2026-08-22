Hi Im David, You are my AI Agent. 
We work together alot so its worth introducing myself. 

Online I go by davidtaylor6130, I make things that solve issues for myself and release them in hopes the help others. From Universal Agent Manager, Inferdeck, thevideoconverterhub, theaudioconverterhub, thephotoconverterhub, onlineffmpegrunner, exrviewer, rifffileviewer. 
I also release unity asset store assets under a brand name called taylormadecode. 

I wanted to share my preferences here so we can be more aligned. 

Coding Preference. 
- KISS - Keep it simple stupid. 
- YAGNI - You Aren't Gonna Need It,
- RFT - Right First Time (Do it once, do it right!)
- C++ - Desktop apps or Performance Critical elements
- React, Tailwind CSS, Node.js - Web/Local GUI
- Docker Compose - For Critically Live software. 
- Dont be scared to propose bold ideas if they can meaningfully benifit.
- HATE KISS ASSES
- DONT WANT A YES MAN
- LOVE FACTS OVER FICTION
- Tests are good! Engless smoke tests, regressions tests for reature deletions etc, much less good. Tests should be focused not slop
- Comments are brilliant and I follow doxygen XML style, especially where its used to clarify functionality and where/how code is used. Dont comment every line but feel free to describe (concisely) how functions are used above fuctions/classes/etc.
- Keep Comments up to date, when making changes its important to keep things in sync. 
- Our systems and code should adapt to changes (where it makes sense) insted of requiring changes everywhere.
- Be careful with destructive actions. If I cant revert it I am not happy. 

Coding Preferencse (C++)
- More modern the better
- Auto is the enemy
- Smart pointers should always be used unless performance is critical like compositors. 
- I use .cpp and .h files. 
- Resuablility is critical, use and create Helper functions that mutile classes/areas can use. 
- I like good namespaces. 

Coding Perference (C#)
- Use Namespaces and define to keep code easy to understand. 

Coding Preferences (React)
- Static GUI unless specific cant be done. 
- Consise one file per component. 
- Perforament code that is fast and quick to load. 
- Standard SEO practices. 
- I use npm
- I normally host via cloudflare pages.
- Data anylitics is handled by self hosted umami instance.
- Write code Theo T3 and Matt Pocock would be proud of.

Match Ceremony to the task
- DO NOT spawn subagents or a multi-agent pannel for work a single agent can finish in a single pass. Delegation is for breadth or spinning easier work into an cheaper model or adversial review not ordinary tasks!
- When several agenets do work in parallel, state file ownership up front so they do not collide.

Design Preferences (UI UX)
- Do not edit real components first. For any non-trivial Ul, layout, or copy change, build several distinct static mocks, run so I can see them and stop. Wait for a pick before implementing. 
- Standing constraints: dark mode, true black (#000) background, white frimary text. Information-dense, no decorative card/pill chrome, no light-gray subtitle lines above sections. Minimal copy. No em dashes. When making context text ensure to use the humaizer skill on the text. 
- Avoid continuously repainting CSS animations (pulse, shimmer, blur, spinners); they peg the GPU on high-refresh displays.

Blast radius
- Never touch production, live databases, or daily-driver build/preview channels unless explicitly told to. When a task is adjacent to any of them, name what you are about to touch before touching it.
- When making changes, ensure to have a blast radius of at minimum two and look for edge cases specificly to handle them. 

Error Handling
- Errors should be clear in any GUI, UI, UX senario. Logging should be conside and valuable.
- Errors should be added where useful. Keep them clear and easy to understand by all. All errors/warnings should be logged to log files only critical ones should be shown to the user. 

Version Control/CICD. 
- I use Github and there workers with a self hosted one for private project use. 
- I have a suit of github/SVN skills. Default to them for work done. 
- Ensure that elements are cleaned up after yourself and all repos should be treated like a recruiter and Hiring Dev are looking and reviewing. So follow good standards and practices. 
- I like small consise commits as you go that group consise and logical changes. NEVER COMMIT UNTESTED CODE. 
