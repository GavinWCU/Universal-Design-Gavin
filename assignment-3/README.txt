MASCOTS – TABLES, FORMS, TABBED BROWSING, AND SCREEN READING
============================================================

Files
  index.html            the page
  css/styles.css        styles (fonts, colors, skip link, table, form)

WHAT IS ON THE PAGE
  Semantic HTML5 elements (no divs)
    header, nav, main, article, section, aside, footer, figure,
    time, data, dfn, cite, abbr, mark, dl/dt/dd, details/summary, small
  Accessible data table ("Famous mascots by year of debut")
    <caption>, <thead>/<tbody>, th scope="col" and th scope="row".
    The table sits in a labelled, focusable <figure> that scrolls
    sideways on small screens instead of the whole page.
  Accessible form ("Nominate a mascot")
    Every field has a <label for>. Fields are grouped with
    <fieldset>/<legend>. Required fields use the required attribute.
    Hints are tied to their fields with aria-describedby.
  Skip navigation (CSS drop-down)
    .skip-link is hidden above the viewport and slides down when it
    gets keyboard focus. Press Tab once on page load to see it.
  Google Fonts
    Headings   Fraunces (serif), 600
    Paragraphs Atkinson Hyperlegible (sans-serif), 400 and 700, plus italics.
               Made by the Braille Institute for low-vision readers.
  Legibility
    18px body text, 1.65 line height, dark ink on a light background,
    links underlined so they never rely on color alone.
  Google Material Icons
    Material Symbols Outlined, every icon has aria-hidden="true"
    so screen readers skip it.

UPLOAD AND TEST
  On the live URL:
  - https://validator.w3.org/nu/  (passes with 0 errors, 0 warnings)
  - WAVE (https://wave.webaim.org/)
  - Silktide: run the accessibility check on the page.
  - HTML5 Outliner extension. Expected outline:
      Mascots
        Primary navigation
        Where mascots came from
          A lucky charm on stage
          Live animals on the sidelines
          The costumed mascot arrives
            Mascot words to know
        Did you know?
        Famous mascots
        Nominate a mascot
  - Lighthouse (Chrome DevTools > Lighthouse > Accessibility).
  Re-check after you edit anything.
