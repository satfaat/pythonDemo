import asyncio
import sqlalchemy
from src.dbDemo.ex_ormar.config import metadata, DATABASE_URL, database
from src.dbDemo.ex_ormar.Book import Book
from src.dbDemo.ex_ormar.Author import Author


engine = sqlalchemy.create_engine(DATABASE_URL)
# just to be sure we clear the db before
metadata.drop_all(engine)
metadata.create_all(engine)


async def create():
    # Create some records to work with through QuerySet.create method.
    # Note that queryset is exposed on each Model's class as objects
    tolkien = await Author.objects.create(name="J.R.R. Tolkien")
    await Book.objects.create(author=tolkien, title="The Hobbit", year=1937)
    await Book.objects.create(author=tolkien, title="The Lord of the Rings", year=1955)
    await Book.objects.create(author=tolkien, title="The Silmarillion", year=1977)

    # alternative creation of object divided into 2 steps
    sapkowski = Author(name="Andrzej Sapkowski")
    # do some stuff
    await sapkowski.save()

    # or save() after initialization
    await Book(author=sapkowski, title="The Witcher", year=1990).save()
    await Book(author=sapkowski, title="The Tower of Fools", year=2002).save()


async def read():
    # Fetch an instance, without loading a foreign key relationship on it.
    # Django style
    book = await Book.objects.get(title="The Hobbit")
    # or python style
    book = await Book.objects.get(Book.title == "The Hobbit")
    book2 = await Book.objects.first()

    # first() fetch the instance with lower primary key value
    assert book == book2

    # you can access all fields on loaded model
    assert book.title == "The Hobbit"
    assert book.year == 1937

    # when no condition is passed to get()
    # it behaves as last() based on primary key column
    book3 = await Book.objects.get()
    assert book3.title == "The Tower of Fools"

    # When you have a relation, ormar always defines a related model for you
    # even when all you loaded is a foreign key value like in this example
    assert isinstance(book.author, Author)
    # primary key is populated from foreign key stored in books table
    assert book.author.pk == 1
    # since the related model was not loaded all other fields are None
    assert book.author.name is None

    # Load the relationship from the database when you already have the related model
    # alternatively see joins section below
    await book.author.load()
    assert book.author.name == "J.R.R. Tolkien"

    # get all rows for given model
    authors = await Author.objects.all()
    assert len(authors) == 2


async def with_connect(function):
    # note that for any other backend than sqlite you actually need to
    # connect to the database to perform db operations
    async with database:
        await function()

print(f"Executing: {read.__name__}")
asyncio.run(with_connect(read))
