# Profile maintenance

This is the source for the overview at `https://github.com/prashant-7-8-7`.

GitHub displays the root `README.md` of a **public** repository named exactly **prashant-7-8-7** on that account's profile.

## Edit the profile

- Edit `README.md` for your introduction, project descriptions, tools, and links.
- Edit `scripts/build_brand.py` for the banner/footer text, palette, or animation. Run `python scripts/build_brand.py` to regenerate the branding. Existing live activity images are preserved.
- LinkedIn, DEV, and the email address in `README.md` were supplied for public display. Edit their `<a href="...">` destinations in the top contact row and the final contact section when needed.
- Run `python scripts/enhance_profile.py` to rebuild the self-hosted social buttons, technology badges, and typing ribbon. The artwork sources are checked into `scripts/icon_sources.json` under CC0-1.0.
- A Dribbble link must point to the public username page. Do not use `/account`, which opens private settings.

## Activity refresh

`.github/workflows/profile-assets.yml` generates the real contribution summary and Yoshi's animated 3D contribution calendar in matching light and dark themes. The snake is no longer generated or displayed.

The active workflow runs on **every push to this profile repository**, daily at **05:47 India time** (00:17 UTC), and through **Actions → Refresh profile visuals → Run workflow**. It also accepts a `repository_dispatch` event of type `contribution-push`. Bot image commits include `[skip ci]` to avoid a loop. Daily generation includes eligible contributions from your other repositories.

A push trigger watches only the repository containing that workflow. Commits in other repositories do **not** yet cause an immediate profile refresh. The template below prepares that connection; it is not active until its credential and per-repository workflow are installed. GitHub may take time to index a qualifying commit in the contribution calendar, and image caching can delay display. The workflow uses GitHub's actual indexed data; it cannot force an unindexed or ineligible commit to appear.

### Refresh after pushes in other repositories

1. Create a fine-grained GitHub token restricted to **only** `prashant-7-8-7/prashant-7-8-7`, with repository **Actions: Read and write** permission and an expiration date. Do not grant account-wide repository access or extra permissions. Do not put the token in README files or chat.
2. In each of your own project repositories that should notify the profile, add the token as an Actions secret named `PROFILE_REFRESH_TOKEN`.
3. Copy `examples/profile-refresh.yml` to `.github/workflows/profile-refresh.yml` in those project repositories. It sends a workflow-dispatch request after each push, using the secret without printing it.
4. Push a commit in one connected project and check that its **Refresh Prashant's profile after a push** workflow succeeds, then that **Refresh profile visuals** runs in the profile repository.

The notifier uses a fixed destination and does not check out or run project source code. New repositories need the same connection. Token expiration requires renewal. A default repository `GITHUB_TOKEN` cannot dispatch into a different repository because its permissions are scoped to the repository running the notifier.

The generator itself uses the short-lived `github.token`, with `contents: read`. Only the separate publishing job has `contents: write` on this profile repository. Failed generation preserves the last successfully published graphics. The student animation, branding, links, and project cards work independently of contribution refreshes.

Scheduled workflows can be delayed or disabled by GitHub after extended inactivity. Re-enable the workflow from Actions if needed. Keep branch protections in place; if bot pushes are blocked, use a pull-request publishing approach.

## File map

| File | Purpose |
| --- | --- |
| `README.md` | Public profile overview |
| `assets/header-*.svg` | Introduction artwork beside the student, light/dark |
| `assets/student-laptop.gif` | Original student animation from the supplied GIF collection |
| `assets/THIRD_PARTY_NOTICES.md` | Retained upstream MIT notices |
| `assets/footer-*.svg` | Original animated closing line, light/dark |
| `assets/focus-*.svg` | Original typing ribbon with a reduced-motion fallback |
| `assets/contact-*.svg` | LinkedIn, DEV, and email icon buttons |
| `assets/tool-*.svg` | Technology badges with recognizable logos |
| `assets/activity-*.svg` | Real contribution summary, generated daily |
| `assets/contributions-3d-*.svg` | Yoshi 3D calendar, generated from real contributions |
| `scripts/3d-settings.json` | Custom light/dark 3D calendar settings |
| `examples/profile-refresh.yml` | Optional notifier for pushes in other owned repositories |
| `scripts/build_brand.py` | Rebuild original SVG branding |
| `scripts/generate_activity.py` | Fetch and render the real calendar |
| `scripts/enhance_profile.py` | Rebuild social buttons, badges, and typing ribbon |
| `scripts/icon_sources.json` | Checked-in CC0 icon sources |
| `.github/workflows/profile-assets.yml` | Generate and publish activity images |
| `SOURCES.md` | Credits and data notes |
