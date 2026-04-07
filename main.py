from src.extract import Extract
from src.load import Load

extract = Extract()
load = Load()

Contrato = extract.extract_contratacoes(dataFinal="20260430", codigoModalidadeContratacao=8, uf="pe", pagina=1, tamanhoPagina=20)
load.create_sqlite_table(Contrato, "contratacoes", "contratacoes_pe")