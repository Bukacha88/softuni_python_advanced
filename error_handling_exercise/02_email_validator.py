class MustContainAtSymbolError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


domain_list = ['.com', '.bg', '.org', '.net']
is_valid = True
while True:
    line = input()
    if line == 'End':
        break

    if '@' not in line:
        is_valid = False
        raise MustContainAtSymbolError('Email must contain @')
    else:
        name, rest = line.split('@')
        server, domain = rest.split('.')
        domain = '.' + domain

    if len(name) < 5:
        is_valid = False
        raise NameTooShortError('Name must be more than 4 characters')

    if domain not in domain_list:
        is_valid = False
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    if is_valid:
        print('Email is valid')

