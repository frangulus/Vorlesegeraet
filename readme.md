## HUGO ein Vorlesegerät

Das Gerät wurde für einen netten Menschen mit einer kognitiven Beeinträchtigung entwickelt. Es dient dazu, dass
er sich selsbtständig Texte aus Zeitungen, Büchern, Prospekt, usw. vorlesen lassen kann.  

Wichtig war dabei eine sehr einfache Bedienung zu ermöglichen, damit das Gerät für den Behinderten ohne fremde Hilfe zu bedienen ist. 

Basis war ein vorhandenes, leider defektes, Produkt eines deutschen Herstellers. 

### Die notwendigen Komponenten:
#### Software
- Linux als OS
- readSpeakNG https://github.com/espeak-ng/espeak-ng 
- MBROLA Voices
- Sane 
- Tesseract 


Das in Python und Bash erstellte Paket bindet diese Komponenten zusammen zu einer Lösung.  

- Das Pythonscript "readspeak.py" steuert den gesamten Ablauf und startet die TexttoSpeech Software "readSpeak NG" 
- messages.py enthält die gesprochenen Hinweise zur Bedienung, dies können da indivduell angepasst werden
- configuration.de enthält Parameter zur verwendeten Stimme und Wartezeit bevor Hinweise wiederholt werden
- Mit reorder.py wird der gescannte Text bereinigt (Z.Bsp. überflüssige Leerzeilen, Sonderzeichen im Text)  
- scan2text.sh scannt die Vorlage und erstellt mit Tesseract eine Textdatei. 


#### Hardware 
- einfacher Flachbett-Scanner (Canon LIDE50)
- Spezielle Tastatur
- Gehäuse
- Computer (Mainboard mit Netzteil, etc) 

Basis für meine Lösung war das vorhandene Gerät. Davon wurde die Tastatur, das Gehäuse und der Scanner verwendet. 
Das sehr alte Mainboard und die defekte Festplatte wurden ersetzt. Nun werkelt ein Raspberry Pi mit einem Audio-Hat 
darin. Ein Arduino-Micro dient als Power-Controller und leitet nachdem eine Powerdown-Taste gedrückt wurde den Shutdown des Raspis ein.



