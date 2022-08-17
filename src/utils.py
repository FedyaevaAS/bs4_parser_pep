import logging

from requests import RequestException

from exceptions import PageLoadException, ParserFindTagException


def get_response(session, url, is_main_page=False):
    try:
        response = session.get(url)
        response.encoding = 'utf-8'
        return response
    except RequestException:
        logging.exception(
            f'Возникла ошибка при загрузке страницы {url}',
            stack_info=True
        )
    if is_main_page is True and response is None:
        error_msg = 'Основная страница не загрузилась'
        raise PageLoadException(error_msg)


def find_tag(soup, tag, attrs=None):
    searched_tag = soup.find(tag, attrs=(attrs or {}))
    if searched_tag is None:
        error_msg = f'Не найден тег {tag} {attrs}'
        logging.error(error_msg, stack_info=True)
        raise ParserFindTagException(error_msg)
    return searched_tag
