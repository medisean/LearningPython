from bar import spam, egg

__all__ = ['spam', 'egg'] # white list, define public API, below all import 

print(spam.spamName)