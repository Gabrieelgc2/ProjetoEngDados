from src.extract import Extract
from src.load import Load

extract = Extract()
load = Load()

br = extract.extract_country('Brazil')
load.create_sqlite_table(br, 'universities', 'universidades_br')

ch = extract.extract_country('China')
load.create_sqlite_table(ch, 'universities', 'universidades_ch')

fr = extract.extract_country('France')
load.create_sqlite_table(fr, 'universities', 'universidades_fr')

it = extract.extract_country('Italy')
load.create_sqlite_table(it, 'universities', 'universidades_it')