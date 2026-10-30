# Profile maintenance

This is the source for the overview at `https://github.com/prashant-7-8-7`.

GitHub displays the root `README.md` of a **public** repository named exactly **prashant-7-8-7** on that account's profile.

## Apply this package

If the profile repository does not exist, create a new public repository under your account named `prashant-7-8-7`, using `main` as the default branch. Copy the files inside the package's `github-profile` folder to that repository's root, including the `.github` folder. Keep the files inside `preview` outside the repository; they are a self-contained review copy.

The profile appears after the root `README.md` is committed. The first workflow run then generates the actual contribution graphics. No account settings or other project repositories need to be changed.

## Edit the profile

- Edit `README.md` for your introduction, project descriptions, tools, and links.
- Edit `scripts/build_brand.py` for the banner/footer text, palette, or animation. Run `python scripts/build_brand.py` to regenerate the branding. Existing live activity images are preserved.
- Add a verified CatalogLink repository link once it is public. The current profile intentionally labels it as in development.
- Add your preferred professional email or verified LinkedIn URL when you want them published. Neither is guessed or taken from private account data.

## Activity refresh

`.github/workflows/profile-assets.yml` refreshes the contribution summary and snake daily at **05:47 India time** (00:17 UTC), on relevant pushes to `main`, or with **Actions → Refresh profile visuals → Run workflow**. Scheduled workflows can be delayed by GitHub.

The first successful run replaces the clearly labeled initial placeholder images with actual contribution data. Failed generation preserves the last successfully published images. The header and footer always work independently of the activity workflow.

There is no personal access token to configure: the workflow uses the short-lived `github.token`. The job that publishes the generated images explicitly requests `contents: write`; generation uses `contents: read`.

If an organization policy disables Actions or blocks token writes, review the specific failed step. Keep branch protections in place; a protected profile branch may require a pull-request publishing approach instead of direct bot commits.

GitHub may disable scheduled workflows in a public repository after an extended period of inactivity. Re-enable the workflow from Actions if needed.

## File map

| File | Purpose |
| --- | --- |
| `README.md` | Public profile overview |
| `assets/header-*.svg` | Original animated introduction, light/dark |
| `assets/footer-*.svg` | Original animated closing line, light/dark |
| `assets/activity-*.svg` | Real contribution summary, generated daily |
| `assets/snake-*.svg` | Contribution snake, generated daily |
| `scripts/build_brand.py` | Rebuild original SVG branding |
| `scripts/generate_activity.py` | Fetch and render the real calendar |
| `.github/workflows/profile-assets.yml` | Generate and publish activity images |
| `SOURCES.md` | Credits and data notes |
