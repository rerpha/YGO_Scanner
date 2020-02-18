class CardType:
    SPELL = "Spell Card"
    TRAP = "Trap Card"
    NORMAL = "Normal"
    EFFECT = "Effect"
    FUSION = "Fusion"
    RITUAL = "Ritual"
    SYNCHRO = "Synchro"
    XYZ = "XYZ"
    LINK = "Link"
    PENDULUM = "Pendulum"


CardColours = {  # Card types and their corresponding colours - sourced from https://yugioh.fandom.com/wiki/Card_colors
    CardType.SPELL: "#1D9E74",
    CardType.TRAP: "#BC5A84",
    CardType.NORMAL: "#FDE68A",
    CardType.EFFECT: "#FF8B53",
    CardType.FUSION: "#A086B7",
    CardType.RITUAL: "#9DB5CC",
    CardType.SYNCHRO: "#CCCCCC",
    CardType.XYZ: "#000000",
    CardType.LINK: "#00008B",
}
