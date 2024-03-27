/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './posts/templates/*.html',
    './home/templates/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('daisyui')
  ],
  daisyui: {
    themes: ["pastel"],
  },

};
