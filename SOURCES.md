# Design notes & credits

The visual identity, SVG header/footer, typing ribbon, contact buttons, technology badges, activity-card renderer, and profile text were created for Prashant Sharma. The profile uses a navy, cyan, and violet palette, with matching light and dark artwork. Identity and project information remain readable without animation, and the original animated SVGs honor reduced-motion preferences.

## Resources reviewed

- [alexandresanlim](https://github.com/alexandresanlim) — clear professional identity and grouped project links.
- [rzashakeri](https://github.com/rzashakeri) — animated introduction and a structured toolbox.
- [Platane](https://github.com/Platane) and [Platane/snk](https://github.com/Platane/snk) — the contribution snake used in this repository.
- [vn7n24fzkq](https://github.com/vn7n24fzkq) — inspiration for generated, self-hosted profile summaries.
- [Anmol-Baranwal/Cool-GIFs-For-GitHub](https://github.com/Anmol-Baranwal/Cool-GIFs-For-GitHub) — animation reference. No third-party GIFs were copied into this profile.
- [yoshi389111](https://github.com/yoshi389111) — inspiration for original SVG branding and contribution visualizations.
- [elangosundar/awesome-README-templates](https://github.com/elangosundar/awesome-README-templates) — layout references.
- [itsVaibhavSharma/itsVaibhavSharma](https://github.com/itsVaibhavSharma/itsVaibhavSharma) — inspiration for the typing introduction, recognizable social badges, and grouped technology icons. No education, employment, awards, or project claims were copied.
- [alexandresanlim/Badges4-README.md-Profile](https://github.com/alexandresanlim/Badges4-README.md-Profile) — social and technology badge references.
- [suryakantamangaraj/AwesomeGithubProfileTemplates](https://github.com/suryakantamangaraj/AwesomeGithubProfileTemplates#categories) — creative, code-oriented, and typing layout references.
- [abhisheknaiidu/awesome-github-profile-readme](https://github.com/abhisheknaiidu/awesome-github-profile-readme) — discoverable profile sections and expandable details.
- [Simple Icons](https://github.com/simple-icons/simple-icons) — technology, DEV Community, and Gmail artwork under [CC0-1.0](https://github.com/simple-icons/simple-icons/blob/develop/LICENSE.md). The LinkedIn button uses a typographic mark because LinkedIn is absent from the current icon set. The checked-in `scripts/icon_sources.json` makes the badges reproducible without a hosted image service.

The project descriptions were checked against the current public READMEs for [Research Agents](https://github.com/prashant-7-8-7/research-agents), [AI Document Workspace](https://github.com/prashant-7-8-7/Macro-Project-), [GridPulse](https://github.com/prashant-7-8-7/GridPulse), and [RailSetu](https://github.com/Gaurav-Rajawat/RailSetu). RailSetu is explicitly credited as a team project in its owner's repository. CatalogLink is identified as in development and has no unverified repository link.

## Data & implementation

- Contribution figures come from GitHub's GraphQL contribution calendar. They follow GitHub's counting rules and are not presented as evidence of engineering skill or code quality.
- No fake statistics, skill percentages, credentials, awards, or work experience are included.
- Generated assets are stored in this repository. Visiting the profile does not depend on a third-party stats-image service.
- The snake is generated with a commit-pinned Platane/snk action. Official GitHub actions are pinned to specific commits too.
- Generation runs with read-only repository access. Only the separate image-publishing job receives permission to update this profile repository.
- No personal access token, paid API, or paid animation service is required. Standard GitHub-hosted runners are used for this public repository.
- LinkedIn, DEV, and the public contact email were supplied by Prashant for this overview. A Dribbble account-settings URL is not used as a public portfolio link; a public profile URL is needed before adding that button.
