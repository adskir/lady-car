/** Tailwind compilato in css/site.css (niente CDN). Ricompila dopo aver cambiato le classi:
 *  npx tailwindcss@3 -i src/tailwind.css -o css/site.css --minify
 *  (lo fa anche la GitHub Action build-css.yml a ogni push) */
module.exports = {
  content: ["./index.html", "./privacy.html"],
  theme: {
    extend: {
      colors: {
        ink: '#15161A', panel: '#1C1D21', panel2: '#232428', paper: '#F2EFEA',
        rosso: '#8C3B2E', rossobright: '#B24A36', oro: '#C9A66B', muted: '#9B968E',
        hair: 'rgba(242,239,234,0.12)'
      },
      fontFamily: {
        serif: ['Fraunces', 'ui-serif', 'Georgia', 'serif'],
        sans: ['Manrope', 'system-ui', '-apple-system', 'sans-serif'],
      },
    }
  }
}
