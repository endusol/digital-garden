"""Digital Garden Zen - philosophy/principles of notes taking in the digital garden."""
from digital_garden.zen.zen_principle import ZenPrinciple
from digital_garden.zen.zen_principle_1 import ZenPrinciple1

ZEN: dict[int, type[ZenPrinciple]] = {
    1: ZenPrinciple1
}
