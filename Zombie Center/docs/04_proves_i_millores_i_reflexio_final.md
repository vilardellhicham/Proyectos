# 04_proves_i_millores_i_reflexio_final

## 1. Proves realitzades

Durant el desenvolupament del joc s'han fet diverses proves per comprovar que les mecàniques principals funcionaven correctament.

### 1.1. Proves del cicle de dia i nit
- S'ha comprovat que `Lighting.ClockTime` canvia amb el temps.
- S'ha verificat que el joc diferencia entre estat de dia i estat de nit.
- S'ha ajustat el cicle perquè sigui visible durant la partida.

### 1.2. Proves de spawn de zombis
- S'ha comprovat que els zombis apareixen als punts de la carpeta `Zombie Spawns`.
- S'ha verificat que de dia n'apareixen menys.
- S'ha comprovat que de nit n'apareixen més.

### 1.3. Proves d'IA dels zombis
- S'ha comprovat que el zombi detecta el jugador a una certa distància.
- S'ha verificat que el persegueix quan entra dins del radi de detecció.
- S'ha ajustat la distància perquè no vinguin des de tot el mapa.
- S'ha corregit que el zombi no continuï fent mal després de morir.

### 1.4. Proves de mort del zombi
- S'ha detectat que el cos es trencava en diverses peces en morir.
- S'ha corregit amb `BreakJointsOnDeath = false`.
- S'ha comprovat que el cadàver deixa d'atacar i queda més estable.

### 1.5. Proves de l'arma
- S'ha verificat que l'arma dispara correctament.
- S'ha comprovat el sistema de recàrrega.
- S'ha ajustat la posició de l'arma perquè es vegi millor en primera persona.
- S'ha provat el sistema de sons i la detecció de bales.
- S'ha revisat que el jugador no es faci mal a si mateix amb el tret.

### 1.6. Proves de càmera i primera persona
- S'ha activat la càmera en primera persona.
- S'ha ajustat la visibilitat del cos i dels accessoris de l'avatar.
- S'han fet proves per millorar la sensació de l'arma i del tret.

### 1.7. Proves de la zona segura
- S'ha comprovat que els zombis no poden entrar durant el dia.
- S'ha comprovat que durant la nit sí que poden passar.
- S'han fet proves amb parets invisibles i control de col·lisions.

## 2. Incidències trobades

Durant el projecte han aparegut diversos problemes tècnics.

### 2.1. Problemes amb animacions
Inicialment es van provar animacions de tret, equipar, recarregar i idle. Algunes no funcionaven correctament o es quedaven en bucle. També hi va haver problemes de compatibilitat entre objectes `Animation` i `KeyframeSequence`.

### 2.2. Problemes amb la recàrrega
La recàrrega provocava un efecte estrany, com si el personatge fes un petit salt o moviment incorrecte. Per això finalment es va prioritzar una solució més simple i funcional.

### 2.3. Problemes amb la càmera en primera persona
La configuració de la primera persona va provocar problemes visuals amb el cap, el cabell i la boina de l'avatar. També hi va haver dificultats per mantenir una ombra correcta del cap.

### 2.4. Problemes amb el muzzle flash i armes externes
Es van provar diferents armes i efectes visuals. Algunes eines externes tenien molts scripts o dependències i no eren pràctiques per al prototip, així que es van descartar per simplificar el projecte.

## 3. Millores aplicades

Les millores més importants que s'han aplicat són aquestes:

- limitació del radi de detecció del zombi
- millora del sistema de mort del zombi
- separació més clara entre scripts del jugador i scripts del servidor
- millor estructura de carpetes
- ajust de l'arma en primera persona
- ús d'una arma més estable en lloc d'una arma massa complexa
- ambientació amb boira i cicle de dia i nit
- zona segura amb comportament diferent segons l'hora

## 4. Millores futures

Si el projecte continués, les millores més lògiques serien:

- afegir més tipus de zombis
- incloure una pantalla d'inici o menú principal
- millorar la interfície de munició i vida
- afegir música o ambient sonor general
- polir millor la càmera i el retrocés de l'arma
- afegir una condició de victòria més clara, com sobreviure un cert nombre de nits
- millorar l'acabat visual del mapa i de la zona segura

## 5. Ús de la IA durant el procés

S'ha utilitzat IA generativa com a suport durant el desenvolupament. L'ús principal ha estat:

- resoldre dubtes de Lua i Roblox Studio
- revisar estructures de scripts
- ajudar a plantejar sistemes com el cicle de dia i nit, el spawn dels zombis o la primera persona
- redactar documents del procés
- preparar diagrames i estructures de lliurament

La IA no ha substituït el desenvolupament pràctic, però sí que ha ajudat a avançar més ràpid i a corregir errors tècnics.

## 6. Reflexió final

Aquest projecte m'ha servit per entendre millor com passar d'una idea simple a un prototip jugable. Al principi la idea era clara, però durant el procés han sortit molts petits problemes tècnics que obligaven a simplificar, provar i corregir.

La decisió més important ha estat mantenir l'abast controlat. En lloc d'intentar fer un joc massa gran, s'ha prioritzat tenir un sistema funcional amb zombis, dia i nit, arma i zona segura. Això ha fet possible arribar a una versió jugable de principi a fi.

També he vist que en aquest tipus de projecte és molt important separar la lògica per blocs: jugador, enemics, spawn, càmera, entorn i arma. Aquesta organització facilita molt tant la programació com la detecció d'errors.

En general considero que el resultat és coherent amb la idea inicial i que el projecte mostra un procés real de desenvolupament, no només el resultat final.
