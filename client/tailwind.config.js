/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        'blast-bg': '#1E0E1A',
        'blast-bg-2': '#2E1D2A',
        'blast-yellow': '#FFFE3E',
        'crocobot-eye': '#CBFBFF'
      }
    },
  },
  fontFamily: {
    'sans': ['Montserrat', 'Helvetica', 'Arial', 'sans-serif']
  },
  plugins: [],
}
