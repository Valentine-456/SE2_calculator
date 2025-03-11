import re


def strToNumSum(param: str):
    if param == "":
        return 0

    allowedDelimiters = [",", "\n"]

    if param.startswith("//"):
        delimiter_end = param.index("\n")
        delimiter_section = param[2:delimiter_end]

        custom_delimiters = re.findall(r"\[(.*?)\]", delimiter_section)

        if custom_delimiters:
            allowedDelimiters.extend(custom_delimiters)
        else:
            allowedDelimiters.append(delimiter_section)
        param = param[(delimiter_end + 1) :]

    isMultipleNumbers = any(delimiter in param for delimiter in allowedDelimiters)
    if not isMultipleNumbers:
        return int(param)

    normalizedParam = param
    for delimiter in allowedDelimiters:
        normalizedParam = normalizedParam.replace(delimiter, ",")

    numbers = list(map(int, normalizedParam.split(",")))

    hasNegativeNumbers = [num for num in numbers if num < 0]
    if hasNegativeNumbers:
        raise ArithmeticError("Has negative numbers")

    numbersFiltered = filter(lambda x: x <= 1000, numbers)

    return sum(numbersFiltered)
