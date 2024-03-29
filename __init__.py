import random

prefixes = ["Gloom",
            "Gray",
            "Dire",
            "Black",
            "Shadow",
            "Haze",
            "Wind",
            "Storm",
            "Warp",
            "Night",
            "Moon",
            "Star",
            "Pit",
            "Fire",
            "Cold",
            "Seethe",
            "Sharp",
            "Ash",
            "Blade",
            "Steel",
            "Stone",
            "Rust",
            "Mold",
            "Blight",
            "Plague",
            "Rot",
            "Ooze",
            "Puke",
            "Snot",
            "Bile",
            "Blood",
            "Pulse",
            "Gut",
            "Gore",
            "Flesh",
            "Bone",
            "Spine",
            "Mind",
            "Spirit",
            "Soul",
            "Wrath",
            "Grief",
            "Foul",
            "Vile",
            "Sin",
            "Chaos",
            "Dread",
            "Doom",
            "Bane",
            "Death",
            "Viper",
            "Dragon",
            "Devi"]

suffixes = [
    "Touch",
    "Spell",
    "Feast",
    "Wound",
    "Grin",
    "Maim",
    "Hack",
    "Bite",
    "Rend",
    "Burn",
    "Rip",
    "Kill",
    "Call",
    "Vex",
    "Jade",
    "Web",
    "Shield",
    "Killer",
    "Razor",
    "Drinker",
    "Shifter",
    "Crawler",
    "Dancer",
    "Bender",
    "Weaver",
    "Eater",
    "Widow",
    "Maggot",
    "Spawn",
    "Wight",
    "Grumble",
    "Growler",
    "Snarl",
    "Wolf",
    "Crow",
    "Hawk",
    "Cloud",
    "Bang",
    "Head",
    "Skull",
    "Brow",
    "Eye",
    "Maw",
    "Tongue",
    "Fang",
    "Horn",
    "Thorn",
    "Claw",
    "Fist",
    "Heart",
    "Shank",
    "Skin",
    "Wing",
    "Pox",
    "Fester",
    "Blister",
    "Pus",
    "Slime",
    "Drool",
    "Froth",
    "Sludge",
    "Venom",
    "Poison",
    "Break",
    "Shard",
    "Flame",
    "Maul",
    "Thirst",
    "Lust",
]

appellations = [
    "the Sharp",
    "the Jagged",
    "the Flayer",
    "the Slasher",
    "the Impaler",
    "the Hunter",
    "the Slayer",
    "the Mauler",
    "the Destroyer",
    "the Quick",
    "the Witch",
    "the Mad",
    "the Wraith",
    "the Shade",
    "the Dead",
    "the Unholy",
    "the Howler",
    "the Grim",
    "the Dark",
    "the Tainted",
    "the Unclean",
    "the Hungry",
    "the Cold",
]

if __name__ == "__main__":
    print(f"{random.choice(prefixes)} {random.choice(suffixes)} {random.choice(appellations)}")
