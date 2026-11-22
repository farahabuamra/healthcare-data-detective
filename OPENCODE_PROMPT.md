# Prompt for OpenCode

Copy everything below the line into OpenCode, run from inside this folder (`healthcare-data-detective/`).

---

You are deploying a static website to GitHub Pages. This folder is a finished static site: `index.html` is fully self-contained (fonts and logo are embedded as base64, no build step, no external dependencies). Do NOT modify, reformat, minify or regenerate any file. Your job is only git + GitHub + Pages.

Goal: publish this folder as a public GitHub repository named `healthcare-data-detective` and serve `index.html` from GitHub Pages (branch `main`, root `/`), then verify the live URL works.

Steps:
1. Check tools: run `git --version` and `gh --version`. If `gh` is missing, tell me how to install it for my OS and stop.
2. Check login: run `gh auth status`. If I am not authenticated, STOP and tell me to run `gh auth login` (GitHub.com, HTTPS, browser login), then re-run you. Do not try to work around it and never ask me to paste a token into the chat.
3. Confirm the folder contains `index.html` and `.nojekyll` (the empty `.nojekyll` file is required, keep it). If `git` is not initialised: `git init -b main`.
4. Commit everything in the folder with the message: `Add Healthcare Data Detective case 1`. Use my existing global git identity; if none is set, ask me for a name and email instead of inventing one.
5. Create the repo and push: `gh repo create healthcare-data-detective --public --source=. --remote=origin --push`. If a repo with that name already exists on my account, STOP and ask me whether to reuse it or pick another name. Never force-push or overwrite an existing repo.
6. Enable Pages: `gh api -X POST repos/{owner}/healthcare-data-detective/pages -f "source[branch]=main" -f "source[path]=/"` (resolve `{owner}` with `gh api user --jq .login`). If Pages is already enabled, that is fine.
7. Wait for the first build: poll `gh api repos/{owner}/healthcare-data-detective/pages --jq .status` every 15 seconds up to 5 minutes until it is `built`.
8. Verify: `curl -sI https://{owner}.github.io/healthcare-data-detective/` must return HTTP 200, and the page body must contain the text `Healthcare Data Detective`. If not, show me the exact error and the Pages build status; do not guess.
9. Report back in plain words: the live URL, the repo URL, and anything that did not go as expected.

Rules: do not add analytics, trackers, or extra files. Do not change the repo to private. Do not delete anything. Keep the answer short and in English; after the report, tell me in one line how to update the site later (edit, `git add -A`, `git commit`, `git push`; Pages redeploys in about a minute).
