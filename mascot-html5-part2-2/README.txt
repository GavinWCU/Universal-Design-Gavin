MASCOT – HTML5 SEMANTIC RECODE (PART 2)
=======================================

Files
  index.html            the page
  css/styles.css        styles (fonts, colors, wrapper, .sr-only class)
  images/               the 10 optimized photos (a .webp and a .jpg of each)
  optimize_images.py    turns downloaded images into the files the page uses

WHAT CHANGED FOR PART 2
  Fonts (Google Fonts, linked in the <head> of index.html)
    Headings   Lora (serif), 600 and 700
    Paragraphs Atkinson Hyperlegible (sans-serif), 400 and 700, plus italics.
               Made by the Braille Institute for low-vision readers.
  Legibility
    18px body text, 1.65 line height, dark ink on warm off-white,
    links underlined so they never rely on color alone.
  Auto-centering wrapper (no divs: <body> is the wrapper)
    body { width: min(100% - 2rem, var(--wrapper)); margin-inline: auto; }
    The navy header/footer bands still run edge to edge using
    border-image outset, which doesn't cause sideways scrolling.
    The text column is 48rem wide, which is about 100 characters per line
    (measured: longest line is 99 characters). On wide screens the wrapper
    grows by exactly the width of the Contents sidebar, so the article
    column stays at 48rem.
  Color scheme (color-blind safe: blue and orange, no red/green pair)
    Navy   #14213D   header/footer background, headings
    Blue   #2B5C9E   links
    Amber  #F2A541   accents on navy only
    Rust   #A84A0E   focus ring and "you are here" highlight
    Paper  #FAF7F0   page background
    For your write-up: open https://color.adobe.com/create/color-wheel,
    type these 5 hex codes into the swatches, then open
    Accessibility Tools > Color Blind Safe. It should show no conflicts.
    (Checked with protanopia, deuteranopia and tritanopia simulations.)
  Contrast (WCAG AA needs 4.5:1)
    Body text #1E2329 on #FAF7F0    14.78:1
    Links     #2B5C9E on #FAF7F0     6.28:1
    Captions  #4A5160 on #FAF7F0     7.44:1
    White text on navy              14.93:1
    Amber on navy                    7.78:1
  .sr-only (clip method) is used for:
    - "Reference" before each citation number, e.g. [1] is read as "Reference 1"
    - "Back to citation N" on the up arrows in the reference list
    - "of reference N" after each "the original" link, so those links
      are not identical to a screen reader
    - a hidden "About this page" heading in the footer

UPLOAD AND TEST
  Upload index.html, css/ and images/ to your server, then on the live URL:
  - HTML5 Outliner extension. Expected outline, no "Untitled" entries:
      Mascot
        Contents
        Overview
        History
        Etymology
        Choices and identities
        Sports mascots
          Controversies
        Corporate mascots
        School mascots
        Olympics and World Expositions
        Government mascots
          Yuru-chara / NASA mascot / Military mascots / Smokey Bear
        In television
        In music
        See also
        References
        External links
        About this page
  - https://validator.w3.org/nu/  (passes with 0 errors, 0 warnings;
    also passes CSS checking)
  - WAVE (https://wave.webaim.org/): Contrast tab should show 0 errors.
  - Silktide: run the accessibility check on the page.
  Re-check after you edit anything.
