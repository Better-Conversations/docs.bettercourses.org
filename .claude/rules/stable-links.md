# Stable Link Maintenance

- If you add or change a stable link in `source/stable-links.rst`, keep `functions/l/[id].js` in sync
- Validate redirect targets after updates
- The two redirect handlers are:
  - `functions/l/[id].js` — stable link redirect map (`/l/:id`)
  - `functions/bc/[id].js` — `/bc/:id` redirect handler
