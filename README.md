## Binary Font
A smart font for hexadecimal and binary numeric transparency.

## TODO
- Shift glyphs right to center better.
- Better test page and README
- See how it works in latex
- Calculator/converter from decimal
- 0x and 0b?
    - Feels kinda bad to invisible them, and it feels kind of gross to leave them unchanged.
    - Would be useful so that eg 0x100 is interpreted correctly
- New name ideas:
    - bit dance
    
    
## Dev process
1. Design glyphs in inkscape, use inkscape export layers to svg for convenient fontforge import
2. In fontforge, 
    - open liberation_binary.sfd
    - add new encoding slots if needed.
    - import the glyph from svg (ctrl-shift-I). Uncheck the option to automatically scale, much better to just get the scale correct in inkscape.
    - Adjust the positioning horizontally and vertically
    - Adjust the vertical line indicating the character advance. Hex are double the monospace width, binary digits are half, and there are a few characters like the binseparator with 0 advance
    - Right click -> Glyph Info -> Glyph Name. Change the glyph name to match the glyph name used in binish.fea
    - You can use the metrics window to check how things look, but it's mostly superior to see how it works in step 4.
    - Save the fontforge project
    - Generate (ctrl-shift-G) liberation_binary_no_rules.otf, replacing and ignoring errors and generating.
3. From project dir, run `fonttools feaLib -o fonts/liberation_binary.otf src/binish.fea fonts/liberation_binary_no_rules.otf`. This will create/overwrite liberation_binary.otf
4. In browser, open or hard refresh index.html to see the font in use.