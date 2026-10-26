import pathlib
from digital_garden.document import Document, DocumentStatus


doc1 = Document(pathlib.Path('test.md'))
doc2 = Document(pathlib.Path('test-no-frontmatter.md'))


print(doc1)
print(doc2)

print('-------- doc 1')
print(doc1._document.metadata)
print(doc1._document.content)
print('-------- doc 2')
print(doc2._document.metadata)
print(doc2._document.content)

print('status tests ----------------')
print('-------- correct status set')
doc1.set_status(DocumentStatus.EVERGREEN)
print(doc1._document.metadata)
print('-------- incorrect status set')
try:
    doc2.set_status('INVALID-DOCUMENT-STATUS')
except Exception as e:
    print(e)