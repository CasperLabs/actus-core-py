import re


def to_camel_case(name: str, separator: str ='_'):
    """Converts passed name to camel case.

    :param name: A name as specified in ontology specification.
    :param separator: Separator to use in order to split name into constituent parts.
    :returns: A string converted to camel case.

    """
    r = ''
    if name is not None:
        s = name.split(separator)
        for s in s:
            if (len(s) > 0):
                r += s[0].upper()
                if (len(s) > 1):
                    r += s[1:]
    return r


def to_pascal_case(name: str, separator: str ='_'):
    """Converts passed name to pascal case.

    :param name: A name as specified in ontology specification.
    :param separator: Separator to use in order to split name into constituent parts.
    :returns: A string converted to pascal case.

    """
    r = ''
    s = to_camel_case(name, separator)
    if (len(s) > 0):
        r += s[0].lower()
        if (len(s) > 1):
            r += s[1:]
    return r


def to_underscore_case(target: str):
    """Helper function to convert a from camel case string to an underscore case string.

    :param target: A string for conversion.
    :returns: A string converted to underscore case, e.g. account_number.

    """
    if target is None or not len(target):
        return ''

    r = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', target)
    r = re.sub('([a-z0-9])([A-Z])', r'\1_\2', r)
    r = r.lower()

    return r


def to_python_type(term) -> str:
    """Maps an Actus term's type to it's pythonic equivalent.
    
    """
    if term.type == "Real":
        return "float"
    elif term.type == "Varchar":
        return "str"
    elif term.type == "Timestamp":
        return "datetime.datetime"
    elif term.type == "ContractReference":
        return "primitives.ContractReference"
    elif term.type == "ContractReference[]":
        return "typing.List[primitives.ContractReference]"
    elif term.type == "Enum":
        return f"enums.{to_camel_case(term.identifier)}"
    elif term.type == "Enum[]":
        return f"typing.List[enums.{to_camel_case(term.identifier)}]"

    raise ValueError(term.type)
    return f"xxx-{term.type}"
