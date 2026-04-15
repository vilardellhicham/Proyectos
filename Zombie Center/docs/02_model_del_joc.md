# 02_model_del_joc

## 1. Components principals del joc

El meu joc és un microvideojoc de supervivència zombi fet amb **Roblox Studio**. Els components principals que formen el sistema són aquests:

- **Jugador**: personatge controlat per l’usuari en primera persona.
- **Arma**: pistola del jugador, amb sistema de tir, recàrrega, sons i retrocés de càmera.
- **Zombie**: enemic bàsic que detecta el jugador, el persegueix i li fa mal.
- **Gestor de partida**: controla el cicle de dia i nit i aplica canvis generals al joc.
- **SpawnManager**: decideix quan i on apareixen els zombis.
- **Zona segura**: espai central del mapa que bloqueja els zombis durant el dia però no durant la nit.

Aquests components són coherents amb la fase 1, perquè el joc es basa en un mapa petit, cicle de dia i nit, una zona segura central i zombis que es tornen més perillosos a la nit.

## 2. Entitats identificades

Les entitats o mòduls principals del joc són:

1. **Jugador**
2. **Arma**
3. **Zombie**
4. **GestorPartida**
5. **SpawnManager**
6. **ZonaSegura**

No totes són classes estrictes en sentit orientat a objectes, perquè a Roblox moltes parts es resolen amb scripts i models, però sí que funcionen com a mòduls lògics del sistema.

## 3. Atributs clau de cada entitat

### Jugador
- `vida`: salut actual del jugador.
- `municioActual`: bales dins del carregador.
- `municioReserva`: munició total de reserva.
- `posicio`: posició del personatge al mapa.
- `dinsZonaSegura`: indica si es troba dins l’àrea segura.

### Arma
- `dany`: mal que fa cada tret.
- `cadencia`: temps entre trets.
- `abast`: distància màxima del tir.
- `sons`: conjunt de sons de tret, recàrrega i clic sense bales.
- `retrocesCamera`: intensitat del retrocés visual.

### Zombie
- `vida`: salut del zombi.
- `walkSpeed`: velocitat de moviment.
- `dany`: mal que causa quan ataca.
- `distanciaDeteccio`: radi en què detecta el jugador.
- `distanciaAtac`: radi en què pot atacar.
- `mort`: indica si el zombi ja és mort.

### GestorPartida
- `clockTime`: hora actual del joc.
- `esDeNit`: estat del cicle.
- `maxZombiesDia`: límit de zombis de dia.
- `maxZombiesNit`: límit de zombis de nit.
- `estatPartida`: estat general del joc, per exemple en curs o acabada.

### SpawnManager
- `spawns`: llista de punts on poden aparèixer zombis.
- `tempsSpawnDia`: temps entre aparicions de dia.
- `tempsSpawnNit`: temps entre aparicions de nit.
- `limitZombies`: màxim de zombis actius al mapa.

### ZonaSegura
- `walls`: parets invisibles que delimiten la zona.
- `bloqueigActiu`: indica si la barrera està activa.
- `permiteixEntradaNit`: permet l’entrada dels zombis de nit.

## 4. Accions, mètodes o funcions principals

### Jugador
- `moure()`: desplaçar-se pel mapa.
- `disparar()`: atacar els zombis.
- `recarregar()`: recuperar munició al carregador.
- `rebreDany()`: reduir la vida quan rep un atac.
- `morir()`: finalitzar la partida si la vida arriba a zero.

### Arma
- `fireServer()`: enviar el tret al servidor.
- `aplicarRetroces()`: moure una mica la càmera quan es dispara.
- `mostrarMuzzleFlash()`: efecte visual del tret.
- `reproduirSo()`: sons de tret i recàrrega.
- `restarMunicio()`: reduir bales del carregador.

### Zombie
- `buscarJugador()`: localitzar el jugador més proper.
- `moureCapAObjectiu()`: avançar cap al jugador.
- `atacar()`: fer mal al jugador quan està a prop.
- `rebreDany()`: perdre vida quan rep un tret.
- `morir()`: quedar aturat i deixar de causar mal.
- `canviarStatsNit()`: augmentar vida, velocitat i dany durant la nit.

### GestorPartida
- `actualitzarCicle()`: avançar el temps del joc.
- `comprovarDiaONit()`: detectar si toca mode dia o nit.
- `aplicarCanvisNit()`: activar canvis nocturns.
- `aplicarCanvisDia()`: restaurar condicions normals.
- `controlarFluxPartida()`: coordinar estat general del joc.

### SpawnManager
- `obtenirSpawnAleatori()`: triar un punt de spawn.
- `comptarZombies()`: saber quants zombis hi ha al mapa.
- `crearZombie()`: clonar un zombi des del model base.
- `aplicarStatsPerHora()`: assignar estadístiques segons si és dia o nit.

### ZonaSegura
- `activarBloqueigDia()`: impedir l’entrada de zombis.
- `desactivarBloqueigNit()`: permetre el pas a la nit.
- `controlarColisions()`: gestionar la barrera invisible.

## 5. Explicació del diagrama de classes

El diagrama de classes representa els principals blocs lògics del joc i les relacions entre ells.

- **Jugador** utilitza **Arma** per disparar i sobreviure.
- **Zombie** interactua amb **Jugador**, perquè el detecta, el persegueix i l’ataca.
- **SpawnManager** crea instàncies de **Zombie** a partir d’un model base.
- **GestorPartida** coordina el cicle dia/nit i activa canvis globals.
- **ZonaSegura** depèn del **GestorPartida**, perquè la barrera funciona diferent de dia i de nit.

He organitzat així el diagrama perquè reflecteix exactament l’estructura funcional que després programaré a Roblox. No és un model genèric, sinó una traducció directa del meu prototip actual.

## 6. Explicació del diagrama de comportament

Per al diagrama de comportament he triat un **diagrama d’activitat**, perquè mostra bé el bucle principal del joc.

El flux és aquest:
1. Comença la partida.
2. El jugador apareix al mapa.
3. El cicle dia/nit s’actualitza.
4. El sistema de spawn comprova l’hora i el nombre de zombis.
5. Si és de nit, es generen més zombis i se’ls augmenten les estadístiques.
6. Els zombis detecten el jugador i intenten perseguir-lo.
7. Si el jugador és dins la zona segura durant el dia, els zombis no poden entrar.
8. Si és de nit, la barrera no bloqueja i poden atacar igualment.
9. El jugador dispara, recarrega, fuig o mor.
10. Si la partida no acaba, el bucle es repeteix.

Aquest diagrama reflecteix el bucle real del joc i serveix per entendre la lògica abans de programar.

## 7. Correspondència entre diagrames i codi futur

Els diagrames es traduiran al codi real així:

- **Jugador** es correspon amb el personatge del jugador i els scripts locals de moviment, càmera i arma.
- **Arma** es correspon amb una `Tool` de Roblox amb `LocalScript`, `RemoteEvent`, sons i efectes.
- **Zombie** es correspon amb el model NPC i el seu script d’IA.
- **GestorPartida** es correspon amb scripts de `ServerScriptService` que controlen `Lighting.ClockTime`, nit i dia.
- **SpawnManager** es correspon amb el script que usa la carpeta `Zombie Spawns` per generar zombis.
- **ZonaSegura** es correspon amb les parets invisibles i la seva activació segons l’hora.

Per tant, els diagrames no són decoratius. Realment m’ajuden a repartir responsabilitats i decidir en quin script anirà cada part de la lògica.

## 8. Estructura inicial del repositori

L’estructura inicial del repositori la plantejo així:

```text
zombie-center-survival/
├── README.md
├── docs/
│   ├── 01_idea_i_abast.md
│   └── 02_model_del_joc.md
├── diagrames/
│   ├── diagrama_classes.png
│   └── diagrama_comportament.png
├── src/
│   ├── client/
│   │   ├── arma.localscript.lua
│   │   └── camera.localscript.lua
│   ├── server/
│   │   ├── cicle_dia_nit.server.lua
│   │   ├── spawn_zombies.server.lua
│   │   └── zona_segura.server.lua
│   └── npc/
│       └── zombie.server.lua
└── assets/
    ├── animacions/
    ├── sons/
    └── models/
```

Aquesta estructura té sentit perquè separa:
- documentació,
- diagrames,
- codi client,
- codi servidor,
- lògica dels NPC,
- i recursos del joc.

## 9. Primer commit i README inicial

El primer commit del repositori el faria amb un missatge com aquest:

```bash
git init
git add .
git commit -m "Initial commit: estructura inicial del projecte i documentacio base"
```

Si el repositori ja està creat a GitHub, després es pot enllaçar i pujar amb:

```bash
git branch -M main
git remote add origin URL_DEL_REPOSITORI
git push -u origin main
```

### Contingut inicial del README

El `README.md` inicial hauria d’incloure:
- títol del projecte,
- descripció curta del joc,
- objectiu del prototip,
- eines utilitzades,
- estructura bàsica del projecte.

Un exemple breu seria aquest:

```md
# Zombie Center Survival

Microvideojoc de supervivència zombi fet amb Roblox Studio.

## Idea
El jugador ha de sobreviure dins d’un mapa petit amb un cicle de dia i nit.
Durant el dia hi ha menys perill i la zona segura central protegeix el jugador.
Durant la nit apareixen més zombis i tenen millors estadístiques.

## Eines
- Roblox Studio
- Lua
- GitHub

## Estat del projecte
Fase 2: model del joc i disseny inicial
```

Aquest primer commit deixa evidència clara de l’inici del projecte i d’una estructura ordenada per continuar la implementació.