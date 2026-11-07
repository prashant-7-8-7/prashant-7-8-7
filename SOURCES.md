# Design notes & credits

The visual identity, SVG header/footer, typing ribbon, contact buttons, technology badges, activity-card renderer, and profile text were created for Prashant Sharma. The profile uses a navy, cyan, and violet palette, with matching light and dark artwork. Identity and project information remain readable without animation, and the original animated SVGs honor reduced-motion preferences. The student GIF and upstream 3D calendar use their own animation behavior.

## Resources reviewed

- [alexandresanlim](https://github.com/alexandresanlim) — clear professional identity and grouped project links.
- [rzashakeri](https://github.com/rzashakeri) — animated introduction and a structured toolbox.
- [Platane](https://github.com/Platane) — earlier animation reference. The snake has been replaced by the requested 3D contribution calendar.
- [vn7n24fzkq](https://github.com/vn7n24fzkq) — inspiration for generated, self-hosted profile summaries.
- [Anmol-Baranwal/Cool-GIFs-For-GitHub](https://github.com/Anmol-Baranwal/Cool-GIFs-For-GitHub) — the **Deep Thinking** student-at-laptop GIF used beside the introduction. The original animation is self-hosted as `assets/student-laptop.gif`, unmodified. [Source asset](https://github.com/Anmol-Baranwal/Cool-GIFs-For-GitHub/assets/74038190/8aa99f6c-267d-4977-9cd3-1a4c11675863). The collection carries the MIT license; its notice is retained in `assets/THIRD_PARTY_NOTICES.md`.
- [yoshi389111/github-profile-3d-contrib](https://github.com/yoshi389111/github-profile-3d-contrib) — the actual 3D calendar generator, including animated contribution columns, contribution radar, and repository language distribution. It is pinned to verified commit `7d95e7d4cdc028dd1e1cbd957d65f35efb12ae39`, with custom light/dark settings in `scripts/3d-settings.json`. MIT license notice retained in `assets/THIRD_PARTY_NOTICES.md`.
- [elangosundar/awesome-README-templates](https://github.com/elangosundar/awesome-README-templates) — layout references.
- [itsVaibhavSharma/itsVaibhavSharma](https://github.com/itsVaibhavSharma/itsVaibhavSharma) — inspiration for the typing introduction, recognizable social badges, and grouped technology icons. No education, employment, awards, or project claims were copied.
- [alexandresanlim/Badges4-README.md-Profile](https://github.com/alexandresanlim/Badges4-README.md-Profile) — social and technology badge references.
- [suryakantamangaraj/AwesomeGithubProfileTemplates](https://github.com/suryakantamangaraj/AwesomeGithubProfileTemplates#categories) — creative, code-oriented, and typing layout references.
- [abhisheknaiidu/awesome-github-profile-readme](https://github.com/abhisheknaiidu/awesome-github-profile-readme) — discoverable profile sections and expandable details.
- [Simple Icons](https://github.com/simple-icons/simple-icons) — technology, DEV Community, and Gmail artwork under [CC0-1.0](https://github.com/simple-icons/simple-icons/blob/develop/LICENSE.md). The LinkedIn button uses a typographic mark because LinkedIn is absent from the current icon set. The checked-in `scripts/icon_sources.json` makes the badges reproducible without a hosted image service.

The project descriptions were checked against the current public READMEs for [Research Agents](https://github.com/prashant-7-8-7/research-agents), [AI Document Workspace](https://github.com/prashant-7-8-7/Macro-Project-), [GridPulse](https://github.com/prashant-7-8-7/GridPulse), and [RailSetu](https://github.com/Gaurav-Rajawat/RailSetu). RailSetu is explicitly credited as a team project in its owner's repository.

## Data & implementation

- Contribution figures come from GitHub's GraphQL contribution calendar. They follow GitHub's counting rules and are not presented as evidence of engineering skill or code quality.
- No fake statistics, skill percentages, credentials, awards, or work experience are included.
- Generated assets are stored in this repository. Visiting the profile does not depend on a third-party stats-image service.
- The 3D calendar is generated with the commit-pinned Yoshi action. Official GitHub actions are pinned to specific commits too.
- Generation runs with read-only repository access. Only the separate image-publishing job receives permission to update this profile repository.
- The main profile workflow requires no personal access token, paid API, or paid animation service. Standard GitHub-hosted runners are used for this public repository. Immediate cross-repository push notifications require the separate, narrowly scoped credential described in `PROFILE_GUIDE.md`; that optional connection is not configured automatically.
- LinkedIn, DEV, and the public contact email were supplied by Prashant for this overview. A Dribbble account-settings URL is not used as a public portfolio link; a public profile URL is needed before adding that button.
