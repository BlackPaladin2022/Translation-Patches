--------------------------------------------------
-BlackPaladin's Last Armageddon Translation Patch-
--------------------------------------------------

*****************
*Last Armageddon*
*****************

For those who are unaware, Last Armageddon is a role-playing game, released originally for PC-8801 and the MSX in 1988.  It was later re-released for PC-Engine CD (Turbografx-CD) on August 20, 1990, and the Famicom (NES) on November 10, 1990.

This game takes place in a post-apocalyptic world where all humans on Earth were completely wiped out and taken over by demons.  Two demons, a minotaur and a skeleton, were exploring the surface and saw that someone (or something) was leaving behind giant slabs on the planet's surface.  During their expedition, Skeleton had its skull blown to bits, and the scene cuts to an alien holding a rifle.  The alien claims that the planet was to be a colony of Planet Chirius and has given its inhabitants two options: submit or fight and perish.  Minotaur returned to relay the news, and the demons send forth twelve warriors with two missions... destroy the aliens and discover the mystery behind the stone slabs.

The game is played with three groups of four.  A day group, (Orc, Harpy, Minotaur and Snake) a night group, (Goblin, Gargoyle, Cyclops and Skeleton) and a Salvan's Day group (Golem, Sphinx, Dragon and Slime).

Each demon has specific traits specific to them.  Because of space limitations, smaller words are to decribe what trait each demon has.

Craft (sword icon) = Has the ability to make weapons
Craft (armor icon) = Has the ability to make armor, helms, and shields
Craft (bottle icon) = has the ability to make items
Flier = Has the ability to fly
Stone (shield icon) = Immune to being petrified
Venom (shield icon) = Immune to being poisoned
Stun (shield icon) = Immune to being paralyzed
Water (shield icon) = Resistant to water
Water (broken shield icon) = Weak against water
Fire (shield icon) = Immune to fire
Fire (broken shield icon) = Weak against fire
Memory = Has the "Memory" skill
Disarm = Can remove traps
Phys. (shield icon) = Strong defense against physical attacks
ESPer = has the "ESP" skill (View World Map)

The patch comes in two flavors...

Last Armageddon (English v1.02a).ips
--This patch requires a clean an unaltered "Last Armageddon" ROM (IPS Format)
Last Armageddon (English v1.02a).bps
--This patch requires a clean an unaltered "Last Armageddon" ROM (BPS Format)

The ROM has to have the following hashes:

File SHA-1: 456474DFEFF280134FD1D59CB39B82E97F269782
File CRC32: 22FBD0E9
ROM SHA-1: 77272C0C0E821E9BB1EA416EF1C983BD46188D68
ROM CRC32: 8EEF8B76

After applying either patch, it should have the following hashes:

File SHA-1: 05F6F229FB895D0C1015152074D97F59A747D403
File CRC32: 73F94CA5
ROM SHA-1: 668F8F4DCDE925EF314A1E7A342D5B1C5E43FCDF
ROM CRC32: DFED173A

Note:  If your ROM has the following hashes...

File SHA-1: 33F42B86F63B4661FBAEC006F6858CB4DEBA03AE
File CRC32: 40F87097
ROM SHA-1: 77272C0C0E821E9BB1EA416EF1C983BD46188D68
ROM CRC32: 8EEF8B76

...or these hashes...

File SHA-1: F6D4CD026D9883C2A94DF152ABB3265025CF09DF
File CRC32: CE0CC857
ROM SHA-1: 77272C0C0E821E9BB1EA416EF1C983BD46188D68
ROM CRC32: 8EEF8B76

You will need to replace the first sixteen hex values in the ROM.  (The ROM header)  If you replace it with...

4E 45 53 1A 20 00 42 08 00 00 7A 09 00 00 00 00

You'll have the correct ROM to use the BPS (or IPS) patch file on.


What has been translated?

All in-game dialogue
Battle menus
Overworld menus
Location cards
Item names
Spell names
Skill names
Save/Load menus
Game Ending

v1.0
Initial release

v1.01
"Ado" spell is renamed "Wake"
"AdoAll" spell is renamed "WakeAll"
"Dias" spell is renamed "Kill"
"Diados spell is renamed "KillAll"
Typo in one of the 108 slabs fixed

v1.02

Failed escape attempt messages during battle will display correctly
Further fixes with the game's script
"Power" in Monster's limits have been renamed "Health"
"Limits" has been renamed "Stats"
After-battle messges have been written more clearly
Many monster traits have been renamed.

v1.02a

Fixed a very minor typo with the "Fire" spell

**************
*Known Issues*
**************

1.  If try to equip a weapon or armor piece that already has been equipped, you'll see the message "Not Equipped" pop on the screen.  Unfortunately, this issue persists even in the original game.  However, you'll see that the item is still equipped while doing so.


Special Thanks:

FCE Ultra Team (Used emulator to test)
Mesen Team (Used emulator to test)
Ratty (This person translated all known text in the game!)
Pennywise (Helped with enabling DTE in the dialogue)
FCandChill (Helped with enabling DTE in the dialogue and other NES ASM hacking)
phonymike (Helped with NES ASM hacking)
Pluvius (Helped with NES ASM hacking)
Klarth (Programmer of Atlas, Cartographer, and ScriptCrunch... programs used to insert translated text)
KingMike (His tutorial of enabling DTE was used in this translation patch)
abridgewater (Romhacking 100 & 200 tutorials helped me with hacking the game)
Bunkai (Romahcking 100 & 200 tutorials helped me with hacking the game)
abw (Very patiently helped me with enabling DTE in the game's ROM)
cccmar (Beta Testing)
kando (Beta Testing)
Louie of the Lords (bug reporting)
mentil (bug reporting)
Braingrey (This company originally released Last Armageddon)
Mind (This company originally released Last Armageddon)
Yutaka (This company ported Last Armageddon to the Famicom/NES)



All credit to "Last Armageddon" belong to Braingrey, Mind, Yutaka, and their respective creators and programers.  This patch is mainly used for pure enjoyment for those who cannot enjoy this game.  All rights reserved. (Braingrey, Mind, and Yutaka, please don't come after me!)