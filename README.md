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

.
