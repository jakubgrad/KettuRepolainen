from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

class ReferenceDao:
    def __init__(self, db_connection: SQLAlchemy):
        self.__db = db_connection
        self.___references_in_bibtex_form: bool = False

    def change_reference_view_format(self):
        self.___references_in_bibtex_form = not self.___references_in_bibtex_form
        print("after change", self.___references_in_bibtex_form)

    def get_reference_view_format(self):
        return self.___references_in_bibtex_form

    def create_reference(self, data):
        """Add a new reference to the database.
        Add reference name to a table containing reference names.
        Connect reference name to a table containing its data.

        Args:
            data (dict): Author, title, journal, year, volume, number, and pages
            of the referenced article.
        """

        sql = text("""
            INSERT INTO \"references\" (
                type,name,author,title,journal,year,volume,number,pages, month, note, howpublished, editor, publisher
            )                
            VALUES (
                :type, :name, :author, :title, :journal,:year,:volume,:number,:pages, :month, :note, :howpublished, :editor, :publisher
            )
        """)

        self.__db.session.execute(
            sql,
            {
                "type":data["type"],
                "name":data["name"],
                "author":data["author"],
                "title":data["title"],
                "journal":data["journal"],
                "year":data["year"],
                "volume":data["volume"],
                "number":data["number"],
                "pages":data["pages"],
                "month":data["month"],
                "note":data["note"],
                "howpublished":data["howpublished"],
                "editor":data["editor"],
                "publisher":data["publisher"]
            }
        )
        self.__db.session.commit()

    def get_references(self):
        """
        Hakee kaikki viitteet tietokannasta yhdellä optimoidulla kyselyllä.
        Returns:
            List[dict]: Lista viitteistä JSON-muodossa.
        """
        sql = text("""
            SELECT 
                id, type, name, author, title, journal, year, volume, number, pages, month, note, howpublished, editor, publisher
            FROM 
                \"references\"
        """)
        result = self.__db.session.execute(sql).fetchall()

        return result
