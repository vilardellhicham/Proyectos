# 03_entorn_i_prototip

## 1. EVIDÈNCIES del treball fet fins ara + breu explicació

Fins aquest punt del projecte ja tinc un primer prototip funcional del microvideojoc de supervivència zombi fet amb Roblox Studio. Les evidències principals del treball realitzat són aquestes:

### 1.1. Cicle de dia i nit
S’ha implementat un sistema bàsic de cicle de dia i nit utilitzant el servei `Lighting` de Roblox Studio. La variable principal és `ClockTime`, que va canviant amb el temps per simular el pas de les hores.

Aquesta part és important perquè afecta directament el comportament del joc. Durant la nit el joc es torna més perillós, ja que hi poden aparèixer més zombis i aquests poden tenir millors estadístiques.

### 1.2. IA bàsica del zombi
S’ha creat un zombi funcional amb un comportament senzill però útil per al prototip. El zombi:

- detecta el jugador dins d’una certa distància
- es desplaça cap al jugador
- canvia entre animació d’idle, caminar i atacar
- fa mal quan està prou a prop

També s’han corregit problemes que han anat sortint durant les proves, com per exemple que el zombi continués fent mal després de morir o que el cos es trenqués en diverses peces quan moria.

### 1.3. Aparició de zombis segons el moment del dia
S’ha preparat una estructura amb punts de spawn perquè els zombis puguin aparèixer en diferents llocs del mapa. Aquesta part es basa en una carpeta de punts de generació i una carpeta per guardar els zombis actius.

La idea del sistema és que:

- de dia apareguin pocs zombis
- de nit apareguin més zombis
- de nit també puguin augmentar les seves estadístiques, com la vida, la velocitat o el mal

Això reforça la diferència entre dia i nit i fa més clar el bucle de joc.

### 1.4. Zona segura
S’ha plantejat una zona segura al centre del mapa. L’objectiu és que durant el dia els zombis no hi puguin entrar, però que durant la nit sí que hi puguin accedir.

Aquesta mecànica dona sentit a la idea de supervivència i crea un espai de pausa relativa durant el dia.

### 1.5. Vista en primera persona
S’ha configurat el joc perquè el jugador jugui en primera persona. També s’ha treballat perquè es pugui veure millor el propi cos en mirar cap avall, fet que ajuda a donar més immersió al prototip.

Durant aquesta part han aparegut alguns problemes visuals amb accessoris de l’avatar, però s’han anat ajustant per millorar la visibilitat.

### 1.6. Arma funcional
S’ha integrat una pistola funcional per al jugador. Inicialment es va provar una arma pròpia amb animacions i efectes, però finalment s’ha optat per una altra arma que funcionava millor com a base del prototip.

Actualment l’arma permet:

- disparar
- recarregar
- reproduir sons
- aplicar dany als enemics
- tenir munició i recàrrega
- afegir efectes locals com el retrocés de càmera

Aquest sistema és suficient per a una primera versió jugable.

### 1.7. Proves i correccions
A mesura que s’ha implementat el prototip s’han fet diverses proves dins de Roblox Studio. Algunes correccions importants han estat:

- limitar la distància de detecció dels zombis
- evitar que el jugador es faci mal a si mateix amb l’arma
- ajustar el comportament dels zombis quan moren
- revisar el sistema de càmera i de primera persona
- preparar l’estructura del joc perquè sigui fàcil afegir noves millores després

## 2. IDE utilitzat i configuració bàsica

L’entorn principal utilitzat és **Roblox Studio**, ja que és l’eina necessària per crear el mapa, els models, els scripts i les proves del joc.

### 2.1. Eines utilitzades
Les eines principals utilitzades fins ara són:

- **Roblox Studio** per crear i provar el joc
- **Explorer** per organitzar objectes, carpetes i scripts
- **Properties** per modificar propietats dels objectes
- **Output** per detectar errors i fer proves amb `print()`
- **Play Test** per comprovar el funcionament del prototip dins del joc
- **GitHub** per preparar el repositori del projecte

### 2.2. Configuració bàsica del projecte
La configuració inicial del projecte s’ha organitzat de forma simple:

- `Workspace` per al mapa, els punts de spawn i els zombis actius
- `ServerStorage` per guardar el model base del zombi
- `ServerScriptService` per als scripts globals del joc
- `StarterPlayer` per als scripts relacionats amb la càmera o el jugador
- `StarterPack` per a l’arma del jugador
- `Lighting` per al cicle de dia i nit i la boira

Aquesta estructura facilita separar la lògica del joc, els enemics, la càmera i les armes.

## 3. Decisions inicials d’implementació

Des del principi s’han pres diverses decisions perquè el projecte fos assumible dins del temps disponible.

### 3.1. Fer un joc petit i funcional
S’ha decidit prioritzar un prototip senzill però jugable. Per això no s’han afegit sistemes massa grans com inventaris complexos, multijugador, crafting o missions.

### 3.2. Separar la lògica del joc per parts
La implementació s’ha pensat per blocs:

- un sistema per al cicle dia/nit
- un sistema per a la IA del zombi
- un sistema de spawn
- un sistema d’arma per al jugador
- un sistema de càmera en primera persona

Això ajuda a detectar errors més fàcilment i permet avançar pas a pas.

### 3.3. Servidor per a la lògica general
Les parts importants del joc, com ara l’aparició dels zombis o els canvis globals del món, s’han plantejat des del servidor. D’aquesta manera tots els jugadors comparteixen el mateix comportament general del joc.

### 3.4. Scripts locals per a càmera i sensacions del jugador
Les parts més visuals o personals, com la càmera o alguns efectes de l’arma, s’han treballat amb scripts locals. Això té sentit perquè afecten directament l’experiència del jugador i no cal que siguin globals.

### 3.5. Prototip abans que acabat visual
També s’ha decidit prioritzar el funcionament abans que l’acabat final. És a dir, primer s’ha buscat que les mecàniques funcionin i després ja es milloraran aspectes visuals o d’ambientació.

## 4. Captures de pantalla

En aquesta fase cal adjuntar captures de pantalla com a evidència del prototip. En la versió final del document s’hi haurien d’afegir, com a mínim, aquestes:

### Captura 1. Vista general del mapa
Imatge del mapa principal on es vegi la zona de joc, la boira i l’ambient general.

### Captura 2. Cicle de dia i nit
Una captura de dia i una altra de nit per mostrar que el sistema canvia correctament.

### Captura 3. Zombie Spawns
Imatge de l’estructura de carpetes o dels punts de spawn dins de Roblox Studio.

### Captura 4. Zombi perseguint el jugador
Captura on es vegi clarament que el zombi detecta el jugador i el segueix.

### Captura 5. Arma equipada
Captura en primera persona amb l’arma visible.

### Captura 6. Proves del codi o Output
Captura de la consola `Output` mostrant proves, missatges de depuració o validació del sistema.

### Captura 7. Estructura del projecte
Captura de l’`Explorer` amb l’organització principal del joc.

## 5. Estat actual del prototip

Actualment el projecte ja té una base jugable i coherent amb la idea definida a la fase 1. Encara falten millores i ajustos, però el prototip ja inclou els sistemes més importants:

- supervivència en un mapa limitat
- zombis amb comportament bàsic
- sistema de dia i nit
- zona segura
- arma funcional
- vista en primera persona

Per tant, es pot considerar que la fase d’entorn i prototip està començada correctament i que el projecte ja disposa d’una base real sobre la qual continuar programant la resta del joc.
