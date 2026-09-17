# summervilleaccidentattorney.com — Frost Law Group's personal injury site

A deployable static rebuild of [summervilleaccidentattorney.com](https://www.summervilleaccidentattorney.com/), the personal injury practice of Frost Law Group, LLC (Summerville, SC), built to the plan in the firm's search audit. The firm's other practice areas live on [frostlawgroupsc.com](https://frostlawgroupsc.com/) (repository `frost-audit`), and the two sites are wired together so they never compete for the same search.

## What is here

| Path | What it is |
|---|---|
| `website/` | The built site: 56 pages, one stylesheet, self-hosted fonts, optimized images, `sitemap.xml`, `robots.txt`, `llms.txt`, `404.html`, and an `.htaccess` for Apache hosts |
| `vercel.json` | Vercel configuration: serve `website/`, keep trailing slashes, redirect the non-www host and every removed old address, cache assets |
| `site/build_site.py` | The generator (same system as the main site, adapted for this one) |
| `site/content/` | All copy: `firm.py` (facts, navigation, redirects), `core.py`, `car.py`, `practice.py`, `cities.py`, `posts.py`, `spanish.py`, `meta.py` (titles and descriptions), `local_data.json` (verified courts, routes, statutes) |
| `site/assets/` | Stylesheet, fonts and the firm's photos |
| `site/BUILD-NOTES.md` | Design decisions, the two-site rules as implemented, and the pre-launch checklist |

## Building

```bash
pip install pillow
python3 site/build_site.py                      # writes website/ and vercel.json
python3 site/build_site.py --preview out.html   # single-file clickable preview
```

The build fails if any page names the main site's practice areas outside the one designed cross-link (see `CANNIBAL_RE` in `build_site.py`), and warns on titles over 70 characters, descriptions outside 60–160, duplicate titles, unresolved links and missing images.

## Site map

- Home, practice-area index, areas index, team, two attorney pages, contact (Formspree form), reviews, blog index, privacy, terms, accessibility, thank-you (not indexed)
- **Car accidents** hub with 14 answer pages (first 48 hours, at-fault, comparative negligence, statute of limitations, SC car accident laws, talking to the insurer, UM/UIM, hit-and-run, distracted driving, drunk-driver crashes, Uber/Lyft, delivery drivers, getting evaluated, where crashes happen)
- Truck, motorcycle, pedestrian, dog bite, slip and fall, workers' compensation, catastrophic injury and wrongful death hubs, with answer pages on truck liability, the helmet law, the dog-bite statute, children and dog bites, homeowner's insurance, and the wrongful death statute
- Nine community pages (Summerville, Goose Creek, Ladson, North Charleston, Charleston, Mount Pleasant, Moncks Corner, Walterboro, West Ashley)
- Four blog articles and a Spanish-language page

## Deploying

See `site/BUILD-NOTES.md`. In short: import the repository in Vercel with the framework set to "Other", add `www.summervilleaccidentattorney.com` (primary) and the apex domain, and point DNS at Vercel. `vercel.json` handles the host redirect, the trailing slashes and the redirect map.
