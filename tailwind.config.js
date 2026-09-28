/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        ocean: {
          950: '#030814',
          900: '#071126',
          800: '#0c1e3d',
          700: '#142d57',
          600: '#1d417a',
          500: '#2657a0',
        },
        slate: {
          850: '#111827',
          950: '#0a0f1d',
        },
        warning: '#f59e0b',
        danger: '#ef4444',
        success: '#10b981',
        cyan: {
          400: '#22d3ee',
          500: '#06b6d4',
          900: '#164e63',
        }
      },
      fontFamily: {
        mono: ['JetBrains Mono', 'Consolas', 'Courier New', 'monospace'],
        sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
