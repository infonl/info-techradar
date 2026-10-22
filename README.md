# INFO Technology Radar - Content

The INFO Technology Radar static site generator based on the [AOE tech radar implementation](https://github.com/AOEpeople/techradar).

## Hosting and Development

### Prerequisites
- Node.js >= 12

### Local Development
To run the application locally:
```bash
npm run serve
```
### Production Build
To create a production build:
```bash
npm run build
```
Host the application under a sub path
To host the application under a sub path with Next.js, you'll need to configure the basePath in your config.json. This replaces the previous PUBLIC_URL environment variable approach.

## Release notes
Every radar version gets a "What's new in Version #N" section at the top of `release-notes.md`, describing what has
changed since the previous version. The version number is the number shown on the radar home page, which is the
number of release folders in `radar/`.

The AOE tech radar generator does not support custom pages, so the release notes page is added through a patch on
`aoe_technology_radar` in `patches/`, applied by [patch-package](https://github.com/ds300/patch-package) on
`npm install`. When upgrading `aoe_technology_radar`, the patch has to be recreated for the new version:
`npm install` fails if the patch no longer applies.
