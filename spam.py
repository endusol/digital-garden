"""spam"""
from pathlib import Path
from digital_garden.document import Document
from digital_garden.contract import CONTRACT


path = Path('/home/endusol/Projects/Obsidian/obsidian--work/digital-garden/valid document.md')
document = Document(path)
print(CONTRACT[8].check(document))
