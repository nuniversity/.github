# `.github` — Nuniversity organization defaults

This is the **special organization repository** — its contents configure repo-wide and
profile-wide GitHub behavior for [github.com/nuniversity](https://github.com/nuniversity).

What lives here:

| Path | Purpose |
| --- | --- |
| `profile/README.md` | The **public organization profile README** rendered on the org's Overview tab ([docs](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/customizing-your-organizations-profile)). |
| `assets/banner.png` | The 1280×640 social-preview image for this repository (uploaded once via *Settings → General → Social preview*). |
| `assets/generate_banner.py` | Regenerates `banner.png` with Pillow — same brand language as the platform OG card. |

To regenerate the banner:

```bash
.venv-from-platform/bin/python assets/generate_banner.py   # writes assets/banner.png
```

Platform code, content and the live site live in the (source-available) workspace behind
[nuniversity.pages.dev](https://nuniversity.pages.dev/en).
