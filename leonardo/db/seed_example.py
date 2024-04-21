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
    "A snowy landscape with jack-o'-lanterns instead of snowmen, and a Santa Claus figure with a mischievous grin",
)
add_or_update_prompt(
    2,
    "Ghosts wearing Santa hats floating around a Christmas tree, with eerie ornaments and spider webs",
)
add_or_update_prompt(
    3,
    "A winter wonderland with a twist, where the snowflakes are tiny, ghostly figures, and icicles resemble fangs",
)
add_or_update_prompt(
    4,
    "Children trick-or-treating in the snow, dressed as elves and goblins, with a shadowy, sinister Santa watching from afar",
)
add_or_update_prompt(
    5,
    "A haunted gingerbread house covered in Halloween decorations, surrounded by a frosty graveyard",
)
add_or_update_prompt(
    6,
    "A group of playful demons building a snowman, but with a creepy, grinning pumpkin for a head",
)
add_or_update_prompt(
    7,
    "A dreamy scene of a frozen lake, where ice-skating witches are circling a Christmas tree made of bones",
)
add_or_update_prompt(
    8,
    "A cozy cabin, with a warm fire burning, but the shadows cast on the wall show eerie, dancing skeletons",
)
add_or_update_prompt(
    9,
    "A sleigh pulled by ghostly reindeer, driven by a Santa Claus with glowing eyes, flying over a haunted forest",
)
add_or_update_prompt(
    10,
    "An old, Victorian house decorated for Christmas, but with cobwebs, bats, and eerie, flickering lights",
)
add_or_update_prompt(
    11,
    "A snow globe that, when shaken, reveals a spooky Christmas village with miniature ghosts floating between the houses",
)
add_or_update_prompt(
    12,
    "A Christmas feast set up in a graveyard, with spectral figures seated at the table, enjoying a ghostly banquet",
)
add_or_update_prompt(
    13,
    "A frosty window scene where Santa's elves are playfully mischievous goblins, wrapping strange, otherworldly gifts",
)
add_or_update_prompt(
    14,
    "A Christmas parade with floats that are haunted houses on wheels, complete with costumed ghosts and ghouls",
)
add_or_update_prompt(
    15,
    "A moonlit forest with trees decorated in Halloween and Christmas themes, and a sinister Santa lurking behind",
)
add_or_update_prompt(
    16,
    "A merry-go-round where the horses are replaced with mythical Halloween creatures, all wearing Santa hats",
)
add_or_update_prompt(
    17,
    "A dreamlike snowfall, but each snowflake is a tiny, intricate spider web, glistening under the moonlight",
)
add_or_update_prompt(
    18,
    "A cozy Christmas scene inside, but the snow outside forms eerie shapes, like whispering ghosts and lurking monsters",
)
add_or_update_prompt(
    19,
    "A group of cheerful demons exchanging gifts under a Christmas tree, with Krampus smiling in the background",
)
add_or_update_prompt(
    20,
    "A winter landscape where the northern lights form shapes of dragons, witches, and other Halloween figures",
)
add_or_update_prompt(
    21,
    "An ice sculpture competition, where the sculptures are all of eerie Halloween characters in festive attire",
)
add_or_update_prompt(
    22,
    "A festive street where each house is decorated with a blend of Halloween horrors and Christmas cheer",
)
add_or_update_prompt(
    23,
    "A snowman dressed as a vampire, complete with a cape and fangs, next to a sleigh with bat-winged reindeer",
)
add_or_update_prompt(
    24,
    "A Christmas tree in a haunted mansion, with ornaments that are mini cauldrons, skulls, and witch hats",
)
add_or_update_prompt(
    25,
    "A group of children dressed as ghosts and goblins, singing carols, with a chilling wind carrying their voices",
)
add_or_update_prompt(
    26,
    "A playful spirit dressed in tattered holiday garb, juggling snowballs that turn into jack-o'-lanterns mid-air",
)
add_or_update_prompt(
    27,
    "A snowy path lined with scarecrows dressed in Santa suits, their pumpkin heads grinning eerily",
)
add_or_update_prompt(
    28,
    "A festive, haunted train ride through a winter landscape, with each carriage telling a different ghostly tale",
)
add_or_update_prompt(
    29,
    "A Christmas market, but each stall is selling bizarre, magical items that blend Yuletide joy with Halloween fright",
)
add_or_update_prompt(
    30,
    "A sinister Santa Claus casting spells over a quaint village, turning the snow into a dance of spectral figures",
)
add_or_update_prompt(
    31,
    "Children building an igloo, but inside, it’s decorated like a haunted house, complete with spooky Christmas lights",
)
add_or_update_prompt(
    32,
    "A reindeer with glowing red eyes pulling a sleigh filled with mysterious, ancient artifacts of Halloween lore",
)
add_or_update_prompt(
    33,
    "A magical forest where Christmas and Halloween decorations hang from every tree, and mystical creatures roam",
)
add_or_update_prompt(
    34,
    "A snowy hill with tombstones, where ghostly figures are sledding down, laughing and howling in the night",
)
add_or_update_prompt(
    35,
    "An abandoned church with a nativity scene, but the figures are replaced with classic Halloween monsters",
)
add_or_update_prompt(
    36,
    "A playful demon disguised as Santa, handing out gifts that magically transform into mischievous creatures",
)
add_or_update_prompt(
    37,
    "A Christmas wreath on a door, but upon closer inspection, it's made of tiny bones and spider webs",
)
add_or_update_prompt(
    38,
    "A blizzard where the snowflakes are shaped like tiny skulls and crossbones, swirling around a festive town",
)
add_or_update_prompt(
    39,
    "A candy cane forest, but the candy canes are twisted into sinister shapes, with ghoulish faces appearing on them",
)
add_or_update_prompt(
    40,
    "A festive ballroom dance, but the dancers are all in Halloween costumes, waltzing to a haunting melody",
)
add_or_update_prompt(
    41,
    "A snowy rooftop scene with Santa’s sleigh, but the presents are all wrapped in black and orange, with spooky ribbons",
)
add_or_update_prompt(
    42,
    "A group of witches conducting a Yuletide ritual, summoning friendly spirits to celebrate in a winter glade",
)
add_or_update_prompt(
    43,
    "A Christmas advent calendar, but each door opens to reveal a miniature Halloween scene with a festive twist",
)
add_or_update_prompt(
    44,
    "A quaint cottage where every window displays a different scene of Halloween creatures enjoying Christmas festivities",
)
add_or_update_prompt(
    45,
    "A frosty garden gnome that, upon a second glance, appears to be a small, mischievous troll in a Santa hat",
)
add_or_update_prompt(
    46,
    "A family of snowmen, but with eerie, glowing eyes, holding hands around a cauldron instead of a Christmas tree",
)
add_or_update_prompt(
    47,
    "A winter forest path lit by lanterns, but each lantern reveals a ghostly face when looked at directly",
)
add_or_update_prompt(
    48,
    "A Christmas elf workshop, but the elves are all goblins and gremlins, creating unusual, enchanted toys",
)
add_or_update_prompt(
    49,
    "A frozen pond where figures are ice skating, but their reflections show them as vampires, werewolves, and witches",
)
add_or_update_prompt(
    50,
    "A sinister Santa reading a book of ghost stories by the fireplace, with the shadows forming the tales on the walls",
)
add_or_update_prompt(
    51,
    "A mysterious Yule altar in a snow-covered forest, adorned with pagan symbols and flickering candles, overlooked by a sinister Santa figure in the shadows",
)
add_or_update_prompt(
    52,
    "A circle of druids conducting a winter solstice ritual under the full moon, with ghostly apparitions and Christmas lights intertwined in the trees",
)
add_or_update_prompt(
    53,
    "An ancient stone circle dusted with snow, where a coven of witches celebrates Yule with a Christmas tree decorated in occult symbols",
)
add_or_update_prompt(
    54,
    "A snow-laden landscape with a pentagram carved into the white blanket, surrounded by eerie figures in festive robes performing an enigmatic rite",
)
add_or_update_prompt(
    55,
    "A mystical forest path leading to a hidden pagan shrine, decorated with holly, ivy, and mysterious runes, under a canopy of haunting Christmas lights",
)
add_or_update_prompt(
    56,
    "A gothic cathedral at midnight, where a secret Christmas mass merges Christian and pagan traditions, with shadowy figures in attendance",
)
add_or_update_prompt(
    57,
    "An eerie procession of cloaked figures carrying Yule logs inscribed with ancient runes, led by a Santa figure with an occult twist",
)
add_or_update_prompt(
    58,
    "A haunted Victorian mansion with a lavish Yule ball, where masked guests perform an old pagan dance, under a ceiling adorned with mistletoe and crystal orbs",
)
add_or_update_prompt(
    59,
    "A secluded cabin in the woods, where a solitary witch prepares a Yule potion, surrounded by arcane Christmas decorations and a protective circle of salt",
)
add_or_update_prompt(
    60,
    "A frost-covered grimoire open to a page revealing a Yule spell, with a backdrop of a Christmas tree festooned with symbols of the occult and twinkling lights",
)
add_or_update_prompt(
    61,
    "A bewitching woman in a snow-white gown, her beauty ethereal, performing a candlelit Yule ritual in a forest clearing, with a sinister Santa lurking in the background",
)
add_or_update_prompt(
    62,
    "A group of enchanting witches, draped in festive yet eerie attire, dancing around a Christmas tree adorned with occult symbols during a full moon ritual",
)
add_or_update_prompt(
    63,
    "An alluring woman with a haunting gaze, wearing a crown of holly and mistletoe, conducting a solstice ceremony with an ancient book of Yule spells",
)
add_or_update_prompt(
    64,
    "A circle of mesmerizing women, each more captivating and ghostly than the last, summoning winter spirits under a starry sky, surrounded by snow-dusted pine trees",
)
add_or_update_prompt(
    65,
    "A frozen lake where a solitary, beautiful figure skates gracefully, her reflection revealing a macabre, ghostly visage, with spectral onlookers in the shadows",
)
add_or_update_prompt(
    66,
    "An enchantress in a velvet Christmas gown, her beauty chilling, casting runes in the snow, with a backdrop of haunted evergreens and a crescent moon",
)
add_or_update_prompt(
    67,
    "A grand hall where a captivating Yule ball is taking place, led by a hostess with an unsettling allure, her eyes glowing unnaturally as she oversees the festivities",
)
add_or_update_prompt(
    68,
    "A shadowy forest path, where a stunning woman in a red cloak whispers to the trees, her words summoning ethereal lights and ghostly figures amongst the snowflakes",
)
add_or_update_prompt(
    69,
    "A mysterious figure cloaked in beauty and darkness, lighting black candles on a snow-covered altar, with a twisted Christmas wreath and ravens perched nearby",
)
add_or_update_prompt(
    70,
    "An abandoned chapel, where a captivating ritual is led by a woman in a tattered angel costume, her beauty both divine and sinister, with eerie carols echoing in the background",
)
add_or_update_prompt(
    71,
    "A whimsical candy cane forest under a moonlit sky, where the candy canes are twisted into spooky shapes and ghoulish figures made of candy roam playfully",
)
add_or_update_prompt(
    72,
    "A haunted gingerbread house adorned with Halloween-themed decorations, surrounded by a frosty landscape, and guarded by a sinister Santa made of marshmallow",
)
add_or_update_prompt(
    73,
    "A surreal scene of a snowy village where the snowflakes are actually colorful candy pieces, with ghostly children gathering them under the watchful eyes of a jack-o'-lantern Santa",
)
add_or_update_prompt(
    74,
    "A mystical chocolate river flowing through a winter wonderland, with eerie, candy-themed boats carrying mysterious, cloaked figures in Santa hats",
)
add_or_update_prompt(
    75,
    "An enchanted Christmas tree in a haunted mansion, decorated with a variety of sinister-looking candies and treats, casting otherworldly shadows in the dim light",
)
add_or_update_prompt(
    76,
    "A stunning young witch in elegant Yule attire, casting spells by moonlight in a snow-covered forest, with a festive but eerie Christmas tree glowing in the background",
)
add_or_update_prompt(
    77,
    "A group of captivating witches, youthful and radiant, gathered around a cauldron in a snowy clearing, brewing a mysterious potion under a garland of Christmas lights",
)
add_or_update_prompt(
    78,
    "An enchanting witch with a mischievous smile, flying on her broomstick over a quaint village decorated for Christmas, her shadow passing over the twinkling lights",
)
add_or_update_prompt(
    79,
    "A beautiful witch in a cloak of holly and mistletoe, reading from an ancient grimoire by the light of a jack-o’-lantern, in a room adorned with Yuletide decorations",
)
add_or_update_prompt(
    80,
    "A bewitching young sorceress, her beauty enhanced by the soft glow of the northern lights, conjuring spectral snowflakes that turn into tiny ghosts around a haunted Christmas tree",
)
add_or_update_prompt(
    81,
    "A mesmerizing vampire lady, reminiscent of Elvira, elegantly draped in a velvet Christmas gown, standing under a mistletoe in a haunted ballroom, her fangs subtly visible",
)
add_or_update_prompt(
    82,
    "An alluring vampire queen, with a striking Elvira-like aura, seated on a throne of ice and bones, surrounded by a ghostly winter landscape and eerie Christmas lights",
)
add_or_update_prompt(
    83,
    "A group of vampire ladies, each embodying the charm and mystique of Elvira, exchanging gifts in a lavishly decorated, candle-lit crypt with a sinister Christmas tree",
)
add_or_update_prompt(
    84,
    "An enigmatic vampire in a flowing black dress, her beauty and style evocative of Elvira, casting a spell over a snow-covered graveyard with a blood-red moon overhead",
)
add_or_update_prompt(
    85,
    "A captivating vampire mistress, channeling Elvira's allure, lounging on a velvet chaise longue by a roaring fireplace, her eyes glowing in the reflection of Christmas ornaments",
)
add_or_update_prompt(
    86,
    "A snowy village where each house is playfully haunted by a different Christmas-themed monster, from a wreath-wrapped werewolf to a Santa-hat-wearing goblin",
)
add_or_update_prompt(
    87,
    "A Christmas Eve scene where monstrous yet jovial creatures are seen decorating a towering tree in a haunted forest, with eerie ornaments and spider webs",
)
add_or_update_prompt(
    88,
    "A group of friendly monsters caroling door-to-door, their appearances a charming mix of festive cheer and Halloween horror, under a moonlit snowy night",
)
add_or_update_prompt(
    89,
    "A monstrous snowman with glowing eyes and sharp icicle teeth, guarding a pile of mysterious gifts in a desolate, frosty landscape",
)
add_or_update_prompt(
    90,
    "A banquet hall where various monsters are having a festive feast, with a grand Christmas tree in the background, adorned with bizarre and whimsical decorations",
)
add_or_update_prompt(
    91,
    "A cavernous ice cave lit by flickering candlelight, where ice sculptures of legendary monsters celebrate Christmas with a chilling elegance",
)
add_or_update_prompt(
    92,
    "An eerie, misty lake where a Loch Ness monster-like creature wearing a Santa hat emerges to join in the Yuletide festivities with nearby villagers",
)
add_or_update_prompt(
    93,
    "A Christmas market in a mystical realm, staffed and frequented by an array of monsters, selling otherworldly holiday wares and treats",
)
add_or_update_prompt(
    94,
    "A group of children building a monster out of snow, only for it to magically come to life as a gentle, festive creature, joining them in their holiday games",
)
add_or_update_prompt(
    95,
    "A haunted mansion's grand hall, where portraits of ancestral monsters are decked in Christmas garlands, and spectral figures dance a ghostly waltz under mistletoe",
)
add_or_update_prompt(
    96,
    "A ghostly choir singing carols in a snowy graveyard, their transparent forms glowing softly under the moonlight, with festive wreaths on each tombstone",
)
add_or_update_prompt(
    97,
    "A Christmas party in an old, haunted mansion where ghouls in tattered Yuletide attire waltz through the cobwebbed halls",
)
add_or_update_prompt(
    98,
    "Zombies trudging through the snow, each humorously wearing a piece of Santa's outfit, approaching a brightly lit, yet eerie, Christmas tree",
)
add_or_update_prompt(
    99,
    "A pack of werewolves, adorned with tinsel and Christmas lights, howling at the full moon on a crisp, snowy night",
)
add_or_update_prompt(
    100,
    "An abandoned snowy village where spectral figures float between the buildings, and a ghostly Santa Claus leads a phantom sleigh",
)
add_or_update_prompt(
    101,
    "A creepy Christmas banquet where ghouls serve a feast to zombie guests, with a spine-chilling Santa presiding over the table",
)
add_or_update_prompt(
    102,
    "A werewolf in a Santa hat, playfully decorating a Christmas tree in a dark, enchanted forest, with ghostly lights flickering around",
)
add_or_update_prompt(
    103,
    "Ghosts gathered around a frozen pond, their ethereal forms skating over the ice, under a sky filled with eerie auroras",
)
add_or_update_prompt(
    104,
    "A zombie Santa Claus delivering presents to haunted houses, his sleigh pulled by ghostly reindeer under a starless sky",
)
add_or_update_prompt(
    105,
    "A festive but chilling scene in a moonlit forest where werewolves and ghouls gather to exchange ghostly gifts under a towering, spectral Christmas tree",
)


# Commit changes
session.commit()
