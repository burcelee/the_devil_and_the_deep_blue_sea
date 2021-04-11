# shipcards
Cards about ships

Software:
- LibreOffice Calc and Writer are used for the open format files.
- A VBA macro is used in the cards spreadsheet to export all cards to csv
- CardMaker is used to create printable card pages from csv. The ".cmp" file is the project file for CardMaker.
  It is available here: https://www.nhmk.com/cardmaker.php
- 
Some rules:
- All data/content files are plaintext
- Version numbers follow [*major revision*.*minor revision*.*patch*] 
  This is the second versioning scheme. 
  The first used only major and minor revision. 
  Therefore all 3 term versions come after all 2 term versions.
- 

Build instructions:

To print out copy of all US/RU cards:
1. Open data/cards.fods
2. Run macro to export all pages to csv
3. Open cmp project file in CardMaker
4. Export in CardMaker

To create a tabletop simulator deck:
1. Open data/cards.fods
2. Run macro to export all pages to csv
3. Open cmp project file in CardMaker
4. Set either RU or US starter deck as default for each layout.
5. File -> Export project to Images
6. Use TTS deck editor to create the deck: https://kb.tabletopsimulator.com/custom-content/custom-deck/
