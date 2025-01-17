module.exports = {
  content: [
    './templates/**/*.{html,js}', // To capture all HTML and JS files inside templates folder
    './gallery/templates/gallery/**/*.{html,js}', // To capture all gallery-specific templates
    './gallery/templates/gallery/registration*.{html,js}', // For registration-related templates
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
