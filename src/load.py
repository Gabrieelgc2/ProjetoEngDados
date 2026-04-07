import sqlite3
class Load:
    def __init__(self):
        pass

    def create_sqlite_table(self, contratacoes_list, db_name, table_name):

        """
        Método responsável por criar uma tabela no banco de dados SQLite e inserir os dados de contratações.
        """
        con = sqlite3.connect(f"{db_name}.db")
        c = con.cursor()

        c.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_controle TEXT UNIQUE,
            objeto TEXT,
            orgao TEXT,
            cnpj TEXT,
            valor REAL,
            uf TEXT,
            municipio TEXT,
            modalidade TEXT,
            data_abertura TEXT,
            data_encerramento TEXT
        );
        """)

        for ctt in contratacoes_list:

            c.execute(
                f"""
                INSERT OR IGNORE INTO {table_name}
                (numero_controle, objeto, orgao, cnpj, valor, uf, municipio, modalidade, data_abertura, data_encerramento)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                """,
                (
                    ctt.get("numeroControlePNCP"),
                    ctt.get("objetoCompra"),
                    (ctt.get("orgaoEntidade") or {}).get("razaoSocial"),
                    (ctt.get("orgaoEntidade") or {}).get("cnpj"),
                    ctt.get("valorTotalEstimado"),
                    (ctt.get("unidadeOrgao") or {}).get("ufSigla"),
                    (ctt.get("unidadeOrgao") or {}).get("municipioNome"),
                    ctt.get("modalidadeNome"),
                    ctt.get("dataAberturaProposta"),
                    ctt.get("dataEncerramentoProposta"),
                ),
            )

        con.commit()
        con.close()