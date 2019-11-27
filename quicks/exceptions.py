class QuicksException(Exception):
    pass


class PathExistsError(QuicksException):
    pass


__all__ = (
    'QuicksException',
    'PathExistsError',
)
