class ParserFindTagException(Exception):
    """Вызывается, когда парсер не может найти тег."""
    pass


class PageLoadException(Exception):
    """Вызывается, когда основная страница не загрузилась."""
    pass
