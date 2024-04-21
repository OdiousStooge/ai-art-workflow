# flake8: noqa
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Prompt

engine = create_engine("sqlite:///prompts.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Add or update a sample prompt
def add_or_update_prompt(id, prompt):
    new_prompt = Prompt(id=id, prompt=prompt)
    session.merge(new_prompt)
    session.commit()


add_or_update_prompt(
    1,
    "A towering Tauren shaman, muscles rippling, as he summons a towering tornado amidst the plains of Mulgore, with a backdrop of epic mountains and a vast, vibrant sunset, capturing the essence of high fantasy and World of Warcraft's stylized art.",
)

add_or_update_prompt(
    2,
    "An enchanted elf forest, where a muscular Night Elf rogue, dual-wielding glowing daggers, stealthily navigates through ancient, magical trees under a starlit sky, embodying the mix of Frank Frazetta's oil painting style and World of Warcraft's fantasy.",
)

add_or_update_prompt(
    3,
    "A fierce battle scene on the snowy fields of Northrend, featuring a heavily armored, muscular Human paladin clashing swords with an Undead warlock, magic and might colliding in an explosion of light and shadow, inspired by Frank Frazetta and World of Warcraft's epic lore.",
)

add_or_update_prompt(
    4,
    "A mystical Draenei mage, her muscular form casting a powerful spell, with arcane energies swirling around her in a display of sorcery and might, set against the alien landscapes of Outland, blending Frazetta's dramatic oil painting style with WoW's unique aesthetic.",
)

add_or_update_prompt(
    5,
    "A high elf hunter, lean and muscular, accompanied by a majestic, ferocious pet, stands vigilant in the ruins of Quel'Thalas. The scene is lit by the ethereal glow of the Sunwell, merging the high fantasy of Frazetta with the intricate detail of World of Warcraft's world.",
)

add_or_update_prompt(
    6,
    "An epic confrontation at the gates of Orgrimmar, featuring a towering, muscular Orc warrior in mid-roar, wielding a massive axe as he leads a charge against an invading force. The scene captures the raw, meaty muscularity of Frazetta's work, infused with the iconic stylized elements of World of Warcraft.",
)

add_or_update_prompt(
    7,
    "A frost mage casting a spell in the icy caverns of Icecrown, her robes fluttering as arcane energy crackles around her, the air shimmering with frost.",
)
add_or_update_prompt(
    8,
    "A bloodthirsty Orc Berserker, axe raised high, leading a charge across the Barrens, with a storm brewing overhead, lightning illuminating his muscular form.",
)
add_or_update_prompt(
    9,
    "An ancient Night Elf druid in the heart of Ashenvale, transforming into a majestic bear, surrounded by glowing wisps and towering, ancient trees.",
)
add_or_update_prompt(
    10,
    "A Dwarf paladin, hammer in hand, standing defiantly on the snowy slopes of Dun Morogh, his armor glinting under the setting sun, a fierce battle cry on his lips.",
)
add_or_update_prompt(
    11,
    "A Gnome warlock tinkering with a demonic portal in Gnomeregan, chaotic energies swirling, as imps and voidwalkers emerge into the neon-lit, steampunk workshop.",
)
add_or_update_prompt(
    12,
    "A Zandalari Troll priestess performing a sacred ritual atop Zuldazar, vibrant feathers and gold adorning her, the city sprawling below in the golden hour.",
)
add_or_update_prompt(
    13,
    "An Undead rogue sneaking through the ruins of Lordaeron, dagger at the ready, the moon casting eerie shadows over the forsaken landscape.",
)
add_or_update_prompt(
    14,
    "A Pandaren monk practicing martial arts on the serene peaks of Kun-Lai Summit, the landscape peaceful and misty, with ancient statues standing guard.",
)
add_or_update_prompt(
    15,
    "A Blood Elf mage in the magical city of Silvermoon, casting spells that illuminate the intricate elven architecture with a warm, ethereal glow.",
)
add_or_update_prompt(
    16,
    "A Human warrior clashing with a Horde opponent in the Arathi Highlands, the clash of steel and the roar of combat filling the air, banners waving in the wind.",
)
add_or_update_prompt(
    17,
    "A Draenei shaman calling upon the elements atop the Exodar, lightning crackling around her, the crystal structures reflecting the vibrant energies.",
)
add_or_update_prompt(
    18,
    "A Worgen hunter, in human form, aiming a longbow from the shadows of Gilneas, the Gothic architecture providing a somber backdrop to the tense hunt.",
)
add_or_update_prompt(
    19,
    "A Tauren Sunwalker, mace in hand, praying to the sun amidst the rolling plains of Mulgore, a serene and powerful presence against the vast landscape.",
)
add_or_update_prompt(
    20,
    "A Goblin engineer speeding across the sands of Tanaris in a makeshift rocket car, explosions of sand and steam trailing behind in the desert sun.",
)
add_or_update_prompt(
    21,
    "An Orc shaman standing at the edge of a lava flow in the heart of Blackrock Mountain, elemental spirits swirling around him in a dance of fire and earth.",
)
add_or_update_prompt(
    22,
    "A Forsaken priest in the depths of the Undercity, channeling dark energies in the eerie green glow of the alchemical labs, surrounded by the undead.",
)
add_or_update_prompt(
    23,
    "A Nightborne sorcerer in Suramar, harnessing the power of the Nightwell, arcane energies weaving through the opulent, ancient city at twilight.",
)
add_or_update_prompt(
    24,
    "A Vrykul warrior shouting a challenge in the stormy cliffs of Stormheim, her towering form silhouetted against the thunderous sky, ready for Valhalla.",
)
add_or_update_prompt(
    25,
    "A Kul Tiran druid in the form of a massive kraken, emerging from the stormy seas around Drustvar, tentacles thrashing as lightning splits the sky.",
)
add_or_update_prompt(
    26,
    "A Mechagnome inventor showcasing a new creation in Mechagon, surrounded by gears and steam, the city's mechanical landscape alive with innovation.",
)
add_or_update_prompt(
    27,
    "A Lightforged Draenei paladin kneeling in prayer within a beam of light aboard the Vindicaar, her armor glowing with holy runes against the backdrop of space.",
)
add_or_update_prompt(
    28,
    "A Mag'har Orc hunter, pet wolf by his side, scouting the desolate landscape of Outland, the reddish sky casting an otherworldly glow over the shattered realm.",
)
add_or_update_prompt(
    29,
    "A Highmountain Tauren fishing in the tranquil waters of Highmountain, the towering peaks reflected in the clear, calm lake at dawn.",
)
add_or_update_prompt(
    30,
    "A Void Elf rogue stepping out of a rift in reality in the Telogrus Rift, her form shifting between the material and the void, eyes glowing with dark energy.",
)

add_or_update_prompt(
    31,
    "A Sylvan elf archer, bow drawn taut, perched high in the boughs of Teldrassil, eyes focused on the distant horizon as the setting sun dapples through the leaves.",
)
add_or_update_prompt(
    32,
    "A muscular Bronzebeard dwarf, forging a legendary weapon in the fiery depths of Ironforge, sparks flying as hammer meets anvil, the glow illuminating his determined face.",
)
add_or_update_prompt(
    33,
    "A spectral banshee, former queen of the Forsaken, hovering over the ruins of a battlefield in Tirisfal Glades, her mournful wail echoing through the twilight.",
)
add_or_update_prompt(
    34,
    "A group of adventurers, diverse in race and class, sharing tales around a crackling fire in the Grizzly Hills, the northern lights flickering above the towering pines.",
)
add_or_update_prompt(
    35,
    "A mighty dragon, scales glittering, perched atop Wyrmrest Temple in Dragonblight, roaring a challenge to the skies, a testament to the epic scale of World of Warcraft.",
)
add_or_update_prompt(
    36,
    "An ethereal Netherwing drake, wings spread wide, gliding over the shattered floating islands of Outland, its rider a cloaked figure wielding a glowing staff.",
)
add_or_update_prompt(
    37,
    "A fierce gladiator, armor shining, standing victorious in the arena of Orgrimmar, raised weapons catching the last light of sunset, a crowd roaring approval.",
)
add_or_update_prompt(
    38,
    "A serene water elemental on the shores of the Isle of Quel'Danas, water swirling around it in harmony, the setting sun turning the sea to liquid gold.",
)
add_or_update_prompt(
    39,
    "A stoic stone paladin statue, guarding the ancient halls of Uldum, as a sandstorm swirls around, the remnants of a once-great civilization whispering secrets.",
)
add_or_update_prompt(
    40,
    "A rogue stealthily navigating the dark, cobbled streets of Gilneas City, the moonlight casting long shadows, the distant howl of worgen filling the air.",
)
add_or_update_prompt(
    41,
    "An angelic priestess in Eversong Woods, light emanating from her hands as she heals a wounded hawk, the tranquil forest a witness to her compassion and power.",
)
add_or_update_prompt(
    42,
    "A fierce Frostwolf orc, wrapped in furs, howling alongside his wolf companion atop the snowy peaks of Frostfire Ridge, the bond between them unbreakable.",
)

add_or_update_prompt(
    43,
    "A serene scene in the tranquil waters of the Vale of Eternal Blossoms, where a Pandaren fisherman sits amidst blooming lotuses, the setting sun casting a golden glow.",
)
add_or_update_prompt(
    44,
    "An imposing Warchief, Thrall, standing on the cliffs of Durotar, thunderstorm brewing overhead, as he calls upon the elements, his cloak billowing in the fierce wind.",
)
add_or_update_prompt(
    45,
    "A group of Silvermoon Blood Knights in formation, their armor gleaming under the sun, as they march through the regal pathways of Silvermoon City, pride in their stride.",
)
add_or_update_prompt(
    46,
    "A Nightborne enchantress weaving arcane magic in the grandeur of Suramar City, her elegant figure illuminated by the intricate patterns of spellwork that dance in the air.",
)
add_or_update_prompt(
    47,
    "A fierce skirmish at the gates of Stormwind, Alliance and Horde clashing in a spectacular melee, the iconic statues of the city's founders overseeing the battlefield.",
)
add_or_update_prompt(
    48,
    "A tranquil moment in the Shimmering Expanse, where a Night Elf druid swims alongside a school of bright, luminescent fish, the water around them alive with magic.",
)
add_or_update_prompt(
    49,
    "A Kul Tiran ship cutting through the foggy seas off the coast of Drustvar, its sails billowed by the strong sea wind, an aura of mystery and adventure in the air.",
)
add_or_update_prompt(
    50,
    "A lone Tauren Earthmother, silhouetted against the vast, starry sky of Mulgore, performing a sacred ritual to the rhythmic beat of drums, the spirit of the land strong.",
)
add_or_update_prompt(
    51,
    "The bustling streets of Boralus at dusk, lanterns lighting up as merchants call out their wares, sailors, and pirates mingling, the city alive with stories untold.",
)
add_or_update_prompt(
    52,
    "An epic confrontation between a Demon Hunter and a Dreadlord in the desolate wastes of Hellfire Peninsula, fel energy crackling, a dance of blades and dark magic.",
)
add_or_update_prompt(
    53,
    "A serene priestess of Elune in a moonlit glade within Ashenvale, moonbeams filtering through the ancient trees, blessing the sacred pool with her prayers.",
)
add_or_update_prompt(
    54,
    "A Viking-like Vrykul warrior standing atop the icy cliffs of Howling Fjord, her gaze steely as she watches over the fjord, the wind carrying tales of valor and conquest.",
)

add_or_update_prompt(
    55,
    "An attractive goblin woman, her multi-colored hair tied back in a practical yet stylish ponytail, intently soldering a complex gizmo. Her workshop is a clutter of blueprints and machinery, the glow of molten metal casting dynamic shadows across her determined face.",
)
add_or_update_prompt(
    56,
    "A goblin engineer, hair dyed in vibrant streaks of green and purple, adjusting the settings on a steampunk-inspired contraption. Around her, the chaotic workshop is alive with sparks and the hum of arcane-powered devices, her eyes gleaming with innovation.",
)
add_or_update_prompt(
    57,
    "In the heart of Gadgetzan, a goblin tinkerer with striking red and blue hair works on a mechanical spider, tools in hand. Her workshop is a testament to goblin ingenuity, filled with gadgets, gears, and the scent of oil, her focus unwavering as she brings her creation to life.",
)

add_or_update_prompt(
    58,
    "Tyrande Whisperwind, bathed in the soft glow of Elune's light, stands at the edge of a moonlit glade in Ashenvale. Her silver hair flows like a river, her eyes reflecting the deep, tranquil wisdom of the ages. In her hands, the iconic Bow of Elune, ready to defend her people.",
)
add_or_update_prompt(
    59,
    "In the heart of Darnassus, Tyrande Whisperwind offers prayers to Elune, surrounded by the verdant, ancient groves of Teldrassil. The moonlight filters through the towering trees, casting ethereal patterns on her regal, white robes, as a serene aura of power envelops her.",
)
add_or_update_prompt(
    60,
    "Amidst the chaos of battle, Tyrande Whisperwind rides atop her loyal frostsaber, her presence commanding and fierce. Her armor glints under the harsh light of conflict, her voice rising in a chant that bolsters her allies and terrifies her foes, the embodiment of the warrior priestess.",
)

add_or_update_prompt(
    61,
    "An Orc female warlock stands in the desolate landscape of Hellfire Peninsula, her green skin illuminated by the flickering flames of her summoned infernal. Her eyes glow with fel energy, her posture exuding power and defiance as dark spells form at her fingertips.",
)
add_or_update_prompt(
    62,
    "In the shadowy halls of the Undercity, an Orc female warlock delves into ancient tomes of forbidden knowledge. Her hair, as dark as the abyss, is tied back to reveal sharp features hardened by battles. Around her, eldritch symbols glow, a testament to her mastery over the dark arts.",
)
add_or_update_prompt(
    63,
    "Amidst the chaos of a battleground, an Orc female warlock chants incantations, summoning demons to her side. Her muscular frame is clad in ornate, dark armor, etched with runes. The air around her crackles with arcane power, her presence a formidable force on the battlefield.",
)

add_or_update_prompt(
    64,
    "Malfurion Stormrage, the Archdruid, stands solemnly in the heart of the Dreamgrove, his antlers silhouetted against the moonlit sky. His eyes, deep pools of wisdom, survey the tranquil forest, as ancient trees whisper secrets only he can understand.",
)
add_or_update_prompt(
    65,
    "In the midst of a fierce storm in Darkshore, Malfurion Stormrage calls upon the raw power of nature, his hands raised high. Lightning illuminates his determined face and the intricate tattoos that mark him as a protector of Azeroth, the wind howling his name.",
)
add_or_update_prompt(
    66,
    "Malfurion Stormrage, in his raven form, glides over Mount Hyjal, his shadow passing over the World Tree. Transforming back to his true self, he lands gracefully, his presence a beacon of hope and strength to the defenders gathered below, ready to face the coming darkness.",
)

add_or_update_prompt(
    67,
    "In the dimly lit, underground laboratory of the Undercity, a male Forsaken alchemist meticulously combines volatile concoctions. His skeletal fingers are steady, despite the ever-present threat of explosion, his glowing eyes fixed on the bubbling potions before him.",
)
add_or_update_prompt(
    68,
    "Surrounded by vials of eerily glowing liquids and ancient alchemical tomes, a male Forsaken alchemist experiments with forbidden recipes. The air is thick with the scent of brimstone and decay, his workbench a testament to the relentless pursuit of knowledge, even in undeath.",
)
add_or_update_prompt(
    69,
    "A male Forsaken alchemist stands before a grand cauldron in the Apothecarium, chanting incantations as he works to perfect a plague capable of turning the tide of war. His tattered robes flutter as he moves, his dedication to the dark arts undiminished by his physical decay.",
)

add_or_update_prompt(
    70,
    "A warlock's succubus stands in the shadows of a crumbling ruin, her form both menacing and beguiling. The moonlight reflects off her leathery wings and the whip in her hand, her eyes glowing with a predatory light as she surveys her domain.",
)
add_or_update_prompt(
    71,
    "In the depths of a darkened forest, a succubus whispers seductive enchantments, her voice carrying through the trees. Surrounded by a faint, demonic aura, she practices her charms, ensuring her loyalty to her warlock master through the manipulation of her foes.",
)
add_or_update_prompt(
    72,
    "Perched atop a desolate cliff, a succubus gazes into the night sky, her thoughts inscrutable. The wind tugs at her hair and wings, the isolation of her vigil emphasizing her eternal bond to the arcane energies that summoned her.",
)

add_or_update_prompt(
    73,
    "In the flickering light of a secluded workshop, an attractive gnome warlock pours over ancient tomes, her succubus guardian watching over her intently. Their bond is palpable, a complex weave of control, loyalty, and dark ambition.",
)
add_or_update_prompt(
    74,
    "A gnome warlock, striking in her beauty and power, stands at the forefront of a battlefield, her succubus by her side. Together, they unleash havoc upon their enemies, a perfect symphony of destruction, their connection unbreakable.",
)
add_or_update_prompt(
    75,
    "Under the canopy of an enchanted forest, a gnome warlock and her succubus share a moment of quiet contemplation. The succubus listens as her master strategizes their next move, her presence both a comfort and a deadly promise to those who would cross them.",
)

add_or_update_prompt(
    76,
    "Cairne Bloodhoof, the venerable chieftain of the Tauren, stands atop the rise of Thunder Bluff, looking out over the vast, rolling plains of Mulgore. His stance is steady, like the ancient mountains, reflecting his deep connection to the earth and his people.",
)
add_or_update_prompt(
    77,
    "In the heart of a sacred grove, Cairne Bloodhoof performs a ritual of thanks to the Earth Mother. Surrounded by the tranquil sounds of nature, his voice carries the weight of his people's hopes and dreams, his great totem staff planted firmly in the ground beside him.",
)
add_or_update_prompt(
    78,
    "Cairne Bloodhoof, in the midst of battle, swings his mighty totem with a strength that belies his age. Each move is precise, a testament to decades of experience as both warrior and leader, his commitment to his people's survival evident in every action.",
)

add_or_update_prompt(
    79,
    "In the shadowy corridors of a Nether fortress, a Dreadlord plots the next phase of the Burning Legion's invasion. His bat-like wings fold behind him as he leans over maps of Azeroth, his red eyes glowing with malevolence and intelligence.",
)
add_or_update_prompt(
    80,
    "A Dreadlord stands atop a ruined battlement, surveying the chaos below with a sinister grin. The night air is filled with the sounds of battle, but he remains untouched, a master of manipulation and strategy, orchestrating the downfall of his enemies from the shadows.",
)
add_or_update_prompt(
    81,
    "Amidst the swirling mists of the Twisting Nether, a Dreadlord convenes with his demonic brethren. His commanding presence is undeniable, even among the legions of the damned, his voice a dark promise of power and destruction to any who dare oppose him.",
)

add_or_update_prompt(
    82,
    "In the frostbitten valleys of Dun Morogh, a Dwarf hunter tracks a mighty bear, his breath visible in the cold air. The snow crunches underfoot, his rifle ready, as the majestic peaks of Ironforge loom in the distance, a symbol of Dwarf resilience.",
)
add_or_update_prompt(
    83,
    "A group of Dwarves gathers around a crackling fire in Loch Modan, their laughter echoing off the Thandol Span. They share tales of ancient battles and lost treasures, their stout figures casting long shadows in the flickering light, the tranquil lake a silent witness.",
)
add_or_update_prompt(
    84,
    "Deep within the stone halls of Ironforge, a Dwarf blacksmith hammers away at a glowing piece of steel, sparks flying. Around him, the great forges roar, the heart of the mountain alive with the sound of creation, the air thick with heat and the promise of new adventures.",
)
add_or_update_prompt(
    85,
    "On the snowy slopes of Dun Morogh, a Dwarf paladin kneels in prayer, the Light illuminating the surrounding peaks. His hammer rests beside him, etched with runes, a testament to his faith and the ancient bond between the Dwarves and the Light.",
)
add_or_update_prompt(
    86,
    "A Dwarf engineer in Loch Modan tests her latest invention, a steam-powered contraption sputtering and whirring. Her goggles reflect the excitement of innovation, the serene loch providing a picturesque backdrop for a breakthrough moment.",
)
add_or_update_prompt(
    87,
    "At the Stoutlager Inn, Dwarves of all professions share a hearty meal, their spirits high. Outside, the landscape of Loch Modan stretches out, peaceful yet full of untold stories, the Dwarves' laughter a melody that speaks of deep bonds and the warmth of hearth and home.",
)

add_or_update_prompt(
    88,
    "In the technologically marvel-laden halls of Gnomeregan, a gnome tinkerer works late into the night. Surrounded by blueprints and gadgets, she fine-tunes a robotic companion, her focus unwavering, the soft hum of machinery a constant companion.",
)
add_or_update_prompt(
    89,
    "A gnome mage experiments with arcane energies in a secluded lab within Gnomeregan. The air crackles with magic as she conjures vibrant, swirling portals, her diminutive stature belied by the immense power at her fingertips.",
)
add_or_update_prompt(
    90,
    "Deep beneath the surface, a gnome adventurer navigates the intricate corridors of Gnomeregan, a headlamp illuminating ancient runes and steam pipes. Each step reveals the wonders and dangers of gnome engineering, the thrill of discovery pushing her forward.",
)
add_or_update_prompt(
    91,
    "In a bustling workshop, a team of gnome engineers collaborates on a revolutionary flying machine. The air is filled with the sounds of welding and laughter, their collective genius forging a new chapter in the annals of gnome innovation.",
)
add_or_update_prompt(
    92,
    "A gnome warrior, armed with a mechanized exoskeleton, trains in the depths of Gnomeregan. His movements are swift and precise, a dance of metal and might, preparing to reclaim their home from the troggs that have overrun it.",
)
add_or_update_prompt(
    93,
    "At the heart of Gnomeregan, the High Tinker addresses a gathering of gnomes, his voice echoing through the vast chambers. Around him, screens and monitors flicker to life, displaying plans for the future, a testament to the resilience and ingenuity of the gnome race.",
)

add_or_update_prompt(
    94,
    "Beneath the canopy of Ashenvale's ancient forest, a Night Elf sentinel moves silently, her bow drawn. The moonlight filters through the leaves, casting dappled shadows, her keen eyes watching for signs of intrusion into their sacred lands.",
)
add_or_update_prompt(
    95,
    "A Night Elf priestess stands before the Moonwell, her hands raised in prayer. The serene waters glow with a soft light, reflecting the stars above, as she seeks Elune's guidance to protect her people and the forest they call home.",
)
add_or_update_prompt(
    96,
    "In the twilight of Ashenvale, a Night Elf rogue scouts an enemy camp. Cloaked in shadows, she moves with grace, her blades ready to defend her homeland against those who would desecrate its beauty.",
)
add_or_update_prompt(
    97,
    "Night Elf archers gather in a clearing, practicing their marksmanship. Their arrows fly true, a testament to their people's connection to the forest and their unwavering dedication to hone their skills for the defense of Ashenvale.",
)
add_or_update_prompt(
    98,
    "A Night Elf druid, in the form of a majestic stag, roams the forest paths of Ashenvale. He pauses to drink from a stream, the tranquility of the forest a stark contrast to the battles fought to preserve it.",
)
add_or_update_prompt(
    99,
    "As night falls on Ashenvale, a group of Night Elves gather around a bonfire, sharing stories of ancient heroes and battles past. Their laughter and songs blend with the sounds of the forest, a celebration of their rich heritage and enduring spirit.",
)


add_or_update_prompt(
    100,
    "In the heart of Felwood, a circle of Night Elf druids concentrates their power, their hands joined as they channel nature's energy to cleanse the land. The corruption recedes inch by inch, their determination a beacon of hope in the blighted forest.",
)
add_or_update_prompt(
    101,
    "A Night Elf druid kneels beside a corrupted stream, whispering ancient incantations. Slowly, the water clears, life returning to its banks, a testament to the druids' relentless fight against the taint that plagues Felwood.",
)
add_or_update_prompt(
    102,
    "Amidst the twisted trees of Felwood, a Night Elf druid summons the spirits of nature. They work together, healing the wounded earth, their efforts slowly undoing the damage wrought by demonic corruption.",
)
add_or_update_prompt(
    103,
    "On a moonlit night, Night Elf druids perform a sacred ritual in a glade within Felwood. The ground pulses with renewed life, flowers blooming instantaneously, a sign of the forest's slow recovery from the fel's grip.",
)
add_or_update_prompt(
    104,
    "A lone Night Elf druid wanders through Felwood, planting seeds of powerful, cleansing herbs in the corrupted soil. Each seedling is a step towards healing, the druid's connection to the land guiding his every move.",
)
add_or_update_prompt(
    105,
    "Night Elf druids gather at the ruins of a once-vibrant grove in Felwood. With focused intent, they restore its vitality, the grove's revival a symbol of the resilience of nature and the druids' unwavering commitment to restoration.",
)

add_or_update_prompt(
    106,
    "In the sprawling plains of Mulgore, a Tauren shaman calls upon the spirits of the earth under a vast, open sky. His deep connection to the land is evident as the wind responds, the grasses whispering ancient tales of the Earth Mother.",
)
add_or_update_prompt(
    107,
    "Atop the towering mesas of Thunder Bluff, a Tauren chieftain overlooks his homeland, the wind tugging at his cloak. The city thrives below, a testament to the Tauren's resilience and their deep bond with the natural world.",
)
add_or_update_prompt(
    108,
    "A Tauren hunter moves silently through the tall grass of Mulgore, tracking her prey with practiced ease. The sun sets behind her, casting long shadows, her connection to the land guiding her steps.",
)
add_or_update_prompt(
    109,
    "Within the sacred halls of a Thunder Bluff totemic temple, a Tauren priest prays for guidance. The air is filled with the scent of sweetgrass, the peaceful atmosphere a reflection of the Tauren's spiritual depth.",
)
add_or_update_prompt(
    110,
    "A Tauren artisan crafts a leather drum in the shade of a towering bluff, the rhythmic sounds echoing through Mulgore. Each beat is a homage to the Earth Mother, his work a blend of artistry and reverence for nature.",
)
add_or_update_prompt(
    111,
    "A group of young Tauren gather around a bonfire in Thunder Bluff, sharing stories and songs of their ancestors. The night sky is clear and full of stars, their laughter and camaraderie a celebration of their rich cultural heritage.",
)

add_or_update_prompt(
    112,
    "In the arid lands of Durotar, an Orc warrior and a Troll hunter stand side by side, gazing into the horizon. The red sands at their feet, they discuss strategies to defend their land against encroaching threats, their alliance as strong as the harsh landscape around them.",
)
add_or_update_prompt(
    113,
    "A group of Troll shamans perform a vibrant ritual by the banks of the Southfury River, their chants blending with the rush of water. Orcs gather around, drawn by the powerful display of spirituality, the bonds between the two races reinforced by shared reverence for the elements.",
)
add_or_update_prompt(
    114,
    "An Orc blacksmith hammers away in a forge within Razor Hill, his Troll apprentice by his side. Together, they craft weapons that blend Orcish strength with Troll cunning, the air around them alive with the sound of creation and the warmth of the forge.",
)
add_or_update_prompt(
    115,
    "Under the sweltering sun of Durotar, Orc and Troll warriors train together, their shouts and the clash of weapons a testament to their determination. The harsh, unforgiving landscape serves as the perfect backdrop for their rigorous preparation.",
)
add_or_update_prompt(
    116,
    "In a quiet corner of the Echo Isles, a Troll voodoo priest shares ancient lore with a group of young Orcs. The mystical tales, full of magic and mystery, weave a spell over the listeners, uniting them in awe and a deep sense of kinship.",
)
add_or_update_prompt(
    117,
    "As dusk falls over Durotar, an Orc and a Troll sit by a fire, sharing stories of battles fought and adventures had. The crackling flames and the stark, beautiful landscape around them serve as a reminder of their shared struggles and victories.",
)

add_or_update_prompt(
    118,
    "In the eerie quiet of Tirisfal Glades, a Forsaken apothecary experiments with new potions in Brill. The glow from his concoctions illuminates the surrounding decay, a symbol of the Forsaken's relentless pursuit of power and independence.",
)
add_or_update_prompt(
    119,
    "A group of Undead Forsaken gather in the ruins of Brill in tirisfal glades, dark forest green hue, plotting their next move against their enemies. Their voices, a whisper among the tombstones, speak of resilience and a fierce desire to claim their place in a world that has shunned them.",
)
add_or_update_prompt(
    120,
    "In the shadow of the Undercity, a Forsaken rogue trains in the art of stealth and assassination. The damp, mist-covered grounds of Tirisfal Glades provide the perfect setting for honing skills that are as much about survival as they are about vengeance.",
)
add_or_update_prompt(
    121,
    "By the light of the moon, a Forsaken priest in Brill prays to the forgotten gods, seeking guidance for her people. Around her, the twisted trees of Tirisfal Glades seem to listen, the land itself a reflection of the Forsaken's tormented souls.",
)
add_or_update_prompt(
    122,
    "A Forsaken warlock delves into dark magic within an abandoned crypt in Tirisfal Glades. His incantations, powerful and forbidden, echo through the halls, drawing curious, unseen watchers from the shadows.",
)
add_or_update_prompt(
    123,
    "The streets of Brill teem with life after death as the Forsaken prepare for the upcoming battle. Armor is donned, weapons sharpened, and vows renewed, their shared undeath a grim bond that ties them together in their quest for vengeance and autonomy.",
)

add_or_update_prompt(
    124,
    "At the vibrant Midsummer Fire Festival, races from all over Azeroth gather around towering bonfires. An Orc and a Human compete in a friendly ribbon pole dance-off, their laughter echoing as Draenei and Goblins play festive drums, the night alight with unity and celebration.",
)
add_or_update_prompt(
    125,
    "On the serene banks of Elwynn Forest, a Tauren and a Night Elf share a quiet moment of fishing. They exchange tips on bait and tales of the one that got away, their cultural differences set aside in the tranquil pursuit of the day's catch.",
)
add_or_update_prompt(
    126,
    "Inside the cozy interior of the Lion's Pride Inn, a group of adventurers from various races huddle over a Hearthstone board. Gnomes, Blood Elves, and Worgen strategize and jest, the competitive spirit tempered by friendly camaraderie and the clinking of tankards.",
)
add_or_update_prompt(
    127,
    "During the lively Brewfest, Dwarves lead the charge in ale tasting, inviting Undead Forsaken and Pandaren to join. The sounds of merriment fill the air as they share brews from across Azeroth, their differences drowned in the universal language of good cheer.",
)
add_or_update_prompt(
    128,
    "In the bustling marketplace of Dalaran, members of different races gather for an impromptu cooking competition. Orcs chop vegetables alongside Nightborne, while Trolls and Humans grill exotic meats, their cooperation turning the contest into a feast for all.",
)
add_or_update_prompt(
    129,
    "At the annual Darkmoon Faire, races from every corner of Azeroth try their hand at games of skill and chance. A Gnome and a Tauren laugh uproariously as they race Darkmoon Striders, their unlikely friendship a testament to the fair's magical ability to bring everyone together.",
)

add_or_update_prompt(
    130,
    "Ashenvale: A panoramic view of Ashenvale's dense, mystical forest, with Night Elves patrolling the verdant pathways. Ancient trees tower over serene moonwells, their roots entwined with the land's magic, the distant howl of wolves echoing through the foliage.",
)
add_or_update_prompt(
    131,
    "Elwynn Forest: The sun filters through the leaves in Elwynn Forest, casting a warm glow over Goldshire. Humans and visiting adventurers mingle, the buzz of daily life against a backdrop of tranquil rivers, bustling farms, and the distant, majestic spires of Stormwind.",
)
add_or_update_prompt(
    132,
    "Felwood: Felwood's once-verdant lands now bear the scars of corruption, with twisted trees and sickly mists. Brave Druids work to heal the land, their efforts a beacon of hope amidst the spreading taint, with the occasional battle against encroaching demons.",
)
add_or_update_prompt(
    133,
    "The Barrens: The vast, sun-baked plains of the Barrens stretch out, a meeting point for travelers and caravans. Horde banners fly over Crossroads, where Orcs, Tauren, and Trolls gather, the air filled with the calls of wild beasts and the distant rumble of kodo herds.",
)
add_or_update_prompt(
    134,
    "Tirisfal Glades: A haunting beauty pervades Tirisfal Glades, the eerie light casting long shadows over Brill. Forsaken move about their tasks, their resilience palpable in the face of the chilling atmosphere and the towering ruins of the Undercity.",
)
add_or_update_prompt(
    135,
    "Azshara: Azshara's rugged landscapes are dotted with ancient ruins and bizarre naga architecture. Goblins experiment with reckless innovations by the coast, their machinery contrasting with the natural beauty and the arcane mysteries hidden within the zone.",
)
add_or_update_prompt(
    136,
    "Westfall: The golden fields of Westfall sway under the azure sky, the land marked by the struggles of the Defias Brotherhood. Farmers toil in the fields, their work a testament to the resilience of the human spirit amidst hardship and the ruins of old battles.",
)
add_or_update_prompt(
    137,
    "Duskwood: Duskwood's perpetual twilight lends an air of mystery, the shadows alive with unseen dangers. Brave adventurers tread carefully among the gnarled trees, the glowing eyes of wolves and worse watching from the darkness.",
)
add_or_update_prompt(
    138,
    "Stranglethorn Vale: The dense jungle of Stranglethorn Vale teems with life, the roar of waterfalls and the calls of exotic beasts filling the air. Troll ruins stand silent among the foliage, a reminder of ancient empires, as both Horde and Alliance adventurers navigate the perilous paths.",
)
add_or_update_prompt(
    139,
    "Arathi Highlands: Arathi Highlands, with its rolling hills and strategic battlegrounds, is a land of conflict and beauty. The ancient Stromgarde Keep stands as a testament to human tenacity, while the Circle of Elements whispers of older magics.",
)
add_or_update_prompt(
    140,
    "Mulgore: The sweeping grasslands of Mulgore offer a vista of peace and serenity, the towering Thunder Bluff a symbol of Tauren culture. Herds of plains animals roam freely, the rhythm of drums and the scent of sage filling the air.",
)
add_or_update_prompt(
    141,
    "Stormwind: Stormwind's grand architecture and bustling streets exemplify human resilience and ingenuity. The city's defenders stand vigilant on the walls, while citizens of all races gather in the Trade District, the heart of Alliance commerce and diplomacy.",
)


add_or_update_prompt(
    142,
    "In the heart of Silvermoon, a Blood Elf Mage conjures arcane energies, her focus unwavering as she prepares to defend her people. Her elegance is matched by her formidable power, a beacon of hope and strength for her allies.",
)

add_or_update_prompt(
    143,
    "On the snowy battlefields of Alterac Valley, a Human Paladin stands resolute, her armor gleaming in the frosty air. She raises her hammer high, a symbol of the Light's enduring justice, inspiring those around her with her bravery and conviction.",
)

add_or_update_prompt(
    144,
    "Deep within the lush jungles of Stranglethorn Vale, a Troll Priestess communes with the Loa, her vibrant tattoos a testament to her spiritual journey. Her wisdom and compassion guide her tribe, her presence a calming force amidst the chaos of the wilds.",
)

add_or_update_prompt(
    145,
    "Atop the windswept cliffs of Howling Fjord, a Dwarf Hunter surveys the land with her eagle-eyed gaze. Accompanied by her loyal bear companion, she navigates the rugged terrain with ease, a master of survival and a protector of her clan's ancestral lands.",
)

add_or_update_prompt(
    146,
    "In the mystical groves of Teldrassil, a Night Elf Druid shifts into the form of a majestic panther, her grace and agility unmatched. She is a guardian of nature, her deep connection to the Emerald Dream guiding her efforts to heal and protect Azeroth.",
)

add_or_update_prompt(
    147,
    "Amidst the engineering marvels of Gnomeregan, a Gnome Warrior, surprisingly formidable for her size, tinkers with her armor and weaponry. Her ingenuity and fearless spirit make her a formidable opponent, proving that true strength comes from within.",
)

add_or_update_prompt(
    148,
    "On the shimmering shores of the Crystal Lake in Elwynn Forest, a Draenei Shaman calls forth the elements, her serene demeanor belied by the storm of power at her command. She seeks harmony between her people and their new home, a beacon of hope in a strange land.",
)

add_or_update_prompt(
    149,
    "In the heart of the Undercity, a Forsaken Warlock delves into forbidden knowledge, her pursuit of power undeterred by her undead state. Her dark elegance and fierce determination strike both awe and fear in the hearts of her foes.",
)

add_or_update_prompt(
    150,
    "Among the golden plains of Mulgore, a Tauren Warrior stands tall, her strength and endurance a proud representation of her people. She is a defender of the peace and a steadfast ally in battle, her horned silhouette iconic against the setting sun.",
)

add_or_update_prompt(
    151,
    "Within the bustling streets of Stormwind, a Worgen Rogue melds into the shadows, her dual identity a perfect blend of human cunning and feral instinct. She navigates the complexities of her existence with grace, a mysterious figure in the city's underbelly.",
)

add_or_update_prompt(
    152,
    "At the edge of the Dark Portal, an Orc Death Knight holds the line against the demonic onslaught. Her presence is both fearsome and awe-inspiring, a testament to the battles she has endured and the strength she has gained from them.",
)

add_or_update_prompt(
    153,
    "In the enchanted woods of Suramar, a Nightborne Sorceress weaves spells of breathtaking complexity, her knowledge of the arcane deep and ancient. Her elegance and power are reminiscent of her people's glorious past, a shining example of their enduring legacy.",
)

add_or_update_prompt(
    154,
    "A Gnome Rogue vanishes into the shadows of Ironforge's alleyways, her agility and cunning making her an invaluable asset to the Alliance. Her small stature belies her deadly skill, a whisper of danger to her foes.",
)

add_or_update_prompt(
    155,
    "A Human Priest, radiating the Light's grace, heals wounded soldiers in the cathedral of Stormwind. Her prayers offer solace and strength, embodying the spirit of compassion and resilience that defines her order.",
)

add_or_update_prompt(
    156,
    "An Undead Mage channels frost and fire in the ruins of Lordaeron, her arcane mastery a chilling reminder of the Forsaken's power and their place in the Horde. Her spells weave destruction and awe in equal measure.",
)

add_or_update_prompt(
    157,
    "An Orc Warrior, battle-axe in hand, leads a charge against the Alliance in the dusty plains of Durotar. His fierce war cries and unmatched strength inspire his comrades to fight with unyielding vigor.",
)

add_or_update_prompt(
    158,
    "A Draenei Paladin, wielding the Light's hammer, stands as a beacon of hope against the shadows on Argus. Her conviction and the shimmering aura of her armor light the way for her people, a testament to their enduring faith.",
)

add_or_update_prompt(
    159,
    "A Blood Elf Warlock, delving into fel magic within the spires of Silvermoon, commands demonic forces with a mix of allure and terror. Her pursuit of power is both a peril and a promise to her kin.",
)

add_or_update_prompt(
    160,
    "A Night Elf Hunter, accompanied by her loyal pet saber, stalks through the forests of Ashenvale. Her connection with the natural world makes her a deadly predator and a guardian of her people's sacred lands.",
)

add_or_update_prompt(
    161,
    "A Tauren Shaman, calling upon the spirits beside the tranquil waters of Mulgore, seeks balance and healing for the land. His deep bond with the elements reflects the Tauren's reverence for nature and the Earth Mother.",
)

add_or_update_prompt(
    162,
    "A Worgen Druid, shifting forms beneath the canopy of Duskwood, protects the realm from encroaching darkness. Her mastery over nature's wrath and bounty is a fierce declaration of the Gilneans' resilience.",
)

add_or_update_prompt(
    163,
    "A Pandaren Monk, practicing ancient martial arts atop the misty peaks of Kun-Lai Summit, embodies harmony and discipline. His journey is one of self-discovery and the pursuit of balance in all things.",
)

add_or_update_prompt(
    164,
    "A Night Elf Demon Hunter, her eyes ablaze with fel fire, hunts her prey in the shattered landscape of Outland. Her sacrifice and the spectral wings that carry her speak of a relentless pursuit of vengeance against the Legion.",
)

add_or_update_prompt(
    165,
    "An Orc Death Knight, raised by the Lich King, wields the power of frost and shadow in the icy reaches of Northrend. His formidable presence is a stark reminder of the Scourge's legacy and the eternal struggle against death itself.",
)

add_or_update_prompt(
    166,
    "In the murky waters of the Wetlands, a group of Crocolisks bask on the riverbank, their eyes just above the waterline, watching adventurers pass with deceptive lethargy, a sudden burst of speed always ready.",
)

add_or_update_prompt(
    167,
    "Through the snow-covered plains of Winterspring, a pack of Dire Wolves moves silently, their thick fur blending with the icy landscape. Their howls echo in the crisp air, a haunting melody of the north.",
)

add_or_update_prompt(
    168,
    "In the shadowy recesses of the Eastern Plaguelands, giant bats swoop and dive, navigating the ruins with eerie precision. Their silent wings are a whisper in the night, a ghostly presence among the devastation.",
)

add_or_update_prompt(
    169,
    "On the savannas of the Barrens, a herd of Giraffes grazes peacefully, their long necks reaching for the sparse treetops. Their serene presence brings a moment of calm to the otherwise harsh environment.",
)

add_or_update_prompt(
    170,
    "In the dense jungles of Stranglethorn Vale, Raptors hunt in packs, their colorful feathers a stark contrast to their ferocious nature. The rustling leaves often betray their presence to wary travelers.",
)

add_or_update_prompt(
    171,
    "Soaring above the cliffs of Azsuna, Hippogriffs glide with grace, their keen eyes scanning the ground below. Their majestic forms are a common sight, embodying the freedom of the skies.",
)

add_or_update_prompt(
    172,
    "In the crystal-clear waters of the Vale of Eternal Blossoms, Koi fish swim in serene patterns, their scales shimmering in the sunlight. They bring a sense of tranquility to the sacred pools.",
)

add_or_update_prompt(
    173,
    "Amidst the ancient ruins of Uldum, a pack of Hyenas laughs in the heat of the sun, their cackles filling the air as they scavenge the sands for any morsel, a reminder of the desert's harsh reality.",
)

add_or_update_prompt(
    174,
    "On the frostbitten landscape of Northrend, a mammoth lumbers through the snow, its massive form a testament to the resilience required to survive in such a brutal climate, a gentle giant of the frozen wastes.",
)

add_or_update_prompt(
    175,
    "In the vibrant ecosystem of Zangarmarsh, Sporebats float lazily among the giant mushrooms, their bioluminescent bodies adding to the area's otherworldly glow, a delicate balance of life in the marsh.",
)

add_or_update_prompt(
    176,
    "Roaming the rolling hills of Nagrand, a herd of Talbuks moves with elegant agility, their horns glistening under the sun. They embody the untamed beauty of Draenor, swift and free.",
)

add_or_update_prompt(
    177,
    "In the shadowed woods of Teldrassil, a family of Moonkin conducts a silent ritual under the moonlight, their figures both odd and endearing. They are the forest's eccentric guardians, shrouded in mystery.",
)

add_or_update_prompt(
    178,
    "In the fiery depths of the Molten Core, Imps scurry about, their cackles echoing off the walls. The small but fiery creatures serve their masters with a mischievous zeal, their flames dancing in the dark.",
)

add_or_update_prompt(
    179,
    "Voidwalkers roam the shattered landscape of Outland, their formless bodies pulsing with dark energy. Summoned from the void, they guard their warlock masters with unwavering loyalty, a silent sentinel against the chaos.",
)

add_or_update_prompt(
    180,
    "Felhunters slink through the ruins of a Draenei temple, sniffing out sources of magic with predatory efficiency. Their presence is a bane to spellcasters, a living embodiment of the Legion's desire to consume all arcane knowledge.",
)

add_or_update_prompt(
    181,
    "Succubi, with their alluring and deadly charm, weave through the ranks of the Burning Legion. In the twisted forests of Felwood, they use seduction as a weapon, leaving a trail of bewitched foes in their wake.",
)

add_or_update_prompt(
    182,
    "Infernals crash down upon the battlegrounds of Azeroth, their meteoric descent a herald of doom. The ground trembles under their weight in Ashenvale, the sky alight with their fiery form, a symbol of the Legion's might.",
)

add_or_update_prompt(
    183,
    "Doomguards stand tall over the ruins of a Night Elf outpost, their massive swords dripping with the blood of their enemies. Their terrifying visage is a testament to the Legion's power, a force of destruction unleashed.",
)

add_or_update_prompt(
    184,
    "Eredar sorcerers chant dark incantations in the depths of the Twisting Nether, their magic twisting the fabric of reality. Their cunning and power make them feared leaders within the demonic ranks, architects of the Legion's conquests.",
)

add_or_update_prompt(
    185,
    "Shivarra priestesses dance a deadly ritual in the shadow of the Black Temple, their six arms wielding blades with lethal grace. They inspire the demonic hordes with fervor, a mesmerizing force of chaos.",
)

add_or_update_prompt(
    186,
    "Gan'arg engineers tinker with fel machinery in the Hellfire Peninsula, their inventions a twisted mirror of Gnomish ingenuity. The smoke and clank of their work fills the air, a testament to the Legion's technological prowess.",
)

add_or_update_prompt(
    187,
    "Wrathguards patrol the broken isles of Argus, their eyes ablaze with fel fire. As frontline soldiers of the Legion, their ferocity in battle is unmatched, a relentless tide of rage and steel.",
)

add_or_update_prompt(
    188,
    "Nathrezim, or Dreadlords, scheme in the shadows, their plots a web of deceit that spans worlds. In the royal courts of Lordaeron, their influence festers, a reminder of the Legion's reach into the hearts of mortals.",
)

add_or_update_prompt(
    189,
    "Man'ari Eredar stride through the ranks of their lesser kin, their presence commanding awe and fear. On the battlefields of Mac'Aree, they wield magic and might, a testament to the twisted glory of their race.",
)

add_or_update_prompt(
    190,
    "Air Elementals dance across the sky above the Arathi Highlands, their forms shifting and twisting with the wind. They play among the clouds, a ballet of gusts and breezes, embodying the freedom of the open air.",
)

add_or_update_prompt(
    191,
    "Fire Elementals rage within the heart of Blackrock Mountain, their flames casting an ominous glow. The heat from their fiery bodies warms the cavernous depths, a constant reminder of the mountain's volcanic fury.",
)

add_or_update_prompt(
    192,
    "Water Elementals glide through the waters of Lake Elune'ara in Moonglade, their liquid forms merging with the serene lake. They ripple gently across the surface, guardians of the sacred waters and the secrets they hold.",
)

add_or_update_prompt(
    193,
    "Earth Elementals lumber through the canyons of Thousand Needles, their rocky forms blending with the rugged terrain. They carve new paths with each step, the very embodiment of the earth's raw power and majesty.",
)

add_or_update_prompt(
    194,
    "Treants wander the forests of Ashenvale, their wooden limbs creaking softly. As protectors of the woodlands, they move with a grace that belies their size, a living testament to the forest's ancient strength.",
)

add_or_update_prompt(
    195,
    "In the swirling sands of Silithus, Sand Elementals emerge from the dunes, their forms barely distinguishable from the desert around them. They are the whisper of the wind over sand, a fleeting presence in the vast emptiness.",
)

add_or_update_prompt(
    196,
    "Ice Elementals haunt the glaciers of Northrend, their crystalline bodies shimmering in the cold light. They drift silently among the ice floes, a chilling reminder of the north's frozen heart.",
)

add_or_update_prompt(
    197,
    "Storm Elementals roar across the tempestuous seas surrounding Kul Tiras, their thunderous voices heralding squalls and gales. They are the wrath of the storm personified, a force of nature that bends to no will but their own.",
)

add_or_update_prompt(
    198,
    "Magma Elementals surge from the depths of the Firelands, their bodies aglow with molten rock. They are born of the world's fiery core, a relentless tide of destruction that scorches everything in their path.",
)

add_or_update_prompt(
    199,
    "Frost Elementals glide through the wintry forests of Winterspring, leaving trails of frost in their wake. They embody the silent, creeping cold of the longest nights, a serene but deadly aspect of winter's embrace.",
)

add_or_update_prompt(
    200,
    "Lightning Elementals crackle with energy atop the Storm Peaks, their forms a blur of motion and light. They are the sudden flash in the dark sky, the electric pulse of the storm's heart, alive with the thrill of the tempest.",
)

add_or_update_prompt(
    201,
    "Mud Elementals seep from the wetlands of the Swamp of Sorrows, their forms thick and dripping. They move with a slow, inexorable will, a manifestation of the earth and water's muddied embrace.",
)

add_or_update_prompt(
    202,
    "Worgen prowl the fog-laden streets of Gilneas, their forms a blend of man and beast. In the moonlight, their howls resonate, a haunting reminder of the curse that transformed them.",
)

add_or_update_prompt(
    203,
    "Naga slither through the underwater ruins off the coast of Azshara, their serpentine bodies gliding gracefully. They guard ancient secrets with ferocity, remnants of a once-mighty empire.",
)

add_or_update_prompt(
    204,
    "Centaur herds thunder across the arid lands of Desolace, their hooves kicking up clouds of dust. Dominating the landscape, they clash with intruders, fiercely protective of their territory.",
)

add_or_update_prompt(
    205,
    "Dryads flit through the woods of Ashenvale, their laughter light and ethereal. Guardians of nature, they move with a grace that enchants all who behold them, embodying the forest's serene beauty.",
)

add_or_update_prompt(
    206,
    "Kobolds scurry through the dark tunnels beneath Elwynn Forest, their candles flickering. Jealously guarding their tunnels and treasures, they're quick to warn off adventurers with a timid yet firm 'You no take candle!'",
)

add_or_update_prompt(
    207,
    "Gnolls maraud through the rolling fields of Westfall, their camps a mishmash of stolen goods and makeshift shelters. They prey on the weak, driven by hunger and a rudimentary sense of conquest.",
)

add_or_update_prompt(
    208,
    "Murlocs swarm the shores of Darkshore, their gurgling calls a familiar sound to any who venture near the water. In groups, they defend their coastal homes with surprising ferocity and coordination.",
)

add_or_update_prompt(
    209,
    "Quilboar, bristling with spikes, fortify the thorn-ridden paths of Razorfen Downs. United under tribal banners, they fight with a fanaticism born of their devotion to the demigod Agamaggan.",
)

add_or_update_prompt(
    210,
    "Troggs, carved from the very rock of Deepholm, infest the caves and tunnels of Azeroth. Primitive and aggressive, they clash with anyone who dares disturb their stony domain.",
)

add_or_update_prompt(
    211,
    "Vrykul, towering and fierce, rule over the Howling Fjord with an iron grip. Their Viking-like culture is marked by raids, battles, and a quest for glory, honoring their gods through combat.",
)

add_or_update_prompt(
    212,
    "Harpy flocks screech across the skies of Stonetalon Mountains, their nests perched high above. They swoop down on unsuspecting travelers, their motives as capricious as the wind.",
)

add_or_update_prompt(
    213,
    "Satyrs stalk the night in Felwood, corrupted by demonic magic. Their twisted forms are a dark mirror to their once-noble origins, now reveling in chaos and destruction.",
)

add_or_update_prompt(
    214,
    "Goblin Shredders tear through the forests of Ashenvale, their saws buzzing as they cut down ancient trees. Piloted by goblins with a penchant for destruction, they represent the invasive impact of industrial greed on nature.",
)
add_or_update_prompt(
    215,
    "Fel Reavers stomp across the Hellfire Peninsula, their massive forms casting shadows over the blasted landscape. These mechanical behemoths, powered by dark energies, leave a trail of devastation, a testament to the Legion's might.",
)
add_or_update_prompt(
    216,
    "In the depths of Gnomeregan, automated defense systems spring to life, targeting intruders with deadly precision. These machines, remnants of gnomish ingenuity, guard the halls against those who would uncover the city's secrets.",
)
add_or_update_prompt(
    217,
    "Arcane Golems patrol the streets of Dalaran, their crystalline bodies shimmering with magical energy. Created to serve and protect, they navigate the city with an eerie silence, ever watchful for disturbances in the peace.",
)
add_or_update_prompt(
    218,
    "Mechanostriders clank through the snowy paths of Dun Morogh, ridden by daring gnomes and dwarves. These mechanical mounts, a marvel of engineering, symbolize the alliance between the two races and their shared love for invention.",
)
add_or_update_prompt(
    219,
    "Dark Iron Dwarves deploy War Golems in the seething heart of Blackrock Depths, their molten fists capable of crushing stone. Forged in the fires of the mountain, they are both weapons of war and symbols of the Dark Iron's mastery over flame and metal.",
)

add_or_update_prompt(
    220,
    "Crypt Lords emerge from the depths of Azjol-Nerub, their carapaces hard as stone. Commanding legions of undead, they strike fear into the hearts of their foes, a dark reminder of the Lich King's power.",
)
add_or_update_prompt(
    221,
    "Ghouls scavenge the battlefields of the Eastern Plaguelands, their grotesque forms a ghastly sight. Driven by insatiable hunger, they are the foot soldiers of the Scourge, ever eager for flesh.",
)
add_or_update_prompt(
    222,
    "Skeletal Warriors march in the wake of the Necropolis, their bones clattering in the cold wind. Clad in rusting armor, they wield ancient swords, a skeletal army that knows no fatigue or fear.",
)
add_or_update_prompt(
    223,
    "Crypt Fiends lurk in the shadowy recesses of Northrend, their spindly limbs ready to ensnare the unwary. Born of Nerubian heritage, they serve the Lich King with a chilling zeal.",
)
add_or_update_prompt(
    224,
    "Necromancers chant dark spells in the ruins of Stratholme, surrounded by their undead minions. Masters of death magic, they seek to unravel the mysteries of life and death, regardless of the cost.",
)
add_or_update_prompt(
    225,
    "Abominations lumber through the streets of the Undercity, their stitched bodies a patchwork of horror. Created from the corpses of the fallen, they are a grotesque testament to the Forsaken's dark alchemy.",
)
add_or_update_prompt(
    226,
    "Banshees wail in the night, their ethereal forms haunting the ruins of Quel'Thalas. Lost souls turned vengeful spirits, they mourn their fate while inflicting terror on the living.",
)
add_or_update_prompt(
    227,
    "Liches, cloaked in frost and shadow, plot from their icy thrones in Icecrown. With intellects as cold as their hearts, they wield necromantic powers to further the Scourge's dominion over the dead.",
)
add_or_update_prompt(
    228,
    "Death Knights, once heroes, now ride under the banner of the Lich King. Clad in dark armor and wielding runic weapons, they bring death and despair, a tragic fall from grace.",
)
add_or_update_prompt(
    229,
    "Skeletal Mages cast spells of ice and fire, their magical prowess undiminished by death. They stand as guardians of the Scourge's secrets, their arcane might a deadly challenge to any who oppose them.",
)
add_or_update_prompt(
    230,
    "Vrykul Skeletons, warriors of a bygone era, rise again in the fjords of Howling Fjord. Their battle cries echo once more, a ghostly echo of their former glory, now bound to the will of the Lich King.",
)
add_or_update_prompt(
    231,
    "Plaguehounds roam the diseased woods of Plaguelands, their forms twisted by the Scourge's experiments. They track the scent of the living with relentless determination, a pestilence on four legs.",
)

add_or_update_prompt(
    232,
    "Jaina Proudmoore stands at the edge of Theramore's ruins, her gaze lost in the distance. The weight of her decisions, and the consequences of the past, are reflected in her eyes, a mix of determination and sorrow as she contemplates the future of peace between the Alliance and Horde.",
)

add_or_update_prompt(
    233,
    "In the halls of Kul Tiras, Jaina Proudmoore faces the judgment of her people. With the pride of a nation and the pain of personal loss etched into her features, she seeks reconciliation, her powerful magic a testament to her resolve and her commitment to lead her homeland towards a new dawn.",
)

add_or_update_prompt(
    234,
    "Amidst the icy winds of Northrend, Jaina Proudmoore confronts the Lich King. Her spells light up the frozen landscape, a beacon of hope against the encroaching darkness. Her strength and leadership inspire those who follow her, a testament to her enduring spirit and her unwavering quest for justice.",
)

add_or_update_prompt(
    238,
    "Varian Wrynn stands tall in the throne room of Stormwind, a king and a warrior. His gaze is firm, his resolve unbreakable, embodying the spirit of the lion that represents his kingdom. He carries the weight of his crown with the strength of his sword arm, ready to defend his people at any cost.",
)

add_or_update_prompt(
    239,
    "On the battlefield, Varian Wrynn leads the charge against the Horde, his shout rallying the Alliance forces. His valor and prowess in combat are unmatched, his sword Shalamayne cleaving through the chaos of war, a symbol of hope and strength for his soldiers.",
)

add_or_update_prompt(
    240,
    "In the quiet of the Stormwind Keep's gardens, Varian Wrynn reflects on the path that has led him here. The scars of past battles and the loss of loved ones mark his journey, but so does the love for his son and his kingdom. His determination to protect Azeroth's future is as steadfast as the ancient stone walls that surround him.",
)

add_or_update_prompt(
    241,
    "Khadgar delves into ancient tomes within the hallowed halls of Karazhan, his brow furrowed in concentration. Surrounded by arcane energy, he seeks knowledge that will arm the forces of Azeroth against the ever-looming threat of the Burning Legion.",
)

add_or_update_prompt(
    242,
    "In the bustling streets of Dalaran, Khadgar addresses a gathering of the Kirin Tor. His voice is steady, filled with wisdom and urgency, as he outlines a plan to safeguard the world from darkness, rallying his fellow mages to unite in defense of their realm.",
)

add_or_update_prompt(
    243,
    "At the Broken Shore, Khadgar stands at the forefront of battle, staff in hand, casting spells that tear through the demonic ranks. His determination is a beacon for all who fight alongside him, his mastery of the arcane a testament to years of study and sacrifice.",
)

add_or_update_prompt(
    244,
    "Medivh, the Guardian of Tirisfal, gazes out from the highest spire of Karazhan, his eyes reflecting the myriad possibilities of time and space. He bears the weight of Azeroth's protection, a solitary figure caught between power and prophecy.",
)

add_or_update_prompt(
    245,
    "In the depths of Karazhan, Medivh conducts a forbidden ritual, the air crackling with arcane energy. His actions, driven by visions of the future, sow the seeds of both salvation and destruction, the line between the two blurred by his immense power.",
)

add_or_update_prompt(
    246,
    "At the Dark Portal, Medivh stands as the architect of a new era, his magic opening the gateway between Azeroth and Draenor. His figure is imposing, a mix of awe and fear surrounding him, as he ushers in an age of war that will reshape the world.",
)

add_or_update_prompt(
    271,
    "Hemet Nessingwary, the renowned hunter, sets up camp in the Sholazar Basin, his rifle at the ready. His tales of hunting the most dangerous beasts inspire adventurers to seek him out, eager to prove their skills and earn his respect.",
)

add_or_update_prompt(
    272,
    "In the green expanse of Nagrand, Hemet Nessingwary tracks his quarry with unmatched expertise. His love for the hunt is only matched by his respect for nature, a balance he maintains even as he pursues the most elusive of game.",
)

add_or_update_prompt(
    273,
    "Hemet Nessingwary's expeditions have become the stuff of legend, his journals a guide for those who wish to follow in his footsteps. From Stranglethorn Vale to the icy reaches of Northrend, his adventures embody the spirit of exploration and the thrill of the hunt.",
)

add_or_update_prompt(
    274,
    "Arthas Menethil, once a prince of Lordaeron, stands before the Frozen Throne, the Lich King's helm in his grasp. His path from paladin to Death Knight to Lich King is a tragic tale of ambition, betrayal, and a descent into darkness.",
)

add_or_update_prompt(
    275,
    "In the cobbled streets of Stratholme, Arthas makes the fateful decision to purge the city, a moment that seals his fate and marks the beginning of his fall. The ghosts of those he slew haunt him, a reminder of the cost of his choices.",
)

add_or_update_prompt(
    276,
    "As the Lich King, Arthas wields the power of Frostmourne with a cold fury, commanding the Scourge from atop Icecrown Citadel. His reign of terror is a dark chapter in Azeroth's history, a legacy of despair that heroes strive to overcome.",
)

add_or_update_prompt(
    277,
    "Sylvanas Windrunner, the Banshee Queen, watches over the Undercity, her bow ever ready. Her transformation from High Elf ranger to leader of the Forsaken is a testament to her resilience, her heart as cold as the grave.",
)

add_or_update_prompt(
    278,
    "In the ruins of Silvermoon, Sylvanas reflects on her past and the loss of her people. Her quest for vengeance against the Lich King drives her, a burning desire that fuels her every action and decision.",
)

add_or_update_prompt(
    279,
    "Sylvanas leads the Forsaken with a strategic mind and an iron will, her dark arrows a promise of retribution. Her alliance with the Horde is one of necessity, her true allegiance only to her people and their quest for a place in a world that shunned them.",
)

add_or_update_prompt(
    280,
    "Sylvanas Windrunner leads a covert operation in the heart of Gilneas, her arrows whispering death to her enemies. The Banshee Queen's tactics are ruthless, her aim true, as she advances the Forsaken's cause with precision and deadly grace.",
)

add_or_update_prompt(
    281,
    "Amidst the ruins of the Undercity, Sylvanas contemplates the Forsaken's future, her resolve hardened by the betrayals and battles she has endured. Her vision for her people is unwavering, a dark queen standing firm against a world that has turned its back on them.",
)

add_or_update_prompt(
    282,
    "On the battlements of Orgrimmar, Sylvanas stands alongside Horde leaders, her gaze piercing the horizon. Her allegiance to the Horde is complex, forged through conflict and necessity, yet she remains a fierce protector of her sovereignty and her people's right to exist.",
)

add_or_update_prompt(
    283,
    "Under the luminescent glow of the moon, Tyrande Whisperwind calls upon the power of Elune to protect her beloved Ashenvale from invaders. Her voice, both serene and commanding, echoes through the forest, rallying the Night Elves to defend their homeland with unwavering resolve.",
)
add_or_update_prompt(
    284,
    "In the Temple of the Moon in Darnassus, Tyrande presides over a solemn ceremony, her presence a comforting light to her people. She speaks of unity and strength, her wisdom guiding the Night Elves through times of peace and war, a beacon of hope in the darkest of times.",
)
add_or_update_prompt(
    285,
    "Amidst the ruins of Teldrassil, Tyrande stands as the embodiment of vengeance and sorrow, her eyes ablaze with the Night Warrior's power. She vows retribution against the Horde, her resolve as unyielding as the ancient trees that once towered over her people's home.",
)
add_or_update_prompt(
    286,
    "In the depths of the Emerald Dream, Malfurion Stormrage battles nightmares that threaten to consume the world. His connection to the dream and the natural world is unparalleled, his power manifesting in the growth of new life and the restoration of balance.",
)
add_or_update_prompt(
    287,
    "Malfurion, alongside Tyrande, confronts the encroaching corruption of the Burning Legion, his mastery over nature turning the tide of battle. Together, they stand as pillars of strength, their love and commitment to Azeroth inspiring all who fight beside them.",
)
add_or_update_prompt(
    288,
    "At the World Tree, Malfurion channels the raw energies of Azeroth to seal a breach torn by dark forces. His figure is a testament to the druidic promise to protect life, his spirit intertwined with the fate of the world itself.",
)
add_or_update_prompt(
    289,
    "Within the stone walls of Gilneas, Genn Greymane faces the curse that has transformed his people. As both king and worgen, he navigates the dual nature of his identity, leading his people with a ferocity and determination born of their shared affliction.",
)
add_or_update_prompt(
    290,
    "Genn Greymane stands at the helm of the Alliance fleet, his resolve steeling him against the storm. His leadership extends beyond the borders of Gilneas, his strategic acumen a vital asset in the fight against the Horde and other threats.",
)
add_or_update_prompt(
    291,
    "In the quiet of his chambers, Genn reflects on the losses endured by Gilneas, his heart heavy with the cost of isolation. Yet, his spirit is unbroken, his commitment to his people and their place within the Alliance unwavering.",
)

add_or_update_prompt(
    292,
    "Gul'dan stands at the heart of the Dark Portal, his hands weaving the fel magic that will bridge the worlds of Draenor and Azeroth. His thirst for power is unquenchable, his pact with the Burning Legion a dark testament to his ambition and his betrayal of his own people.",
)

add_or_update_prompt(
    293,
    "In the depths of the Tomb of Sargeras, Gul'dan seeks the ultimate prize, the power to command the Legion itself. His path is marked by deceit and destruction, his legacy a warning of the cost of wielding magic untethered by morality or conscience.",
)

add_or_update_prompt(
    294,
    "Gul'dan's shadow looms over the orc clans, his promise of power seductive and deadly. As the architect of the Horde's bloodlust, he manipulates leaders and warriors alike, his dark vision of conquest and glory a poison that threatens to consume all.",
)


# Commit changes
session.commit()
