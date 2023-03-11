## HUGO ein Vorlesegerät

Das Gerät wurde für einen netten Menschen mit einer kognitiven Beeinträchtigung entwickelt. Es dient dazu, dass
er sich selsbtständig Texte aus Zeitungen, Büchern, Prospekt, usw. vorlesen lassen kann.  

Wichtig war dabei eine sehr einfache Bedienung zu ermöglichen, damit das Gerät für den Behinderten ohne fremde Hilfe zu bedienen ist. 

Basis war ein vorhandenes, leider defektes, Produkt eines deutschen Herstellers. Es ist eigentlich für Sehbehinderte Menschen gedacht.  
Zu dem Gerät gehört eine spezielle Tastatur, dies hat nurwenige große Tasten. Die Tasten haben unterschiedliche Formen und können dadurch 
von sehbehinderten Personen durch Fühlen erkannt werden. Die deutliche unterschiedlichen Formen können jedoch auch von Menschen mit kognitiven
Einschränkungen erkannt werden.  

#### Die Tastatur als zentrales Element
Ich verwendete die vorhandene Tastatur, es sollte allerdings möglich sein per 3D-Druck, etc. eine solche zu bauen.

##### Tasten (siehe Folder documenation)
1. eine runde Taste (-) zum Starten eines Vorgangs
2. eine quadratische Taste (+) zum Unterbrechen, bzw. Wiederholen
3. zwei dreieckige Tasten (PgUp and PgDown) zur Regelung der Lautstärke, eine mit der Spitze nach oben (lauter), die andere nach unten(leiser)    


### Die notwendigen Komponenten:
#### Software
- Linux als OS
- eSpeakNG https://github.com/espeak-ng/espeak-ng 
- MBROLA Voices
- Sane 
- Tesseract 

Das in Python und Bash erstellte Paket bindet diese Komponenten zusammen zu einer Lösung.  

- Das Pythonscript "readspeak.py" steuert den gesamten Ablauf und startet die TexttoSpeech Software "eSpeakNG" 
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
Doku zu Harware folgt. 



